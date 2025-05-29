from os import getcwd, listdir, path, makedirs
from typing import Self, Dict
import pkgutil
from msgspec import json, Struct, field
from subprocess import run
from importlib.metadata import distribution
from re import sub


class Config:
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.source_dir = getcwd()
            cls._instance.source_files = listdir()
            cls._instance.dirs_to_create = [
                "tests",
                "templates",
                "static",
                "static/css",
                "static/js",
                "static/images",
            ]

            # cls._instance.pyproject_deps: list
            cls._instance.project_name = path.basename(cls._instance.source_dir)
            cls.install = AutoManager().get_config_managers()
            cls.pkg_manager = AutoManager().get_pkg_manager()

        return cls._instance

    def create_dirs(cls, app_path, extra_dirs=[]) -> None:
        dirs_to_create: list = cls._instance.dirs_to_create.copy()
        dirs_to_create.extend(extra_dirs)
        #
        for _dir in dirs_to_create:
            makedirs(path.join(app_path, _dir), exist_ok=True)
            
    def create_files(cls, file_paths) -> None:
        for file_path in file_paths:
            with open(path.join(cls._instance.source_dir, file_path), "w"): ...


class AutoManager:
    _instance = None

        
    def __new__(cls, config_name: str = "managers.json") -> Self:
        if cls._instance is None:
            cls._instance = super(AutoManager, cls).__new__(cls)
            
            class _ConfigCommands(Struct):
                install: str
                uninstall: str
                list_: str = field(name="list")

            class _ConfigFormat(Struct):
                managers: Dict[str, _ConfigCommands]
            
            cls._instance.config_name = config_name
            cls._instance._ConfigFormat = _ConfigFormat
            cls._instance.decoder = json.Decoder()
            
        return cls._instance
            
    
    def get_config_managers(cls) -> dict:
        config = pkgutil.get_data("rapidframework", f"configs/{cls._instance.config_name}")
        return json.decode(config.decode("utf-8"), type=cls._instance._ConfigFormat)
    
    
    def get_pkg_manager(cls) -> str:
        try:
            return sub(r'\s+', '', distribution("rapidframework-lib").read_text("INSTALLER"))
        except:
            return "pip"
    
    
    def install_libs(cls, libs: list) -> None:
        print(libs)
        run([cls.get_pkg_manager(), cls.get_config_managers().managers.get(cls.get_pkg_manager()).install] + libs)