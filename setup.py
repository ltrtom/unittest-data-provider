import os
from setuptools import setup, find_packages



setup(
    name='unittest-data-provider',
    version='1.0.2',
    description='PHPUnit-like @dataprovider decorator for unittest',
    author='drm from melp.nl, packaged for reuse by James Pic',
    author_email='jamespic@gmail.com',
    url='https://github.com/ltrtom/unittest-data-provider',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description='PHPUnit-like @dataprovider decorator for unittest',
    license='MIT',
    keywords='unittest dataprovider',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
