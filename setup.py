from setuptools import setup, find_packages

setup(
    name="aiogram_cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "watchdog"
    ],
    url="https://github.com/sinofarmonov323/aiogram-cli",
    author="https://t.me/jackson_rodger",
    description="bu aiogram kutubxonasi uchun aiogram cli (command line tool)",
    entry_points={
        'console_scripts': [
            'aiogram = aiogram_cli.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
