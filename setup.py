from setuptools import setup, find_packages

setup(
    name="lognotify",
    version="0.0.1",
    author="411Gamer",
    author_email="ponrobot0@gmail.com",
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.6',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    license='GPL-3.0',
)
