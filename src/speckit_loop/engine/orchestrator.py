import subprocess
import os
from pathlib import Path
from typing import Optional, Dict
import datetime


class Orchestrator:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir

    def run_command(
        self, cmd: str, args: str = "", pre_prompt: Optional[str] = None
    ) -> bool:
        """
        Executes a SpecKit command. If running within an agent harness,
        emits a recognizable instruction. Also handles basic file bootstrapping.
        """
        print(f"\n[Orchestrator] Executing SpecKit Skill: {cmd}")
        if pre_prompt:
            print(f"[Orchestrator] Context: {pre_prompt}")

        # Emit for the agent to catch
        print(f"AGENT_INSTRUCTION: /{cmd} {args}")

        # Basic bootstrapping for Specify and Plan to make it "feel" real
        # even if the agent hasn't intercepted the instruction yet.
        if cmd == "speckit.specify":
            self._bootstrap_spec(args, pre_prompt)
        elif cmd == "speckit.plan":
            self._bootstrap_plan()
        elif cmd == "speckit.tasks":
            self._bootstrap_tasks()

        return True

    def _bootstrap_spec(self, description: str, context: Optional[str]):
        # Find feature dir from git branch or guess
        branch = self._get_current_branch()
        spec_path = self.root_dir / "specs" / branch / "spec.md"
        spec_path.parent.mkdir(parents=True, exist_ok=True)

        if not spec_path.exists():
            template_path = (
                self.root_dir / ".specify" / "templates" / "spec-template.md"
            )
            if template_path.exists():
                with open(template_path, "r") as f:
                    content = f.read()

                content = content.replace(
                    "[FEATURE NAME]",
                    branch.replace("auto-", "").replace("-", " ").title(),
                )
                content = content.replace("[###-feature-name]", branch)
                content = content.replace("[DATE]", datetime.date.today().isoformat())
                content = content.replace("$ARGUMENTS", description)

                with open(spec_path, "w") as f:
                    f.write(content)
                print(f"[Orchestrator] Bootstrapped specification: {spec_path}")

    def _bootstrap_plan(self):
        branch = self._get_current_branch()
        plan_path = self.root_dir / "specs" / branch / "plan.md"
        if not plan_path.exists():
            template_path = (
                self.root_dir / ".specify" / "templates" / "plan-template.md"
            )
            if template_path.exists():
                with open(template_path, "r") as f:
                    content = f.read()

                content = content.replace(
                    "[FEATURE]", branch.replace("auto-", "").replace("-", " ").title()
                )
                content = content.replace("[###-feature-name]", branch)
                content = content.replace("[DATE]", datetime.date.today().isoformat())

                with open(plan_path, "w") as f:
                    f.write(content)
                print(f"[Orchestrator] Bootstrapped plan: {plan_path}")

    def _bootstrap_tasks(self):
        branch = self._get_current_branch()
        tasks_path = self.root_dir / "specs" / branch / "tasks.md"
        if not tasks_path.exists():
            template_path = (
                self.root_dir / ".specify" / "templates" / "tasks-template.md"
            )
            if template_path.exists():
                with open(template_path, "r") as f:
                    content = f.read()

                content = content.replace(
                    "[FEATURE NAME]",
                    branch.replace("auto-", "").replace("-", " ").title(),
                )
                content = content.replace("[###-feature-name]", branch)

                with open(tasks_path, "w") as f:
                    f.write(content)
                print(f"[Orchestrator] Bootstrapped tasks: {tasks_path}")

    def _get_current_branch(self) -> str:
        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except:
            return "unknown-feature"
