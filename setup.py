from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot:main",
        ],
    },
    version="0.1",
    author="Maksimelyan Tamashevich",
    author_email="mtamaashevich@gmail.com",
    description="Example of the snapshot application",
    license="MIT"
)