# Python Protobuf Generation Scripts

## Overview

This directory contains scripts to enhance the Python protobuf generation process by automatically creating `__init__.py` files in all generated package directories.

## Files

### `generate_python_init.py`

Automatically generates `__init__.py` files in all directories under `gen/python/` to make them proper Python packages.

#### Usage

```bash
# Generate __init__.py files in default location (gen/python)
python3 scripts/generate_python_init.py

# Generate __init__.py files in custom location
python3 scripts/generate_python_init.py path/to/python/package
```

#### Features

- Creates empty `__init__.py` files in all directories
- Skips special directories (`__pycache__`, `.egg-info`)
- Provides summary of files created vs existing
- Idempotent - safe to run multiple times

## Integration

### Local Development

Use the Makefile target:

```bash
# Generate Go and Python protobuf stubs
make gen
```

The `make gen` target will:

1. Run `buf generate` to create Go and Python protobuf files
2. Automatically create `__init__.py` files in all Python package directories
3. Display a summary of the generation process

### CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/buf-ci.yaml`) automatically runs the script after `buf generate` to ensure all pushed Python packages have proper package structure.

## Why `__init__.py` Files?

Python requires `__init__.py` files in directories to treat them as packages. Without these files:

- Imports will fail with `ModuleNotFoundError`
- IDE autocomplete and type hints won't work properly
- Package structure won't be recognized

The standard protobuf Python plugins don't generate these files automatically, so this script fills that gap.

## Example Output

```text
Generating __init__.py files in gen/python...
Created: gen/python/__init__.py
Created: gen/python/artifact/__init__.py
Created: gen/python/artifact/artifact/__init__.py
Created: gen/python/artifact/artifact/v1alpha/__init__.py
...

✅ Summary:
   - Created 24 new __init__.py files
   - Found 0 existing __init__.py files
```
