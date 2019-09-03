try:
    from setuptools import setup

except ImportError:
        from distutils.core import setup

config = {
    "description": "LPTHW_Project",
    "author": "almazkun",
    "url": "https://almazkun.github.io/works/LPTHW_project",
    "download_url": "https://almazkun.github.io/works/LPTHW_project/LPTHW_project.zip",
    "author_email": "almaz.kun@gmail.com",
    "version": "2019.09.0001",
    "install_requires": "nose",
    "packages": ["NAME"],
    "scripts": [],
    "name": "LPTHW_project"
}


setup(**config)
