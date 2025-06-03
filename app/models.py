from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    site: str
    subject: str
    body: str
    assigned_to: str | None = None


db: List[Task] = []
