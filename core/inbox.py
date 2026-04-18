"""
Inbox read/write operations.
Thin wrapper around kb/ inbox directory.
"""

from pathlib import Path
from datetime import datetime
from .kb import INBOX


def write_inbox(content: str) -> Path:
    """Write a new inbox file with timestamp filename."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = INBOX / f"{timestamp}.md"
    filename.write_text(content)
    return filename


def list_inbox():
    """List all inbox files."""
    return sorted(INBOX.glob("*.md"), reverse=True)
