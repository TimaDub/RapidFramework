from pathlib import Path
from .config import AutoManager
from .config import Config
from typing import Optional, List
from copy import deepcopy


cfg = Config()

class Template:
    extra_libs: List[str]
    extra_dirs: List[str]
    extra_files: List[str]
    example: bool = True

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.framework_name = cls.__name__.lower().removesuffix("manager")

        bases = [base for base in cls.__mro__[1:] if issubclass(base, Template)]
        
        fields = ["extra_libs", "extra_dirs", "extra_files"]
        
        seen = set()
        for attr in fields:
            values = [
                item
                for base in reversed(bases)
                if base not in seen and not seen.add(base)
                for item in getattr(base, attr, [])
            ]
            values += getattr(cls, attr, [])
            setattr(cls, attr, values)

        cls.example = getattr(cls, "example", True)
        

    def __init__(
        self,
        name: str,
        framework_name: Optional[str] = None,
        source_dir: Optional[str] = None,
        project_name: Optional[str] = None
    ):
        self.name = name
        self.source_dir = source_dir or cfg.source_dir
        self.project_name = project_name or cfg.project_name
        self.framework_name = framework_name or self.__class__.framework_name
        self.AutoManager = AutoManager()
        #
        self.extra_libs = deepcopy(self.__class__.extra_libs)
        self.extra_dirs = deepcopy(self.__class__.extra_dirs)
        self.extra_files = deepcopy(self.__class__.extra_files)
        self.example = self.__class__.example
        
    def install_framework(self, _version: Optional[str] = None) -> None:
        self.AutoManager.install_libs(
            [f"{self.framework_name}=={_version}"] if _version else [self.framework_name]
            + self.extra_libs)
        self._setup_framework()

    def _setup_framework(self) -> None:
        if self.extra_dirs:
            cfg.create_dirs(self.extra_dirs)
        if self.extra_files:
            cfg.create_files(self.extra_files)

    def create_example(self, example_id) -> None:
        if self.example:
            from pkgutil import get_data
            
            example_code = get_data("rapidframework", f"frameworks/examples/{self.framework_name}_{example_id}.py")
            
            if example_code is None:
                raise FileNotFoundError(f"Example {example_id} not found for {self.framework_name} framework.")

            with open(Path(self.source_dir) / f"{self.name}.py", "w", encoding="utf-8") as f:
                f.write(example_code.decode("utf-8"))
        else:
            raise NotImplementedError(f"Example creation is not implemented for {self.framework_name} framework.")
