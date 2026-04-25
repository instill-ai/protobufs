# Custom method URL shape

## AIP-INV-3: Custom method URLs use `/` not `:`

Google AIP-136 recommends `POST /v1/{name=…}:actionName` for custom actions. We **must not** use the colon form in any `google.api.http` binding, for a single concrete reason: the Instill api-gateway runs on KrakenD, and KrakenD's URL router does not match routes that contain `:` inside a path segment (it treats them as dynamic-endpoint markers at the config layer, which breaks the route entirely — the request returns 404 before it ever reaches the backend). See [`api-gateway/AGENTS.md`](../../../api-gateway/AGENTS.md) for the gateway-side contract.

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

- Use kebab-case for multi-word actions (`search-chunks`, `download-url`, `reset-embeddings`) — stays readable and matches the rest of the URL.
- Use a noun or imperative verb that reads well at the end of the path; prefer `/reprocess` over `/do-reprocess`.
- Keep the RPC name itself in AIP-136 `PascalCase` verb form (`ReprocessFile`, `SearchChunks`) — only the URL segment changes.

A grep that must return zero matches in this repo:

```shell
rg '(get|post|put|patch|delete):\s*"[^"]*\}:[a-zA-Z]' --glob '*.proto'
```

If that command finds anything, the gateway will silently 404 the route at runtime and every integration test against it will fail without a clear signal — fix the URL to use `/` before merging.
