# Python-Process-Sniffer


Version 1.0.7

---

# Process Log Recorder

**Description:**  
This Python script allows you to monitor the console output of any running process on your Windows machine. It captures the console output and stores it in a log file for later analysis. The script uses the `psutil` and `subprocess` modules to interact with processes and capture their console output.

**How to Use:**

1. **Installation:**  
   - Clone or download this repository to your local machine.

2. **Setup:**  
   - Ensure you have Python installed on your system.
   - Install the required Python packages by running:
     ```
     pip install psutil
     ```

3. **Usage:**
   - Run the script `process_log_recorder.py`.
   - The script will list all running processes on your system.
   - Choose the number corresponding to the process you want to monitor.
   - The script will start monitoring the console output of the selected process.
   - The console output will be displayed in real-time in the command prompt and stored in a log file.
   - Press `Ctrl + C` to stop monitoring the process.

**Shortcut Creation:**
   
   To create a shortcut to quickly access the script:
   
   1. Right-click on your desktop and select `New` -> `Shortcut`.
   2. In the location field, type `python` followed by the full path to the `process_log_recorder.py` script.
   3. Name the shortcut as desired and click `Finish`.
   4. Now, whenever you want to start monitoring a process, simply double-click on the shortcut.

**Note:**  
   - By default, the log file is stored on the desktop (`C:/Users/<username>/Desktop`). You can modify the `log_file_path` variable in the script to change the location of the log file.

Replace `<username>` in the `log_file_path` with your actual username.
