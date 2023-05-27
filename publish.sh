#!/bin/bash

# Set the Python script path and arguments
script_path="blogfrommd/publish.py"
src_dir="temple"
#tool_dir="blogfrommd"
args="--src_dir $src_dir " #--tool_dir $tool_dir"

# Check if "serve" argument is passed
if [[ "$@" == *"serve"* ]]; then
    args+=" --serve"
fi

# Run the Python script with the arguments
echo "$script_path $args"
python3 "$script_path" $args
