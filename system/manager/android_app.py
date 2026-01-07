#!/usr/bin/env python3
import os
import shutil
import subprocess
import time

from openpilot.common.swaglog import cloudlog

APP_COMPONENT = os.getenv("ANDROID_APP_COMPONENT", "ai.flow.android/ai.flow.android.AndroidLauncher")
APP_PROCESS = os.getenv("ANDROID_APP_PROCESS", "ai.flow.android")


def app_running() -> bool:
  try:
    out = subprocess.check_output(["pidof", APP_PROCESS], text=True).strip()
    return bool(out)
  except Exception:
    return False


def launch_app() -> None:
  try:
    am_candidates = [
      shutil.which("am"),
      "/system/bin/am",
      "/host-rootfs/system/bin/am",
    ]
    am_cmd = next((p for p in am_candidates if p and os.path.exists(p)), None)
    if not am_cmd:
      raise FileNotFoundError("am not found (checked PATH, /system/bin/am, /host-rootfs/system/bin/am)")
    if am_cmd.startswith("/host-rootfs/"):
      subprocess.run(["/system/bin/sh", am_cmd, "start", "--user", "0", "-n", APP_COMPONENT], check=False)
    else:
      subprocess.run([am_cmd, "start", "--user", "0", "-n", APP_COMPONENT], check=False)
  except Exception as exc:
    cloudlog.exception(f"android_app launch failed: {exc}")


def main() -> None:
  if not os.getenv("ANDROID_DATA"):
    cloudlog.warning("ANDROID_DATA not set; android_app will not run")
    return

  cloudlog.info(f"android_app monitor start: {APP_COMPONENT}")
  while True:
    if not app_running():
      cloudlog.warning("android_app not running, starting")
      launch_app()
    time.sleep(5)


if __name__ == "__main__":
  main()
