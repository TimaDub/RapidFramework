from ..template import Template
import os
import pathlib
from subprocess import run


class DjangoManager(Template):
    extra_libs = ["Pillow", "djangorestframework", "django-cors-headers", \
        "celery", "django-redis", "redis", "django-allauth", "django-crispy-forms", "django-environ", \
        "django-extensions", "gunicorn", "whitenoise", "django-configurations", "django-debug-toolbar"]
    example = True
    
    def create_example(self, example_id) -> None: 
        package_dir = pathlib.Path(__file__).resolve().parent
        example_folder_path = package_dir / "examples" / f"{self.framework_name}_{example_id}"     
        
        if os.path.isdir(example_folder_path):
            run(["django-admin", "startproject", f"--template={example_folder_path}", self.name])
