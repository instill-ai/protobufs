# Changelog

## [0.4.0-alpha](https://github.com/instill-ai/protobufs/compare/v0.3.3-alpha...v0.4.0-alpha) (2024-06-26)


### Features

* **all:** use camelCase in HTTP bodies ([#362](https://github.com/instill-ai/protobufs/issues/362)) ([4108aed](https://github.com/instill-ai/protobufs/commit/4108aed052c58613977484a3e10a00b9f23f60e1))
* **api:** stream user pipeline trigger response ([#318](https://github.com/instill-ai/protobufs/issues/318)) ([bf709f3](https://github.com/instill-ai/protobufs/commit/bf709f3d2a93b78fe582681c4f40cd4d8337b7b7))
* **artifact:** add kb related rpc & message ([#345](https://github.com/instill-ai/protobufs/issues/345)) ([85ef118](https://github.com/instill-ai/protobufs/commit/85ef118c4acb47ffc8d1475340ff3999964b11b5))
* **artifact:** add services ([#269](https://github.com/instill-ai/protobufs/issues/269)) ([c7f99b2](https://github.com/instill-ai/protobufs/commit/c7f99b28caa56eb73b299eac7f17645d0d542d60))
* **artifact:** add tag create / list endpoints ([#286](https://github.com/instill-ai/protobufs/issues/286)) ([6678571](https://github.com/instill-ai/protobufs/commit/667857142e141c21e6aa8bd59057e5f23031ead6))
* **artifact:** document optional tag fields ([#290](https://github.com/instill-ai/protobufs/issues/290)) ([b7348c6](https://github.com/instill-ai/protobufs/commit/b7348c630ac726d6c2c0d27981b7449cec0105ff))
* **controller:** add rpc methods for controller ([#144](https://github.com/instill-ai/protobufs/issues/144)) ([b31be1a](https://github.com/instill-ai/protobufs/commit/b31be1ad082e7e6d9ce8fe9b4183e2af45dfa8e5))
* **core:** add `Owner` message for embedding user and organization information ([#273](https://github.com/instill-ai/protobufs/issues/273)) ([3ec60b8](https://github.com/instill-ai/protobufs/commit/3ec60b8bf219a0b05a07459b30f955ea2892db99))
* **core:** remove `/core`, `/vdp`, `/model` path prefix ([#312](https://github.com/instill-ai/protobufs/issues/312)) ([2dd58dc](https://github.com/instill-ai/protobufs/commit/2dd58dc6733540e6651de189fb17a213085bc933))
* **core:** update pricing tier names ([#327](https://github.com/instill-ai/protobufs/issues/327)) ([caf98fe](https://github.com/instill-ai/protobufs/commit/caf98fed8490b85a7a062f3bc02696cd973b4751))
* **kb:** file-related api spec ([#358](https://github.com/instill-ai/protobufs/issues/358)) ([6517d76](https://github.com/instill-ai/protobufs/commit/6517d76267d565bc2130f420d974bdf0c3e87734))
* **knowledge-base:** follow the convention ([#349](https://github.com/instill-ai/protobufs/issues/349)) ([e582423](https://github.com/instill-ai/protobufs/commit/e5824234b40159c93208b32dac3fa7232874ecd1))
* **metric:** add protobuf ([#140](https://github.com/instill-ai/protobufs/issues/140)) ([aca0b4c](https://github.com/instill-ai/protobufs/commit/aca0b4cdb4216af7532b77349c437eea07f1c998))
* **mgmt:** add CheckNamespaceAdmin endpoint ([#376](https://github.com/instill-ai/protobufs/issues/376)) ([18387a3](https://github.com/instill-ai/protobufs/commit/18387a3a347bafe41d06e05e152c23446ae280ed))
* **mgmt:** add concept to credit entries ([#306](https://github.com/instill-ai/protobufs/issues/306)) ([e20cc12](https://github.com/instill-ai/protobufs/commit/e20cc12cc18282f705e77d5d18dc114d53af018d))
* **mgmt:** add credit consumption chart endpoint ([#359](https://github.com/instill-ai/protobufs/issues/359)) ([6b98dfb](https://github.com/instill-ai/protobufs/commit/6b98dfb4c17161f4500dd90681172e2c87288338))
* **mgmt:** add credit methods ([#304](https://github.com/instill-ai/protobufs/issues/304)) ([f28895a](https://github.com/instill-ai/protobufs/commit/f28895ae866a5bd0ad02935fcd14f7a854045d01))
* **mgmt:** add credit purchase endpoints ([#360](https://github.com/instill-ai/protobufs/issues/360)) ([0700745](https://github.com/instill-ai/protobufs/commit/0700745d8b69036c35c1e555d54437fd17e2fd49))
* **mgmt:** add description field in subscription response ([#275](https://github.com/instill-ai/protobufs/issues/275)) ([4bf574c](https://github.com/instill-ai/protobufs/commit/4bf574cca4144500de053fe48be1d18db2042184))
* **mgmt:** add new TEAM_PRO subscription plan ([#323](https://github.com/instill-ai/protobufs/issues/323)) ([6e4f7c9](https://github.com/instill-ai/protobufs/commit/6e4f7c900a560c515e30b65ffc9258a55f8e12ae))
* **mgmt:** add Permission field in organization response ([#308](https://github.com/instill-ai/protobufs/issues/308)) ([2f399f9](https://github.com/instill-ai/protobufs/commit/2f399f924d7604209cf3aa7ab451d69fa5432dec))
* **mgmt:** add Stripe `status` and `trial_end` ([#268](https://github.com/instill-ai/protobufs/issues/268)) ([15d3669](https://github.com/instill-ai/protobufs/commit/15d36695a85011500217983a8b4f5915a25375c5))
* **mgmt:** refactor APIs for `Get` and `Patch` authenticated user ([#261](https://github.com/instill-ai/protobufs/issues/261)) ([0e4e9e6](https://github.com/instill-ai/protobufs/commit/0e4e9e684a3766b2b3529e5b1737f0a7c31eb67f))
* **mgmt:** refactor user/org profile and subscription endpoints ([#264](https://github.com/instill-ai/protobufs/issues/264)) ([b41e6f8](https://github.com/instill-ai/protobufs/commit/b41e6f867a6326869e2e8375916954389956a2fd))
* **mgmt:** rename organization freemium to non-paid plan ([#324](https://github.com/instill-ai/protobufs/issues/324)) ([0793aed](https://github.com/instill-ai/protobufs/commit/0793aed5600a3daf75aad23d350d46a2a0f05bf2))
* **mgmt:** update SubtractCredit endpoint ([#332](https://github.com/instill-ai/protobufs/issues/332)) ([e2d94bb](https://github.com/instill-ai/protobufs/commit/e2d94bb4b0f2089d1983b581dfc6340664a28238))
* **mgmt:** user can check which tokens can be deleted ([#353](https://github.com/instill-ai/protobufs/issues/353)) ([6084c24](https://github.com/instill-ai/protobufs/commit/6084c245ecaed7fe42120fb9e6d72c8b910013c5))
* **model,pipeline,connector,controller,usage:** remove model instance ([#151](https://github.com/instill-ai/protobufs/issues/151)) ([a009e64](https://github.com/instill-ai/protobufs/commit/a009e64a23ba151dbb954b98dfe1fae49bce54ce))
* **model:** add `tags` field in model ([#363](https://github.com/instill-ai/protobufs/issues/363)) ([3445389](https://github.com/instill-ai/protobufs/commit/344538974c388a1e56e75e61831c9a7fe908b4ae))
* **model:** add instance segmentation task output ([#109](https://github.com/instill-ai/protobufs/issues/109)) ([e6b2490](https://github.com/instill-ai/protobufs/commit/e6b2490766fa4374fadbda4665fbe4cb91be28a3))
* **model:** add model async trigger ([#293](https://github.com/instill-ai/protobufs/issues/293)) ([3dcf05f](https://github.com/instill-ai/protobufs/commit/3dcf05fb4375c387cf20a2fc23ec9f5ffc9254e8))
* **model:** add order_by field for list model endpoints ([#346](https://github.com/instill-ai/protobufs/issues/346)) ([6e9050e](https://github.com/instill-ai/protobufs/commit/6e9050ef9d10eb61cc000e4bf19ce6de95d404e0))
* **model:** add semantic segmentation output ([#115](https://github.com/instill-ai/protobufs/issues/115)) ([c0f8198](https://github.com/instill-ai/protobufs/commit/c0f8198d668d151e9792c4cd7f558727bac295b2))
* **model:** add text generation task ([#136](https://github.com/instill-ai/protobufs/issues/136)) ([94cc54f](https://github.com/instill-ai/protobufs/commit/94cc54fcf2cd90284918781c5b37046ba0b1f2e8))
* **model:** support model version deletion ([#374](https://github.com/instill-ai/protobufs/issues/374)) ([78cbc19](https://github.com/instill-ai/protobufs/commit/78cbc19626adce13322580646b838ec8fe130438))
* **model:** update chat_history schema to align with OpenAI message field ([#246](https://github.com/instill-ai/protobufs/issues/246)) ([dcc5ed1](https://github.com/instill-ai/protobufs/commit/dcc5ed1dea742bf6dd93f430323d1ede3f19bed4))
* **model:** Update Text-Generation Task Schema to Align with OpenAI Standards ([#243](https://github.com/instill-ai/protobufs/issues/243)) ([cd1acb9](https://github.com/instill-ai/protobufs/commit/cd1acb93a47935729f979332b12fe45120d195ab))
* **openapi:** keep public and private API docs in sync with main branch ([#270](https://github.com/instill-ai/protobufs/issues/270)) ([36c13f8](https://github.com/instill-ai/protobufs/commit/36c13f8632ee9ea455ac7281aff293aa90fb6c81))
* **pipeline:** add `tags` field in pipeline ([#337](https://github.com/instill-ai/protobufs/issues/337)) ([a1ba890](https://github.com/instill-ai/protobufs/commit/a1ba8908bd66ed7e22ae0b9c84523b61497f7f21))
* **pipeline:** remove resource_specification field in ConnectorSpec ([#309](https://github.com/instill-ai/protobufs/issues/309)) ([02b17d6](https://github.com/instill-ai/protobufs/commit/02b17d6e68b92eb6a421fed46f8ffcf8db50d77c))
* **pipeline:** return `can_release` permission in pipeline response ([#322](https://github.com/instill-ai/protobufs/issues/322)) ([cc193e7](https://github.com/instill-ai/protobufs/commit/cc193e7b28ed67af2b07b6c82445161d36c9e334))
* **usage:** add artifact usage data ([#266](https://github.com/instill-ai/protobufs/issues/266)) ([a688843](https://github.com/instill-ai/protobufs/commit/a6888434503abf2085d9dbdc0340b719d826593b))
* **usage:** use `AuthenticatedUser` message in usage collection ([#271](https://github.com/instill-ai/protobufs/issues/271)) ([a8196c1](https://github.com/instill-ai/protobufs/commit/a8196c12219ad9fb80a78c863b51c3bd7b75ef3b))
* **vdp:** add `CloneUserPipeline` and `CloneOrganizationPipeline` endpoints ([#257](https://github.com/instill-ai/protobufs/issues/257)) ([d11f8c4](https://github.com/instill-ai/protobufs/commit/d11f8c46c41bfec6013e22d1c47f813094f9938a))
* **vdp:** add `secrets` field in trigger endpoints ([#303](https://github.com/instill-ai/protobufs/issues/303)) ([e6d7c95](https://github.com/instill-ai/protobufs/commit/e6d7c95ec3a0b0114eb13deea861a598820ab086))
* **vdp:** add CheckName endpoint ([#258](https://github.com/instill-ai/protobufs/issues/258)) ([e2ab83c](https://github.com/instill-ai/protobufs/commit/e2ab83c3e1582d304052aaa0573109d078b7b370))
* **vdp:** add component definition list endpoint ([#274](https://github.com/instill-ai/protobufs/issues/274)) ([16afda7](https://github.com/instill-ai/protobufs/commit/16afda749f34f607563edcce37c2412f399b14c8))
* **vdp:** add connection field in ConnectorComponent ([#299](https://github.com/instill-ai/protobufs/issues/299)) ([a8de3f1](https://github.com/instill-ai/protobufs/commit/a8de3f10ab26e034186fda9eb0707f76969b872f))
* **vdp:** add description and sharing fields in pipeline clone endpoints ([#375](https://github.com/instill-ai/protobufs/issues/375)) ([56f0eea](https://github.com/instill-ai/protobufs/commit/56f0eeae6c97f4ef0356dc2f8546450b785e36a8))
* **vdp:** add description field to component definitions ([#279](https://github.com/instill-ai/protobufs/issues/279)) ([938b02b](https://github.com/instill-ai/protobufs/commit/938b02bf8beb2b6b5d9112d1aabc01bb23d9b5cf))
* **vdp:** add endpoints for cloning pipeline release ([#378](https://github.com/instill-ai/protobufs/issues/378)) ([c7e60ee](https://github.com/instill-ai/protobufs/commit/c7e60ee510c295801ca52c56b62b247ccddba329))
* **vdp:** add endpoints for secrets management ([#301](https://github.com/instill-ai/protobufs/issues/301)) ([90ead67](https://github.com/instill-ai/protobufs/commit/90ead67590874a9a0fa819674f33b67b413b470a))
* **vdp:** Add hub stats contract ([#333](https://github.com/instill-ai/protobufs/issues/333)) ([0100938](https://github.com/instill-ai/protobufs/commit/0100938c36cccf65c68164557b0963af459acd28))
* **vdp:** add private remaining credit endpont ([#331](https://github.com/instill-ai/protobufs/issues/331)) ([2eea197](https://github.com/instill-ai/protobufs/commit/2eea197d10330623159a9d3e2b54e29d601849e2))
* **vdp:** add release stage to component definitions ([#283](https://github.com/instill-ai/protobufs/issues/283)) ([8c20b4b](https://github.com/instill-ai/protobufs/commit/8c20b4b1d1d9343d7ea85d2925848d8ff6804f9e))
* **vdp:** add visibility param for list pipelines endpoints ([#256](https://github.com/instill-ai/protobufs/issues/256)) ([d739f8c](https://github.com/instill-ai/protobufs/commit/d739f8cb5419620fa2fef385e4e0f0b6b4c8bc46))
* **vdp:** adjust user secrets endpoint ([#307](https://github.com/instill-ai/protobufs/issues/307)) ([1bfc597](https://github.com/instill-ai/protobufs/commit/1bfc5976a5510d71b13b7899f731ec218658aa9a))
* **vdp:** expose `raw_recipe` field in pipeline endpoint ([#373](https://github.com/instill-ai/protobufs/issues/373)) ([afe1b7d](https://github.com/instill-ai/protobufs/commit/afe1b7d40f81b8260e1dc6da2f359d3991973bf9))
* **vdp:** extend component definitions ([#262](https://github.com/instill-ai/protobufs/issues/262)) ([d93f8e5](https://github.com/instill-ai/protobufs/commit/d93f8e5183f748edeca6f94683772d15c04e9ab4))
* **vdp:** redesign component-definitions endpoint ([#350](https://github.com/instill-ai/protobufs/issues/350)) ([e093231](https://github.com/instill-ai/protobufs/commit/e093231782fa71f089f7c8e784cadc54decb3351))
* **vdp:** refactor pipeline recipe and optimize the validation endpoint ([#341](https://github.com/instill-ai/protobufs/issues/341)) ([c076571](https://github.com/instill-ai/protobufs/commit/c076571818f7b36d79fb8d82e4fc264d9e607214))
* **vdp:** remove openapi_specification and add data_specification ([#282](https://github.com/instill-ai/protobufs/issues/282)) ([c4cdf98](https://github.com/instill-ai/protobufs/commit/c4cdf98e23510d5937720ad74c5de7ad72bdc4c7))
* **vdp:** remove ResponseComponent and merge it into TriggerByRequest ([#302](https://github.com/instill-ai/protobufs/issues/302)) ([f9a884b](https://github.com/instill-ai/protobufs/commit/f9a884b1b1f08c7dc281511fcddbe0172a65b6df))
* **vdp:** remove watch endpoints for pipeline releases ([#300](https://github.com/instill-ai/protobufs/issues/300)) ([be0db8c](https://github.com/instill-ai/protobufs/commit/be0db8c0ffcade050ce5fc8ffeebfdcb3fe697ad))
* **vdp:** retire connector ([#295](https://github.com/instill-ai/protobufs/issues/295)) ([05f4a3b](https://github.com/instill-ai/protobufs/commit/05f4a3baa610a7748474a718ea76b938d8d4cc50))
* **vdp:** return pipeline run stats ([#351](https://github.com/instill-ai/protobufs/issues/351)) ([cded1e5](https://github.com/instill-ai/protobufs/commit/cded1e5f79eeb7b9ea17b28ed4f5ff6a5a739d9e))
* **vdp:** revamp pipeline recipe and introduce iterator component ([#281](https://github.com/instill-ai/protobufs/issues/281)) ([e128375](https://github.com/instill-ai/protobufs/commit/e1283758bb43f23b04d754e8a981a78bc8d32743))
* **vdp:** revamp start component and end component ([#298](https://github.com/instill-ai/protobufs/issues/298)) ([86bf2bd](https://github.com/instill-ai/protobufs/commit/86bf2bdcf047c3bd8c0e2be4c80552956348ff4f))
* **vdp:** stream Organization pipeline trigger response ([#366](https://github.com/instill-ai/protobufs/issues/366)) ([36b8318](https://github.com/instill-ai/protobufs/commit/36b8318abf7a6dc0549405def180846cb5ba2c04))
* **vdp:** support sorting pipelines options by id and update_time ([#328](https://github.com/instill-ai/protobufs/issues/328)) ([ccfa000](https://github.com/instill-ai/protobufs/commit/ccfa000c5a6687cbc7aea307572a2e3a0505de6e))
* **vdp:** support sorting pipelines under a namespace ([#334](https://github.com/instill-ai/protobufs/issues/334)) ([8845d5e](https://github.com/instill-ai/protobufs/commit/8845d5e7b1e64e96f6c6853cef6bf1c175183ddf))
* **vdp:** Update payload for TriggerUserPipelineWithStreamRequest ([#357](https://github.com/instill-ai/protobufs/issues/357)) ([90adfd7](https://github.com/instill-ai/protobufs/commit/90adfd76a1ba34a7f8f227f7675b740dc866f3dc))


### Bug Fixes

* **artifact:** remove unnecessary parent param in tag creation ([#291](https://github.com/instill-ai/protobufs/issues/291)) ([3c32980](https://github.com/instill-ai/protobufs/commit/3c32980c5601dfd50c1792e36b6b86a96d190a1a))
* **docs:** regenerate OpenAPI with camelCase ([#364](https://github.com/instill-ai/protobufs/issues/364)) ([32357d2](https://github.com/instill-ai/protobufs/commit/32357d244a5b847b5a50e792ba45efe10e73f23e))
* **mgmt,billing:** refactor mgmt message, endpoints and add billing service ([#130](https://github.com/instill-ai/protobufs/issues/130)) ([366c0f8](https://github.com/instill-ai/protobufs/commit/366c0f8cda7e1a80fde14de0ce31b0fbbedd8160))
* **mgmt:** reference owner by ID in credit endpoints. ([#330](https://github.com/instill-ai/protobufs/issues/330)) ([796a98a](https://github.com/instill-ai/protobufs/commit/796a98ae1cd3f03d329e684b73527a69ee7e266f))
* **mgmt:** separate into admin and public services ([#133](https://github.com/instill-ai/protobufs/issues/133)) ([ddf0a4e](https://github.com/instill-ai/protobufs/commit/ddf0a4ea018ae45e30d0fb64a328ff87c3a6d02a))
* **model:** fix type inconsistency of field ExtraParamObject ([#240](https://github.com/instill-ai/protobufs/issues/240)) ([bf92376](https://github.com/instill-ai/protobufs/commit/bf92376a005104c7c771afc1f8abafa178935fe9))
* **openapi:** add readme.com extension for showing "Bearer" in auth ([#278](https://github.com/instill-ai/protobufs/issues/278)) ([a8c7a0c](https://github.com/instill-ai/protobufs/commit/a8c7a0ce7941bd6ba2e6afb791f77576c7cebed8))
* **vdp:** correct reference to credit owner id-&gt;uid ([#321](https://github.com/instill-ai/protobufs/issues/321)) ([2b79ef0](https://github.com/instill-ai/protobufs/commit/2b79ef096e60b509c3194a4712bcf8dd58832224))
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
