Android Port Maintenance

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
- common/system.py
- common/path.py
- selfdrive/manager/flowinitd.py
- selfdrive/manager/process_config.py
- selfdrive/manager/services.yaml
- selfdrive/boardd/pandad.py
- selfdrive/loggerd/config.py
