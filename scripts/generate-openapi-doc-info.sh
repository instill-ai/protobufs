#!/usr/bin/env bash

set -eo pipefail

# The goal of this script is generating the OpenAPI info for the different
# backend servers (e.g. model, vdp, core).
#
# In order to have different base paths, each backend has a different OpenAPI
# document. Most of the API info is common, so only the particular information
# is documented in an `openapi.proto.templ` file within each domain. The common
# information will be read from a common document and injected into these
# files.

# We'll replace the {{$info}} and {{$conf}} patterns using the sed command. In
# order to use it, we need to escape special characters such as newlines and
# slashes (present in URLs).
ESCAPE_SLASHES='s/\//\\\//g'
ESCAPE_NEWLINES='s/$/\\n/g'

PATTERN_INFO='{{\$info}}'
PATTERN_CONF='{{\$conf}}'

ESCAPED_INFO=$(sed $ESCAPE_SLASHES  common/openapi/v1beta/api_info.conf | sed $ESCAPE_NEWLINES | tr -d '\n')
ESCAPED_CONF=$(sed $ESCAPE_SLASHES  common/openapi/v1beta/api_config.conf | sed $ESCAPE_NEWLINES | tr -d '\n')

# For each template file, insert the configuration in the pattern and save it
# as an openapi.proto file.
for templ in $(find . -name 'openapi.proto.templ' | cut -d'/' -f 1-4); do
  sed "s/$PATTERN_INFO/$ESCAPED_INFO/g" ${templ}/openapi.proto.templ | sed "s/$PATTERN_CONF/$ESCAPED_CONF/g" >| ${templ}/openapi.proto
done
