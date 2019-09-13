import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
	name="py7z",
	version="0.0.2",
	description="Use 7zip Commands In Python With Expanded Functionality",
	long_description=README,
	url="https://github.com/thicklord/py7z",
	# author="Chris Sanchez",
	author="Thick Lord",
	author_email="7hickl0rd@gmail.com",
	license="GNU",
	classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
	# packages=["py7z"],
	# packages=find_packages(exclude=["help-messages", "tests", "*.tests", "*.tests.*", "tests.*",]),
	include_package_data=True,
	install_requires=["p7zip"],
	entry_points={
		"console_scripts": [
			"py7z=py7z.__main__:main"
		]
	
	},
	
	
	
)

