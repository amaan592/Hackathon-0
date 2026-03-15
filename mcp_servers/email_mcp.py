from pathlib import Path
import time

def send_email_approval(to, subject, body):
    pending = Path("Pending_Approval") / f"EMAIL_{to}_{int(time.time())}.md"
    content = f"""---
type: approval_request
action: send_email
to: {to}
subject: {subject}
---
Body: {body}

Move this file to Approved folder to actually send.
"""
    pending.write_text(content)
    print("Approval file created in Pending_Approval. Waiting for human.")

print("✅ Safe Email MCP created - NO direct sending ever.")
