package main

import (
	"fmt"
	"html/template"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strings"

	"github.com/jhump/protoreflect/desc"
	"github.com/jhump/protoreflect/desc/protoparse"
)

type generatorConfig struct {
	methodMap, customizedFieldNameMap, customizedParamMap, fieldDefaultValueMap map[string]string
	predefinedTypeMap                                                           map[string]string
	interfaceNameMap                                                            map[string]string
	protoFileInterfaceMap                                                       map[string]string
	protoDir, tmplPath, defaultInterfaceName                                    string
}

var generatorConfigMap = map[string]generatorConfig{
	"model": {
		methodMap: map[string]string{
			// "look_up_model": "lookup_model",
		},
		customizedFieldNameMap: map[string]string{
			"name":   "model_name",
			"filter": "filter_str",
		},
		fieldDefaultValueMap: map[string]string{
			"page_size":    " = 10",
			"page":         " = 0",
			"page_token":   ` = ""`,
			"filter":       ` = ""`,
			"parent":       ` = ""`,
			"order_by":     ` = ""`,
			"show_deleted": ` = False`,
		},
		customizedParamMap: map[string]string{
			"name":       `f"{self.namespace}/models/{model_name}"`,
			"view":       `model_definition_interface.VIEW_FULL`,
			"visibility": "model_interface.Model.VISIBILITY_PUBLIC",
		},
		predefinedTypeMap: map[string]string{
			"task_inputs": "model_interface.TaskInput",
			"task_input":  "model_interface.TaskInputStream",
		},
		protoDir: "./model/model/v1alpha/",
		tmplPath: "model.tmpl",
	},
	"pipeline": {
		methodMap: map[string]string{
			"validate_user_pipeline": "validate_pipeline",
			"trigger_user_pipeline":  "trigger_pipeline",
			"release":                "pipeline_release",
		},
		customizedFieldNameMap: map[string]string{
			"update_mask": "mask",
			"page_size":   "total_size",
			"page_token":  "next_page_token",
			"filter":      "filter_str",
		},
		fieldDefaultValueMap: map[string]string{
			"page_size":    " = 10",
			"page_token":   ` = ""`,
			"page":         " = 0",
			"order_by":     ` = ""`,
			"filter":       ` = ""`,
			"show_deleted": ` = False`,
		},
		customizedParamMap: map[string]string{
			"name":   "f\"{self.target_namespace}/pipelines/{name}\"",
			"target": `f"{self.target_namespace}/pipelines/{target}"`,
			"view":   `pipeline_interface.Pipeline.VIEW_RECIPE`,
		},
		predefinedTypeMap: map[string]string{
			"update_mask": "field_mask_pb2.FieldMask",
			"secret":      "secret_interface.Secret",
			"release":     "pipeline_interface.PipelineRelease",
			"sharing":     "common_pb2.Sharing",
			"visibility":  "pipeline_interface.Pipeline.Visibility",
			"pipeline":    "pipeline_interface.Pipeline",
			"connection":  "integration_interface.Connection",
		},
		interfaceNameMap: map[string]string{
			"ListConnectorDefinitions":  "component_definition",
			"GetConnectorDefinition":    "component_definition",
			"ListOperatorDefinitions":   "component_definition",
			"ListComponentDefinitions":  "component_definition",
			"GetOperatorDefinition":     "component_definition",
			"CheckName":                 "common_pb2",
			"CreateUserSecret":          "secret_interface",
			"ListUserSecrets":           "secret_interface",
			"GetUserSecret":             "secret_interface",
			"UpdateUserSecret":          "secret_interface",
			"DeleteUserSecret":          "secret_interface",
			"CreateOrganizationSecret":  "secret_interface",
			"ListOrganizationSecrets":   "secret_interface",
			"GetOrganizationSecret":     "secret_interface",
			"UpdateOrganizationSecret":  "secret_interface",
			"DeleteOrganizationSecret":  "secret_interface",
			"CreateNamespaceSecret":     "secret_interface",
			"ListNamespaceSecrets":      "secret_interface",
			"GetNamespaceSecret":        "secret_interface",
			"UpdateNamespaceSecret":     "secret_interface",
			"DeleteNamespaceSecret":     "secret_interface",
			"GetIntegration":            "integration_interface",
			"ListIntegrations":          "integration_interface",
			"TestNamespaceConnection":   "integration_interface",
			"DeleteNamespaceConnection": "integration_interface",
			"UpdateNamespaceConnection": "integration_interface",
			"CreateNamespaceConnection": "integration_interface",
			"GetNamespaceConnection":    "integration_interface",
			"ListNamespaceConnections":  "integration_interface",
		},
		protoFileInterfaceMap: map[string]string{
			"vdp/pipeline/v1beta/pipeline.proto":             "pipeline_interface",
			"vdp/pipeline/v1beta/integration.proto":          "integration_interface",
			"vdp/pipeline/v1beta/secret.proto":               "secret_interface",
			"vdp/pipeline/v1beta/common.proto":               "common_pb2",
			"vdp/pipeline/v1beta/component_definition.proto": "component_definition",
		},
		defaultInterfaceName: "pipeline_interface",
		protoDir:             "./vdp/pipeline/v1beta/",
		tmplPath:             "pipeline.tmpl",
	},
	"mgmt": {
		methodMap: nil,
		customizedFieldNameMap: map[string]string{
			"update_mask": "mask",
			"page_size":   "total_size",
			"page_token":  "next_page_token",
			"filter":      "filter_str",
		},
		fieldDefaultValueMap: map[string]string{
			"page_size":  " = 10",
			"page_token": ` = ""`,
			"filter":     ` = ""`,
		},
		customizedParamMap: map[string]string{
			"view": `mgmt_interface.VIEW_FULL`,
		},
		predefinedTypeMap: map[string]string{
			"organization": "mgmt_interface.Organization",
			"token":        "mgmt_interface.ApiToken",
			"membership":   "mgmt_interface.OrganizationMembership",
			"update_mask":  "field_mask_pb2.FieldMask",
			"start":        "timestamp_pb2.Timestamp",
			"stop":         "timestamp_pb2.Timestamp",
			//
		},
		interfaceNameMap: map[string]string{
			"ListPipelineTriggerRecords":        "metric_interface",
			"ListPipelineTriggerTableRecords":   "metric_interface",
			"ListPipelineTriggerChartRecords":   "metric_interface",
			"ListCreditConsumptionChartRecords": "metric_interface",
		},
		defaultInterfaceName: "mgmt_interface",
		protoDir:             "./core/mgmt/v1beta/",
		tmplPath:             "mgmt.tmpl",
	},
	"artifact": {
		methodMap: map[string]string{
			// "look_up_model": "lookup_model",
		},
		customizedFieldNameMap: map[string]string{
			"filter": "files_filter",
			"type":   "message_type",
		},
		customizedParamMap: map[string]string{
			"type": `conversation_interface.Message.MessageType.MESSAGE_TYPE_TEXT`,
			// "name": `f"{self.namespace}/models/{model_name}"`,
			// "view": `model_definition_interface.VIEW_FULL`,
		},
		fieldDefaultValueMap: map[string]string{
			"page_size":  " = 10",
			"page_token": ` = ""`,
		},
		predefinedTypeMap: map[string]string{
			"file":   "artifact_interface.File",
			"filter": "artifact_interface.ListCatalogFilesFilter",
			"type":   "conversation_interface.Message.MessageType.ValueType",
		},
		interfaceNameMap: map[string]string{
			"ListChunks":             "chunk_interface",
			"GetSourceFile":          "chunk_interface",
			"UpdateChunk":            "chunk_interface",
			"SimilarityChunksSearch": "chunk_interface",
			"DeleteConversation":     "conversation_interface",
			"UpdateConversation":     "conversation_interface",
			"ListConversations":      "conversation_interface",
			"CreateConversation":     "conversation_interface",
			"ListMessages":           "conversation_interface",
			"UpdateMessage":          "conversation_interface",
			"DeleteMessage":          "conversation_interface",
			"CreateMessage":          "conversation_interface",
			"QuestionAnswering":      "qa_interface",
			"GetFileCatalog":         "file_catalog_interface",
		},
		defaultInterfaceName: "artifact_interface",
		protoFileInterfaceMap: map[string]string{
			"app/app/v1alpha/app.proto":          "app_interface",
			"app/app/v1alpha/conversation.proto": "conversation_interface",
		},
		protoDir: "./artifact/artifact/v1alpha/",
		// protoDir: "./app/app/v1alpha/",
		tmplPath: "artifact.tmpl",
	},
	"app": {
		methodMap: map[string]string{
			// "look_up_model": "lookup_model",
		},
		customizedFieldNameMap: map[string]string{
			"filter": "files_filter",
			"type":   "message_type",
			"id":     "app_id",
		},
		customizedParamMap: map[string]string{
			// "type": `conversation_interface.Message.MessageType.MESSAGE_TYPE_TEXT`,
			// "name": `f"{self.namespace}/models/{model_name}"`,
			// "view": `model_definition_interface.VIEW_FULL`,
		},
		fieldDefaultValueMap: map[string]string{
			"page_size":  " = 10",
			"page_token": ` = ""`,
			"if_all":     ` = False`,
		},
		predefinedTypeMap: map[string]string{
			// "file":   "artifact_interface.File",
			// "filter": "artifact_interface.ListCatalogFilesFilter",
			// "type":   "conversation_interface.Message.MessageType.ValueType",
		},
		interfaceNameMap: map[string]string{
			// "ListChunks":             "chunk_interface",
			// "GetSourceFile":          "chunk_interface",
			// "UpdateChunk":            "chunk_interface",
			// "SimilarityChunksSearch": "chunk_interface",
			// "DeleteConversation":     "conversation_interface",
			// "UpdateConversation":     "conversation_interface",
			// "ListConversations":      "conversation_interface",
			// "CreateConversation":     "conversation_interface",
			// "ListMessages":           "conversation_interface",
			// "UpdateMessage":          "conversation_interface",
			// "DeleteMessage":          "conversation_interface",
			// "CreateMessage":          "conversation_interface",
			// "QuestionAnswering":      "qa_interface",
			// "GetFileCatalog":         "file_catalog_interface",
		},
		defaultInterfaceName: "app_interface",
		protoFileInterfaceMap: map[string]string{
			"app/app/v1alpha/app.proto":          "app_interface",
			"app/app/v1alpha/conversation.proto": "conversation_interface",
		},
		protoDir: "./app/app/v1alpha/",
		tmplPath: "app.tmpl",
	},
}

var config generatorConfig

func main() {
	if len(os.Args) < 2 {
		log.Fatalln("Please provide the client type as an argument")
	}

	clientType := os.Args[1]
	config = generatorConfigMap[clientType]

	// Slice to hold the names of .proto files
	var protoFiles []string

	// Walk the directory
	err := filepath.Walk(config.protoDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		// Check if the file has a .proto extension
		if !info.IsDir() && filepath.Ext(path) == ".proto" && !strings.Contains(path, "private") {
			protoFiles = append(protoFiles, path)
		}
		return nil
	})
	if err != nil {
		fmt.Printf("Error walking the path %q: %v\n", config.protoDir, err)
		return
	}
	// List of proto files to parse
	// files := []string{"./model/model/v1alpha/model_public_service.proto"}

	// Create a new parser
	parser := protoparse.Parser{
		ImportPaths: []string{"./../../googleapis/", "./../../grpc-gateway/", "./../../protoc-gen-validate/", "."},
	}

	// Parse the files
	descriptors, err := parser.ParseFiles(protoFiles...)
	if err != nil {
		log.Fatalf("failed to parse proto files: %v", err)
	}

	var protoDefs []protoDefinition
	// Process the parsed files
	for _, fd := range descriptors {
		protoDefs = append(protoDefs, printFileDescriptor(fd)...)
	}

	for k, v := range typeSourceMap {
		fmt.Println(k, v)
	}
	for i, def := range protoDefs {
		if v, ok := typeSourceMap[def.InputTypeName]; ok {
			protoDefs[i].InputTypeSourceFile = v
			if v, ok := config.protoFileInterfaceMap[v]; ok {
				protoDefs[i].InputTypeInterface = v
			}
		}
		if v, ok := typeSourceMap[def.OutputTypeName]; ok {
			protoDefs[i].OutputTypeSourceFile = v
			if v, ok := config.protoFileInterfaceMap[v]; ok {
				protoDefs[i].OutputTypeInterface = v
			}
		}
	}

	t, err := os.ReadFile(config.tmplPath)
	if err != nil {
		log.Fatal(err)
	}
	log.Println(string(t))

	tmpl, err := template.New("client").Funcs(template.FuncMap{
		"toSnakeCase":        toSnakeCase,
		"typeConvert":        convertType,
		"customizeFieldName": customizeFieldName,
		"customizeParam":     customizeParam,
		"isEnumOrMsgType":    isEnumOrMsgType,
		"safeHTML":           safeHTML,
		"convertMethod":      convertMethod,
		"addDefaultValue":    addDefaultValue,
		"getInterfaceName":   getInterfaceName,
	}).Parse(string(t))
	if err != nil {
		log.Fatalf("Error parsing template: %v", err)
	}

	file, err := os.Create(clientType + ".py")
	if err != nil {
		log.Fatalf("Error creating output file: %v", err)
	}
	defer file.Close()

	log.Println(len(protoDefs))

	// Execute the template and write to the file
	err = tmpl.Execute(file, protoDefs)
	if err != nil {
		log.Fatalf("Error executing template: %v", err)
	}
}

type fieldDefinition struct {
	Name, Type string
	IsRepeated bool
}

type protoDefinition struct {
	Method, FileName, InputTypeName, OutputTypeName string
	InputTypeSourceFile, OutputTypeSourceFile       string
	InputTypeInterface, OutputTypeInterface         string
	InputTypes                                      []fieldDefinition
}

var typeSourceMap = make(map[string]string)

// Function to print file descriptor details
func printFileDescriptor(fd *desc.FileDescriptor) []protoDefinition {
	fmt.Printf("File: %s\n", fd.GetName())
	var protoDefs []protoDefinition
	// typeSourceMap := make(map[string]string)

	for _, msg := range fd.GetMessageTypes() {
		fmt.Printf("  Message: %s\n", msg.GetName())
		typeSourceMap[msg.GetName()] = fd.GetName()
		for _, field := range msg.GetFields() {
			fmt.Printf("    Field: %s (type: %s)\n", field.GetName(), field.GetType().String())
		}
	}

	for _, svc := range fd.GetServices() {
		fmt.Printf("  Service: %s\n", svc.GetName())
		for _, method := range svc.GetMethods() {
			fmt.Printf("    Method: %s\n", method.GetName())
			fmt.Printf("      Input: %s\n", method.GetInputType().GetName())
			def := protoDefinition{
				Method:              method.GetName(),
				FileName:            fd.GetName(),
				InputTypeName:       method.GetInputType().GetName(),
				InputTypeInterface:  config.defaultInterfaceName,
				OutputTypeInterface: config.defaultInterfaceName,
			}

			var inputTypes, inputTypesWithDefaultValue []fieldDefinition
			for _, field := range method.GetInputType().GetFields() {
				s := fmt.Sprintf("        Field: %s (type: %s)", field.GetName(), field.GetType().String())
				// if !field.IsRequired() {
				// 	continue
				// }
				fieldDef := fieldDefinition{
					Name:       field.GetName(),
					Type:       field.GetType().String(),
					IsRepeated: field.IsRepeated(),
				}

				if msgType := field.GetMessageType(); msgType != nil {
					fieldDef.Type = msgType.GetName()
					if v, ok := config.protoFileInterfaceMap[msgType.GetFile().GetName()]; ok {
						fieldDef.Type = v + "." + fieldDef.Type
					}

					s += fmt.Sprintf(" (%s) (QualifiedName: %s)", msgType.GetName(), msgType.GetFullyQualifiedName())
					s += fmt.Sprintf(" (file: %s)", msgType.GetFile().GetName())
				}

				if _, ok := config.fieldDefaultValueMap[fieldDef.Name]; ok {
					inputTypesWithDefaultValue = append(inputTypesWithDefaultValue, fieldDef)
				} else {
					inputTypes = append(inputTypes, fieldDef)
				}

				fmt.Print(s + "\n")
			}
			def.InputTypes = append(inputTypes, inputTypesWithDefaultValue...)

			fmt.Printf("      Output: %s\n", method.GetOutputType().GetName())
			def.OutputTypeName = method.GetOutputType().GetName()
			protoDefs = append(protoDefs, def)
		}
	}

	return protoDefs
}

// LookAdmin --> look_admin
// Convert a PascalCase or camelCase string to snake_case
func toSnakeCase(str string) string {
	// Handle the case where there are multiple consecutive uppercase letters followed by lowercase
	regex := regexp.MustCompile("([a-z0-9])([A-Z])")
	snake := regex.ReplaceAllString(str, "${1}_${2}")

	// Handle the case where there are multiple consecutive uppercase letters
	regex = regexp.MustCompile("([A-Z]+)([A-Z][a-z])")
	snake = regex.ReplaceAllString(snake, "${1}_${2}")

	// Convert the entire string to lowercase
	return strings.ToLower(snake)
}

var typeMap = map[string]string{
	"TYPE_INT32":  "int",
	"TYPE_UINT32": "int",
	"TYPE_STRING": "str",
	"TYPE_BOOL":   "bool",
}

func repeatedType(isRepeated bool, fieldType string) string {
	if isRepeated {
		return fmt.Sprintf("list[%s]", fieldType)
	}
	return fieldType
}

func convertType(fieldName, fieldType string, isRepeated bool) string {
	if v, ok := config.predefinedTypeMap[fieldName]; ok {
		return repeatedType(isRepeated, v)
	}
	if v, ok := typeMap[fieldType]; ok {
		return repeatedType(isRepeated, v)
	}

	return repeatedType(isRepeated, fieldType)
}

func convertMethod(input string) string {
	// if v, ok := config.methodMap[input]; ok {
	// 	return v
	// }
	// return input
	output := strings.ReplaceAll(input, "_user_", "_")
	output = strings.ReplaceAll(output, "look_up", "lookup")
	return output
}

func customizeFieldName(s string) string {
	if v, ok := config.customizedFieldNameMap[s]; ok {
		return v
	}
	return s
}

func customizeParam(s string) string {
	if v, ok := config.customizedParamMap[s]; ok {
		return v
	}
	return customizeFieldName(s)
}

func isEnumOrMsgType(t string) bool {
	return t == "TYPE_ENUM"
}

// Custom function to mark strings as safe HTML
func safeHTML(s string) template.HTML {
	return template.HTML(s)
}

func addDefaultValue(s string) string {
	if v, ok := config.fieldDefaultValueMap[s]; ok {
		return v
	}
	return ""
}

func getInterfaceName(s string) string {
	if v, ok := config.interfaceNameMap[s]; ok {
		return v
	}
	return config.defaultInterfaceName
}
