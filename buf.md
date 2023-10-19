# Instill AI Protobufs

This repository is the interface definitions of the APIs of [Instill Core](https://github.com/instill-ai/core), [Instill Model](https://github.com/instill-ai/model), and [Instill VDP](https://github.com/instill-ai/vdp) that support both REST and gRPC protocols. You can also use these definitions with open source tools to generate client libraries, documentation, and other artifacts.

## Overview

The APIs use Protocol Buffers version 3 (proto3) as the Interface Definition Language (IDL) to define the API interface and the structure of the payload messages. The same interface definition is used for both RESTful (via [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway)) and RPC versions of the API, which can be accessed over different wire protocols:

- **JSON over HTTP**
- **Protocol Buffers over gRPC**
