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
	@# Generate a common OpenAPI file, representing the public interface
	@# of Instill AI.
	@echo '-> Generate OpenAPI specs'
	@buf generate --template buf.gen.openapi.yaml --output openapi/v2
	@echo \# This file is auto-generated. DO NOT EDIT. | cat - openapi/v2/service.swagger.yaml > openapi/v2/service.swagger.tmp.yaml
	@mv openapi/v2/service.swagger.tmp.yaml openapi/v2/service.swagger.yaml
.PHONY: openapi-lint
openapi-lint:
	@# The spectral ruleset adds extra validation rules that allow us to
	@# keep the documents consistent.
	@spectral lint openapi/v2/service.swagger.yaml

gen-python-client:
	cd tools/gen-python-client && go build -o gen-python-client ./main.go
	rm log.txt && ./tools/gen-python-client/gen-python-client > log.txt
	echo "build and gen completed"
