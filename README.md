# Instill AI Protobufs

This repository is the API definitions of [Instill Core](https://github.com/instill-ai/instill-core) that support both REST
and gRPC protocols.

## Overview

The APIs use Protocol Buffers version 3 (proto3) as the Interface Definition
Language (IDL) to define the API interface and the structure of the payload
messages. The same interface definition is used for both RESTful (via
[gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway)) and RPC versions
of the API, which can be accessed over different wire protocols:

- **JSON over HTTP**
- **Protocol Buffers over gRPC**

## CI/CD

1. PR sent to the `main` branch will automatically generate, lint and commit the
   OpenAPI definitions for the gRPC methods exposed over HTTP. This is done with
   the `buf` and `rdme` CLIs.
1. PR sent to the `main` branch will trigger `buf-check` job, in which
   the changes in proto files will be validated via the [Buf
   action](https://github.com/bufbuild/buf-action).
1. Push to the `main` branch will push the Buf module to the [BSR
   repository](https://buf.build/instill-ai/protobufs) and the auto-generated
   codes to the corresponding `protogen-*` repository.
1. Merging to `main` an update in the [API
   version](./common/openapi/v1beta/api_info.conf) will upload the OpenAPI docs
   to [openapi.instill-ai.dev](https://openapi.instill-ai.dev/).
