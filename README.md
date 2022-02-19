# Visual Data Preparation (VDP) Protobufs

This repository is the interface definitions of [Visual Data Preparation (VDP) APIs](https://github.com/instill-ai/vdp) that support both REST and gRPC protocols. You can also use these definitions with open source tools to generate client libraries, documentation, and other artifacts.

## Overview

VDP APIs use Protocol Buffers version 3 (proto3) as our Interface Definition Language (IDL) to define the API interface and the structure of the payload messages. The same interface definition is used for both REST (via [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway)) and RPC versions of the API, which can be accessed over different wire protocols

There are several ways of accessing VDP APIs:

1. JSON over HTTP: You can access all Instill AI APIs directly using JSON over HTTP
2. Protocol Buffers over gRPC: You can also use gRPC, which is a high-performance binary RPC protocol over HTTP/2, to access Instill AI APIs. It offers many useful features, including request/response multiplex and full-duplex streaming.
