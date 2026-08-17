import multiprocessing
multiprocessing.freeze_support()  # must be first — prevents recursive spawn on Mac

import os
import sys
import threading
import webbrowser
import time
import traceback

# Set paths before importing any app module
if getattr(sys, "frozen", False):
    os.environ["KC_BASE_DIR"] = sys._MEIPASS
    docs_dir = os.path.expanduser("~/Documents/Krishna Chains")
    os.makedirs(docs_dir, exist_ok=True)
    os.environ["KC_DB_PATH"] = os.path.join(docs_dir, "billing.db")
    _log_path = os.path.join(docs_dir, "app.log")
else:
    docs_dir = None
    _log_path = "app.log"


def _log(msg):
    with open(_log_path, "a") as f:
        import datetime
        f.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n")


def _alert(title, msg):
    """Show a native Mac error dialog."""
    import subprocess
    safe = msg.replace('"', "'")
    subprocess.run([
        "osascript", "-e",
        f'display alert "{title}" message "{safe}" as critical'
    ])


def _open_browser():
    time.sleep(2.5)
    webbrowser.open("http://127.0.0.1:8000")


def _find_free_port(preferred=8000):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex(("127.0.0.1", preferred)) != 0:
            return preferred  # preferred port is free
    # fallback: let the OS assign one
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


if __name__ == "__main__":
    try:
        _log("Starting Krishna Chains...")

        import uvicorn
        from app.main import app  # imported after env vars are set

        port = _find_free_port(8000)
        _log(f"Using port {port}")

        threading.Thread(target=lambda: (
            time.sleep(2.5),
            webbrowser.open(f"http://127.0.0.1:{port}")
        ), daemon=True).start()

        config = uvicorn.Config(
            app,
            host="127.0.0.1",
            port=port,
            log_level="error",
            loop="asyncio",
        )
        server = uvicorn.Server(config)
        _log("Server starting...")
        server.run()

    except Exception:
        tb = traceback.format_exc()
        _log(f"CRASH:\n{tb}")
        _alert("Krishna Chains failed to start", tb[:300])
