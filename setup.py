from setuptools import setup

setup(
    name='WFH',
    version='1.0.0',
    packages=['wfh'],
    url='https://github.com/tejksat/docker-compose_console_scripts',
    author='Alexander K',
    description='Sample Docker Compose project with console_scripts in setup.py',
    entry_points={
        'console_scripts': ['wfh=wfh.command_line:main']
    }
)
