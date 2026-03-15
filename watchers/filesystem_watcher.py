from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil
import time

# Get the absolute path to the project root (parent of watchers folder)
BASE_DIR = Path(__file__).resolve().parent.parent
NEEDS_ACTION_DIR = BASE_DIR / 'Needs_Action'

class DropFolderHandler(FileSystemEventHandler):
    def __init__(self):
        # Ensure Needs_Action directory exists
        NEEDS_ACTION_DIR.mkdir(exist_ok=True)
        
    def on_created(self, event):
        if event.is_directory:
            return
        source = Path(event.src_path)
        # Skip files already in Needs_Action or Done folders
        if 'Needs_Action' in str(source) or 'Done' in str(source):
            return
        dest = NEEDS_ACTION_DIR / f'FILE_{source.name}'
        try:
            shutil.copy2(source, dest)
            print(f"✅ New file detected: {source.name}")
        except Exception as e:
            print(f"⚠️ Error copying {source.name}: {e}")

observer = Observer()
observer.schedule(DropFolderHandler(), str(BASE_DIR), recursive=True)
observer.start()

print("🚀 File Watcher started... (Ctrl+C se stop)")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
