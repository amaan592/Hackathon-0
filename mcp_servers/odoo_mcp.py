from pathlib import Path
import time

def create_odoo_draft(action_type, data):
    pending = Path("Pending_Approval") / f"ODOO_{action_type}_{int(time.time())}.md"
    content = f"""---
type: approval_request
action: odoo_{action_type}
data: {data}
---
Move this file to Approved folder to actually send to Odoo.
"""
    pending.write_text(content)
    print("Odoo draft created in Pending_Approval. Waiting for human.")

print("✅ Safe Odoo MCP created - NO direct changes ever.")
