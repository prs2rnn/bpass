from os import path

from setuptools import find_packages, setup
from bpass import VERSION

# read the contents of README, esspecially all that stuff for PYPI
current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # Mandatory arg, unic
    name="bpass",

    # Mandatory arg, PEP 440 compliance
    version=VERSION,

    # Mandatory arg, used in PyPi, but not a long_description
    description="simple cli password-generator",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Optional args
    author="luculliano",
    author_email="vederecento@gmail.com",

    # Optional args
    license="MIT",
    # url="https://github.com/lotblack/...",

    # Mandatory arg, full list of installed packages - nested packages not
    # included automatically
    # You can just specify the packages here if the project is simple
    # or you can use find_packages()
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=['my_module'],

    # Optional arg, allows versioning pyclip==0.7.0
    install_requires=["pyclip"],

    # Optional arg, to add pics, templates, CSS to package, not support
    # recursion, add manually
    # package_data= {
    #     '': ['views/*.tpl',
    #         'static/css/*'],
    #     }

    # Optional arg, lets creates script that call specified funcs of module
    # Scripts create in $HOME/.local/bin or /usr/local/bin
    # i.e. name of utility = package_name.module_with_main_logic
    entry_points={
        "console_scripts": ["bpass = bpass.pwd:main"],
    },

    # Optional arg
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
