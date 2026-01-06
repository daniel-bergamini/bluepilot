Android Port Maintenance

Initial checkout (host or proot)
1) Clone and switch to the Android branch:
   - git clone --depth 1 --branch android-port https://github.com/daniel-bergamini/bluepilot.git
   - cd bluepilot
   - git checkout android-port
   - If you already cloned without the branch: git fetch origin android-port:android-port
2) Initialize submodules:
   - git submodule update --init --depth 1

First-Run (Android proot)
0) Enter the Ubuntu rootfs shell (from Termux):
   - login-bluepilot
   - cd /data/data/com.termux/files/home/bluepilot
1) Ensure submodules are available:
   - git submodule update --init --depth 1 msgq_repo rednose_repo panda tinygrad_repo teleoprtc_repo
2) Create a per-project venv (avoid python version conflicts):
   - python3 -m venv .venv
   - . .venv/bin/activate
3) Install runtime/build deps:
   - pip install --upgrade pip setuptools wheel
   - pip install -e .
4) If git-lfs is missing in the rootfs:
   - apt update
   - apt install -y git-lfs
   - git lfs install
5) Build msgq only (avoid full SConstruct):
   - python -m SCons -C msgq_repo -j2
6) Run manager with Android env:
   - export PYTHONPATH=$PWD
   - export CAPNP_PATH=$PWD:$PWD/cereal:$PWD/cereal/include
   - export ANDROID_STORAGE_ROOT=/sdcard/flowpilot
   - ./launch_bluepilot.sh
6) Convenience runner (optional):
   - scripts/bluepilot-run-android.sh

Notes: Catch2 v2 headers on Ubuntu 24.04
- Ubuntu 24.04's `catch2` package installs Catch2 v3, which does not provide `catch2/catch.hpp`.
- Workaround (manual install of v2):
  - git clone https://github.com/catchorg/Catch2.git
  - cd Catch2
  - git checkout v2.x
  - cmake -Bbuild -H. -DBUILD_TESTING=OFF
  - sudo cmake --build build/ --target install

Env setup script
- Default rootfs: Ubuntu 24.04 (noble server rootfs).
- Old rootfs flag: --ubuntu20 (focal).
- Root mode: --root
- The setup script also configures DNS, ANDROID_DATA, PIP_ROOT_USER_ACTION, and Android `aid_*` groups.
Examples:
  - scripts/bluepilot-setup-env-android
  - scripts/bluepilot-setup-env-android --ubuntu20
  - scripts/bluepilot-setup-env-android --root

Notes on Flowpilot APK
- APK expects assets in /sdcard/flowpilot/selfdrive.
- manager.py syncs assets to external storage on Android startup.
- Params bridge (keyvald) exposes ports 6001–6003 to match the Java client.

Goal
- Keep Android glue isolated so upstream syncs are routine.
- Track Bluepilot upstream plus SunnyPilot (parent) with minimal conflicts.

Remotes
- origin: your fork
- upstream: bluepilotdev/bluepilot
- parent: sunnyhaibin/sunnypilot

Branches (suggested)
- bp-dev: upstream Bluepilot tracking branch (no Android changes)
- android-port: Android glue + integration changes

Sync flow (typical)
1) Update Bluepilot base:
   - git fetch upstream
   - git switch bp-dev
   - git merge --ff-only upstream/bp-dev
2) Rebase Android port on top:
   - git switch android-port
   - git rebase bp-dev
3) Resolve conflicts and run smoke tests.

Sync from SunnyPilot (parent)
- Use the same pattern but merge parent into bp-dev first:
  - git fetch parent
  - git switch bp-dev
  - git merge --no-ff parent/<parent-branch>
  - git push origin bp-dev
  - git switch android-port
  - git rebase bp-dev

Notes
- If your parent branch name differs (e.g., master-devbranch), replace <parent-branch>.
- Keep Android glue changes in narrow files and directories to reduce conflicts.
- Maintain a short list of Android-specific touch points in this file.

Android-specific touch points (update as you port)
- android/
- cereal/messaging/utils.py
- common/java/
- selfdrive/ui/java/
- selfdrive/modeld/java/
- selfdrive/sensord/java/
- selfdrive/launcher/java/
- selfdrive/calibration/
- system/manager/android_app.py
- system/manager/keyvald.py
- system/manager/manager.py
- system/manager/process_config.py
- system/hardware/__init__.py
- system/hardware/hw.py
- system/hardware/hw.h
- selfdrive/pandad/pandad.py
- launch_bluepilot.sh
- scripts/bluepilot-setup-env-android
