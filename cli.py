import argparse
import os
import shutil
import time

import sys
import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class RestartOnChange(FileSystemEventHandler):
    def __init__(self, file):
        self.file = str(Path(file).resolve())
        self.process = None
        self.run_file()

    def run_file(self):
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
        print(f"▶️ Running {self.file}...")
        # Run safely with subprocess
        self.process = subprocess.Popen([sys.executable, self.file])

    def on_modified(self, event):
        if str(Path(event.src_path).resolve()) == self.file:
            print(f"⚡ Change detected in {self.file}, restarting...")
            self.run_file()

class Open:
    def __init__(self, path: str):
        self.path = open(path, "+a", encoding="utf-8")

    def edit(self, text: str):
        pass


def watcher(file: str):
    file_path = Path(file).resolve()
    event_handler = RestartOnChange(file_path)

    observer = Observer()
    observer.schedule(event_handler, str(file_path.parent), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process and event_handler.process.poll() is None:
            event_handler.process.terminate()
    observer.join()


def init(args):
    repo = "https://github.com/sinofarmonov323/aiogram-bot-template.git"
    project_name = repo.replace("https://github.com/", "").replace(".git", "").split("/")[1]
    
    os.system(f"git clone {repo}")
    
    os.makedirs(args.path, exist_ok=True)
    source_dir = project_name
    dest_dir = args.path

    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(dest_dir, item)
        shutil.move(src_path, dst_path)
    time.sleep(0.5)
    shutil.rmtree(source_dir)
    with open(f".project", "w", encoding="utf-8") as file:
        file.write(f"{args.path}")
    print(".project file is created. Please do not delete or move it to another place")

def helpp(args):
    print("""USAGE:
aiogram:
    init [project-name] - initialize the project
    help - get help
    run [filename] - runs the file with auto reload
""")

def run(args):
    watcher(args.path)

def handler_func(args):
    print("not ready yet. Will be ready soon ;)")


def main():
    parser = argparse.ArgumentParser(prog="aiogram")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize project with template")
    init_parser.add_argument("path", nargs="?", default=".", help="Path to initialize")
    init_parser.set_defaults(func=init)

    help_parser = subparsers.add_parser("help", help="get help")
    help_parser.set_defaults(func=helpp)

    watcher = subparsers.add_parser("run", help="runs the file with auto reload")
    watcher.add_argument("path", nargs="?", help="enter path to file name to run")
    watcher.set_defaults(func=run)

    handler = subparsers.add_parser("handler", help="adds new handler to your code")
    handler.add_argument("handler", nargs="?", help="enter the name of the handler")
    handler.set_defaults(func=handler_func)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
