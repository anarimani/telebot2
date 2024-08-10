from setuptools import setup, find_packages

setup(
    name='telebot2',
    version='1.0.0',
    description='A custom telebot package for Bale messenger API integration',
    author='Armin Narimani',
    author_email='a.narimani1998@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',  # or any other dependencies your package has
    ],
)
