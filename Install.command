#!/bin/bash
# Krishna Chains — First-time installer
# Double-click this file to remove the macOS security block on the app.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$SCRIPT_DIR/Krishna Chains.app"

if [ ! -d "$APP" ]; then
  osascript -e 'display alert "Krishna Chains.app not found" message "Make sure Install.command and Krishna Chains.app are in the same folder, then try again." as critical'
  exit 1
fi

# Prompt for password and remove the macOS quarantine flag recursively.
# sudo is required on macOS Ventura and later for this to take full effect.
osascript -e 'display dialog "Krishna Chains needs your Mac password to complete setup." default answer "" with hidden answer buttons {"Cancel", "Continue"} default button "Continue"' > /dev/null 2>&1

sudo xattr -rd com.apple.quarantine "$APP"

if [ $? -eq 0 ]; then
  osascript -e 'display alert "Setup complete!" message "Krishna Chains is ready. You can now double-click the app anytime to open it." as informational buttons {"Open App"} default button "Open App"'
  open "$APP"
else
  osascript -e 'display alert "Setup failed" message "Could not remove the security block. Please open Terminal and run:\n\nsudo xattr -rd com.apple.quarantine ~/Downloads/\"Krishna Chains.app\"" as critical'
fi
