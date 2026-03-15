import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from pathlib import Path
import time

# NOTE: User will add credentials later in .env

class GmailWatcher:
    def __init__(self, vault_path):
        self.needs_action = Path(vault_path) / 'Needs_Action'
        
    def check_and_create_action(self):
        # Placeholder - real setup later
        print("Gmail watcher running (safe mode - only detects)")
        # In real, it will create .md file in Needs_Action for new emails

print("Gmail watcher created (read-only). No sending possible.")
