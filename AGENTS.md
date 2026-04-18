# AGENTS.md

Guidance for Claude Code when working in this repository.

## Purpose

`instill-ai/protobufs` is the canonical Protocol Buffers (proto3) API definition
repository for [Instill Core](https://github.com/instill-ai/instill-core). The
same `.proto` files define both:

- **gRPC** (native Protocol Buffers over HTTP/2)
- **REST/JSON** (via [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway) annotations)

The BSR module is published as `buf.build/instill-ai/protobufs`. Generated
client/server stubs are pushed to sibling `protogen-*` repos (e.g. `protogen-go`,
`protogen-python`) on merge to `main`.

## Tooling

- **[Buf](https://buf.build/)** is the sole proto toolchain — lint, breaking-change
  detection, generation, and BSR publishing. No raw `protoc` invocations.
- **Spectral** lints the generated OpenAPI.
- `gsed` is required on macOS (`brew install gsed`); CI uses GNU `sed`.
- Python post-processing runs via `scripts/generate_python_init.py`.

## Verified commands

Sourced from `Makefile`:

- `make gen` — runs `buf generate` (Go + Python stubs into `gen/go`, `gen/python`,
  plus `gen/grpc-doc` markdown), then post-processes Python `__init__.py` files.
- `make openapi` — generates `openapi/v2/service.swagger.yaml` via
  `buf.gen.openapi.yaml` and prepends the auto-generated banner.
- `make openapi-lint` — `spectral lint openapi/v2/service.swagger.yaml`.
- `buf lint` / `buf breaking` — run directly per `buf.yaml` rules (STANDARD +
  comment rules; breaking uses `FILE` mode, unstable packages ignored).

## Layout

- `artifact/`, `mgmt/`, `model/`, `pipeline/`, `usage/` — per-service proto
  packages, each versioned under `vNalpha` / `vNbeta` subdirs.
- `common/` — shared messages (`healthcheck/`, `run/`, `task/`).
- `openapi/` — OpenAPI annotation protos; excluded from lint and from `buf generate`
  inputs (see `buf.yaml` and `buf.gen.yaml`).
- `gen/` — generated Go, Python, and grpc-doc output (committed).
- `scripts/`, `release-please/`, `CHANGELOG.md`, `buf.md`.

## Conventions

- Proto3 only. Package versions are unstable (`v1alpha`, `v1beta`); breaking
  changes there are permitted (`ignore_unstable_packages: true`).
- Enum zero values must end in `_UNSPECIFIED`; services must end in `Service`.
- All enums, services, RPCs, messages, fields, and oneofs require comments
  (enforced by `COMMENT_*` lint rules).
- Go package prefix is managed centrally: `github.com/instill-ai/protogen-go`.
  Do not set `go_package` per-file.
- `model/ray/serve.proto` is vendored from the Ray repo and is lint-ignored —
  don't reformat it.
- Edit `.proto` files only; do not hand-edit anything in `gen/` or
  `openapi/v2/service.swagger.yaml` (regenerate via `make`).

## API Design Rules (AIP-INV-\*)

This repo is the wire contract for every Instill backend — CE and EE. Shape
drift here costs every downstream SDK (`protogen-go`, `protogen-python`,
console, python-sdk) and every gateway route. The following rules are
non-negotiable and apply equally to `protobufs-ee`.

### AIP-INV-1: Strictly follow Google AIP

Every resource, RPC, request/response message, list pagination, filter
expression, long-running operation, and error model **must** follow
[Google AIP](https://google.aip.dev/) — no exceptions for convenience.
The concrete AIPs this repo adheres to:

| AIP                                 | Use for                                                                                |
| ----------------------------------- | -------------------------------------------------------------------------------------- |
| [AIP-121](https://google.aip.dev/121) | Resource-oriented design                                                               |
| [AIP-122](https://google.aip.dev/122) | Resource names                                                                         |
| [AIP-123](https://google.aip.dev/123) | Resource types (`api.instill.tech/<Resource>`)                                         |
| [AIP-131](https://google.aip.dev/131) | `Get<Resource>` — standard read                                                        |
| [AIP-132](https://google.aip.dev/132) | `List<Resource>s` — standard list with `page_size` / `page_token` / `total_size`       |
| [AIP-133](https://google.aip.dev/133) | `Create<Resource>` — parent + `<resource>_id` + `<resource>` body                      |
| [AIP-134](https://google.aip.dev/134) | `Update<Resource>` — resource body + `google.protobuf.FieldMask update_mask`           |
| [AIP-135](https://google.aip.dev/135) | `Delete<Resource>` — `name` identifies the target                                      |
| [AIP-136](https://google.aip.dev/136) | Custom methods (action verbs)                                                          |
| [AIP-154](https://google.aip.dev/154) | Soft-delete                                                                            |
| [AIP-160](https://google.aip.dev/160) | Filter expression grammar in `ListXRequest.filter`                                     |
| [AIP-161](https://google.aip.dev/161) | `google.protobuf.FieldMask` semantics                                                  |
| [AIP-163](https://google.aip.dev/163) | Change validation (field behavior, `OUTPUT_ONLY` / `REQUIRED` / `OPTIONAL` / `IMMUTABLE`) |
| [AIP-192](https://google.aip.dev/192) | Documentation (every field requires a comment)                                         |
| [AIP-203](https://google.aip.dev/203) | Field behavior annotations (`google.api.field_behavior`)                               |

When introducing a new RPC or message, the first reviewer question is
"which AIP does this implement?" — if the answer is "none", the PR is
malformed.

### AIP-INV-2: Resource messages follow a constant field layout

Every resource message (anything declared with `option (google.api.resource)`
— collections, files, knowledge bases, chunks, agents, chats, etc.) **must**
use the following field layout. Field numbers are part of the contract: they
do not shift per resource, because the union of all resources is scanned by
code generators, UI renderers, and export pipelines that rely on the
positional meaning.

```proto
message <Resource> {
  option (google.api.resource) = {
    type: "api.instill.tech/<Resource>"
    pattern: "<collection>/{<id>}/..."
  };

  // ===== Standard AIP fields 1-6 (ALL resources must follow this order) =====

  // Field 1: Canonical resource name. OUTPUT_ONLY.
  // Format: `<collection>/{<id>}/...`
  string name = 1 [(google.api.field_behavior) = OUTPUT_ONLY];

  // Field 2: Immutable canonical resource ID (80-96 bits entropy, base62).
  // OUTPUT_ONLY. Example: "kb-8f3a2k9E7c1".
  string id = 2 [(google.api.field_behavior) = OUTPUT_ONLY];

  // Field 3: Human-readable display name for UI. REQUIRED.
  string display_name = 3 [(google.api.field_behavior) = REQUIRED];

  // Field 4: URL-friendly slug (NO prefix). OPTIONAL.
  // Server generates from display_name if omitted. Slug is NOT identity.
  string slug = 4 [(google.api.field_behavior) = OPTIONAL];

  // Field 5: Previous slugs kept for backward compatibility. OUTPUT_ONLY.
  repeated string aliases = 5 [(google.api.field_behavior) = OUTPUT_ONLY];

  // Field 6: Optional description. OPTIONAL.
  string description = 6 [(google.api.field_behavior) = OPTIONAL];

  // ===== Timestamps (common to all resources) =====

  // Field 7: Creation time. OUTPUT_ONLY.
  google.protobuf.Timestamp create_time = 7 [(google.api.field_behavior) = OUTPUT_ONLY];

  // Field 8: Last update time. OUTPUT_ONLY.
  google.protobuf.Timestamp update_time = 8 [(google.api.field_behavior) = OUTPUT_ONLY];

  // ===== Resource-specific fields start at field 9 =====

  // ... anything else ...
}
```

Rules that follow from the shape:

1. **No field renumbering, ever.** Changing a field number is a wire-breaking
   change even on unstable (`v1alpha`/`v1beta`) packages — consumers rely on
   the positional meaning of 1-8. `buf breaking` enforces this.
2. **Fields 1-6 are reserved for the AIP identity block.** If a resource
   genuinely does not need a field (e.g., `slug` on an ephemeral resource),
   reserve the number (`reserved 4;`) rather than reusing it for something
   else.
3. **`name` is the canonical resource name**, not the display name — it
   matches the `pattern` in `option (google.api.resource)` exactly.
   Parent-child resources chain collections (`namespaces/{namespace}/knowledge-bases/{knowledge_base}/files/{file}`).
4. **`id` is opaque, immutable, server-assigned.** Format is
   `<prefix>-<base62-random>` (e.g. `kb-`, `col-`, `file-`, `prj-`). The
   prefix is part of the stable ABI — downstream code uses it for
   mention-tag routing and entity-type detection. When adding a new resource,
   pick a short, collision-free prefix and record it in the resource's proto
   comment.
5. **`display_name` is the only required human-readable field.** Every
   surface (CLI, console, SDK) renders it; therefore it must never be empty
   on create.
6. **Every field carries `google.api.field_behavior`** (AIP-203). Ambiguous
   fields get rejected at lint time.
7. **Canonical reference is `artifact/v1alpha/knowledge_base.proto`.** When
   in doubt, copy its layout — not an older resource that predates this
   invariant.

Request/response messages mirror the AIP-131..135 shapes verbatim:
`Get<Resource>Request{name}`, `List<Resource>sRequest{parent, page_size,
page_token, filter}`, `Create<Resource>Request{parent, <resource>}`,
`Update<Resource>Request{<resource>, update_mask}`,
`Delete<Resource>Request{name}`. Do not invent new request shapes for
operations that are really just the five standard methods in disguise.

### AIP-INV-3: Custom method URLs use `/` not `:`

Google AIP-136 recommends `POST /v1/{name=…}:actionName` for custom
actions. We **must not** use the colon form in any `google.api.http`
binding, for a single concrete reason: the Instill api-gateway runs on
KrakenD, and KrakenD's URL router does not match routes that contain
`:` inside a path segment (it treats them as dynamic-endpoint markers at
the config layer, which breaks the route entirely — the request returns
404 before it ever reaches the backend). See
[`api-gateway-ee/AGENTS.md`](../api-gateway-ee/AGENTS.md) for the
gateway-side contract.

Therefore every custom action uses a slash-separated kebab-case noun:

```proto
// CORRECT — works through KrakenD
rpc ReprocessFile(ReprocessFileRequest) returns (ReprocessFileResponse) {
  option (google.api.http) = {
    post: "/v1alpha/{name=namespaces/*/knowledge-bases/*/files/*}/reprocess"
    body: "*"
  };
}

rpc SearchChunks(SearchChunksRequest) returns (SearchChunksResponse) {
  option (google.api.http) = {
    post: "/v1alpha/{parent=namespaces/*}/search-chunks"
    body: "*"
  };
}

// FORBIDDEN — KrakenD will not route this
// post: "/v1alpha/{name=namespaces/*/knowledge-bases/*/files/*}:reprocess"
// post: "/v1alpha/{parent=namespaces/*}:searchChunks"
```

Naming guidance for the action segment:

- Use kebab-case for multi-word actions (`search-chunks`, `download-url`,
  `reset-embeddings`) — stays readable and matches the rest of the URL.
- Use a noun or imperative verb that reads well at the end of the path;
  prefer `/reprocess` over `/do-reprocess`.
- Keep the RPC name itself in AIP-136 `PascalCase` verb form
  (`ReprocessFile`, `SearchChunks`) — only the URL segment changes.

A grep that must return zero matches in both proto repos:

```shell
rg '(get|post|put|patch|delete):\s*"[^"]*\}:[a-zA-Z]' --glob '*.proto'
```

If that command finds anything, the gateway will silently 404 the route
at runtime and every integration test against it will fail without a
clear signal — fix the URL to use `/` before merging.

### AIP-INV-4: Run `buf breaking` and `buf lint` before merging

`make gen && make openapi && buf lint && buf breaking --against '.git#branch=main'`
must all pass locally. The AIP invariants above are reinforced by the
`STANDARD + COMMENT_*` rule set declared in `buf.yaml`, but the
layout-ordering rule (AIP-INV-2) is enforced by reviewer discipline, not
by the linter — so it is called out explicitly here.
