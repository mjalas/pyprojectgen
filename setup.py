from setuptools import setup, find_packages
from os import path
import boot_pyproject.metadata as metadata

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = ""

try:
    from pypandoc import convert
    if path.exists(path.join(here, 'README.md')):
        long_description = convert('README.md', 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

setup(
    name=metadata.NAME,
    version=metadata.VERSION,
    description=metadata.DESCRIPTION,
    long_description=long_description,
    url=metadata.URL,
    author=metadata.AUTHOR,
    author_email=metadata.AUTHOR_EMAIL,
    license=metadata.LICENSE,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=[]),
    setup_requires=['nose>=1.0', 'coverage>=4.0.3', 'pypandoc>=1.1.3'],
    test_suite='nose.collector',
    tests_require=['nose']
)