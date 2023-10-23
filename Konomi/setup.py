from pathlib import Path
from configparser import ConfigParser
from setuptools import setup, find_packages

config = ConfigParser()
config.read('setup.cfg')

setup(
    name="Konomi",
    license="MIT",
    author="Kono",
    author_email="Fahadtalal441@gmail.com",
    description="Easily create a bot for Amino Apps using a modern easy to use synchronous library.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/Konoyoi/Konomi",
    version = config.get('metadata', 'version'),
    packages=find_packages(),
    install_requires=[
        "requests==2.31.0",
        "colorama==0.4.6",
        "websocket-client==1.6.1",
        "diskcache==5.6.1",
        "aiohttp==3.8.4"
    ],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8"
)