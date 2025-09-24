from setuptools import setup, find_packages

setup(
    name="ACIT_GAME_Module",
    version="0.2",
    packages=find_packages(),  # Includes the 'games' package
    py_modules=['main'],       # Includes main.py as a top-level module
    include_package_data=True,
    description="A fun game module as a part of ACIT4420 the lecture series. Basically from Lecture 5, 6, and 7.",
    author="Shailendra Bhandari",
    author_email="shailendra.bhandari@oslomet.no",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'games=main:main',  # Points to main() in main.py (root directory)
        ],
    },
)