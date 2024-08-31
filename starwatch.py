



import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_positions, max_filename_length):
        super().__init__()
        self.file_positions = file_positions
        self.max_filename_length = max_filename_length
        self.colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]
        self.color_index = 0
        self.last_file = None  # Track the last file that was updated

    def on_modified(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        file_name = os.path.basename(file_path)  # Extract the file name from the path

        if file_path in self.file_positions:
            with open(file_path, 'r') as file:
                file.seek(self.file_positions[file_path])
                changes = file.read()
                if changes:
                    if self.last_file != file_path:  # Change color only if the file is different
                        self.color_index = (self.color_index + 1) % len(self.colors)
                    self.last_file = file_path
                    color = self.colors[self.color_index]
                    padded_file_name = file_name.ljust(self.max_filename_length)
                    # Print with alignment: file name followed by the log content
                    for line in changes.splitlines():
                        print(f"{color}{padded_file_name}: {line}")
                self.file_positions[file_path] = file.tell()

def monitor_logs(directory):
    file_positions = {}

    # Find the max length of file names
    max_filename_length = max(len(filename) for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename)))

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_positions[filepath] = os.path.getsize(filepath)

    event_handler = LogFileHandler(file_positions, max_filename_length)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    log_directory = "/var/log/pi-star"  # Replace with your log folder path

    print("")
    print(" ____  _              __        __    _       _")
    print("/ ___|| |_ __ _ _ __  \\ \\      / /_ _| |_ ___| |__")
    print("\\___ \\| __/ _` | '__|  \\ \\ /\\ / / _` | __/ __| '_ \\")
    print(" ___) | || (_| | |      \\ V  V / (_| | || (__| | | |")
    print("|____/ \\__\\__,_|_|       \\_/\\_/ \\__,_|\\__\\___|_| |_|")
    print("")
    print("An AI generated tool to watch your pi-star log directory")
    print("")



    monitor_logs(log_directory)

