# protobufs

Canonical OSS Protocol Buffer API definitions for Instill Core gRPC and REST surfaces.

## Stack

Buf, grpc-gateway annotations, Spectral OpenAPI lint, generated Go/Python/doc outputs.

## Common Commands

- `make gen`
- `make openapi`
- `buf lint`
- `buf breaking --against '.git#branch=main'`

## Working Rules

- Follow Google AIP resource/RPC shapes; identify the AIP behind new APIs.
- Resource messages reserve fields 1-8 for the standard identity/timestamp block.
- Custom HTTP bindings use slash-separated actions, never colon actions, because KrakenD will 404 colon routes.
- Edit proto sources only; regenerate generated outputs with make commands.

## Invariants Index

`docs/invariants/README.md` indexes the per-domain `AIP-INV-*` invariants. Read only what you need:

- `aip-compliance.md` — AIP rule set + pre-merge `buf lint` / `buf breaking`.
- `resource-layout.md` — standard field 1-8 layout for resource messages.
- `custom-method-urls.md` — slash-separated custom-method URLs (KrakenD compatibility).
