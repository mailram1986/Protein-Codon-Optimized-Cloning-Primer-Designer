import subprocess
import webbrowser
import time
import sys
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(base_dir, "app.py")

    # Start Streamlit WITHOUT auto browser
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            app_path,
            "--server.headless=true",
            "--browser.gatherUsageStats=false",
            "--server.port=8501"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Wait for server to initialize
    time.sleep(3)

    # Open browser ONCE
    webbrowser.open_new("http://localhost:8501")

    # Keep process alive
    process.wait()

if __name__ == "__main__":
    main()
