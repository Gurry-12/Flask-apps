from setuptools import setup, find_packages

setup(
    name="crisisconnect",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        # Add others from pyproject.toml if needed
    ],
)
