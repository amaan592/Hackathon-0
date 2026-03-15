from pathlib import Path
import time

def create_linkedin_draft(post_text):
    pending = Path("Pending_Approval") / f"LINKEDIN_{int(time.time())}.md"
    content = f"""---
type: approval_request
action: linkedin_post
content: {post_text}
---
Move to Approved to post on LinkedIn.
"""
    pending.write_text(content)
    print("LinkedIn draft created in Pending_Approval. Waiting for human approval.")

print("✅ LinkedIn Draft system created - NO auto posting")
