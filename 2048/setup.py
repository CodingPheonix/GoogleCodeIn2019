import os
from setuptools import setup

setup(
    name = "2048",
    version = "1.0",
    author = "Aditya Agrawal",
    author_email = "agraw17107@gapps.uwcsea.edy.sg",
    description = "2048 game recreation in tkinter",
    license = "MIT",
    url = "https://github.com/CodingPheonix/GoogleCodeIn2019/",
    packages=['2048'],
    entry_points = {
        'gui_scripts' : ['2048 = 2048.2048:main']
    },
    data_files = [
        ('share/applications/', ['GCI-2048.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)
