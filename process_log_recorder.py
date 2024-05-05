# make sure you change log_file_path to your directory
import time
import psutil
import logging
import os
import subprocess

# Specify the full path for the log file
log_file_path = "C:/Users/<username>/Desktop/process_console_logs.txt"

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file_path,
                    filemode='a')

# Function to monitor console output of a specific process
def monitor_console(process_name):
    try:
        # Find the process by name
        process = [p for p in psutil.process_iter(['name']) if p.info['name'] == process_name][0]

        # Get the process's PID (Process ID)
        pid = process.pid

        # Open a pipe to capture the process's stdout and stderr
        process = subprocess.Popen(["powershell", "-Command", f"Get-Process -Id {pid} | Select-Object -ExpandProperty Id"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE,
                                    universal_newlines=True)

        # Read the process's console output line by line
        while True:
            console_input = process.stdout.readline().strip()
            error_input = process.stderr.readline().strip()

            # Log the console input
            if console_input:
                logging.info(console_input)
                print(console_input)  # Print to the console
            if error_input:
                logging.error(error_input)
                print(error_input)  # Print to the console

            # Add a small delay to reduce output frequency
            time.sleep(0.1)

    except (IndexError, psutil.NoSuchProcess):
        logging.error(f"No process with the name '{process_name}' found.")
        return

if __name__ == "__main__":
    last_process_list = []  

    while True:
        current_process_list = [proc.info['name'] for proc in psutil.process_iter(['name'])]

        if current_process_list != last_process_list:
            last_process_list = current_process_list.copy()

            # Print the list of running processes
            print("List of running processes:")
            for idx, proc_name in enumerate(current_process_list):
                print(f"{idx + 1}. {proc_name}")

            # Prompt to choose a process
            while True:
                try:
                    choice = int(input("Enter the number of the process you want to monitor (0 to exit): "))
                    if choice == 0:
                        exit()
                    elif 1 <= choice <= len(current_process_list):
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and", len(current_process_list))
                except ValueError:
                    print("Invalid input. Please enter a number.")

            process_name = current_process_list[choice - 1]
            print(f"Selected process: {process_name}")

            # Start monitoring the chosen process
            print(f"Starting monitoring of process '{process_name}'...")
            print("Press Ctrl + C to stop monitoring.")
            try:
                monitor_console(process_name)
            except KeyboardInterrupt:
                print("\nMonitoring stopped.")
