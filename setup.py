from setuptools import setup, find_packages


setup(
    name="rapidframework-lib",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "msgspec",
        "uv"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'rapidframework=rapidframework.main:main_entry_point',
        ],
    },
)
