from setuptools import setup, find_packages

setup(
    name='ci-cd-demo-basics',        # your project/repo name
    version='0.1',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        # list dependencies here if you want
    ],
)
