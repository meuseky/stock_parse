import pkg_resources
from setuptools import setup, find_packages


def read_deps(requirements_file="requirements.txt"):
    def clean_line(line):
        return line.split("#")[0].strip()

    requirements_file = pkg_resources.resource_filename(
        "src", "../" + requirements_file)

    with open(requirements_file) as fh:
        return [clean_line(line) for line in fh if clean_line(line)]

setup(
    name="stock_parse",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "stock_parse = src.stock_parse:main"
        ]
    },
    install_requires=read_deps(),
    author="Kyle Meuse",
    author_email="meuseky@users.noreply.github.com",
    description="A simple stock assessent app."
)
