import setuptools
import aiogram_oop_framework

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiogram_oop_framework",
    version=aiogram_oop_framework.__version__,
    author="drforse",
    author_email="george.lifeslice@gmail.com",
    description="An extender for aiogram to make it more OOP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drforse/aiogram_oop_framework",
    packages=setuptools.find_packages(exclude=('tests', 'tests*')),
    include_package_data=True,
    install_requires=['aiogram>=2.8', 'click==7.1.2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)