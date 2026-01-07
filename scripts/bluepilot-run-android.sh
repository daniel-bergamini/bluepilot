#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ -f ".venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

export PYTHONPATH="$ROOT_DIR"
export CAPNP_PATH="$ROOT_DIR:$ROOT_DIR/cereal:$ROOT_DIR/cereal/include"
export ANDROID_STORAGE_ROOT="${ANDROID_STORAGE_ROOT:-/sdcard/flowpilot}"
export PARAMS_ROOT="${PARAMS_ROOT:-/data/data/com.termux/files/home/flowpilot/params}"
export ZMQ_MESSAGING_ADDRESS="${ZMQ_MESSAGING_ADDRESS:-0.0.0.0}"

./launch_bluepilot.sh
