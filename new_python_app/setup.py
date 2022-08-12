from importlib.metadata import entry_points
import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="timtest",
    version="0.0.1",
    author="Tim",
    author_email="nope@nope.com",
    description="Package to test hello world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'timTest = test:timTest',
        ],
    },
    python_requires='>=3.7',
)