import setuptools
from pathlib import Path

SRC_ROOT = Path(__file__).parent

with open(SRC_ROOT / "README.md", "r") as f:
    long_description = f.read()

with open(SRC_ROOT / "__init__.py", "r") as f:
    version_line = next(filter(lambda l: 'version' in l, f.readlines()))
    version = version_line.split('=')[-1].strip(" \"'\n")

setuptools.setup(
    name="my-sorting-algo",
    version=version,
    author="Olle Lindgren",
    author_email="lindgrenolle@live.se",
    description="A package for sorting files quickly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OlleLindgren/my-sorting-algo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
