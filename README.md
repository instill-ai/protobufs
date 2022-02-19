# Instill AI  APIs

This repository is the interface definitions of public Instill AI APIs that support both REST and gRPC protocols. We think this repository can provide a better understanding of Instill AI APIs by reading the original interface definitions to help you utilize them more efficiently. You can also use these definitions with open source tools to generate client libraries, documentation, and other artifacts.

## Overview

Instill AI APIs use Protocol Buffers version 3 (proto3) as our Interface Definition Language (IDL) to define the API interface and the structure of the payload messages. The same interface definition is used for both REST and RPC versions of the API, which can be accessed over different wire protocols

There are several ways of accessing Instill AI APIs:

1. JSON over HTTP: You can access all Instill AI APIs directly using JSON over HTTP
2. Protocol Buffers over gRPC: You can also use GRPC, which is a high-performance binary RPC protocol over HTTP/2, to access Instill AI APIs. It offers many useful features, including request/response multiplex and full-duplex streaming.
