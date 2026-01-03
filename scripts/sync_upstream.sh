#!/usr/bin/env bash
set -euo pipefail

REMOTE="${1:-upstream}"
BASE_BRANCH="${2:-bp-dev}"
PORT_BRANCH="${3:-android-port}"

echo "Fetching $REMOTE..."
git fetch "$REMOTE"

echo "Updating base branch $BASE_BRANCH from $REMOTE/$BASE_BRANCH..."
git switch "$BASE_BRANCH"
git merge --ff-only "$REMOTE/$BASE_BRANCH"

echo "Rebasing $PORT_BRANCH onto $BASE_BRANCH..."
git switch "$PORT_BRANCH"
git rebase "$BASE_BRANCH"

echo "Done. Resolve any conflicts and run smoke tests."
