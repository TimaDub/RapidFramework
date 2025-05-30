from ..template import Template as Template
from .examples import *

import os
import importlib

def import_all_modules_from_package():
    current_dir = os.path.dirname(__file__)
    package_name = __name__

    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            importlib.import_module(f"{package_name}.{module_name}")

import_all_modules_from_package()