#!/bin/bash
# Krishna Chains — First-time installer
# Double-click this file to remove the macOS security block on the app.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$SCRIPT_DIR/Krishna Chains.app"

if [ ! -d "$APP" ]; then
  osascript -e 'display alert "Krishna Chains.app not found" message "Make sure Install.command and Krishna Chains.app are in the same folder." as critical'
  exit 1
fi

# Remove macOS quarantine flag so Gatekeeper stops blocking the app
xattr -cr "$APP"

osascript -e 'display alert "Setup complete!" message "You can now double-click Krishna Chains.app to open it anytime." as informational'

# Open the app immediately
open "$APP"
