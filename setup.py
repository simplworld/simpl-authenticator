import os
from setuptools import setup, find_packages

VERSION = '0.0.2'

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='simpl-authenticator',
    version=VERSION,
    description='',
    long_description=readme,
    author='',
    author_email='',
    url='',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        "autobahn==17.5.1",
    ],
    tests_require=[
    ]
)
