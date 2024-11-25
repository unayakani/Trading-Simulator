import webview as wb
import threading as tr
import subprocess as sb
import time
import os
import signal

def start_sim():
    sb.run(["streamlit", "run", "main.py", "--server.headless", "True"])

def on_closing():
    os.kill(os.getpid(), signal.SIGINT)

if __name__ == "__main__":
    tr.Thread(target=start_sim).start()

    time.sleep(5)
    
    window = wb.create_window("Trading Simulator", "http://localhost:8501")
    window.events.closing += on_closing
    wb.start()