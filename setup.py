from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in weberp/__init__.py
from weberp import __version__ as version

setup(
	name="weberp",
	version=version,
	description="Website ERP",
	author="Sourabh",
	author_email="sourabh@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
