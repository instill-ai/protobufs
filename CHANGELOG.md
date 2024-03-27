# Changelog

## [0.4.0-alpha](https://github.com/instill-ai/protobufs/compare/v0.3.3-alpha...v0.4.0-alpha) (2024-03-27)


### Features

* **artifact:** add services ([#269](https://github.com/instill-ai/protobufs/issues/269)) ([c7f99b2](https://github.com/instill-ai/protobufs/commit/c7f99b28caa56eb73b299eac7f17645d0d542d60))
* **artifact:** add tag create / list endpoints ([#286](https://github.com/instill-ai/protobufs/issues/286)) ([6678571](https://github.com/instill-ai/protobufs/commit/667857142e141c21e6aa8bd59057e5f23031ead6))
* **artifact:** document optional tag fields ([#290](https://github.com/instill-ai/protobufs/issues/290)) ([b7348c6](https://github.com/instill-ai/protobufs/commit/b7348c630ac726d6c2c0d27981b7449cec0105ff))
* **controller:** add rpc methods for controller ([#144](https://github.com/instill-ai/protobufs/issues/144)) ([b31be1a](https://github.com/instill-ai/protobufs/commit/b31be1ad082e7e6d9ce8fe9b4183e2af45dfa8e5))
* **core:** add `Owner` message for embedding user and organization information ([#273](https://github.com/instill-ai/protobufs/issues/273)) ([3ec60b8](https://github.com/instill-ai/protobufs/commit/3ec60b8bf219a0b05a07459b30f955ea2892db99))
* **metric:** add protobuf ([#140](https://github.com/instill-ai/protobufs/issues/140)) ([aca0b4c](https://github.com/instill-ai/protobufs/commit/aca0b4cdb4216af7532b77349c437eea07f1c998))
* **mgmt:** add description field in subscription response ([#275](https://github.com/instill-ai/protobufs/issues/275)) ([4bf574c](https://github.com/instill-ai/protobufs/commit/4bf574cca4144500de053fe48be1d18db2042184))
* **mgmt:** add Stripe `status` and `trial_end` ([#268](https://github.com/instill-ai/protobufs/issues/268)) ([15d3669](https://github.com/instill-ai/protobufs/commit/15d36695a85011500217983a8b4f5915a25375c5))
* **mgmt:** refactor APIs for `Get` and `Patch` authenticated user ([#261](https://github.com/instill-ai/protobufs/issues/261)) ([0e4e9e6](https://github.com/instill-ai/protobufs/commit/0e4e9e684a3766b2b3529e5b1737f0a7c31eb67f))
* **mgmt:** refactor user/org profile and subscription endpoints ([#264](https://github.com/instill-ai/protobufs/issues/264)) ([b41e6f8](https://github.com/instill-ai/protobufs/commit/b41e6f867a6326869e2e8375916954389956a2fd))
* **model,pipeline,connector,controller,usage:** remove model instance ([#151](https://github.com/instill-ai/protobufs/issues/151)) ([a009e64](https://github.com/instill-ai/protobufs/commit/a009e64a23ba151dbb954b98dfe1fae49bce54ce))
* **model:** add instance segmentation task output ([#109](https://github.com/instill-ai/protobufs/issues/109)) ([e6b2490](https://github.com/instill-ai/protobufs/commit/e6b2490766fa4374fadbda4665fbe4cb91be28a3))
* **model:** add semantic segmentation output ([#115](https://github.com/instill-ai/protobufs/issues/115)) ([c0f8198](https://github.com/instill-ai/protobufs/commit/c0f8198d668d151e9792c4cd7f558727bac295b2))
* **model:** add text generation task ([#136](https://github.com/instill-ai/protobufs/issues/136)) ([94cc54f](https://github.com/instill-ai/protobufs/commit/94cc54fcf2cd90284918781c5b37046ba0b1f2e8))
* **model:** update chat_history schema to align with OpenAI message field ([#246](https://github.com/instill-ai/protobufs/issues/246)) ([dcc5ed1](https://github.com/instill-ai/protobufs/commit/dcc5ed1dea742bf6dd93f430323d1ede3f19bed4))
* **model:** Update Text-Generation Task Schema to Align with OpenAI Standards ([#243](https://github.com/instill-ai/protobufs/issues/243)) ([cd1acb9](https://github.com/instill-ai/protobufs/commit/cd1acb93a47935729f979332b12fe45120d195ab))
* **openapi:** keep public and private API docs in sync with main branch ([#270](https://github.com/instill-ai/protobufs/issues/270)) ([36c13f8](https://github.com/instill-ai/protobufs/commit/36c13f8632ee9ea455ac7281aff293aa90fb6c81))
* **usage:** add artifact usage data ([#266](https://github.com/instill-ai/protobufs/issues/266)) ([a688843](https://github.com/instill-ai/protobufs/commit/a6888434503abf2085d9dbdc0340b719d826593b))
* **usage:** use `AuthenticatedUser` message in usage collection ([#271](https://github.com/instill-ai/protobufs/issues/271)) ([a8196c1](https://github.com/instill-ai/protobufs/commit/a8196c12219ad9fb80a78c863b51c3bd7b75ef3b))
* **vdp:** add `CloneUserPipeline` and `CloneOrganizationPipeline` endpoints ([#257](https://github.com/instill-ai/protobufs/issues/257)) ([d11f8c4](https://github.com/instill-ai/protobufs/commit/d11f8c46c41bfec6013e22d1c47f813094f9938a))
* **vdp:** add CheckName endpoint ([#258](https://github.com/instill-ai/protobufs/issues/258)) ([e2ab83c](https://github.com/instill-ai/protobufs/commit/e2ab83c3e1582d304052aaa0573109d078b7b370))
* **vdp:** add component definition list endpoint ([#274](https://github.com/instill-ai/protobufs/issues/274)) ([16afda7](https://github.com/instill-ai/protobufs/commit/16afda749f34f607563edcce37c2412f399b14c8))
* **vdp:** add description field to component definitions ([#279](https://github.com/instill-ai/protobufs/issues/279)) ([938b02b](https://github.com/instill-ai/protobufs/commit/938b02bf8beb2b6b5d9112d1aabc01bb23d9b5cf))
* **vdp:** add release stage to component definitions ([#283](https://github.com/instill-ai/protobufs/issues/283)) ([8c20b4b](https://github.com/instill-ai/protobufs/commit/8c20b4b1d1d9343d7ea85d2925848d8ff6804f9e))
* **vdp:** add visibility param for list pipelines endpoints ([#256](https://github.com/instill-ai/protobufs/issues/256)) ([d739f8c](https://github.com/instill-ai/protobufs/commit/d739f8cb5419620fa2fef385e4e0f0b6b4c8bc46))
* **vdp:** extend component definitions ([#262](https://github.com/instill-ai/protobufs/issues/262)) ([d93f8e5](https://github.com/instill-ai/protobufs/commit/d93f8e5183f748edeca6f94683772d15c04e9ab4))
* **vdp:** remove openapi_specification and add data_specification ([#282](https://github.com/instill-ai/protobufs/issues/282)) ([c4cdf98](https://github.com/instill-ai/protobufs/commit/c4cdf98e23510d5937720ad74c5de7ad72bdc4c7))
* **vdp:** revamp pipeline recipe and introduce iterator component ([#281](https://github.com/instill-ai/protobufs/issues/281)) ([e128375](https://github.com/instill-ai/protobufs/commit/e1283758bb43f23b04d754e8a981a78bc8d32743))


### Bug Fixes

* **artifact:** remove unnecessary parent param in tag creation ([#291](https://github.com/instill-ai/protobufs/issues/291)) ([3c32980](https://github.com/instill-ai/protobufs/commit/3c32980c5601dfd50c1792e36b6b86a96d190a1a))
* **mgmt,billing:** refactor mgmt message, endpoints and add billing service ([#130](https://github.com/instill-ai/protobufs/issues/130)) ([366c0f8](https://github.com/instill-ai/protobufs/commit/366c0f8cda7e1a80fde14de0ce31b0fbbedd8160))
* **mgmt:** separate into admin and public services ([#133](https://github.com/instill-ai/protobufs/issues/133)) ([ddf0a4e](https://github.com/instill-ai/protobufs/commit/ddf0a4ea018ae45e30d0fb64a328ff87c3a6d02a))
* **model:** fix type inconsistency of field ExtraParamObject ([#240](https://github.com/instill-ai/protobufs/issues/240)) ([bf92376](https://github.com/instill-ai/protobufs/commit/bf92376a005104c7c771afc1f8abafa178935fe9))
* **openapi:** add readme.com extension for showing "Bearer" in auth ([#278](https://github.com/instill-ai/protobufs/issues/278)) ([a8c7a0c](https://github.com/instill-ai/protobufs/commit/a8c7a0ce7941bd6ba2e6afb791f77576c7cebed8))
* **vdp:** implement offset pagination in component list endpoint ([#277](https://github.com/instill-ai/protobufs/issues/277)) ([ef8c929](https://github.com/instill-ai/protobufs/commit/ef8c929354e7d4cdedf9b948821cdf6f64dc6967))

## [0.3.3-alpha](https://github.com/instill-ai/protobufs/compare/v0.3.2-alpha...v0.3.3-alpha) (2022-09-13)


### Miscellaneous Chores

* release v0.3.3-alpha ([b8f0cf7](https://github.com/instill-ai/protobufs/commit/b8f0cf72fb12a3a7bd3c885eeb2f815f587f1ca8))

## [0.3.2-alpha](https://github.com/instill-ai/protobufs/compare/v0.3.1-alpha...v0.3.2-alpha) (2022-09-13)


### Miscellaneous Chores

* release v0.3.2-alpha ([b5daaa2](https://github.com/instill-ai/protobufs/commit/b5daaa2926a03f6d8b3cd74ca1ba0d9e95b2ffdd))

## [0.3.1-alpha](https://github.com/instill-ai/protobufs/compare/v0.2.1-alpha...v0.3.1-alpha) (2022-08-17)


### Features

* **model:** add ocr output ([#94](https://github.com/instill-ai/protobufs/issues/94)) ([a84ed0d](https://github.com/instill-ai/protobufs/commit/a84ed0d2d5beef5be3d63d31907c2fbe61700413))


### Bug Fixes

* **model:** fix wrong field name ([1bdf2d3](https://github.com/instill-ai/protobufs/commit/1bdf2d3afdd2ff86baa590f373dea8c3dff93d4a))


### Miscellaneous Chores

* release v0.3.1-alpha ([78c9037](https://github.com/instill-ai/protobufs/commit/78c9037e2abafa00500a1b25ba126a900244f878))

## [0.2.1-alpha](https://github.com/instill-ai/protobufs/compare/v0.2.0-alpha...v0.2.1-alpha) (2022-07-07)


### Miscellaneous Chores

* release v0.2.1-alpha ([fa62c70](https://github.com/instill-ai/protobufs/commit/fa62c70dfce28a3980bd02ad33287c235620f1a7))

## [0.2.0-alpha](https://github.com/instill-ai/protobufs/compare/v0.1.5-alpha...v0.2.0-alpha) (2022-06-20)


### Features

* add mgmt-backend proto ([#62](https://github.com/instill-ai/protobufs/issues/62)) ([59f03aa](https://github.com/instill-ai/protobufs/commit/59f03aa2930d87b95b5688f67c9523db10497165))
* add usage package ([#74](https://github.com/instill-ai/protobufs/issues/74)) ([15a5103](https://github.com/instill-ai/protobufs/commit/15a5103a28675ff654241c6f5a40b49942a2bc3d))
* **connector:** add connect/disconnect custom rpc method ([87a40ab](https://github.com/instill-ai/protobufs/commit/87a40ab4778620dd03cb131b5c055b2c5063757b))
* **connector:** add protobuf ([#54](https://github.com/instill-ai/protobufs/issues/54)) ([f7f637b](https://github.com/instill-ai/protobufs/commit/f7f637bc719eabf98355b11f3e307ef1abdb5e10))
* **connector:** add read and write custom rpc methods ([0bdc41d](https://github.com/instill-ai/protobufs/commit/0bdc41d6522eca8e3fe211c0609443ddd3183348))
* **model:** add method create model by GitHub ([#49](https://github.com/instill-ai/protobufs/issues/49)) ([7ddc142](https://github.com/instill-ai/protobufs/commit/7ddc142c190964bd168875968610e84df3460943))


### Bug Fixes

* add v1alpha to health check endpoint ([4257891](https://github.com/instill-ai/protobufs/commit/42578915fdb4bc8e04d7b918b5305d68d19cc2c2))
* fix openapi using snake case ([#46](https://github.com/instill-ai/protobufs/issues/46)) ([fe755b7](https://github.com/instill-ai/protobufs/commit/fe755b71d09b0e83970e61a21570d10562bcb0aa))
* fix protoc-gen-openapiv2/options import issue ([26cc626](https://github.com/instill-ai/protobufs/commit/26cc626f40216685ad10c7e73b5ebf64083744f0))
* **model:** add optional view param for GET operation ([#70](https://github.com/instill-ai/protobufs/issues/70)) ([a739d95](https://github.com/instill-ai/protobufs/commit/a739d95d0f55750932fec2f771a5bed5389077ab))
* **model:** change configuration from struct to string ([#72](https://github.com/instill-ai/protobufs/issues/72)) ([77b02ea](https://github.com/instill-ai/protobufs/commit/77b02eaa10b98a9b0a5027da235ddba943257385))
* **model:** move github from model to model version ([#51](https://github.com/instill-ai/protobufs/issues/51)) ([03170d7](https://github.com/instill-ai/protobufs/commit/03170d7a131037906eecfc81173c7a29a492a1fb))
* **model:** support inferencing multiple files  ([#56](https://github.com/instill-ai/protobufs/issues/56)) ([c821464](https://github.com/instill-ai/protobufs/commit/c8214643c5b7019c4aef497e0b08e4d2f385b0b5))
* move buf.yaml into the module to fix usage package import error ([#75](https://github.com/instill-ai/protobufs/issues/75)) ([3b33ff4](https://github.com/instill-ai/protobufs/commit/3b33ff4119ed5f398904dd7a90f1559298e2bb2c))
* refactor mgmt-backend proto ([fc38f0d](https://github.com/instill-ai/protobufs/commit/fc38f0d7399c5ff6235b2621dc279945215966ce))

### [0.1.5-alpha](https://github.com/instill-ai/protobufs/compare/v0.1.4-alpha...v0.1.5-alpha) (2022-03-22)


### Bug Fixes

* fix naming discrepancies ([ce8a0e1](https://github.com/instill-ai/protobufs/commit/ce8a0e1364d9dc343765a34a4f6c30d3a32296fe))

### [0.1.4-alpha](https://github.com/instill-ai/protobufs/compare/v0.1.3-alpha...v0.1.4-alpha) (2022-03-21)


### Miscellaneous Chores

* release 0.1.4-alpha ([4a63531](https://github.com/instill-ai/protobufs/commit/4a635312c4f5ed94af91df34126e3944dfbcf972))

### [0.1.3-alpha](https://github.com/instill-ai/protobufs/compare/v0.1.2-alpha...v0.1.3-alpha) (2022-03-16)


### Miscellaneous Chores

* release 0.1.3-alpha ([c0c19e2](https://github.com/instill-ai/protobufs/commit/c0c19e2a49c4a0c032441139c2b4502a36da6b1e))

### [0.1.2-alpha](https://github.com/instill-ai/protobufs/compare/v0.1.1-alpha...v0.1.2-alpha) (2022-03-16)


### Miscellaneous Chores

* release 0.1.2-alpha ([9d7d0a0](https://github.com/instill-ai/protobufs/commit/9d7d0a03632efd65e6b3e2f97c9b40cd15625ccd))

### [0.1.1-alpha](https://github.com/instill-ai/protobufs/compare/v0.1.0-alpha...v0.1.1-alpha) (2022-02-24)


### Bug Fixes

* create TriggerPipeline rpc for new model-backend ([#27](https://github.com/instill-ai/protobufs/issues/27)) ([3c9f861](https://github.com/instill-ai/protobufs/commit/3c9f861fec699bb4ec08422409461bdfdb190e30))
* **model:** move name and version out of updated model info message struct ([#29](https://github.com/instill-ai/protobufs/issues/29)) ([919a751](https://github.com/instill-ai/protobufs/commit/919a75102c38ff8f075732dde525e2acde336407))
* udpate predict method for url/base64 ([#26](https://github.com/instill-ai/protobufs/issues/26)) ([9bd38a3](https://github.com/instill-ai/protobufs/commit/9bd38a31a0922c4fecd2759d0e40b56d60239ed2))

## [0.1.0-alpha](https://github.com/instill-ai/protobufs/compare/v0.0.0-alpha...v0.1.0-alpha) (2022-02-20)


### Features

* initialize repo ([30d5d90](https://github.com/instill-ai/protobufs/commit/30d5d90991a62624e1c1c8a3d559351e25b14412))
* **model-backend:** add protobuf for model-backend service ([#4](https://github.com/instill-ai/protobufs/issues/4)) ([3628bcb](https://github.com/instill-ai/protobufs/commit/3628bcb97e942d46261714401153f834e9487b49))


### Bug Fixes

* change message content and bump buf dependency ([f26fcd0](https://github.com/instill-ai/protobufs/commit/f26fcd0e667f08a319114fbd0b9d470e25a06ac2))
* **pipeline-backend:** change the definition of protobuff ([#3](https://github.com/instill-ai/protobufs/issues/3)) ([5d2b040](https://github.com/instill-ai/protobufs/commit/5d2b040d9b85f073be83a1d6b7f032ad00f0d4dd))
* **pipeline:** remove unsed code ([#22](https://github.com/instill-ai/protobufs/issues/22)) ([4e2f9db](https://github.com/instill-ai/protobufs/commit/4e2f9dbbdd5f9b6a328a06a31e9933182a376786))
* **pipeline:** use `full_name` instead of `fullName` ([#19](https://github.com/instill-ai/protobufs/issues/19)) ([9fb7451](https://github.com/instill-ai/protobufs/commit/9fb74510c9346482b25bd291ed2d913e7e3df734))
* remove version from creating model, the version will be to increased ([#18](https://github.com/instill-ai/protobufs/issues/18)) ([bd18728](https://github.com/instill-ai/protobufs/commit/bd18728fcb334bd5c85f88f90bfe6870b6cc7e68))
