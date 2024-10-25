# in-place sed command works different depending on the OS. When developing
# locally macOS is the standard at Instill AI, but CI actions use Linux.
#
# TODO instead of checking the OS we should run these commands from a container
# that matches the one in our CI.
OS_NAME := $(shell uname -s | tr A-Z a-z)
SED_IN_PLACE := sed -i

# On macOS, you can install the `gsed` command via `brew install gsed` to
# achieve the same behavior as the `sed` command on Linux.
ifeq (${OS_NAME}, darwin)
	SED_IN_PLACE = gsed -i
endif
.PHONY: openapi
openapi:
	@# ====
	@# Generate one OpenAPI file per service. These files are uploaded to
	@# readme.com and each file represents a category.
	@# ====

	@# Inject common API configuration into each OpenAPI proto template.
	@echo '-> Generate common configuration from templates'
	@./scripts/generate-openapi-doc-info.sh

	@# Generate an OpenAPI definition for each directory at the root that
	@# contains at least one public proto file.
	@echo '-> Generate service OpenAPI specs'
	@find . -name '*public*proto' | cut -d'/' -f 2-2 | sort | uniq | xargs -I '{}' buf generate --template buf.gen.openapi.yaml --path {} --path common -o openapi/v2/{}

	@# Clean up generated OpenAPI config files
	@find . -name 'openapi.proto' -delete

	@# ====
	@# Generate a common OpenAPI file, representing the interface at the
	@# gateway. Some SDKs like C# use the OpenAPI spec as the source for
	@# the generated code, and they require a merged OpenAPI spec.
	@# ====
	@echo '-> Generate gateway OpenAPI specs'
	@buf generate --template buf.gen.openapi.yaml --output openapi/v2
	@echo \# This file is auto-generated. DO NOT EDIT. | cat - openapi/v2/service.swagger.yaml > openapi/v2/service.swagger.tmp.yaml
	@mv openapi/v2/service.swagger.tmp.yaml openapi/v2/service.swagger.yaml
.PHONY: openapi-lint
openapi-lint:
	@# Lint each file under openapi/v2.
	@find openapi/v2 -type f | xargs -I '{}' rdme openapi:validate {}
