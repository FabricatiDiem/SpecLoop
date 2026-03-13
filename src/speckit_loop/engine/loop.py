from pathlib import Path
from speckit_loop.parsers.epic_parser import EpicParser, EpicStatus
from speckit_loop.parsers.goal_parser import GoalParser
from speckit_loop.engine.workflow import WorkflowEngine
from speckit_loop.engine.verifier import Verifier
from speckit_loop.git.wrapper import GitWrapper


class LoopRunner:
    def __init__(self, root_dir: Path, epics_path: Path, goals_path: Path):
        self.root_dir = root_dir
        self.epics_path = epics_path
        self.goals_path = goals_path
        self.workflow = WorkflowEngine(root_dir)
        self.verifier = Verifier(root_dir)
        self.git = GitWrapper()

    def run(self):
        # 1. Parse goals
        goal = GoalParser.parse_file(self.goals_path)
        global_context = (
            f"Mission: {goal.mission}. Constraints: {', '.join(goal.constraints)}"
        )

        # 2. Main loop
        while True:
            epics = EpicParser.parse_file(self.epics_path)
            unfinished = [
                e
                for s in [EpicStatus.PENDING, EpicStatus.IN_PROGRESS]
                for e in epics
                if e.status == s
            ]

            if not unfinished:
                print("No unfinished epics found. Work complete!")
                break

            current_epic = unfinished[0]
            print(f"Processing Epic: {current_epic.title}")

            # Update status to In Progress
            EpicParser.update_status(
                self.epics_path, current_epic.title, EpicStatus.IN_PROGRESS
            )

            try:
                # 3. Execute SpecKit lifecycle
                success = self.workflow.execute_epic(
                    current_epic.title, current_epic.description, global_context
                )

                if success:
                    # 4. Final verification
                    if self.verifier.run_verification():
                        print(
                            f"Epic {current_epic.title} successfully implemented and verified."
                        )
                        EpicParser.update_status(
                            self.epics_path, current_epic.title, EpicStatus.COMPLETED
                        )
                    else:
                        print(f"Verification failed for {current_epic.title}.")
                        EpicParser.update_status(
                            self.epics_path, current_epic.title, EpicStatus.FAILED
                        )
                else:
                    EpicParser.update_status(
                        self.epics_path, current_epic.title, EpicStatus.FAILED
                    )

            except Exception as e:
                print(f"Error processing epic {current_epic.title}: {e}")
                EpicParser.update_status(
                    self.epics_path, current_epic.title, EpicStatus.FAILED
                )
                break  # Stop the loop on unexpected errors

            # Reset to main branch for next epic (or keep on auto branch?)
            # Assuming we return to a baseline for the next epic
            # self.git.checkout("main")
