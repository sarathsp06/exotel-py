from setuptools import setup, find_packages

setup(
    # Application name:
    name="exotel",

    # Version number (initial):
    version="0.1.5",

    # Application author details:
    author="sarath",
    author_email="sarath.sp06@gmail.com",

    # Packages
    packages=find_packages(),

    # Details
    url="https://github.com/sarathsp06/exotel-py",
    download_url = 'https://github.com/sarathsp06/exotel-py/archive/v0.1.5.tar.gz',
    license="LICENSE.txt",
    description="Python SDK for Exotel API[Unofficial]",
    long_description="""
exotel-py
---------

Python module for exotels call and sms api's

installation
~~~~~~~~~~~~

``pip install exotel``

Usage
-----

-  Initialize

    ``from exotel import Exotel``

    ``client = Exotel(sid,token)``

- make call to connect a number to another

    ``client.call_number('from_number','exophone','to_number')``

-  make call to connect a number to a flow

    ``client.call_flow('from_number','exophone','flow_id')``

-  send an sms

    ``client.sms('from_number',to_number',"sms_body")``

- get details of an sms

    ``client.sms_details('sms_sid')``

- get details of a call

    ``client.call_details('call_sid')``

"""
)
