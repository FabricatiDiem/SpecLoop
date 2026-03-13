from typing import List
from pydantic import BaseModel
from pathlib import Path
import re


class GlobalGoal(BaseModel):
    mission: str
    constraints: List[str]


class GoalParser:
    @staticmethod
    def parse_file(file_path: Path) -> GlobalGoal:
        if not file_path.exists():
            return GlobalGoal(mission="No mission statement provided.", constraints=[])

        with open(file_path, "r") as f:
            content = f.read()

        mission = ""
        mission_match = re.search(
            r"# Project Mission\n(.*?)(?=\n#|\Z)", content, re.DOTALL
        )
        if mission_match:
            mission = mission_match.group(1).strip()

        constraints = []
        constraints_match = re.search(
            r"# Constraints\n(.*?)(?=\n#|\Z)", content, re.DOTALL
        )
        if constraints_match:
            lines = constraints_match.group(1).strip().split("\n")
            constraints = [line.strip("- ").strip() for line in lines if line.strip()]

        return GlobalGoal(mission=mission, constraints=constraints)
