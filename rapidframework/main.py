import argparse
import importlib
import os
from pathlib import Path

#
from .uv import UvManager

# 

FRAMEWORKS_PATH = Path(__file__).parent / "frameworks"


class Main:
    def __init__(self):
        #
        self.available_frameworks = self._discover_frameworks()
        #
        self.parser = argparse.ArgumentParser(description="Framework project creator")
        self.parser.add_argument(
            "framework",
            help="Choose the framework",
            choices=self.available_frameworks,
        )
        self.parser.add_argument(
            "--name", type=str, help="Name for framework app", required=True
        )
        self.parser.add_argument("--version", type=str, help="Version for framework")
        self.parser.add_argument("--example", type=int, help="Example id")
        #
        self.args = self.parser.parse_args()
        #
        self.UvManager = UvManager()
        self.framework_manager = self._load_framework_manager()

    def _discover_frameworks(self):
        frameworks = []
        for file in os.listdir(FRAMEWORKS_PATH):
            if file.endswith(".py") and file != "__init__.py":
                framework_name = file.removesuffix('.py').lower()
                frameworks.append(framework_name)
        return frameworks

    def _load_framework_manager(self):
        module_name = f"rapidframework.frameworks.{self.args.framework}"
        class_name = f"{self.args.framework.capitalize()}Manager"
        
        module = importlib.import_module(module_name)
        manager_class = getattr(module, class_name)
        
        return manager_class(name=self.args.name)

    def run(self):      
        self.UvManager.check_for_venv()
        #
        example_id = 1 if self.args.example is None else self.args.example
        #
        if hasattr(self.framework_manager, "check"):
            self.framework_manager.check(version=self.args.version)
        
        if hasattr(self.framework_manager, "create_example"):
            self.framework_manager.create_example(self.args.name, example_id)


def main_entry_point():
    Main().run()


if __name__ == "__main__":
    main_entry_point()
