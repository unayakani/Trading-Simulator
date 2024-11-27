import webview as wb
import threading as tr
import subprocess as sb
from subprocess import check_output
import time

def start_sim():
    global stream
    stream = sb.Popen(["streamlit", "run", "main.py", "--server.headless", "True"])

def on_closing():
    stream.terminate()
    print("Closing...")
    stream.wait()

if __name__ == "__main__":
    tr.Thread(target=start_sim).start()

    time.sleep(5)
    
    window = wb.create_window("Trading Simulator", "http://localhost:8501")
    window.events.closing += on_closing
    wb.start()