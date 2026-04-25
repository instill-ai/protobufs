# Resource message layout

## AIP-INV-2: Resource messages follow a constant field layout

Every resource message (anything declared with `option (google.api.resource)` — collections, files, knowledge bases, chunks, agents, chats, etc.) **must** use the following field layout. Field numbers are part of the contract: they do not shift per resource, because the union of all resources is scanned by code generators, UI renderers, and export pipelines that rely on the positional meaning.

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

1. **No field renumbering, ever.** Changing a field number is a wire-breaking change even on unstable (`v1alpha`/`v1beta`) packages — consumers rely on the positional meaning of 1-8. `buf breaking` enforces this.
2. **Fields 1-6 are reserved for the AIP identity block.** If a resource genuinely does not need a field (e.g., `slug` on an ephemeral resource), reserve the number (`reserved 4;`) rather than reusing it for something else.
3. **`name` is the canonical resource name**, not the display name — it matches the `pattern` in `option (google.api.resource)` exactly. Parent-child resources chain collections (`namespaces/{namespace}/knowledge-bases/{knowledge_base}/files/{file}`).
4. **`id` is opaque, immutable, server-assigned.** Format is `<prefix>-<base62-random>` (e.g. `kb-`, `col-`, `file-`, `prj-`). The prefix is part of the stable ABI — downstream code uses it for mention-tag routing and entity-type detection. When adding a new resource, pick a short, collision-free prefix and record it in the resource's proto comment.
5. **`display_name` is the only required human-readable field.** Every surface (CLI, console, SDK) renders it; therefore it must never be empty on create.
6. **Every field carries `google.api.field_behavior`** (AIP-203). Ambiguous fields get rejected at lint time.
7. **Canonical reference is `artifact/v1alpha/knowledge_base.proto`.** When in doubt, copy its layout — not an older resource that predates this invariant.

Request/response messages mirror the AIP-131..135 shapes verbatim: `Get<Resource>Request{name}`, `List<Resource>sRequest{parent, page_size, page_token, filter}`, `Create<Resource>Request{parent, <resource>}`, `Update<Resource>Request{<resource>, update_mask}`, `Delete<Resource>Request{name}`. Do not invent new request shapes for operations that are really just the five standard methods in disguise.
