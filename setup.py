from setuptools import find_packages, setup


setup(
    name="aiken_eng",
    version="0.0.1",
    description="Tools for use at Aiken Engineering Company",
    package_dir={"": "aiken_eng"},
    packages=find_packages("aiken_eng"),
    url="https://github.com/eric-rudolph/aiken_eng.git",
    author="eric-rudolph",
    author_email="",
    license="MIT",
    classifiers=[],
    install_requires=[],
    python_requires=">=3.6",
)