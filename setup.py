from setuptools import setup, find_packages

setup (
    name='github-activity',
    version='0.1.0',
    description='Github UserActivity CLI',
    url='https://github.com/KoushikReddy3103/GitHub-UserActivity/tree/main',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'argparse',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'github-activity=Github_cli.cli:cli'
        ]
    }
)