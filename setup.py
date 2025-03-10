import os
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        os.system('python -m unidic download')


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        os.system('python -m unidic download')


with open('requirements.txt') as f:
    required = f.read().splitlines()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="melotts-wrapper",
    version="0.1.0",
    author="ThuGie",
    author_email="thughack@hotmail.com",
    description="User-friendly wrapper for MeloTTS multi-lingual text-to-speech library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThuGie/MeloTTS-Wrapper",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    entry_points={
        "console_scripts": [
            "melotts-wrapper=melotts_wrapper.cli:main",
            "melotts-web=melotts_wrapper.web:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    keywords="tts, text-to-speech, speech synthesis, melotts, multilingual",
)
