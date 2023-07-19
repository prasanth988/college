from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in college/__init__.py
from college import __version__ as version

setup(
	name="college",
	version=version,
	description="this is demo",
	author="prasanth",
	author_email="prasanth@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
