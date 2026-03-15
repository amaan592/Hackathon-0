from pathlib import Path
from datetime import datetime

def generate_ceo_briefing():
    briefing_path = Path("Briefings") / f"{datetime.now().strftime('%Y-%m-%d')}_CEO_Briefing.md"
    content = """# Monday Morning CEO Briefing

## Revenue
- This week: 

## Bottlenecks
- 

## Proactive Suggestions
- 

Move any approval files to Approved if needed.
"""
    briefing_path.write_text(content)
    print("CEO Briefing draft created in Briefings folder (safe mode).")

print("✅ CEO Briefing generator ready - runs safely")
