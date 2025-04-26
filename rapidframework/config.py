from os import getcwd, listdir, path, makedirs
from typing import Self
from msgspec import toml
import re


class Config:
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.source_dir = getcwd()
            cls._instance.source_files = listdir()
            cls._instance.pyproject_file = "pyproject.toml"
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

        return cls._instance

    def create_dirs(cls, app_path, extra_dirs=[]) -> None:
        dirs_to_create: list = cls._instance.dirs_to_create.copy()
        dirs_to_create.extend(extra_dirs)
        #
        for _dir in dirs_to_create:
            makedirs(path.join(app_path, _dir), exist_ok=True)
            
    def create_files(cls, file_paths):
        for file_path in file_paths:
            with open(path.join(cls._instance.source_dir, file_path), "w"): ...

    def check_lib(cls, lib_name) -> bool:
        return lib_name in [
            re.match(r"^[a-zA-Z0-9-_]+", dep).group(0)
            for dep in cls._instance.pyproject_deps
        ]

    def get_dependencies(cls) -> list:
        with open(
            path.join(cls._instance.source_dir, cls._instance.pyproject_file)
        ) as pyproject_deps:
            cls._instance.pyproject_deps = toml.decode(pyproject_deps.read()).get("project").get("dependencies")
            return cls._instance.pyproject_deps
