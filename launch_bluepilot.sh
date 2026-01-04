#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

export ANDROID_STORAGE_ROOT="${ANDROID_STORAGE_ROOT:-/sdcard/flowpilot}"
export PARAMS_ROOT="${PARAMS_ROOT:-${ANDROID_STORAGE_ROOT}/params}"
export LOG_ROOT="${LOG_ROOT:-${ANDROID_STORAGE_ROOT}/realdata}"
export COMMA_CACHE="${COMMA_CACHE:-${ANDROID_STORAGE_ROOT}/cache}"
export MODEL_ROOT="${MODEL_ROOT:-${ANDROID_STORAGE_ROOT}/models}"
export ZMQ_MESSAGING_PROTOCOL="${ZMQ_MESSAGING_PROTOCOL:-TCP}"

mkdir -p "$PARAMS_ROOT" "$LOG_ROOT" "$COMMA_CACHE" "$MODEL_ROOT"

exec python3 -u system/manager/manager.py
