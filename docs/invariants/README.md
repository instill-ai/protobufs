# protobufs invariants

This folder is the on-demand index of `AIP-INV-*` invariants for the OSS protobufs repo. Read only the file that matches the change you are making — the AGENTS.md file deliberately keeps this section short so it does not auto-load on every Cursor session.

## Index

| File                       | Invariants                | Topic                                                                |
| -------------------------- | ------------------------- | -------------------------------------------------------------------- |
| `aip-compliance.md`        | AIP-INV-1, AIP-INV-4      | AIP rule set the repo follows; pre-merge `buf lint` / `buf breaking` |
| `resource-layout.md`       | AIP-INV-2                 | Standard field 1-8 layout for resource messages                      |
| `custom-method-urls.md`    | AIP-INV-3                 | Slash-separated custom-method URLs (KrakenD compatibility)           |

## Cross-cutting rules

- Edit `.proto` sources only. Regenerate `gen/` and `openapi/v2/service.swagger.yaml` via the `make` targets — do not hand-edit generated output.
- Every new RPC or message must answer the reviewer question "which AIP does this implement?". If the answer is "none", the change is malformed.
- The KrakenD URL invariant (`AIP-INV-3`) has a paired contract on the gateway side; see `api-gateway/AGENTS.md` for the runtime check.
