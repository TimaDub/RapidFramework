from os import getcwd, listdir, path, makedirs
from typing import Self, Dict
import pkgutil
from msgspec import json, Struct, field, DecodeError
from subprocess import run
from importlib.metadata import distribution
from re import sub


class Config:
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.source_dir = getcwd()
            self.project_name = path.basename(self.source_dir)
            self.source_files = listdir()
            self.dirs_to_create = [
                "tests",
                "templates",
                "static",
                "static/css",
                "static/js",
                "static/images",
            ]
            self.install = AutoManager().get_config_managers()
            self.pkg_manager = AutoManager().get_pkg_manager()
            self._initialized = True


    def create_dirs(self, app_path, extra_dirs=[]) -> None:
        dirs_to_create: list = self.dirs_to_create.copy()
        dirs_to_create.extend(extra_dirs)
        #
        for _dir in dirs_to_create:
            makedirs(path.join(app_path, _dir), exist_ok=True)
    
    def create_files(self, file_paths) -> None:
        for file_path in file_paths:
            with open(path.join(self.source_dir, file_path), "w"): ...

    
class _ConfigCommands(Struct):
    install: str
    uninstall: str
    list_: str = field(name="list")

class _ConfigFormat(Struct):
    managers: Dict[str, _ConfigCommands]

class AutoManager:
    _instance = None    
    _decoder = json.Decoder(type=_ConfigFormat, strict=True)
    
    def __new__(cls, config_name: str = "managers.json") -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config_name: str = "managers.json"):
        if not hasattr(self, "_initialized"):
            self.config_name = config_name
            self._ConfigFormat = _ConfigFormat
            self._initialized = True
            
    def get_config_managers(self) -> _ConfigFormat:
        config = pkgutil.get_data("rapidframework", f"configs/{self.config_name}")
        #
        if config is None:
            raise FileNotFoundError(f"Configuration file '{self.config_name}' not found.")
        #
        return self._decoder.decode(config.decode("utf-8"))
    
    def get_pkg_manager(self) -> str:
        try:
            return sub(r'\s+', '', distribution("rapidframework-lib").read_text("INSTALLER")) # type: ignore
        except (DecodeError, FileNotFoundError, ValueError):
            return "pip"
    
    def install_libs(self, libs: list) -> None:
        managers = self.get_config_managers().managers
        pkg = self.get_pkg_manager()
        if pkg not in managers:
            raise ValueError(f"Package manager '{pkg}' not found in configuration.")
        run([pkg, managers[pkg].install] + libs)
                
if __name__ == "__main__":
    # Example usage of AutoManager singleton
    a = AutoManager()
    b = AutoManager()
    print(f"{a is b=}")  # Should print True, confirming singleton behavior
    assert a is b
    # # Example usage of Config singleton
    c = Config()
    d = Config()
    print(f"{c is d=}")  # Should print True, confirming singleton behavior
    assert c is d