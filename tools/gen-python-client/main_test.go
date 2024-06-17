package main

import (
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestFilePath(t *testing.T) {
	dir := "./../../model/model/v1alpha/"
	var protoFiles []string

	// Walk the directory
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		// Check if the file has a .proto extension
		if !info.IsDir() && filepath.Ext(path) == ".proto" {
			protoFiles = append(protoFiles, path)
		}
		return nil
	})
	require.NoError(t, err)

	for _, file := range protoFiles {
		t.Log(file)
	}
}

func TestToSnakeCase(t *testing.T) {
	testCases := []struct {
		input    string
		expected string
	}{{
		input: "FilePath", expected: "file_path",
	}, {
		input: "FilePathToDelete", expected: "file_path_to_delete",
	}, {
		input: "YetAnotherHTTPRequestExample", expected: "yet_another_http_request_example",
	}}

	for _, tc := range testCases {
		require.Equal(t, tc.expected, toSnakeCase(tc.input))
	}
}
