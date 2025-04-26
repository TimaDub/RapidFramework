from subprocess import run
from .config import Config

cfg = Config()


class UvManager:
    def __init__(self):
        self.source_dir = cfg.source_dir
        self.source_files = cfg.source_files

    def check_for_venv(self):
        if cfg.pyproject_file not in self.source_files:
            self.init_uv()
        else:
            self.sync_uv()
            
        cfg.get_dependencies()

    def install_uv(self):
        try:
            run(["pip", "install", "uv"])
            run(["uv", "init"])
        except Exception as error:
            raise Exception(f"Unexpected Error during installing uv: {error}")

    def sync_uv(self):
        try:
            run(["uv", "sync"])
        except ModuleNotFoundError:
            self.install_uv()

    def init_uv(self):
        try:
            run(["uv", "init"])
        except ModuleNotFoundError:
            self.install_uv()
    
    def install_libs(self, libs: list):
        for lib in libs:
            run(["uv", "add", lib])
