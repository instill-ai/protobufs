# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [pipeline/pipeline.proto](#pipeline/pipeline.proto)
    - [CreatePipelineRequest](#instill.pipeline.CreatePipelineRequest)
    - [DeletePipelineRequest](#instill.pipeline.DeletePipelineRequest)
    - [Destination](#instill.pipeline.Destination)
    - [GetPipelineRequest](#instill.pipeline.GetPipelineRequest)
    - [HealthCheckResponse](#instill.pipeline.HealthCheckResponse)
    - [ListPipelinesRequest](#instill.pipeline.ListPipelinesRequest)
    - [ListPipelinesResponse](#instill.pipeline.ListPipelinesResponse)
    - [Model](#instill.pipeline.Model)
    - [PipelineInfo](#instill.pipeline.PipelineInfo)
    - [Recipe](#instill.pipeline.Recipe)
    - [Scheduler](#instill.pipeline.Scheduler)
    - [Source](#instill.pipeline.Source)
    - [TriggerPipelineContent](#instill.pipeline.TriggerPipelineContent)
    - [TriggerPipelineRequest](#instill.pipeline.TriggerPipelineRequest)
    - [UpdatePipelineRequest](#instill.pipeline.UpdatePipelineRequest)

    - [HealthCheckResponse.ServingStatusCode](#instill.pipeline.HealthCheckResponse.ServingStatusCode)
    - [ListPipelinesRequest.View](#instill.pipeline.ListPipelinesRequest.View)

    - [Pipeline](#instill.pipeline.Pipeline)

- [Scalar Value Types](#scalar-value-types)



<a name="pipeline/pipeline.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## pipeline/pipeline.proto



<a name="instill.pipeline.CreatePipelineRequest"></a>

### CreatePipelineRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| active | [bool](#bool) |  |  |
| recipe | [Recipe](#instill.pipeline.Recipe) |  |  |






<a name="instill.pipeline.DeletePipelineRequest"></a>

### DeletePipelineRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="instill.pipeline.Destination"></a>

### Destination



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  |  |
| name | [string](#string) |  |  |






<a name="instill.pipeline.GetPipelineRequest"></a>

### GetPipelineRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="instill.pipeline.HealthCheckResponse"></a>

### HealthCheckResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [HealthCheckResponse.ServingStatusCode](#instill.pipeline.HealthCheckResponse.ServingStatusCode) |  |  |
| status | [string](#string) |  |  |






<a name="instill.pipeline.ListPipelinesRequest"></a>

### ListPipelinesRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| page_size | [int32](#int32) |  |  |
| page_token | [string](#string) |  |  |
| view | [ListPipelinesRequest.View](#instill.pipeline.ListPipelinesRequest.View) |  |  |






<a name="instill.pipeline.ListPipelinesResponse"></a>

### ListPipelinesResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| contents | [PipelineInfo](#instill.pipeline.PipelineInfo) | repeated |  |
| next_page_token | [string](#string) |  |  |






<a name="instill.pipeline.Model"></a>

### Model



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| version | [int32](#int32) |  |  |






<a name="instill.pipeline.PipelineInfo"></a>

### PipelineInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  |  |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| active | [bool](#bool) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| updated_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| recipe | [Recipe](#instill.pipeline.Recipe) |  |  |
| full_name | [string](#string) |  |  |






<a name="instill.pipeline.Recipe"></a>

### Recipe



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| source | [Source](#instill.pipeline.Source) |  |  |
| destination | [Destination](#instill.pipeline.Destination) |  |  |
| model | [Model](#instill.pipeline.Model) | repeated |  |






<a name="instill.pipeline.Scheduler"></a>

### Scheduler



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| crontab | [string](#string) |  |  |






<a name="instill.pipeline.Source"></a>

### Source



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  |  |
| name | [string](#string) |  |  |
| scheduler | [Scheduler](#instill.pipeline.Scheduler) |  |  |






<a name="instill.pipeline.TriggerPipelineContent"></a>

### TriggerPipelineContent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| url | [string](#string) |  |  |
| base64 | [string](#string) |  |  |
| chunk | [bytes](#bytes) |  |  |






<a name="instill.pipeline.TriggerPipelineRequest"></a>

### TriggerPipelineRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| contents | [TriggerPipelineContent](#instill.pipeline.TriggerPipelineContent) | repeated |  |






<a name="instill.pipeline.UpdatePipelineRequest"></a>

### UpdatePipelineRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pipeline | [PipelineInfo](#instill.pipeline.PipelineInfo) |  |  |
| update_mask | [google.protobuf.FieldMask](#google.protobuf.FieldMask) |  |  |








<a name="instill.pipeline.HealthCheckResponse.ServingStatusCode"></a>

### HealthCheckResponse.ServingStatusCode


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| SERVING | 1 |  |
| NOT_SERVING | 2 |  |
| SERVICE_UNKNOWN | 3 | Used only by the Watch method. |



<a name="instill.pipeline.ListPipelinesRequest.View"></a>

### ListPipelinesRequest.View


| Name | Number | Description |
| ---- | ------ | ----------- |
| VIEW_UNSPECIFIED | 0 |  |
| BASIC | 1 |  |
| WITH_RECIPE | 2 |  |







<a name="instill.pipeline.Pipeline"></a>

### Pipeline


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Liveness | [.google.protobuf.Empty](#google.protobuf.Empty) | [HealthCheckResponse](#instill.pipeline.HealthCheckResponse) |  |
| Readiness | [.google.protobuf.Empty](#google.protobuf.Empty) | [HealthCheckResponse](#instill.pipeline.HealthCheckResponse) |  |
| CreatePipeline | [CreatePipelineRequest](#instill.pipeline.CreatePipelineRequest) | [PipelineInfo](#instill.pipeline.PipelineInfo) |  |
| ListPipelines | [ListPipelinesRequest](#instill.pipeline.ListPipelinesRequest) | [ListPipelinesResponse](#instill.pipeline.ListPipelinesResponse) |  |
| GetPipeline | [GetPipelineRequest](#instill.pipeline.GetPipelineRequest) | [PipelineInfo](#instill.pipeline.PipelineInfo) |  |
| UpdatePipeline | [UpdatePipelineRequest](#instill.pipeline.UpdatePipelineRequest) | [PipelineInfo](#instill.pipeline.PipelineInfo) |  |
| DeletePipeline | [DeletePipelineRequest](#instill.pipeline.DeletePipelineRequest) | [.google.protobuf.Empty](#google.protobuf.Empty) |  |
| TriggerPipelineByUpload | [TriggerPipelineRequest](#instill.pipeline.TriggerPipelineRequest) stream | [.google.protobuf.Struct](#google.protobuf.Struct) |  |





## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |
