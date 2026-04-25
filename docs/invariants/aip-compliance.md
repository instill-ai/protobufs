# AIP compliance

This repo is the wire contract for every Instill backend. Shape drift here costs every downstream SDK (`protogen-go`, `protogen-python`, `console`, `python-sdk`) and every gateway route. The following rules are non-negotiable.

## AIP-INV-1: Strictly follow Google AIP

Every resource, RPC, request/response message, list pagination, filter expression, long-running operation, and error model **must** follow [Google AIP](https://google.aip.dev/) — no exceptions for convenience. The concrete AIPs this repo adheres to:

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

When introducing a new RPC or message, the first reviewer question is "which AIP does this implement?" — if the answer is "none", the PR is malformed.

## AIP-INV-4: Run `buf breaking` and `buf lint` before merging

`make gen && make openapi && buf lint && buf breaking --against '.git#branch=main'` must all pass locally. The AIP invariants in this folder are reinforced by the `STANDARD + COMMENT_*` rule set declared in `buf.yaml`, but the layout-ordering rule (AIP-INV-2) is enforced by reviewer discipline, not by the linter — so it is called out explicitly in `resource-layout.md`.
