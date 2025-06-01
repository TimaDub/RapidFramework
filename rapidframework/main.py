import argparse
from pathlib import Path
from . import Template
# 
import gc

def all_subclasses(cls):
    subclasses = cls.__subclasses__()
    for subclass in subclasses:
        subclasses += all_subclasses(subclass)
    return subclasses

def find_manager_class(base_name: str):
    base_name_lower = base_name.lower()
    target_suffix = "manager"

    for obj in gc.get_objects():
        if isinstance(obj, type):
            cls_name = obj.__name__
            if cls_name.lower() == base_name_lower + target_suffix:
                return obj
    raise Exception(f"Manager class for '{base_name}' not found. Ensure it is defined and imported correctly.")

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
        self.framework_manager: type = find_manager_class(self.args.framework)

    def _discover_frameworks(self):
        return sorted(set([cls.__name__.removesuffix("Manager").lower() for cls in all_subclasses(Template)]))

    def run(self):
        framework = self.framework_manager(self.args.name)
        #
        if hasattr(self.framework_manager, "install_framework"):
            framework.install_framework(version=self.args.version)
        if hasattr(self.framework_manager, "create_example"):
            framework.create_example(1 if self.args.example is None else self.args.example)

def main_entry_point():
    Main().run()


if __name__ == "__main__":
    main_entry_point()
