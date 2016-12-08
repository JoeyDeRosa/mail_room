"""Setup up for sample distrobution"""

from setuptools import setup

setup(
    name="mail_room",
    description="Automation of a donation response system",
    version=0.1,
    author="Marc Fieser and Joey DeRosa",
    author_email="midfies@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['mail_room'],
    install_requires=['ipython'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
    entry_points={},
)
