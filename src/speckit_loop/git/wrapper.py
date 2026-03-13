import subprocess
from pathlib import Path
from typing import List, Optional


class GitWrapper:
    @staticmethod
    def create_branch(branch_name: str):
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)

    @staticmethod
    def commit_changes(message: str, paths: Optional[List[str]] = None):
        if paths:
            for path in paths:
                subprocess.run(["git", "add", path], check=True)
        else:
            subprocess.run(["git", "add", "."], check=True)

        # Check if there are changes to commit
        status = subprocess.run(
            ["git", "status", "--porcelain"], capture_output=True, text=True, check=True
        )
        if status.stdout.strip():
            subprocess.run(["git", "commit", "-m", message], check=True)
        else:
            print("No changes to commit.")

    @staticmethod
    def get_current_branch() -> str:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()

    @staticmethod
    def checkout(branch_name: str):
        subprocess.run(["git", "checkout", branch_name], check=True)
