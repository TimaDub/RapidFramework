# from ..template import Template
# from subprocess import run
# from os import chdir


# class DjangoManager(Template):
#     extra_libs = ["Pillow"]
#     example = False

#     def run_manage(self, commands: list):
#         manage_py = f"{self.source_dir}/{self.project_name}/manage.py"
#         for command in commands:
#             full_command = ["python", manage_py] + command.strip().split(" ")
#             run(full_command, check=True)

#     def setup_framework(self):
#         run([
#             "python", "-m", "django", "startproject",
#             self.project_name, self.source_dir
#         ], check=True)

#         chdir(f"{self.source_dir}/{self.project_name}")
#         self.run_manage([f"startapp {self.name}", "makemigrations", "migrate"])

#         self.extra_files.append(f"{self.project_name}/{self.name}/urls.py")

#         return super().setup_framework(
#             source_dir=f"{self.source_dir}/{self.project_name}/{self.name}",
#             extra_files=self.extra_files
#         ) 
"""
The class is being redeveloped for better performance and capabilities
    """