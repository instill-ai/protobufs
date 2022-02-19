# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [model/model.proto](#model/model.proto)
    - [BoundingBoxPrediction](#instill.model.BoundingBoxPrediction)
    - [Box](#instill.model.Box)
    - [ClassificationOutput](#instill.model.ClassificationOutput)
    - [ClassificationOutputs](#instill.model.ClassificationOutputs)
    - [CreateModelRequest](#instill.model.CreateModelRequest)
    - [CreateModelsResponse](#instill.model.CreateModelsResponse)
    - [DeleteModelRequest](#instill.model.DeleteModelRequest)
    - [DetectionOutput](#instill.model.DetectionOutput)
    - [DetectionOutputs](#instill.model.DetectionOutputs)
    - [GetModelRequest](#instill.model.GetModelRequest)
    - [HealthCheckResponse](#instill.model.HealthCheckResponse)
    - [ListModelRequest](#instill.model.ListModelRequest)
    - [ListModelResponse](#instill.model.ListModelResponse)
    - [LoadModelRequest](#instill.model.LoadModelRequest)
    - [LoadModelResponse](#instill.model.LoadModelResponse)
    - [ModelInfo](#instill.model.ModelInfo)
    - [ModelVersion](#instill.model.ModelVersion)
    - [PredictModelRequest](#instill.model.PredictModelRequest)
    - [UnloadModelRequest](#instill.model.UnloadModelRequest)
    - [UnloadModelResponse](#instill.model.UnloadModelResponse)
    - [UpdateModelInfo](#instill.model.UpdateModelInfo)
    - [UpdateModelRequest](#instill.model.UpdateModelRequest)
  
    - [CreateModelRequest.CVTask](#instill.model.CreateModelRequest.CVTask)
    - [ModelStatus](#instill.model.ModelStatus)
  
    - [Model](#instill.model.Model)
  
- [Scalar Value Types](#scalar-value-types)



<a name="model/model.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## model/model.proto



<a name="instill.model.BoundingBoxPrediction"></a>

### BoundingBoxPrediction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [string](#string) |  |  |
| score | [float](#float) |  |  |
| box | [Box](#instill.model.Box) |  |  |






<a name="instill.model.Box"></a>

### Box



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| top | [float](#float) |  |  |
| left | [float](#float) |  |  |
| width | [float](#float) |  |  |
| height | [float](#float) |  |  |






<a name="instill.model.ClassificationOutput"></a>

### ClassificationOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [string](#string) |  |  |
| score | [float](#float) |  |  |






<a name="instill.model.ClassificationOutputs"></a>

### ClassificationOutputs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| contents | [ClassificationOutput](#instill.model.ClassificationOutput) | repeated |  |






<a name="instill.model.CreateModelRequest"></a>

### CreateModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| content | [bytes](#bytes) |  |  |
| type | [string](#string) |  |  |
| framework | [string](#string) |  |  |
| description | [string](#string) |  |  |
| optimized | [bool](#bool) |  |  |
| visibility | [string](#string) |  |  |
| cv_task | [CreateModelRequest.CVTask](#instill.model.CreateModelRequest.CVTask) |  | CV task type such as object detection, classification |






<a name="instill.model.CreateModelsResponse"></a>

### CreateModelsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| models | [ModelInfo](#instill.model.ModelInfo) | repeated |  |






<a name="instill.model.DeleteModelRequest"></a>

### DeleteModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="instill.model.DetectionOutput"></a>

### DetectionOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| contents | [BoundingBoxPrediction](#instill.model.BoundingBoxPrediction) | repeated |  |






<a name="instill.model.DetectionOutputs"></a>

### DetectionOutputs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| contents | [DetectionOutput](#instill.model.DetectionOutput) | repeated |  |






<a name="instill.model.GetModelRequest"></a>

### GetModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="instill.model.HealthCheckResponse"></a>

### HealthCheckResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status | [int32](#int32) |  |  |






<a name="instill.model.ListModelRequest"></a>

### ListModelRequest







<a name="instill.model.ListModelResponse"></a>

### ListModelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| models | [ModelInfo](#instill.model.ModelInfo) | repeated |  |






<a name="instill.model.LoadModelRequest"></a>

### LoadModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="instill.model.LoadModelResponse"></a>

### LoadModelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sizeInBytes | [uint64](#uint64) |  | OPTIONAL - If nontrivial cost is involved in determining the size, return 0 here and do the sizing in the modelSize function |
| maxConcurrency | [uint32](#uint32) |  | EXPERIMENTAL - Applies only if limitModelConcurrency = true was returned from runtimeStatus rpc. See RuntimeStatusResponse.limitModelConcurrency for more detail |






<a name="instill.model.ModelInfo"></a>

### ModelInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [int32](#int32) |  |  |
| name | [string](#string) |  |  |
| optimized | [bool](#bool) |  |  |
| description | [string](#string) |  |  |
| type | [string](#string) |  |  |
| framework | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| updated_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| organization | [string](#string) |  |  |
| visibility | [string](#string) |  |  |
| versions | [ModelVersion](#instill.model.ModelVersion) | repeated |  |
| icon | [string](#string) |  |  |
| Author | [string](#string) |  |  |
| fullName | [string](#string) |  |  |






<a name="instill.model.ModelVersion"></a>

### ModelVersion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [int32](#int32) |  |  |
| model_id | [int32](#int32) |  |  |
| description | [string](#string) |  |  |
| created_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| updated_at | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| status | [ModelStatus](#instill.model.ModelStatus) |  |  |






<a name="instill.model.PredictModelRequest"></a>

### PredictModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | model name |
| version | [int32](#int32) |  | model version |
| content | [bytes](#bytes) |  | byte array of image content |






<a name="instill.model.UnloadModelRequest"></a>

### UnloadModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="instill.model.UnloadModelResponse"></a>

### UnloadModelResponse







<a name="instill.model.UpdateModelInfo"></a>

### UpdateModelInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| status | [ModelStatus](#instill.model.ModelStatus) |  |  |






<a name="instill.model.UpdateModelRequest"></a>

### UpdateModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| model | [UpdateModelInfo](#instill.model.UpdateModelInfo) |  |  |
| update_mask | [google.protobuf.FieldMask](#google.protobuf.FieldMask) |  |  |





 


<a name="instill.model.CreateModelRequest.CVTask"></a>

### CreateModelRequest.CVTask


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED | 0 |  |
| CLASSIFICATION | 1 |  |
| DETECTION | 2 |  |



<a name="instill.model.ModelStatus"></a>

### ModelStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| OFFLINE | 0 |  |
| ONLINE | 1 |  |
| ERROR | 2 |  |


 

 


<a name="instill.model.Model"></a>

### Model


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Liveness | [.google.protobuf.Empty](#google.protobuf.Empty) | [HealthCheckResponse](#instill.model.HealthCheckResponse) |  |
| Readiness | [.google.protobuf.Empty](#google.protobuf.Empty) | [HealthCheckResponse](#instill.model.HealthCheckResponse) |  |
| CreateModelByUpload | [CreateModelRequest](#instill.model.CreateModelRequest) stream | [CreateModelsResponse](#instill.model.CreateModelsResponse) |  |
| CreateModel | [CreateModelRequest](#instill.model.CreateModelRequest) | [CreateModelsResponse](#instill.model.CreateModelsResponse) |  |
| UpdateModel | [UpdateModelRequest](#instill.model.UpdateModelRequest) | [ModelInfo](#instill.model.ModelInfo) |  |
| PredictModelByUpload | [PredictModelRequest](#instill.model.PredictModelRequest) stream | [.google.protobuf.Struct](#google.protobuf.Struct) | This method handle upload file request |
| PredictModel | [PredictModelRequest](#instill.model.PredictModelRequest) | [.google.protobuf.Struct](#google.protobuf.Struct) | This method handle request with file in body such as url/base64 encode |
| ListModels | [ListModelRequest](#instill.model.ListModelRequest) | [ListModelResponse](#instill.model.ListModelResponse) |  |
| GetModel | [GetModelRequest](#instill.model.GetModelRequest) | [ModelInfo](#instill.model.ModelInfo) |  |
| DeleteModel | [DeleteModelRequest](#instill.model.DeleteModelRequest) | [.google.protobuf.Empty](#google.protobuf.Empty) |  |

 



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

