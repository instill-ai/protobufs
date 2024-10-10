# pylint: disable=no-member,wrong-import-position,too-many-lines,no-name-in-module
from typing import Dict, Union

from google.protobuf import field_mask_pb2
from google.protobuf.struct_pb2 import Struct

# common
import instill.protogen.common.healthcheck.v1beta.healthcheck_pb2 as healthcheck

# pipeline
import instill.protogen.vdp.pipeline.v1beta.pipeline_pb2 as pipeline_interface
import instill.protogen.vdp.pipeline.v1beta.pipeline_public_service_pb2_grpc as pipeline_service
import instill.protogen.vdp.pipeline.v1beta.component_definition_pb2 as component_definition
import instill.protogen.vdp.pipeline.v1beta.secret_pb2 as secret_interface
import instill.protogen.vdp.pipeline.v1beta.integration_pb2 as integration_interface
import instill.protogen.vdp.pipeline.v1beta.common_pb2 as common_pb2
from instill.clients.base import Client, RequestFactory
from instill.clients.constant import DEFAULT_INSTANCE
from instill.clients.instance import InstillInstance
from instill.configuration import global_config
from instill.utils.error_handler import grpc_handler

# from instill.utils.logger import Logger


class PipelineClient(Client):
    def __init__(
        self, namespace: str, async_enabled: bool, target_namespace: str = ""
    ) -> None:
        self.hosts: Dict[str, InstillInstance] = {}
        self.namespace: str = namespace
        self.target_namespace: str = (
            namespace if target_namespace == "" else target_namespace
        )
        if DEFAULT_INSTANCE in global_config.hosts:
            self.instance = DEFAULT_INSTANCE
        elif len(global_config.hosts) == 0:
            self.instance = ""
        else:
            self.instance = list(global_config.hosts.keys())[0]

        if global_config.hosts is not None:
            for instance, config in global_config.hosts.items():
                self.hosts[instance] = InstillInstance(
                    pipeline_service.PipelinePublicServiceStub,
                    url=config.url,
                    token=config.token,
                    secure=config.secure,
                    async_enabled=async_enabled,
                )

    @property
    def hosts(self):
        return self._hosts

    @hosts.setter
    def hosts(self, hosts: Dict[str, InstillInstance]):
        self._hosts = hosts

    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, instance: str):
        self._instance = instance

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: str):
        self._metadata = metadata


    @grpc_handler
    def liveness(
        self,
        health_check_request: HealthCheckRequest,
        async_enabled: bool = False,
    ) -> pipeline_interface.LivenessResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.Liveness,
                request=pipeline_interface.LivenessRequest(
                    health_check_request=health_check_request,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.Liveness,
            request=pipeline_interface.LivenessRequest(
                health_check_request=health_check_request,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def readiness(
        self,
        health_check_request: HealthCheckRequest,
        async_enabled: bool = False,
    ) -> pipeline_interface.ReadinessResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.Readiness,
                request=pipeline_interface.ReadinessRequest(
                    health_check_request=health_check_request,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.Readiness,
            request=pipeline_interface.ReadinessRequest(
                health_check_request=health_check_request,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_hub_stats(
        self,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetHubStatsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetHubStats,
                request=pipeline_interface.GetHubStatsRequest(
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetHubStats,
            request=pipeline_interface.GetHubStatsRequest(
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_pipelines(
        self,
        view: TYPE_ENUM,
        visibility: pipeline_interface.Pipeline.Visibility,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        order_by: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListPipelinesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListPipelines,
                request=pipeline_interface.ListPipelinesRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    visibility=visibility,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                    order_by=order_by,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListPipelines,
            request=pipeline_interface.ListPipelinesRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                visibility=visibility,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
                order_by=order_by,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def lookup_pipeline(
        self,
        permalink: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.LookUpPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.LookUpPipeline,
                request=pipeline_interface.LookUpPipelineRequest(
                    permalink=permalink,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.LookUpPipeline,
            request=pipeline_interface.LookUpPipelineRequest(
                permalink=permalink,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_namespace_pipelines(
        self,
        namespace_id: str,
        view: TYPE_ENUM,
        visibility: pipeline_interface.Pipeline.Visibility,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        order_by: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListNamespacePipelinesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListNamespacePipelines,
                request=pipeline_interface.ListNamespacePipelinesRequest(
                    namespace_id=namespace_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    visibility=visibility,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                    order_by=order_by,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListNamespacePipelines,
            request=pipeline_interface.ListNamespacePipelinesRequest(
                namespace_id=namespace_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                visibility=visibility,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
                order_by=order_by,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline: pipeline_interface.Pipeline,
        async_enabled: bool = False,
    ) -> pipeline_interface.CreateNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateNamespacePipeline,
                request=pipeline_interface.CreateNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline=pipeline,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateNamespacePipeline,
            request=pipeline_interface.CreateNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline=pipeline,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetNamespacePipeline,
                request=pipeline_interface.GetNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetNamespacePipeline,
            request=pipeline_interface.GetNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        pipeline: pipeline_interface.Pipeline,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> pipeline_interface.UpdateNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateNamespacePipeline,
                request=pipeline_interface.UpdateNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    pipeline=pipeline,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateNamespacePipeline,
            request=pipeline_interface.UpdateNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                pipeline=pipeline,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.DeleteNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteNamespacePipeline,
                request=pipeline_interface.DeleteNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteNamespacePipeline,
            request=pipeline_interface.DeleteNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def validate_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.ValidateNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ValidateNamespacePipeline,
                request=pipeline_interface.ValidateNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ValidateNamespacePipeline,
            request=pipeline_interface.ValidateNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def rename_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        new_pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RenameNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RenameNamespacePipeline,
                request=pipeline_interface.RenameNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    new_pipeline_id=new_pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RenameNamespacePipeline,
            request=pipeline_interface.RenameNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                new_pipeline_id=new_pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def clone_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        description: str,
        sharing: common_pb2.Sharing,
        target_namespace_id: str,
        target_pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.CloneNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CloneNamespacePipeline,
                request=pipeline_interface.CloneNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    description=description,
                    sharing=sharing,
                    target_namespace_id=target_namespace_id,
                    target_pipeline_id=target_pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CloneNamespacePipeline,
            request=pipeline_interface.CloneNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                description=description,
                sharing=sharing,
                target_namespace_id=target_namespace_id,
                target_pipeline_id=target_pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def send_namespace_pipeline_event(
        self,
        namespace_id: str,
        pipeline_id: str,
        event: str,
        code: str,
        data: Struct,
        async_enabled: bool = False,
    ) -> pipeline_interface.SendNamespacePipelineEventResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.SendNamespacePipelineEvent,
                request=pipeline_interface.SendNamespacePipelineEventRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    event=event,
                    code=code,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.SendNamespacePipelineEvent,
            request=pipeline_interface.SendNamespacePipelineEventRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                event=event,
                code=code,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def send_namespace_pipeline_release_event(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        event: str,
        code: str,
        data: Struct,
        async_enabled: bool = False,
    ) -> pipeline_interface.SendNamespacePipelineReleaseEventResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.SendNamespacePipelineReleaseEvent,
                request=pipeline_interface.SendNamespacePipelineReleaseEventRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                    event=event,
                    code=code,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.SendNamespacePipelineReleaseEvent,
            request=pipeline_interface.SendNamespacePipelineReleaseEventRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
                event=event,
                code=code,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerNamespacePipeline,
                request=pipeline_interface.TriggerNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerNamespacePipeline,
            request=pipeline_interface.TriggerNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_pipeline_with_stream(
        self,
        namespace_id: str,
        pipeline_id: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerNamespacePipelineWithStreamResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerNamespacePipelineWithStream,
                request=pipeline_interface.TriggerNamespacePipelineWithStreamRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerNamespacePipelineWithStream,
            request=pipeline_interface.TriggerNamespacePipelineWithStreamRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_namespace_pipeline(
        self,
        namespace_id: str,
        pipeline_id: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerAsyncNamespacePipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerAsyncNamespacePipeline,
                request=pipeline_interface.TriggerAsyncNamespacePipelineRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerAsyncNamespacePipeline,
            request=pipeline_interface.TriggerAsyncNamespacePipelineRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release: pipeline_interface.PipelineRelease,
        async_enabled: bool = False,
    ) -> pipeline_interface.CreateNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateNamespacePipelineRelease,
                request=pipeline_interface.CreateNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release=release,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateNamespacePipelineRelease,
            request=pipeline_interface.CreateNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release=release,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_namespace_pipeline_releases(
        self,
        namespace_id: str,
        pipeline_id: str,
        view: TYPE_ENUM,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        async_enabled: bool = False,
    ) -> pipeline_interface.ListNamespacePipelineReleasesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListNamespacePipelineReleases,
                request=pipeline_interface.ListNamespacePipelineReleasesRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListNamespacePipelineReleases,
            request=pipeline_interface.ListNamespacePipelineReleasesRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetNamespacePipelineRelease,
                request=pipeline_interface.GetNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetNamespacePipelineRelease,
            request=pipeline_interface.GetNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        release: pipeline_interface.PipelineRelease,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> pipeline_interface.UpdateNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateNamespacePipelineRelease,
                request=pipeline_interface.UpdateNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                    release=release,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateNamespacePipelineRelease,
            request=pipeline_interface.UpdateNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
                release=release,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.DeleteNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteNamespacePipelineRelease,
                request=pipeline_interface.DeleteNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteNamespacePipelineRelease,
            request=pipeline_interface.DeleteNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def clone_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        description: str,
        sharing: common_pb2.Sharing,
        target_namespace_id: str,
        target_pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.CloneNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CloneNamespacePipelineRelease,
                request=pipeline_interface.CloneNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                    description=description,
                    sharing=sharing,
                    target_namespace_id=target_namespace_id,
                    target_pipeline_id=target_pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CloneNamespacePipelineRelease,
            request=pipeline_interface.CloneNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
                description=description,
                sharing=sharing,
                target_namespace_id=target_namespace_id,
                target_pipeline_id=target_pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerNamespacePipelineRelease,
                request=pipeline_interface.TriggerNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerNamespacePipelineRelease,
            request=pipeline_interface.TriggerNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_namespace_pipeline_release(
        self,
        namespace_id: str,
        pipeline_id: str,
        release_id: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerAsyncNamespacePipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerAsyncNamespacePipelineRelease,
                request=pipeline_interface.TriggerAsyncNamespacePipelineReleaseRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    release_id=release_id,
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerAsyncNamespacePipelineRelease,
            request=pipeline_interface.TriggerAsyncNamespacePipelineReleaseRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                release_id=release_id,
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_namespace_secret(
        self,
        namespace_id: str,
        secret: secret_interface.Secret,
        async_enabled: bool = False,
    ) -> secret_interface.CreateNamespaceSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateNamespaceSecret,
                request=secret_interface.CreateNamespaceSecretRequest(
                    namespace_id=namespace_id,
                    secret=secret,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateNamespaceSecret,
            request=secret_interface.CreateNamespaceSecretRequest(
                namespace_id=namespace_id,
                secret=secret,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_namespace_secrets(
        self,
        namespace_id: str,
        total_size: int = 10,
        next_page_token: str = "",
        async_enabled: bool = False,
    ) -> secret_interface.ListNamespaceSecretsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListNamespaceSecrets,
                request=secret_interface.ListNamespaceSecretsRequest(
                    namespace_id=namespace_id,
                    page_size=total_size,
                    page_token=next_page_token,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListNamespaceSecrets,
            request=secret_interface.ListNamespaceSecretsRequest(
                namespace_id=namespace_id,
                page_size=total_size,
                page_token=next_page_token,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_secret(
        self,
        namespace_id: str,
        secret_id: str,
        async_enabled: bool = False,
    ) -> secret_interface.GetNamespaceSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetNamespaceSecret,
                request=secret_interface.GetNamespaceSecretRequest(
                    namespace_id=namespace_id,
                    secret_id=secret_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetNamespaceSecret,
            request=secret_interface.GetNamespaceSecretRequest(
                namespace_id=namespace_id,
                secret_id=secret_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_namespace_secret(
        self,
        namespace_id: str,
        secret_id: str,
        secret: secret_interface.Secret,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> secret_interface.UpdateNamespaceSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateNamespaceSecret,
                request=secret_interface.UpdateNamespaceSecretRequest(
                    namespace_id=namespace_id,
                    secret_id=secret_id,
                    secret=secret,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateNamespaceSecret,
            request=secret_interface.UpdateNamespaceSecretRequest(
                namespace_id=namespace_id,
                secret_id=secret_id,
                secret=secret,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_namespace_secret(
        self,
        namespace_id: str,
        secret_id: str,
        async_enabled: bool = False,
    ) -> secret_interface.DeleteNamespaceSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteNamespaceSecret,
                request=secret_interface.DeleteNamespaceSecretRequest(
                    namespace_id=namespace_id,
                    secret_id=secret_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteNamespaceSecret,
            request=secret_interface.DeleteNamespaceSecretRequest(
                namespace_id=namespace_id,
                secret_id=secret_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_component_definitions(
        self,
        view: TYPE_ENUM,
        total_size: int = 10,
        filter_str: str = "",
        page: int = 0,
        async_enabled: bool = False,
    ) -> component_definition.ListComponentDefinitionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListComponentDefinitions,
                request=component_definition.ListComponentDefinitionsRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    page_size=total_size,
                    filter=filter_str,
                    page=page,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListComponentDefinitions,
            request=component_definition.ListComponentDefinitionsRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                page_size=total_size,
                filter=filter_str,
                page=page,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_operation(
        self,
        operation_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetOperationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetOperation,
                request=pipeline_interface.GetOperationRequest(
                    operation_id=operation_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetOperation,
            request=pipeline_interface.GetOperationRequest(
                operation_id=operation_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_pipeline(
        self,
        pipeline: pipeline_interface.Pipeline,
        parent: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.CreateUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateUserPipeline,
                request=pipeline_interface.CreateUserPipelineRequest(
                    pipeline=pipeline,
                    parent=parent,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateUserPipeline,
            request=pipeline_interface.CreateUserPipelineRequest(
                pipeline=pipeline,
                parent=parent,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_pipelines(
        self,
        view: TYPE_ENUM,
        parent: str,
        visibility: pipeline_interface.Pipeline.Visibility,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        order_by: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListUserPipelinesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListUserPipelines,
                request=pipeline_interface.ListUserPipelinesRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    parent=parent,
                    visibility=visibility,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                    order_by=order_by,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListUserPipelines,
            request=pipeline_interface.ListUserPipelinesRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                parent=parent,
                visibility=visibility,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
                order_by=order_by,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_pipeline(
        self,
        name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetUserPipeline,
                request=pipeline_interface.GetUserPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetUserPipeline,
            request=pipeline_interface.GetUserPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_pipeline(
        self,
        pipeline: pipeline_interface.Pipeline,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> pipeline_interface.UpdateUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateUserPipeline,
                request=pipeline_interface.UpdateUserPipelineRequest(
                    pipeline=pipeline,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateUserPipeline,
            request=pipeline_interface.UpdateUserPipelineRequest(
                pipeline=pipeline,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_pipeline(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.DeleteUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteUserPipeline,
                request=pipeline_interface.DeleteUserPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteUserPipeline,
            request=pipeline_interface.DeleteUserPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def validate_pipeline(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.ValidateUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ValidateUserPipeline,
                request=pipeline_interface.ValidateUserPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ValidateUserPipeline,
            request=pipeline_interface.ValidateUserPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def rename_pipeline(
        self,
        name: str,
        new_pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RenameUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RenameUserPipeline,
                request=pipeline_interface.RenameUserPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    new_pipeline_id=new_pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RenameUserPipeline,
            request=pipeline_interface.RenameUserPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                new_pipeline_id=new_pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_pipeline(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerUserPipeline,
                request=pipeline_interface.TriggerUserPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerUserPipeline,
            request=pipeline_interface.TriggerUserPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_pipeline_with_stream(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerUserPipelineWithStreamResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerUserPipelineWithStream,
                request=pipeline_interface.TriggerUserPipelineWithStreamRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerUserPipelineWithStream,
            request=pipeline_interface.TriggerUserPipelineWithStreamRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_pipeline(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerAsyncUserPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerAsyncUserPipeline,
                request=pipeline_interface.TriggerAsyncUserPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerAsyncUserPipeline,
            request=pipeline_interface.TriggerAsyncUserPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_pipeline_release(
        self,
        release: pipeline_interface.PipelineRelease,
        parent: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.CreateUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateUserPipelineRelease,
                request=pipeline_interface.CreateUserPipelineReleaseRequest(
                    release=release,
                    parent=parent,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateUserPipelineRelease,
            request=pipeline_interface.CreateUserPipelineReleaseRequest(
                release=release,
                parent=parent,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_pipeline_releases(
        self,
        view: TYPE_ENUM,
        parent: str,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        async_enabled: bool = False,
    ) -> pipeline_interface.ListUserPipelineReleasesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListUserPipelineReleases,
                request=pipeline_interface.ListUserPipelineReleasesRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    parent=parent,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListUserPipelineReleases,
            request=pipeline_interface.ListUserPipelineReleasesRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                parent=parent,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_pipeline_release(
        self,
        name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetUserPipelineRelease,
                request=pipeline_interface.GetUserPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetUserPipelineRelease,
            request=pipeline_interface.GetUserPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_pipeline_release(
        self,
        release: pipeline_interface.PipelineRelease,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> pipeline_interface.UpdateUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateUserPipelineRelease,
                request=pipeline_interface.UpdateUserPipelineReleaseRequest(
                    release=release,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateUserPipelineRelease,
            request=pipeline_interface.UpdateUserPipelineReleaseRequest(
                release=release,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_pipeline_release(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.DeleteUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteUserPipelineRelease,
                request=pipeline_interface.DeleteUserPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteUserPipelineRelease,
            request=pipeline_interface.DeleteUserPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def restore_pipeline_release(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RestoreUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RestoreUserPipelineRelease,
                request=pipeline_interface.RestoreUserPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RestoreUserPipelineRelease,
            request=pipeline_interface.RestoreUserPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def rename_pipeline_release(
        self,
        name: str,
        new_pipeline_release_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RenameUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RenameUserPipelineRelease,
                request=pipeline_interface.RenameUserPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    new_pipeline_release_id=new_pipeline_release_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RenameUserPipelineRelease,
            request=pipeline_interface.RenameUserPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                new_pipeline_release_id=new_pipeline_release_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_pipeline_release(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerUserPipelineRelease,
                request=pipeline_interface.TriggerUserPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerUserPipelineRelease,
            request=pipeline_interface.TriggerUserPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_pipeline_release(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerAsyncUserPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerAsyncUserPipelineRelease,
                request=pipeline_interface.TriggerAsyncUserPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerAsyncUserPipelineRelease,
            request=pipeline_interface.TriggerAsyncUserPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_organization_pipeline(
        self,
        pipeline: pipeline_interface.Pipeline,
        parent: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.CreateOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateOrganizationPipeline,
                request=pipeline_interface.CreateOrganizationPipelineRequest(
                    pipeline=pipeline,
                    parent=parent,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateOrganizationPipeline,
            request=pipeline_interface.CreateOrganizationPipelineRequest(
                pipeline=pipeline,
                parent=parent,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_organization_pipelines(
        self,
        view: TYPE_ENUM,
        parent: str,
        visibility: pipeline_interface.Pipeline.Visibility,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        order_by: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListOrganizationPipelinesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListOrganizationPipelines,
                request=pipeline_interface.ListOrganizationPipelinesRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    parent=parent,
                    visibility=visibility,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                    order_by=order_by,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListOrganizationPipelines,
            request=pipeline_interface.ListOrganizationPipelinesRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                parent=parent,
                visibility=visibility,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
                order_by=order_by,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_organization_pipeline(
        self,
        name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetOrganizationPipeline,
                request=pipeline_interface.GetOrganizationPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetOrganizationPipeline,
            request=pipeline_interface.GetOrganizationPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_organization_pipeline(
        self,
        pipeline: pipeline_interface.Pipeline,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> pipeline_interface.UpdateOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateOrganizationPipeline,
                request=pipeline_interface.UpdateOrganizationPipelineRequest(
                    pipeline=pipeline,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateOrganizationPipeline,
            request=pipeline_interface.UpdateOrganizationPipelineRequest(
                pipeline=pipeline,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_organization_pipeline(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.DeleteOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteOrganizationPipeline,
                request=pipeline_interface.DeleteOrganizationPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteOrganizationPipeline,
            request=pipeline_interface.DeleteOrganizationPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def validate_organization_pipeline(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.ValidateOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ValidateOrganizationPipeline,
                request=pipeline_interface.ValidateOrganizationPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ValidateOrganizationPipeline,
            request=pipeline_interface.ValidateOrganizationPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def rename_organization_pipeline(
        self,
        name: str,
        new_pipeline_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RenameOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RenameOrganizationPipeline,
                request=pipeline_interface.RenameOrganizationPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    new_pipeline_id=new_pipeline_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RenameOrganizationPipeline,
            request=pipeline_interface.RenameOrganizationPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                new_pipeline_id=new_pipeline_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_organization_pipeline_stream(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerOrganizationPipelineStreamResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerOrganizationPipelineStream,
                request=pipeline_interface.TriggerOrganizationPipelineStreamRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerOrganizationPipelineStream,
            request=pipeline_interface.TriggerOrganizationPipelineStreamRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_organization_pipeline(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerOrganizationPipeline,
                request=pipeline_interface.TriggerOrganizationPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerOrganizationPipeline,
            request=pipeline_interface.TriggerOrganizationPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_organization_pipeline(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerAsyncOrganizationPipelineResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerAsyncOrganizationPipeline,
                request=pipeline_interface.TriggerAsyncOrganizationPipelineRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerAsyncOrganizationPipeline,
            request=pipeline_interface.TriggerAsyncOrganizationPipelineRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_organization_pipeline_release(
        self,
        release: pipeline_interface.PipelineRelease,
        parent: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.CreateOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateOrganizationPipelineRelease,
                request=pipeline_interface.CreateOrganizationPipelineReleaseRequest(
                    release=release,
                    parent=parent,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateOrganizationPipelineRelease,
            request=pipeline_interface.CreateOrganizationPipelineReleaseRequest(
                release=release,
                parent=parent,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_organization_pipeline_releases(
        self,
        view: TYPE_ENUM,
        parent: str,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        show_deleted: bool = False,
        async_enabled: bool = False,
    ) -> pipeline_interface.ListOrganizationPipelineReleasesResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListOrganizationPipelineReleases,
                request=pipeline_interface.ListOrganizationPipelineReleasesRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    parent=parent,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                    show_deleted=show_deleted,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListOrganizationPipelineReleases,
            request=pipeline_interface.ListOrganizationPipelineReleasesRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                parent=parent,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
                show_deleted=show_deleted,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_organization_pipeline_release(
        self,
        name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> pipeline_interface.GetOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetOrganizationPipelineRelease,
                request=pipeline_interface.GetOrganizationPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetOrganizationPipelineRelease,
            request=pipeline_interface.GetOrganizationPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_organization_pipeline_release(
        self,
        release: pipeline_interface.PipelineRelease,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> pipeline_interface.UpdateOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateOrganizationPipelineRelease,
                request=pipeline_interface.UpdateOrganizationPipelineReleaseRequest(
                    release=release,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateOrganizationPipelineRelease,
            request=pipeline_interface.UpdateOrganizationPipelineReleaseRequest(
                release=release,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_organization_pipeline_release(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.DeleteOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteOrganizationPipelineRelease,
                request=pipeline_interface.DeleteOrganizationPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteOrganizationPipelineRelease,
            request=pipeline_interface.DeleteOrganizationPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def restore_organization_pipeline_release(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RestoreOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RestoreOrganizationPipelineRelease,
                request=pipeline_interface.RestoreOrganizationPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RestoreOrganizationPipelineRelease,
            request=pipeline_interface.RestoreOrganizationPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def rename_organization_pipeline_release(
        self,
        name: str,
        new_pipeline_release_id: str,
        async_enabled: bool = False,
    ) -> pipeline_interface.RenameOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.RenameOrganizationPipelineRelease,
                request=pipeline_interface.RenameOrganizationPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    new_pipeline_release_id=new_pipeline_release_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.RenameOrganizationPipelineRelease,
            request=pipeline_interface.RenameOrganizationPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                new_pipeline_release_id=new_pipeline_release_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_organization_pipeline_release(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerOrganizationPipelineRelease,
                request=pipeline_interface.TriggerOrganizationPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerOrganizationPipelineRelease,
            request=pipeline_interface.TriggerOrganizationPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_organization_pipeline_release(
        self,
        name: str,
        inputs: list[Struct],
        data: list[pipeline_interface.TriggerData],
        async_enabled: bool = False,
    ) -> pipeline_interface.TriggerAsyncOrganizationPipelineReleaseResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TriggerAsyncOrganizationPipelineRelease,
                request=pipeline_interface.TriggerAsyncOrganizationPipelineReleaseRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    inputs=inputs,
                    data=data,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TriggerAsyncOrganizationPipelineRelease,
            request=pipeline_interface.TriggerAsyncOrganizationPipelineReleaseRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                inputs=inputs,
                data=data,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_connector_definitions(
        self,
        view: TYPE_ENUM,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        async_enabled: bool = False,
    ) -> component_definition.ListConnectorDefinitionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListConnectorDefinitions,
                request=component_definition.ListConnectorDefinitionsRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListConnectorDefinitions,
            request=component_definition.ListConnectorDefinitionsRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_connector_definition(
        self,
        name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> component_definition.GetConnectorDefinitionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetConnectorDefinition,
                request=component_definition.GetConnectorDefinitionRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetConnectorDefinition,
            request=component_definition.GetConnectorDefinitionRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_operator_definitions(
        self,
        view: TYPE_ENUM,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        async_enabled: bool = False,
    ) -> component_definition.ListOperatorDefinitionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListOperatorDefinitions,
                request=component_definition.ListOperatorDefinitionsRequest(
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListOperatorDefinitions,
            request=component_definition.ListOperatorDefinitionsRequest(
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_operator_definition(
        self,
        name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> component_definition.GetOperatorDefinitionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetOperatorDefinition,
                request=component_definition.GetOperatorDefinitionRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetOperatorDefinition,
            request=component_definition.GetOperatorDefinitionRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def check_name(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> common_pb2.CheckNameResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CheckName,
                request=common_pb2.CheckNameRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CheckName,
            request=common_pb2.CheckNameRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_secret(
        self,
        secret: secret_interface.Secret,
        parent: str,
        async_enabled: bool = False,
    ) -> secret_interface.CreateUserSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateUserSecret,
                request=secret_interface.CreateUserSecretRequest(
                    secret=secret,
                    parent=parent,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateUserSecret,
            request=secret_interface.CreateUserSecretRequest(
                secret=secret,
                parent=parent,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_secrets(
        self,
        parent: str,
        total_size: int = 10,
        next_page_token: str = "",
        async_enabled: bool = False,
    ) -> secret_interface.ListUserSecretsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListUserSecrets,
                request=secret_interface.ListUserSecretsRequest(
                    parent=parent,
                    page_size=total_size,
                    page_token=next_page_token,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListUserSecrets,
            request=secret_interface.ListUserSecretsRequest(
                parent=parent,
                page_size=total_size,
                page_token=next_page_token,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_secret(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> secret_interface.GetUserSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetUserSecret,
                request=secret_interface.GetUserSecretRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetUserSecret,
            request=secret_interface.GetUserSecretRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_secret(
        self,
        secret: secret_interface.Secret,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> secret_interface.UpdateUserSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateUserSecret,
                request=secret_interface.UpdateUserSecretRequest(
                    secret=secret,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateUserSecret,
            request=secret_interface.UpdateUserSecretRequest(
                secret=secret,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_secret(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> secret_interface.DeleteUserSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteUserSecret,
                request=secret_interface.DeleteUserSecretRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteUserSecret,
            request=secret_interface.DeleteUserSecretRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_organization_secret(
        self,
        secret: secret_interface.Secret,
        parent: str,
        async_enabled: bool = False,
    ) -> secret_interface.CreateOrganizationSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateOrganizationSecret,
                request=secret_interface.CreateOrganizationSecretRequest(
                    secret=secret,
                    parent=parent,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateOrganizationSecret,
            request=secret_interface.CreateOrganizationSecretRequest(
                secret=secret,
                parent=parent,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_organization_secrets(
        self,
        parent: str,
        total_size: int = 10,
        next_page_token: str = "",
        async_enabled: bool = False,
    ) -> secret_interface.ListOrganizationSecretsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListOrganizationSecrets,
                request=secret_interface.ListOrganizationSecretsRequest(
                    parent=parent,
                    page_size=total_size,
                    page_token=next_page_token,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListOrganizationSecrets,
            request=secret_interface.ListOrganizationSecretsRequest(
                parent=parent,
                page_size=total_size,
                page_token=next_page_token,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_organization_secret(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> secret_interface.GetOrganizationSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetOrganizationSecret,
                request=secret_interface.GetOrganizationSecretRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetOrganizationSecret,
            request=secret_interface.GetOrganizationSecretRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_organization_secret(
        self,
        secret: secret_interface.Secret,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> secret_interface.UpdateOrganizationSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateOrganizationSecret,
                request=secret_interface.UpdateOrganizationSecretRequest(
                    secret=secret,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateOrganizationSecret,
            request=secret_interface.UpdateOrganizationSecretRequest(
                secret=secret,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_organization_secret(
        self,
        name: str,
        async_enabled: bool = False,
    ) -> secret_interface.DeleteOrganizationSecretResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteOrganizationSecret,
                request=secret_interface.DeleteOrganizationSecretRequest(
                    name=f"{self.target_namespace}/pipelines/{name}",
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteOrganizationSecret,
            request=secret_interface.DeleteOrganizationSecretRequest(
                name=f"{self.target_namespace}/pipelines/{name}",
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_pipeline_runs(
        self,
        namespace_id: str,
        pipeline_id: str,
        view: TYPE_ENUM,
        page: int = 0,
        total_size: int = 10,
        filter_str: str = "",
        order_by: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListPipelineRunsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListPipelineRuns,
                request=pipeline_interface.ListPipelineRunsRequest(
                    namespace_id=namespace_id,
                    pipeline_id=pipeline_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    page=page,
                    page_size=total_size,
                    filter=filter_str,
                    order_by=order_by,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListPipelineRuns,
            request=pipeline_interface.ListPipelineRunsRequest(
                namespace_id=namespace_id,
                pipeline_id=pipeline_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                page=page,
                page_size=total_size,
                filter=filter_str,
                order_by=order_by,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_component_runs(
        self,
        pipeline_run_id: str,
        view: TYPE_ENUM,
        page: int = 0,
        total_size: int = 10,
        filter_str: str = "",
        order_by: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListComponentRunsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListComponentRuns,
                request=pipeline_interface.ListComponentRunsRequest(
                    pipeline_run_id=pipeline_run_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                    page=page,
                    page_size=total_size,
                    filter=filter_str,
                    order_by=order_by,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListComponentRuns,
            request=pipeline_interface.ListComponentRunsRequest(
                pipeline_run_id=pipeline_run_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
                page=page,
                page_size=total_size,
                filter=filter_str,
                order_by=order_by,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_namespace_connections(
        self,
        namespace_id: str,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        async_enabled: bool = False,
    ) -> integration_interface.ListNamespaceConnectionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListNamespaceConnections,
                request=integration_interface.ListNamespaceConnectionsRequest(
                    namespace_id=namespace_id,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListNamespaceConnections,
            request=integration_interface.ListNamespaceConnectionsRequest(
                namespace_id=namespace_id,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_connection(
        self,
        namespace_id: str,
        connection_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> integration_interface.GetNamespaceConnectionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetNamespaceConnection,
                request=integration_interface.GetNamespaceConnectionRequest(
                    namespace_id=namespace_id,
                    connection_id=connection_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetNamespaceConnection,
            request=integration_interface.GetNamespaceConnectionRequest(
                namespace_id=namespace_id,
                connection_id=connection_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def create_namespace_connection(
        self,
        connection: integration_interface.Connection,
        async_enabled: bool = False,
    ) -> integration_interface.CreateNamespaceConnectionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.CreateNamespaceConnection,
                request=integration_interface.CreateNamespaceConnectionRequest(
                    connection=connection,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.CreateNamespaceConnection,
            request=integration_interface.CreateNamespaceConnectionRequest(
                connection=connection,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def update_namespace_connection(
        self,
        connection_id: str,
        connection: integration_interface.Connection,
        mask: field_mask_pb2.FieldMask,
        async_enabled: bool = False,
    ) -> integration_interface.UpdateNamespaceConnectionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.UpdateNamespaceConnection,
                request=integration_interface.UpdateNamespaceConnectionRequest(
                    connection_id=connection_id,
                    connection=connection,
                    update_mask=mask,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.UpdateNamespaceConnection,
            request=integration_interface.UpdateNamespaceConnectionRequest(
                connection_id=connection_id,
                connection=connection,
                update_mask=mask,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def delete_namespace_connection(
        self,
        namespace_id: str,
        connection_id: str,
        async_enabled: bool = False,
    ) -> integration_interface.DeleteNamespaceConnectionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.DeleteNamespaceConnection,
                request=integration_interface.DeleteNamespaceConnectionRequest(
                    namespace_id=namespace_id,
                    connection_id=connection_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.DeleteNamespaceConnection,
            request=integration_interface.DeleteNamespaceConnectionRequest(
                namespace_id=namespace_id,
                connection_id=connection_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def test_namespace_connection(
        self,
        namespace_id: str,
        connection_id: str,
        async_enabled: bool = False,
    ) -> integration_interface.TestNamespaceConnectionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.TestNamespaceConnection,
                request=integration_interface.TestNamespaceConnectionRequest(
                    namespace_id=namespace_id,
                    connection_id=connection_id,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.TestNamespaceConnection,
            request=integration_interface.TestNamespaceConnectionRequest(
                namespace_id=namespace_id,
                connection_id=connection_id,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_pipeline_i_ds_by_connection_id(
        self,
        namespace_id: str,
        connection_id: str,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        async_enabled: bool = False,
    ) -> pipeline_interface.ListPipelineIDsByConnectionIDResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListPipelineIDsByConnectionID,
                request=pipeline_interface.ListPipelineIDsByConnectionIDRequest(
                    namespace_id=namespace_id,
                    connection_id=connection_id,
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListPipelineIDsByConnectionID,
            request=pipeline_interface.ListPipelineIDsByConnectionIDRequest(
                namespace_id=namespace_id,
                connection_id=connection_id,
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def list_integrations(
        self,
        total_size: int = 10,
        next_page_token: str = "",
        filter_str: str = "",
        async_enabled: bool = False,
    ) -> integration_interface.ListIntegrationsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.ListIntegrations,
                request=integration_interface.ListIntegrationsRequest(
                    page_size=total_size,
                    page_token=next_page_token,
                    filter=filter_str,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.ListIntegrations,
            request=integration_interface.ListIntegrationsRequest(
                page_size=total_size,
                page_token=next_page_token,
                filter=filter_str,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

    @grpc_handler
    def get_integration(
        self,
        integration_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> integration_interface.GetIntegrationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.host.async_client.GetIntegration,
                request=integration_interface.GetIntegrationRequest(
                    integration_id=integration_id,
                    view=pipeline_interface.Pipeline.VIEW_RECIPE,
                ),
                metadata=self.host.metadata + self.metadata,
            ).send_async()

        return RequestFactory(
            method=self.host.client.GetIntegration,
            request=integration_interface.GetIntegrationRequest(
                integration_id=integration_id,
                view=pipeline_interface.Pipeline.VIEW_RECIPE,
            ),
            metadata=self.host.metadata + self.metadata,
        ).send_sync()

