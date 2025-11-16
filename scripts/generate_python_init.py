#!/usr/bin/env python3
"""
Generate __init__.py files for Python protobuf package structure.

This script traverses the generated Python code directory and creates __init__.py
files in each directory to make them proper Python packages.
"""

import os
from pathlib import Path


def generate_init_files(root_dir: str = "gen/python"):
    """
    Generate __init__.py files in all directories under the specified root.

    Args:
        root_dir: Root directory to start generating __init__.py files from
    """
    python_gen_dir = Path(root_dir)

    if not python_gen_dir.exists():
        print(f"Warning: {root_dir} does not exist. Skipping __init__.py generation.")
        return

    init_files_created = []
    init_files_existed = []

    for dirpath, dirnames, filenames in os.walk(python_gen_dir):
        # Skip __pycache__ and other special directories
        if '__pycache__' in dirpath or '.egg-info' in dirpath:
            continue

        dir_path = Path(dirpath)
        init_file = dir_path / "__init__.py"

        if not init_file.exists():
            # Create empty __init__.py file
            init_file.touch()
            init_files_created.append(str(init_file))
            print(f"Created: {init_file}")
        else:
            init_files_existed.append(str(init_file))

    print(f"\n✅ Summary:")
    print(f"   - Created {len(init_files_created)} new __init__.py files")
    print(f"   - Found {len(init_files_existed)} existing __init__.py files")


if __name__ == "__main__":
    import sys

    # Allow custom directory as argument
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "gen/python"

    print(f"Generating __init__.py files in {root_dir}...")
    generate_init_files(root_dir)
