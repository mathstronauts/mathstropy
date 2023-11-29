from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mathstropy", # Replace with your own username
    version="3.0.0",
    author="Richard Hamilton",
    author_email="richard.ha@mathstronauts.ca",
    description="Python library with functions to make learning more efficient",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathstronauts/mathstropy",
    packages=find_packages(),
    install_requires=[
        "pygame"
    ],
    extras_require={
        "dev": [
            "build",
            "twine",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
