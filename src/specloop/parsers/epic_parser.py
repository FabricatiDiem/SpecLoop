from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
import re
from pathlib import Path


class EpicStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Epic(BaseModel):
    id: str
    title: str
    description: str
    priority: int
    status: EpicStatus
    branch: Optional[str] = None


class EpicParser:
    @staticmethod
    def parse_file(file_path: Path) -> List[Epic]:
        if not file_path.exists():
            return []

        with open(file_path, "r") as f:
            content = f.read()

        epics = []
        # Regex to find H2 headers like ## [Title]
        # And following fields Description, Priority, Status
        pattern = r"## \[(.*?)\]\nDescription: (.*?)\nPriority: (\d+)\n- \[(.*?)\] Status: (.*?)(?=\n##|\Z)"
        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            title = match.group(1)
            description = match.group(2).strip()
            priority = int(match.group(3))
            checkbox = match.group(4)
            status_text = match.group(5).strip()

            # Map checkbox/text to EpicStatus
            status = EpicStatus.PENDING
            if checkbox == "x":
                status = EpicStatus.COMPLETED
            elif checkbox == "~":
                status = EpicStatus.IN_PROGRESS
            elif checkbox == "!":
                status = EpicStatus.FAILED

            epic_id = title.lower().replace(" ", "-").replace("[", "").replace("]", "")

            epics.append(
                Epic(
                    id=epic_id,
                    title=title,
                    description=description,
                    priority=priority,
                    status=status,
                )
            )

        return sorted(epics, key=lambda x: x.priority)

    @staticmethod
    def update_status(file_path: Path, title: str, new_status: EpicStatus):
        if not file_path.exists():
            return

        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        in_target_epic = False

        checkbox_map = {
            EpicStatus.PENDING: " ",
            EpicStatus.IN_PROGRESS: "~",
            EpicStatus.COMPLETED: "x",
            EpicStatus.FAILED: "!",
        }

        for line in lines:
            if line.startswith(f"## [{title}]"):
                in_target_epic = True
            elif in_target_epic and line.startswith("- ["):
                char = checkbox_map[new_status]
                line = f"- [{char}] Status: {new_status.value}\n"
                in_target_epic = False
            new_lines.append(line)

        with open(file_path, "w") as f:
            f.writelines(new_lines)
