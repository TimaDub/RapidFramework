from os import path
from .config import AutoManager
from .config import Config


cfg = Config()


class Template:
    def __init__(
        self,
        framework_name: str | None = None,
        source_dir=cfg.source_dir,
        project_name=cfg.project_name,
        **kwargs
    ):
        if framework_name is None:
            self.framework_name = self.__class__.__name__.lower().replace("manager", "")
        else:
            self.framework_name = framework_name
        #
        self.source_dir = source_dir
        self.project_name = project_name
        self.name = kwargs.get("name")
        #
        self.AutoManager = AutoManager()
        #        

    def install_framework(self, **kwargs):
        version = f"=={kwargs.get('version')}" if kwargs.get('version') else ""
        libs_to_install: list = kwargs.get("libs") or []
        #
        libs_to_install.extend([f"{self.framework_name}{version}"])
        print("Getting libs")
        self.AutoManager.install_libs(libs_to_install)
        #
        self.setup_framework()

    def setup_framework(self, source_dir=cfg.source_dir, extra_dirs=[], extra_files: list=None):
        cfg.create_dirs(source_dir, extra_dirs)
        if extra_files is not None:
            cfg.create_files(extra_files)

    def create_example(self, name, example_id):
        from pkgutil import get_data

        example_code = get_data(
            "rapidframework",
            f"frameworks/examples/{self.framework_name}_{example_id}.py",
        ).decode("utf-8")

        with open(
            path.join(cfg.source_dir, name + ".py"), "w", encoding="utf-8"
        ) as example_file:
            example_file.write(example_code)
