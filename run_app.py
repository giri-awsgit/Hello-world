import os
import sys
import threading
import webbrowser
import time

# When running as a PyInstaller .app bundle, sys.frozen is True.
# Set env vars BEFORE importing app modules so database.py and main.py
# pick up the correct paths at import time.
if getattr(sys, "frozen", False):
    # All bundled files live under sys._MEIPASS
    os.environ["KC_BASE_DIR"] = sys._MEIPASS

    # Keep the database in ~/Documents/Krishna Chains/ so it survives app updates
    docs_dir = os.path.expanduser("~/Documents/Krishna Chains")
    os.makedirs(docs_dir, exist_ok=True)
    os.environ["KC_DB_PATH"] = os.path.join(docs_dir, "billing.db")

import uvicorn
from app.main import app  # imported after env vars are in place


def _open_browser():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    threading.Thread(target=_open_browser, daemon=True).start()
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
