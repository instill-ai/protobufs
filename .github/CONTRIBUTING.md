# Contributing Guidelines

We appreciate your contribution to this amazing project! Any form of engagement is welcome, including but not limiting to

- feature request
- documentation wording
- bug report
- roadmap suggestion
- ...and so on!

## Introduction

Before delving into the details to come up with your first PR, please
familiarize yourself with the project structure of 🔮 [**Instill
Core**](https://github.com/instill-ai/instill-core).

Instill AI contracts are defined as [Protocol
Buffers](https://protobuf.dev/). The proto files are the source from which
different code is auto-generated (e.g., language SDKs, OpenAPI
specification of the contracts).

### OpenAPI Contracts

All the public endpoints are exposed in a single service
([`api-gateway`](https://github.com/instill-ai/api-gateway)]). These
endpoints are documented [in OpenAPI V2
format](../openapi/v2/service.swagger.yaml) and publicly available at
[openapi.instill-ai.dev](https://openapi.instill-ai.dev/) through
(readme.com)[https://readme.com]. The OpenAPI specification is
auto-generated via [`grpc-gateway`](https://grpc-ecosystem.github.io/grpc-gateway/)
and it only reflects the protobuf specification.

## Codebase Contribution

The Instill AI contracts follow most of the guidelines provided by [Google
AIP](https://google.aip.dev/) but have made adjustments in certain areas
based on our product experience and specific needs.

Some of these conventions are checked at the CI workflows, though for some
others we rely on the developer's awareness and good judgement. Please,
use the following guidelines to align your contract updates with our
conventions.

### Field Behavior

APIs **MUST** apply the `google.api.field_behavior` annotation on every
field on a message or sub-message used in a request. Even `optional` fields
must include this annotation in order to keep annotations consistent.

This helps users to understand how an endpoint works. Annotations also
[modify the generated OpenAPI
spec](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/customizing_openapi_output/#using-googleapifield_behavior)
marking fields as `required` or `readonly`.

### Method Tags

Every **public** endpoint **MUST** have one (and only one) tag. This tag
**MUST** also be defined in the [OpenAPI
configuration](../openapi/v2/conf.proto) with a name and description. The
tag can be added with `grpc-gateway`'s `tags` operation option:

```proto
// Get a pipeline
//
// Returns the details of a pipeline.
rpc GetNamespacePipeline(GetNamespacePipelineRequest) returns (GetNamespacePipelineResponse) {
    option (google.api.http) = {get: "/v1beta/namespaces/{namespace_id}/pipelines/{pipeline_id}"};
    option (grpc.gateway.protoc_gen_openapiv2.options.openapiv2_operation) = {tags: "Pipeline"};
}
```

We tend to group our endpoints by service (i.e., use a single tag for all
the endpoints in a service), though this isn't a hard requirement.

[openapi.instill-ai.dev](https://openapi.instill-ai.dev) groups the endpoints
under the first tag defined in their specification and supports exactly one
tag. If more tags are defined, it will result in empty sections at the end
of the sidebar.

### Method Title & Description

Every **public** method **MUST** have a comment with a title and a
description, separated by a blank comment line. The description might have
several paragraphs separated by blank lines. Try to document the endpoint
in detail, including behaviors such as who can access a given resource of
perform an operation, how to access the result of the operation or if the
endpoint produces any effect in the system that might not be obvious.

```proto
// Update a pipeline
//
// Udpates a pipeline, accessing it by its resource name, which is defined by
// the parent namespace and the ID of the pipeline. The authenticated namespace must be
// the parent of the pipeline in order to modify it.
//
// In REST requests, only the supplied pipeline fields will be taken into
// account when updating the resource.
rpc UpdateNamespacePipeline(UpdateNamespacePipelineRequest) returns (UpdateNamespacePipelineResponse) {
    option (google.api.http) = {
        patch: "/v1beta/namespaces/{namespace_id}/pipelines/{pipeline_id}"
        body: "pipeline"
    };
}
```

[openapi.instill-ai.dev](https://openapi.instill-ai.dev) will render each part
as the endpoint title (which can also used in the search engine) and the
description in the endpoint's view.

### Swagger Extensions

The [Swagger
Extension](https://swagger.io/docs/specification/2-0/swagger-extensions/)
`x-stage` **MUST** be present in every **public** method for endpoints in
_alpha_ or _beta_ stage. This extension can be added with the
`openapiv2_operation` option:

```proto
// Get a pipeline
//
// Returns the details of a pipeline.
rpc GetNamespacePipeline(GetNamespacePipelineRequest) returns (GetNamespacePipelineResponse) {
    option (google.api.http) = {get: "/v1beta/namespaces/{namespace_id}/pipelines/{pipeline_id}"};
    option (grpc.gateway.protoc_gen_openapiv2.options.openapiv2_operation) = {
    tags: "Pipeline"
    extensions: {
        key: "x-stage"
            value {string_value: "beta"}
        }
    };
}
```

This is used in the C# SDK generator to warn about the stage of the
endpoints

## Sending PRs

Please take these general guidelines into consideration when you are sending a PR:

1. **Fork the Repository:** Begin by forking the repository to your GitHub account.
2. **Create a New Branch:** Create a new branch to house your work. Use a clear and descriptive name, like `<your-github-username>/<what-your-pr-about>`.
3. **Make and Commit Changes:** Implement your changes and commit them. We encourage you to follow these best practices for commits to ensure an efficient review process:
   - Adhere to the [conventional commits guidelines](https://www.conventionalcommits.org/) for meaningful commit messages.
   - Follow the [7 rules of commit messages](https://chris.beams.io/posts/git-commit/) for well-structured and informative commits.
   - Rearrange commits to squash trivial changes together, if possible. Utilize [git rebase](http://gitready.com/advanced/2009/03/20/reorder-commits-with-rebase.html) for this purpose.
4. **Push to Your Branch:** Push your branch to your GitHub repository: `git push origin feat/<your-feature-name>`.
5. **Open a Pull Request:** Initiate a pull request to our repository. Our team will review your changes and collaborate with you on any necessary refinements.

When you are ready to send a PR, we recommend you to first open a `draft` one. This will trigger a bunch of `tests` [workflows](https://github.com/instill-ai/connector-ai/tree/main/.github/workflows) running a thorough test suite on multiple platforms. After the tests are done and passed, you can now mark the PR `open` to notify the codebase owners to review. We appreciate your endeavour to pass the integration test for your PR to make sure the sanity with respect to the entire scope of **Instill Core**.

## Last words

Your contributions make a difference. Let's build something amazing together!
