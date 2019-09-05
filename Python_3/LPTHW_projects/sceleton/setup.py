try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "LPTHW_Project",
    "author": "almazkun",
    "url": "https://almazkun.github.io/works/LPTHW_Project",
    "download_url": "https://almazkun.github.io/works/LPTHW_project/LPTHW_Project",
    "author_email": "almaz.kun@gmail.com",
    "version": "2019.09.0001",
    "install_requires": ["nose"],
    "packages": ["NAME"],
    "scripts": [],
    "name": "project_name",
}


setup(**config)
