# in-place sed command works different depending on the OS. When developing
# locally macOS is the standard at Instill AI, but CI actions use Linux.
#
# TODO instead of checking the OS we should run these commands from a container
# that matches the one in our CI.
OS_NAME := $(shell uname -s | tr A-Z a-z)
SED_IN_PLACE := sed -i
ifeq (${OS_NAME}, darwin)
	SED_IN_PLACE += ''
endif
openapi:
	@# Inject common API configuration into each OpeAPI proto template.
	./scripts/generate-openapi-doc-info.sh

	@# Generate an OpenAPI definition for each directory at the root that
	@# contains at least one public proto file.
	find . -name '*public*proto' | cut -d'/' -f 2-2 | sort | uniq | xargs -I '{}' buf generate --template buf.gen.openapi.yaml --path {} --path common -o openapiv2/{}

	@# grpc-ecosystem/openapiv2:v2.19.0 will define protobufNullValue as an
	@# empty enum, which isn't allowed by the linter we use. This linter is
	@# used before importing the definitions and exposing them in a public
	@# server.
	@#
	@# For each file in openapiv2, remove empty enum declarations.
	find openapiv2 -type f | xargs -I '{}' ${SED_IN_PLACE} '/^[[:space:]]*enum: \[\]/,+0d' {}
openapi-lint:
	@# Lint each file under openapiv2.
	find openapiv2 -type f | xargs -I '{}' swagger-cli validate {}
openapi-info:
	@# ESCAPED_INFO=$(sed 's/\//\\\//g'  common/openapi/v1beta/api_info.conf | sed 's/$/\\n/g' | tr -d '\n')
	@# sed "s/{{\$info}}/$ESCAPED_INFO/g" model/model/v1alpha/openapi.proto.templ > model/model/v1alpha/openapi.proto
