from abc import ABC, abstractmethod
from pathlib import Path
from agent_agnostic.models.manifest import Manifest

class BaseDeployment(ABC):
    def __init__(self, manifest: Manifest, root_dir: Path):
        self.manifest = manifest
        self.root_dir = root_dir

    @abstractmethod
    def deploy(self) -> bool:
        """Perform deployment sync."""
        pass

    def log(self, message: str):
        print(f"[{self.__class__.__name__}] {message}")
