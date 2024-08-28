from typing import Dict

from google.protobuf import field_mask_pb2

# common
import instill.protogen.common.healthcheck.v1beta.healthcheck_pb2 as healthcheck
import instill.protogen.model.model.v1alpha.model_definition_pb2 as model_definition_interface

# model
import instill.protogen.model.model.v1alpha.model_pb2 as model_interface
import instill.protogen.model.model.v1alpha.model_public_service_pb2_grpc as model_service
from instill.clients.base import Client, RequestFactory
from instill.clients.constant import DEFAULT_INSTANCE
from instill.clients.instance import InstillInstance
from instill.configuration import global_config
from instill.utils.error_handler import grpc_handler


class ModelClient(Client):


    @grpc_handler
    def liveness(
        self,
        health_check_request: TYPE_MESSAGE,
        async_enabled: bool = False,
    ) -> model_interface.LivenessResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.Liveness,
                request=model_interface.LivenessRequest(
                    health_check_request=health_check_request,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.Liveness,
            request=model_interface.LivenessRequest(
                health_check_request=health_check_request,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def readiness(
        self,
        health_check_request: TYPE_MESSAGE,
        async_enabled: bool = False,
    ) -> model_interface.ReadinessResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.Readiness,
                request=model_interface.ReadinessRequest(
                    health_check_request=health_check_request,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.Readiness,
            request=model_interface.ReadinessRequest(
                health_check_request=health_check_request,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_model_definitions(
        self,
        view: TYPE_ENUM,
        page_size: int = 10,
        page_token: str = "",
        async_enabled: bool = False,
    ) -> model_interface.ListModelDefinitionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListModelDefinitions,
                request=model_interface.ListModelDefinitionsRequest(
                    view=model_definition_interface.VIEW_FULL,
                    page_size=page_size,
                    page_token=page_token,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListModelDefinitions,
            request=model_interface.ListModelDefinitionsRequest(
                view=model_definition_interface.VIEW_FULL,
                page_size=page_size,
                page_token=page_token,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_available_regions(
        self,
        async_enabled: bool = False,
    ) -> model_interface.ListAvailableRegionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListAvailableRegions,
                request=model_interface.ListAvailableRegionsRequest(
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListAvailableRegions,
            request=model_interface.ListAvailableRegionsRequest(
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_model_definition(
        self,
        view: TYPE_ENUM,
        model_definition_id: str,
        async_enabled: bool = False,
    ) -> model_interface.GetModelDefinitionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetModelDefinition,
                request=model_interface.GetModelDefinitionRequest(
                    view=model_definition_interface.VIEW_FULL,
                    model_definition_id=model_definition_id,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetModelDefinition,
            request=model_interface.GetModelDefinitionRequest(
                view=model_definition_interface.VIEW_FULL,
                model_definition_id=model_definition_id,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_models(
        self,
        view: TYPE_ENUM,
        visibility: TYPE_ENUM,
        page_size: int = 10,
        page_token: str = "",
        show_deleted: bool = False,
        filter_str: str = "",
        order_by: str = "",
        async_enabled: bool = False,
    ) -> model_interface.ListModelsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListModels,
                request=model_interface.ListModelsRequest(
                    view=model_definition_interface.VIEW_FULL,
                    visibility=model_interface.Model.VISIBILITY_PUBLIC,
                    page_size=page_size,
                    page_token=page_token,
                    show_deleted=show_deleted,
                    filter=filter_str,
                    order_by=order_by,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListModels,
            request=model_interface.ListModelsRequest(
                view=model_definition_interface.VIEW_FULL,
                visibility=model_interface.Model.VISIBILITY_PUBLIC,
                page_size=page_size,
                page_token=page_token,
                show_deleted=show_deleted,
                filter=filter_str,
                order_by=order_by,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def lookup_model(
        self,
        permalink: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.LookUpModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.LookUpModel,
                request=model_interface.LookUpModelRequest(
                    permalink=permalink,
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.LookUpModel,
            request=model_interface.LookUpModelRequest(
                permalink=permalink,
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_namespace_models(
        self,
        namespace_id: str,
        view: TYPE_ENUM,
        visibility: TYPE_ENUM,
        page_size: int = 10,
        page_token: str = "",
        show_deleted: bool = False,
        filter_str: str = "",
        order_by: str = "",
        async_enabled: bool = False,
    ) -> model_interface.ListNamespaceModelsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListNamespaceModels,
                request=model_interface.ListNamespaceModelsRequest(
                    namespace_id=namespace_id,
                    view=model_definition_interface.VIEW_FULL,
                    visibility=model_interface.Model.VISIBILITY_PUBLIC,
                    page_size=page_size,
                    page_token=page_token,
                    show_deleted=show_deleted,
                    filter=filter_str,
                    order_by=order_by,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListNamespaceModels,
            request=model_interface.ListNamespaceModelsRequest(
                namespace_id=namespace_id,
                view=model_definition_interface.VIEW_FULL,
                visibility=model_interface.Model.VISIBILITY_PUBLIC,
                page_size=page_size,
                page_token=page_token,
                show_deleted=show_deleted,
                filter=filter_str,
                order_by=order_by,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def create_namespace_model(
        self,
        namespace_id: str,
        model: TYPE_MESSAGE,
        async_enabled: bool = False,
    ) -> model_interface.CreateNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.CreateNamespaceModel,
                request=model_interface.CreateNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model=model,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.CreateNamespaceModel,
            request=model_interface.CreateNamespaceModelRequest(
                namespace_id=namespace_id,
                model=model,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetNamespaceModel,
                request=model_interface.GetNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetNamespaceModel,
            request=model_interface.GetNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def update_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        model: TYPE_MESSAGE,
        update_mask: TYPE_MESSAGE,
        async_enabled: bool = False,
    ) -> model_interface.UpdateNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.UpdateNamespaceModel,
                request=model_interface.UpdateNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    model=model,
                    update_mask=update_mask,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.UpdateNamespaceModel,
            request=model_interface.UpdateNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                model=model,
                update_mask=update_mask,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def delete_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        async_enabled: bool = False,
    ) -> model_interface.DeleteNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.DeleteNamespaceModel,
                request=model_interface.DeleteNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.DeleteNamespaceModel,
            request=model_interface.DeleteNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def rename_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        new_model_id: str,
        async_enabled: bool = False,
    ) -> model_interface.RenameNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.RenameNamespaceModel,
                request=model_interface.RenameNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    new_model_id=new_model_id,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.RenameNamespaceModel,
            request=model_interface.RenameNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                new_model_id=new_model_id,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def watch_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.WatchNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.WatchNamespaceModel,
                request=model_interface.WatchNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.WatchNamespaceModel,
            request=model_interface.WatchNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def watch_namespace_latest_model(
        self,
        namespace_id: str,
        model_id: str,
        async_enabled: bool = False,
    ) -> model_interface.WatchNamespaceLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.WatchNamespaceLatestModel,
                request=model_interface.WatchNamespaceLatestModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.WatchNamespaceLatestModel,
            request=model_interface.WatchNamespaceLatestModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_namespace_model_versions(
        self,
        namespace_id: str,
        model_id: str,
        page_size: int = 10,
        page: int = 0,
        async_enabled: bool = False,
    ) -> model_interface.ListNamespaceModelVersionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListNamespaceModelVersions,
                request=model_interface.ListNamespaceModelVersionsRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    page_size=page_size,
                    page=page,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListNamespaceModelVersions,
            request=model_interface.ListNamespaceModelVersionsRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                page_size=page_size,
                page=page,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def delete_namespace_model_version(
        self,
        namespace_id: str,
        model_id: str,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.DeleteNamespaceModelVersionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.DeleteNamespaceModelVersion,
                request=model_interface.DeleteNamespaceModelVersionRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.DeleteNamespaceModelVersion,
            request=model_interface.DeleteNamespaceModelVersionRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        task_inputs: list[model_interface.TaskInput],
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerNamespaceModel,
                request=model_interface.TriggerNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    task_inputs=task_inputs,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerNamespaceModel,
            request=model_interface.TriggerNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                task_inputs=task_inputs,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_namespace_model(
        self,
        namespace_id: str,
        model_id: str,
        task_inputs: list[model_interface.TaskInput],
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerAsyncNamespaceModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerAsyncNamespaceModel,
                request=model_interface.TriggerAsyncNamespaceModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    task_inputs=task_inputs,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerAsyncNamespaceModel,
            request=model_interface.TriggerAsyncNamespaceModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                task_inputs=task_inputs,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_latest_model(
        self,
        namespace_id: str,
        model_id: str,
        task_inputs: list[model_interface.TaskInput],
        async_enabled: bool = False,
    ) -> model_interface.TriggerNamespaceLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerNamespaceLatestModel,
                request=model_interface.TriggerNamespaceLatestModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    task_inputs=task_inputs,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerNamespaceLatestModel,
            request=model_interface.TriggerNamespaceLatestModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                task_inputs=task_inputs,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_namespace_latest_model(
        self,
        namespace_id: str,
        model_id: str,
        task_inputs: list[model_interface.TaskInput],
        async_enabled: bool = False,
    ) -> model_interface.TriggerAsyncNamespaceLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerAsyncNamespaceLatestModel,
                request=model_interface.TriggerAsyncNamespaceLatestModelRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    task_inputs=task_inputs,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerAsyncNamespaceLatestModel,
            request=model_interface.TriggerAsyncNamespaceLatestModelRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                task_inputs=task_inputs,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_model_binary_file_upload(
        self,
        namespace_id: str,
        model_id: str,
        task_input: model_interface.TaskInputStream,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerNamespaceModelBinaryFileUploadResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerNamespaceModelBinaryFileUpload,
                request=model_interface.TriggerNamespaceModelBinaryFileUploadRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    task_input=task_input,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerNamespaceModelBinaryFileUpload,
            request=model_interface.TriggerNamespaceModelBinaryFileUploadRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                task_input=task_input,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_namespace_latest_model_binary_file_upload(
        self,
        namespace_id: str,
        model_id: str,
        task_input: model_interface.TaskInputStream,
        async_enabled: bool = False,
    ) -> model_interface.TriggerNamespaceLatestModelBinaryFileUploadResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerNamespaceLatestModelBinaryFileUpload,
                request=model_interface.TriggerNamespaceLatestModelBinaryFileUploadRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    task_input=task_input,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerNamespaceLatestModelBinaryFileUpload,
            request=model_interface.TriggerNamespaceLatestModelBinaryFileUploadRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                task_input=task_input,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_model_operation(
        self,
        namespace_id: str,
        model_id: str,
        version: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetNamespaceModelOperationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetNamespaceModelOperation,
                request=model_interface.GetNamespaceModelOperationRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    version=version,
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetNamespaceModelOperation,
            request=model_interface.GetNamespaceModelOperationRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                version=version,
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_namespace_latest_model_operation(
        self,
        namespace_id: str,
        model_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetNamespaceLatestModelOperationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetNamespaceLatestModelOperation,
                request=model_interface.GetNamespaceLatestModelOperationRequest(
                    namespace_id=namespace_id,
                    model_id=model_id,
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetNamespaceLatestModelOperation,
            request=model_interface.GetNamespaceLatestModelOperationRequest(
                namespace_id=namespace_id,
                model_id=model_id,
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_model_operation(
        self,
        operation_id: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetModelOperationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetModelOperation,
                request=model_interface.GetModelOperationRequest(
                    operation_id=operation_id,
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetModelOperation,
            request=model_interface.GetModelOperationRequest(
                operation_id=operation_id,
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_models(
        self,
        view: TYPE_ENUM,
        visibility: TYPE_ENUM,
        page_size: int = 10,
        page_token: str = "",
        parent: str = "",
        show_deleted: bool = False,
        filter_str: str = "",
        order_by: str = "",
        async_enabled: bool = False,
    ) -> model_interface.ListUserModelsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListUserModels,
                request=model_interface.ListUserModelsRequest(
                    view=model_definition_interface.VIEW_FULL,
                    visibility=model_interface.Model.VISIBILITY_PUBLIC,
                    page_size=page_size,
                    page_token=page_token,
                    parent=parent,
                    show_deleted=show_deleted,
                    filter=filter_str,
                    order_by=order_by,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListUserModels,
            request=model_interface.ListUserModelsRequest(
                view=model_definition_interface.VIEW_FULL,
                visibility=model_interface.Model.VISIBILITY_PUBLIC,
                page_size=page_size,
                page_token=page_token,
                parent=parent,
                show_deleted=show_deleted,
                filter=filter_str,
                order_by=order_by,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def create_model(
        self,
        model: TYPE_MESSAGE,
        parent: str = "",
        async_enabled: bool = False,
    ) -> model_interface.CreateUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.CreateUserModel,
                request=model_interface.CreateUserModelRequest(
                    model=model,
                    parent=parent,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.CreateUserModel,
            request=model_interface.CreateUserModelRequest(
                model=model,
                parent=parent,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_model(
        self,
        model_name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetUserModel,
                request=model_interface.GetUserModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetUserModel,
            request=model_interface.GetUserModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def update_model(
        self,
        model: TYPE_MESSAGE,
        update_mask: TYPE_MESSAGE,
        async_enabled: bool = False,
    ) -> model_interface.UpdateUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.UpdateUserModel,
                request=model_interface.UpdateUserModelRequest(
                    model=model,
                    update_mask=update_mask,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.UpdateUserModel,
            request=model_interface.UpdateUserModelRequest(
                model=model,
                update_mask=update_mask,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def delete_model(
        self,
        model_name: str,
        async_enabled: bool = False,
    ) -> model_interface.DeleteUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.DeleteUserModel,
                request=model_interface.DeleteUserModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.DeleteUserModel,
            request=model_interface.DeleteUserModelRequest(
                name=f"{self.namespace}/models/{model_name}",
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def rename_model(
        self,
        model_name: str,
        new_model_id: str,
        async_enabled: bool = False,
    ) -> model_interface.RenameUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.RenameUserModel,
                request=model_interface.RenameUserModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    new_model_id=new_model_id,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.RenameUserModel,
            request=model_interface.RenameUserModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                new_model_id=new_model_id,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def watch_model(
        self,
        model_name: str,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.WatchUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.WatchUserModel,
                request=model_interface.WatchUserModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.WatchUserModel,
            request=model_interface.WatchUserModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def watch_latest_model(
        self,
        model_name: str,
        async_enabled: bool = False,
    ) -> model_interface.WatchUserLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.WatchUserLatestModel,
                request=model_interface.WatchUserLatestModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.WatchUserLatestModel,
            request=model_interface.WatchUserLatestModelRequest(
                name=f"{self.namespace}/models/{model_name}",
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_model_versions(
        self,
        model_name: str,
        page_size: int = 10,
        page: int = 0,
        async_enabled: bool = False,
    ) -> model_interface.ListUserModelVersionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListUserModelVersions,
                request=model_interface.ListUserModelVersionsRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    page_size=page_size,
                    page=page,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListUserModelVersions,
            request=model_interface.ListUserModelVersionsRequest(
                name=f"{self.namespace}/models/{model_name}",
                page_size=page_size,
                page=page,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def delete_model_version(
        self,
        model_name: str,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.DeleteUserModelVersionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.DeleteUserModelVersion,
                request=model_interface.DeleteUserModelVersionRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.DeleteUserModelVersion,
            request=model_interface.DeleteUserModelVersionRequest(
                name=f"{self.namespace}/models/{model_name}",
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerUserModel,
                request=model_interface.TriggerUserModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerUserModel,
            request=model_interface.TriggerUserModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerAsyncUserModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerAsyncUserModel,
                request=model_interface.TriggerAsyncUserModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerAsyncUserModel,
            request=model_interface.TriggerAsyncUserModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_latest_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        async_enabled: bool = False,
    ) -> model_interface.TriggerUserLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerUserLatestModel,
                request=model_interface.TriggerUserLatestModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerUserLatestModel,
            request=model_interface.TriggerUserLatestModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_latest_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        async_enabled: bool = False,
    ) -> model_interface.TriggerAsyncUserLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerAsyncUserLatestModel,
                request=model_interface.TriggerAsyncUserLatestModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerAsyncUserLatestModel,
            request=model_interface.TriggerAsyncUserLatestModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_model_binary_file_upload(
        self,
        model_name: str,
        task_input: model_interface.TaskInputStream,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerUserModelBinaryFileUploadResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerUserModelBinaryFileUpload,
                request=model_interface.TriggerUserModelBinaryFileUploadRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_input=task_input,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerUserModelBinaryFileUpload,
            request=model_interface.TriggerUserModelBinaryFileUploadRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_input=task_input,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_organization_models(
        self,
        view: TYPE_ENUM,
        visibility: TYPE_ENUM,
        page_size: int = 10,
        page_token: str = "",
        parent: str = "",
        show_deleted: bool = False,
        filter_str: str = "",
        order_by: str = "",
        async_enabled: bool = False,
    ) -> model_interface.ListOrganizationModelsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListOrganizationModels,
                request=model_interface.ListOrganizationModelsRequest(
                    view=model_definition_interface.VIEW_FULL,
                    visibility=model_interface.Model.VISIBILITY_PUBLIC,
                    page_size=page_size,
                    page_token=page_token,
                    parent=parent,
                    show_deleted=show_deleted,
                    filter=filter_str,
                    order_by=order_by,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListOrganizationModels,
            request=model_interface.ListOrganizationModelsRequest(
                view=model_definition_interface.VIEW_FULL,
                visibility=model_interface.Model.VISIBILITY_PUBLIC,
                page_size=page_size,
                page_token=page_token,
                parent=parent,
                show_deleted=show_deleted,
                filter=filter_str,
                order_by=order_by,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def create_organization_model(
        self,
        model: TYPE_MESSAGE,
        parent: str = "",
        async_enabled: bool = False,
    ) -> model_interface.CreateOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.CreateOrganizationModel,
                request=model_interface.CreateOrganizationModelRequest(
                    model=model,
                    parent=parent,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.CreateOrganizationModel,
            request=model_interface.CreateOrganizationModelRequest(
                model=model,
                parent=parent,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_organization_model(
        self,
        model_name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetOrganizationModel,
                request=model_interface.GetOrganizationModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetOrganizationModel,
            request=model_interface.GetOrganizationModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def update_organization_model(
        self,
        model: TYPE_MESSAGE,
        update_mask: TYPE_MESSAGE,
        async_enabled: bool = False,
    ) -> model_interface.UpdateOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.UpdateOrganizationModel,
                request=model_interface.UpdateOrganizationModelRequest(
                    model=model,
                    update_mask=update_mask,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.UpdateOrganizationModel,
            request=model_interface.UpdateOrganizationModelRequest(
                model=model,
                update_mask=update_mask,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def delete_organization_model(
        self,
        model_name: str,
        async_enabled: bool = False,
    ) -> model_interface.DeleteOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.DeleteOrganizationModel,
                request=model_interface.DeleteOrganizationModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.DeleteOrganizationModel,
            request=model_interface.DeleteOrganizationModelRequest(
                name=f"{self.namespace}/models/{model_name}",
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def rename_organization_model(
        self,
        model_name: str,
        new_model_id: str,
        async_enabled: bool = False,
    ) -> model_interface.RenameOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.RenameOrganizationModel,
                request=model_interface.RenameOrganizationModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    new_model_id=new_model_id,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.RenameOrganizationModel,
            request=model_interface.RenameOrganizationModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                new_model_id=new_model_id,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def watch_organization_model(
        self,
        model_name: str,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.WatchOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.WatchOrganizationModel,
                request=model_interface.WatchOrganizationModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.WatchOrganizationModel,
            request=model_interface.WatchOrganizationModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def watch_organization_latest_model(
        self,
        model_name: str,
        async_enabled: bool = False,
    ) -> model_interface.WatchOrganizationLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.WatchOrganizationLatestModel,
                request=model_interface.WatchOrganizationLatestModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.WatchOrganizationLatestModel,
            request=model_interface.WatchOrganizationLatestModelRequest(
                name=f"{self.namespace}/models/{model_name}",
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_organization_model_versions(
        self,
        model_name: str,
        page_size: int = 10,
        page: int = 0,
        async_enabled: bool = False,
    ) -> model_interface.ListOrganizationModelVersionsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListOrganizationModelVersions,
                request=model_interface.ListOrganizationModelVersionsRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    page_size=page_size,
                    page=page,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListOrganizationModelVersions,
            request=model_interface.ListOrganizationModelVersionsRequest(
                name=f"{self.namespace}/models/{model_name}",
                page_size=page_size,
                page=page,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def delete_organization_model_version(
        self,
        model_name: str,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.DeleteOrganizationModelVersionResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.DeleteOrganizationModelVersion,
                request=model_interface.DeleteOrganizationModelVersionRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.DeleteOrganizationModelVersion,
            request=model_interface.DeleteOrganizationModelVersionRequest(
                name=f"{self.namespace}/models/{model_name}",
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_organization_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerOrganizationModel,
                request=model_interface.TriggerOrganizationModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerOrganizationModel,
            request=model_interface.TriggerOrganizationModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_organization_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerAsyncOrganizationModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerAsyncOrganizationModel,
                request=model_interface.TriggerAsyncOrganizationModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerAsyncOrganizationModel,
            request=model_interface.TriggerAsyncOrganizationModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_organization_latest_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        async_enabled: bool = False,
    ) -> model_interface.TriggerOrganizationLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerOrganizationLatestModel,
                request=model_interface.TriggerOrganizationLatestModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerOrganizationLatestModel,
            request=model_interface.TriggerOrganizationLatestModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_async_organization_latest_model(
        self,
        model_name: str,
        task_inputs: list[model_interface.TaskInput],
        async_enabled: bool = False,
    ) -> model_interface.TriggerAsyncOrganizationLatestModelResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerAsyncOrganizationLatestModel,
                request=model_interface.TriggerAsyncOrganizationLatestModelRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_inputs=task_inputs,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerAsyncOrganizationLatestModel,
            request=model_interface.TriggerAsyncOrganizationLatestModelRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_inputs=task_inputs,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def trigger_organization_model_binary_file_upload(
        self,
        model_name: str,
        task_input: model_interface.TaskInputStream,
        version: str,
        async_enabled: bool = False,
    ) -> model_interface.TriggerOrganizationModelBinaryFileUploadResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.TriggerOrganizationModelBinaryFileUpload,
                request=model_interface.TriggerOrganizationModelBinaryFileUploadRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    task_input=task_input,
                    version=version,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.TriggerOrganizationModelBinaryFileUpload,
            request=model_interface.TriggerOrganizationModelBinaryFileUploadRequest(
                name=f"{self.namespace}/models/{model_name}",
                task_input=task_input,
                version=version,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_latest_model_operation(
        self,
        model_name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetUserLatestModelOperationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetUserLatestModelOperation,
                request=model_interface.GetUserLatestModelOperationRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetUserLatestModelOperation,
            request=model_interface.GetUserLatestModelOperationRequest(
                name=f"{self.namespace}/models/{model_name}",
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def get_organization_latest_model_operation(
        self,
        model_name: str,
        view: TYPE_ENUM,
        async_enabled: bool = False,
    ) -> model_interface.GetOrganizationLatestModelOperationResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.GetOrganizationLatestModelOperation,
                request=model_interface.GetOrganizationLatestModelOperationRequest(
                    name=f"{self.namespace}/models/{model_name}",
                    view=model_definition_interface.VIEW_FULL,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.GetOrganizationLatestModelOperation,
            request=model_interface.GetOrganizationLatestModelOperationRequest(
                name=f"{self.namespace}/models/{model_name}",
                view=model_definition_interface.VIEW_FULL,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

    @grpc_handler
    def list_model_runs(
        self,
        view: TYPE_ENUM,
        namespace_id: str,
        model_id: str,
        page_size: int = 10,
        page: int = 0,
        order_by: str = "",
        filter_str: str = "",
        async_enabled: bool = False,
    ) -> model_interface.ListModelRunsResponse:
        if async_enabled:
            return RequestFactory(
                method=self.hosts[self.instance].async_client.ListModelRuns,
                request=model_interface.ListModelRunsRequest(
                    view=model_definition_interface.VIEW_FULL,
                    namespace_id=namespace_id,
                    model_id=model_id,
                    page_size=page_size,
                    page=page,
                    order_by=order_by,
                    filter=filter_str,
                ),
                metadata=self.hosts[self.instance].metadata,
            ).send_async()

        return RequestFactory(
            method=self.hosts[self.instance].client.ListModelRuns,
            request=model_interface.ListModelRunsRequest(
                view=model_definition_interface.VIEW_FULL,
                namespace_id=namespace_id,
                model_id=model_id,
                page_size=page_size,
                page=page,
                order_by=order_by,
                filter=filter_str,
            ),
            metadata=self.hosts[self.instance].metadata,
        ).send_sync()

