from setuptools import setup

import pyminifier

setup(
    name="pyminifier3",
    version=pyminifier.__version__,
    description="Python code minifier, obfuscator, and compressor",
    author=pyminifier.__author__,
    author_email="daniel.mcdougall@liftoffsoftware.com, dzhuang.scut@gmail.com",
    url="https://github.com/dzhuang/pyminifier3",
    license="Proprietary",
    packages=["pyminifier"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    provides=["pyminifier"],
    entry_points={
        "console_scripts": [
            "pyminifier = pyminifier.__main__:main"
        ],
    },
    test_suite="tests",
)
