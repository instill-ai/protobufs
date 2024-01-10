openapi: # build public OpenAPI definitions from proto files
	find . -name '*public*proto' | cut -d'/' -f 2-2 | sort | uniq | xargs -I '{}' buf generate --template buf.gen.openapi.yaml --path {} -o openapiv2/{}
openapi-lint: # lint OpenAPI files
	find openapiv2 -type f | xargs -I '{}' swagger-cli validate {}
