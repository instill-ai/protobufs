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
	methodMap, customizedFieldNameMap, customizedParamMap map[string]string
	protoDir, tmplPath                                    string
}

var generatorConfigMap = map[string]generatorConfig{
	"model": {
		methodMap: nil,
		customizedFieldNameMap: map[string]string{
			"name": "model_name",
		},
		customizedParamMap: nil,
		protoDir:           "./model/model/v1alpha/",
		tmplPath:           "model.tmpl",
	},
	"pipeline": {
		methodMap: map[string]string{
			"validate_user_pipeline": "validate_pipeline",
			"trigger_user_pipeline":  "trigger_pipeline",
		},
		customizedFieldNameMap: nil,
		customizedParamMap: map[string]string{
			"name": "f\"{self.target_namespace}/pipelines/{name}\"",
			"view": `pipeline_interface.Pipeline.VIEW_RECIPE`,
		},
		protoDir: "./vdp/pipeline/v1beta/",
		tmplPath: "pipeline.tmpl",
	},
}

var config generatorConfig

func main() {
	clientType := "pipeline"
	config = generatorConfigMap[clientType]

	// Slice to hold the names of .proto files
	var protoFiles []string

	// Walk the directory
	err := filepath.Walk(config.protoDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		// Check if the file has a .proto extension
		if !info.IsDir() && filepath.Ext(path) == ".proto" {
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
		ImportPaths: []string{"./../../googleapis/", "./../../grpc-gateway/", "."},
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
}

type protoDefinition struct {
	Method, FileName, InputTypeName, OutputTypeName string
	InputTypes                                      []fieldDefinition
}

// Function to print file descriptor details
func printFileDescriptor(fd *desc.FileDescriptor) []protoDefinition {
	fmt.Printf("File: %s\n", fd.GetName())
	var protoDefs []protoDefinition

	for _, svc := range fd.GetServices() {
		fmt.Printf("  Service: %s\n", svc.GetName())
		for _, method := range svc.GetMethods() {
			fmt.Printf("    Method: %s\n", method.GetName())
			fmt.Printf("      Input: %s\n", method.GetInputType().GetName())
			def := protoDefinition{
				Method:        method.GetName(),
				FileName:      fd.GetName(),
				InputTypeName: method.GetInputType().GetName(),
			}

			for _, field := range method.GetInputType().GetFields() {
				s := fmt.Sprintf("        Field: %s (type: %s)", field.GetName(), field.GetType().String())
				def.InputTypes = append(def.InputTypes, fieldDefinition{Name: field.GetName(), Type: field.GetType().String()})
				if msgType := field.GetMessageType(); msgType != nil {
					s += fmt.Sprintf(" (%s) ", msgType.GetName())
				}
				fmt.Print(s + "\n")
			}
			fmt.Printf("      Output: %s\n", method.GetOutputType().GetName())
			def.OutputTypeName = method.GetOutputType().GetName()
			protoDefs = append(protoDefs, def)
		}
	}

	for _, msg := range fd.GetMessageTypes() {
		fmt.Printf("  Message: %s\n", msg.GetName())
		for _, field := range msg.GetFields() {
			fmt.Printf("    Field: %s (type: %s)\n", field.GetName(), field.GetType().String())
		}
	}
	return protoDefs
}

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
	"TYPE_STRING": "str",
	"TYPE_BOOL":   "bool",
}

func convertType(input string) string {
	if v, ok := typeMap[input]; ok {
		return v
	}
	return input
}

func convertMethod(input string) string {
	// if v, ok := config.methodMap[input]; ok {
	// 	return v
	// }
	// return input
	return strings.ReplaceAll(input, "_user_", "_")
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
