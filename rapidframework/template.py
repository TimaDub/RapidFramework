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
        
        seen = set()
        for attr in ["extra_libs", "extra_dirs", "extra_files"]:
            values = []
            for base in reversed(bases):
                if base not in seen:
                    seen.add(base)
                    values += getattr(base, attr, [])
            values += getattr(cls, attr, [])
            setattr(cls, attr, values)

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

    def setup_framework(self, _source_dir: Optional[str] = None, extra_dirs: Optional[list] = None, extra_files: Optional[list] = None):
        source_dir: str = _source_dir or self.source_dir
        #
        dirs = (extra_dirs or []) + self.extra_dirs
        files = (extra_files or []) + self.extra_files
        #
        if dirs:
            cfg.create_dirs(source_dir, dirs)
        if files:
            cfg.create_files(files)

    def create_example(self, example_id) -> None:
        if self.example:
            from pkgutil import get_data
            
            example_code = get_data(
                "rapidframework",
                f"frameworks/examples/{self.framework_name}_{example_id}.py",
            )
            if not example_code:
                raise Exception(f"Example {example_id} not found for {self.framework_name} framework.")
            
            with open(
                path.join(self.source_dir, self.name + ".py"), "w", encoding="utf-8"
            ) as example_file:
                example_file.write(example_code.decode("utf-8"))
        else:
            raise Exception("Example method is'n allowed for this framework !")
