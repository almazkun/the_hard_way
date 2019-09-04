try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "ex42",
    "author": "almazkun",
    "url": "https://almazkun.github.io/works/ex42",
    "download_url": "https://almazkun.github.io/works/LPTHW_project/ex42",
    "author_email": "almaz.kun@gmail.com",
    "version": "2019.09.0001",
    "install_requires": ["nose"],
    "packages": ["ex42"],
    "scripts": [],
    "name": "ex42"
}


setup(**config)
