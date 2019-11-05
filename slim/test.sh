#!/bin/bash

# Exit script on error.
set -e
# Echo each command, easier for debugging.
set -x
source "$PWD/constants.sh"
python3 d_and_convert.py \
  --dataset_name=flowers \
  --dataset_dir="${DATASET_DIR}"