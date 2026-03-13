from enum import Enum
from pathlib import Path
from typing import List, Dict
from speckit_loop.engine.orchestrator import Orchestrator
from speckit_loop.git.wrapper import GitWrapper


class WorkflowPhase(Enum):
    SPECIFY = "specify"
    PLAN = "plan"
    TASKS = "tasks"
    ANALYZE = "analyze"
    IMPLEMENT = "implement"
    VERIFY = "verify"
    COMMIT = "commit"
    UPDATE = "update"


class WorkflowEngine:
    def __init__(self, root_dir: Path):
        self.orchestrator = Orchestrator(root_dir)
        self.git = GitWrapper()

    def execute_epic(self, epic_title: str, description: str, global_context: str):
        branch_name = f"auto-{epic_title.lower().replace(' ', '-')}"
        print(f"Starting workflow for Epic: {epic_title} on branch {branch_name}")

        # 1. Branch
        self.git.create_branch(branch_name)

        # 2. Specify
        self.orchestrator.run_command(
            "speckit.specify",
            args=f'"{description}"',
            pre_prompt=f"Global Mission: {global_context}",
        )
        self.git.commit_changes(f"docs: specify {epic_title}")

        # 3. Plan
        self.orchestrator.run_command("speckit.plan")
        self.git.commit_changes(f"docs: plan {epic_title}")

        # 4. Tasks
        self.orchestrator.run_command("speckit.tasks")
        self.git.commit_changes(f"docs: generate tasks for {epic_title}")

        # 5. Analyze (with auto-remedy)
        self.orchestrator.run_command(
            "speckit.analyze",
            pre_prompt="You are running in an autonomous loop. For any ambiguities or decision points, proceed with the 'Recommended' action immediately without requesting user input.",
        )

        # 6. Implement
        self.orchestrator.run_command("speckit.implement")
        self.git.commit_changes(f"feat: implement {epic_title}")

        # 7. Verify (Placeholder for now)
        print("Verifying implementation...")

        return True
