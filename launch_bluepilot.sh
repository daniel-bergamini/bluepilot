#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Android wrapper defaults
export ANDROID_STORAGE_ROOT="${ANDROID_STORAGE_ROOT:-/sdcard/flowpilot}"
export PARAMS_ROOT="${PARAMS_ROOT:-${ANDROID_STORAGE_ROOT}/params}"
export LOG_ROOT="${LOG_ROOT:-${ANDROID_STORAGE_ROOT}/realdata}"
export COMMA_CACHE="${COMMA_CACHE:-${ANDROID_STORAGE_ROOT}/cache}"
export MODEL_ROOT="${MODEL_ROOT:-${ANDROID_STORAGE_ROOT}/models}"

export PASSIVE="${PASSIVE:-0}"
export ZMQ_MESSAGING_PROTOCOL="${ZMQ_MESSAGING_PROTOCOL:-TCP}"

mkdir -p "$PARAMS_ROOT" "$LOG_ROOT" "$COMMA_CACHE" "$MODEL_ROOT"

if pgrep -x "manager" > /dev/null; then
  echo "another instance of manager is already running"
  exit 1
fi

if command -v tmux >/dev/null 2>&1; then
  tmux new-session -d -s "bluepilot" "python3 -u system/manager/manager.py"
  tmux attach -t bluepilot
else
  exec python3 -u system/manager/manager.py
fi

while true; do sleep 1; done
