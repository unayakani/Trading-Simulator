import webview as wb
import threading as tr
import subprocess as sb
import time

# Extra Dependencies include only pywebview
# Use pip install pywebview

def start_sim():
    sb.run(["streamlit", "run", "main.py", "--server.headless", "True"])

if __name__ == "__main__":
    tr.Thread(target=start_sim).start()

    time.sleep(5)
    
    wb.create_window("Trading Simulator", "http://localhost:8501")
    wb.start()