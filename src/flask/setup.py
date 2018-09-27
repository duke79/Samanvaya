from setuptools import setup, find_packages

setup(
    name='Samanvaya',
    version='0.0.1',
    # license='Creative Commons Attribution-Noncommercial-Share Alike license',
    author='Pulkit Singh',
    author_email='pulkitsingh01@gmail.com',
    description='Scraping things.',
    long_description=open('readme.md').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
)
