from setuptools import setup, find_packages
from shhcloud import __version__


def readme():
    try:
        with open('README.md') as readme:
            return readme.read()
    except:
        pass


setup(
    name='shhcloud',
    version='.'.join(str(i) for i in __version__),
    description='create wordclouds based on shell history',
    author="Adithya Nair",
    author_email='adtya.nair@gmail.com',
    long_description=readme(),
    long_description_type='text/markdown',
    url="https://gitlab.com/adtya/shhcloud",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['wordcloud==1.5.0'],

    entry_points={'console_scripts': ['shhcloud=shhcloud.main:main']},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",

    ]
)
