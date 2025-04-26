from os import path
from ..uv import UvManager
from ..config import Config


cfg = Config()


class Template:
    def __init__(
        self,
        framework_name: str,
        source_dir=cfg.source_dir,
        project_name=cfg.project_name,
        **kwargs
    ):

        self.source_dir = source_dir
        self.project_name = project_name
        self.framework_name = framework_name
        self.name = kwargs.get("name")
        #
        self.UvManager = UvManager()
        self.UvManager.check_for_venv()
        #        

    def check(self, **kwargs) -> None:
        if not cfg.check_lib(self.framework_name):
            self.install_framework(**kwargs)
        else:
            self.setup_framework()

    def install_framework(self, **kwargs):
        version = f"=={kwargs.get('version')}" if kwargs.get('version') else ""
        libs_to_install: list = kwargs.get("libs") or []
        #
        libs_to_install.extend([f"{self.framework_name}{version}"])
        self.UvManager.install_libs(libs_to_install)
        #
        self.setup_framework()

    def setup_framework(self, source_dir=cfg.source_dir, extra_dirs=[], extra_files: list=None):
        cfg.create_dirs(source_dir, extra_dirs)
        if extra_files is not None:
            cfg.create_files(extra_files)

    def create_example(self, name, example_id):
        print(self.framework_name)
        from pkgutil import get_data

        example_code = get_data(
            "rapidframework",
            f"frameworks/examples/{self.framework_name}_example_{example_id}.py",
        ).decode("utf-8")

        with open(
            path.join(cfg.source_dir, name + ".py"), "w", encoding="utf-8"
        ) as example_file:
            example_file.write(example_code)
