from os import path
from .config import AutoManager
from .config import Config
from typing import Optional, List

cfg = Config()

class Template:
    extra_libs: List[str] = []
    extra_dirs: List[str] = []
    extra_files: List[str] = []
    example: bool = True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.framework_name = cls.__name__.lower().replace("manager", "")

        bases = [base for base in cls.__mro__[1:] if issubclass(base, Template)]
        
        cls.extra_libs = sum([getattr(base, "extra_libs", []) for base in reversed(bases)], []) + cls.extra_libs
        cls.extra_dirs = sum([getattr(base, "extra_dirs", []) for base in reversed(bases)], []) + cls.extra_dirs
        cls.extra_files = sum([getattr(base, "extra_files", []) for base in reversed(bases)], []) + cls.extra_files

        cls.example = getattr(cls, "example", True)

    def __init__(
        self,
        name: str,
        framework_name: Optional[str] = None,
        source_dir = cfg.source_dir,
        project_name = cfg.project_name
    ):
        self.name = name
        self.framework_name = framework_name or self.__class__.framework_name
        self.source_dir = source_dir
        self.project_name = project_name
        self.AutoManager = AutoManager()
        self.extra_libs = self.__class__.extra_libs
        self.extra_dirs = self.__class__.extra_dirs
        self.extra_files = self.__class__.extra_files
        self.example = self.__class__.example
        
    def install_framework(self, **kwargs):
        version = f"=={kwargs.get('version')}" if kwargs.get('version') else ""
        libs_to_install: list = kwargs.get("libs") or []
        #
        libs_to_install.extend([f"{self.framework_name}{version}"])
        libs_to_install.extend(self.extra_libs)
        #
        self.AutoManager.install_libs(libs_to_install)
        #
        self.setup_framework()

    def setup_framework(self, source_dir: list = None, extra_dirs: list = None, extra_files: list = None):
        source_dir = source_dir or self.source_dir
        #
        dirs = (extra_dirs or []) + self.extra_dirs
        files = (extra_files or []) + self.extra_files
        #
        if dirs:
            cfg.create_dirs(source_dir, dirs)
        if files:
            cfg.create_files(files)

    def create_example(self, example_id):
        if self.__class__.example:
            from pkgutil import get_data

            example_code = get_data(
                "rapidframework",
                f"frameworks/examples/{self.framework_name}_{example_id}.py",
            ).decode("utf-8")

            with open(
                path.join(self.source_dir, self.name + ".py"), "w", encoding="utf-8"
            ) as example_file:
                example_file.write(example_code)
        else:
            raise Exception("Example method is'n allowed for this framework !")
