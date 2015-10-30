from distutils.core import setup

setup(
    # Application name:
    name="exotel",

    # Version number (initial):
    version="0.1.1",

    # Application author details:
    author="sarath",
    author_email="sarath.sp06@gmail.com",

    # Packages
    packages=['exotel'],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/sarathsp06/exotel-py",
    download_url = 'https://github.com/sarathsp06/exotel-py/archive/v0.1.1.tar.gz'
    #
    license="LICENSE.txt",
    description="Python SDK for Exotel API",
    long_description=open("README.rst").read(),

    # Dependent packages (distributions)
    install_requires=[
        "requests==2.2.1",
        "requests-oauthlib==0.5.0"
    ],
)
