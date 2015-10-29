from distutils.core import setup

setup(
    # Application name:
    name="exotel",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="sarath",
    author_email="sarath@exotel.in",

    # Packages
    packages=['exotel'],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/exotel_py_v010/",

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "requests==2.2.1",
        "requests-oauthlib==0.5.0"
    ],
)
