from ..template import Template
from subprocess import run
from os import chdir


class DjangoManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run_manage(self, commands: list):
        chdir(f"{self.source_dir}/{self.project_name}")
        for command in commands:
            run(("uv run manage.py " + command.strip()).split(" "))

    def setup_framework(self):
        run(["uvx", "--from", "django", "django-admin", "startproject", self.project_name])
        self.run_manage([f"startapp {self.name}", "makemigrations", "migrate"])
        return super().setup_framework(f"{self.source_dir}/{self.project_name}/{self.name}", \
            extra_files=[f"{self.project_name}/{self.name}/urls.py"])
        
    def install_framework(self, **kwargs):
        return super().install_framework(libs=["Pillow"], **kwargs)
        
    def create_example(self, name, example_id) -> None:
        return None
