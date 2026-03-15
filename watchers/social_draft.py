from pathlib import Path
import time

def create_social_draft(platform, post_text):
    pending = Path("Pending_Approval") / f"{platform.upper()}_{int(time.time())}.md"
    content = f"""---
type: approval_request
action: {platform}_post
content: {post_text}
---
Move to Approved to post.
"""
    pending.write_text(content)
    print(f"{platform} draft created in Pending_Approval. Waiting for approval.")

print("✅ Safe Social Draft system created for FB, IG, X - NO auto posting")
