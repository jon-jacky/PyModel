"""
setup.py for PyModel, model-based testing in Python
see http://docs.python.org/distutils/packageindex.html

To create or update the PyModel page at PyPI: python setup.py register

To make distribution: python setup.py sdist -v -f --formats=gztar,zip

To upload distribution to PyPI: 
 python setup.py sdist -v -f --formats=gztar,zip upload --show-response

It is not necessary to install, you can just run out of the unpacked
distrbution.  It is convenient to put PyModel-0.9/pymodel on the
execution PATH.

The distribution contents are all specified in MANIFEST.in,
not in setup.py.  Therefore python setup.py install has no effect.
"""

from distutils.core import setup

setup(
    # Metadata for PyPI
    # from http://docs.python.org/distutils/setupscript.html#meta-data
    # also http://docs.python.org/distutils/apiref.html#module-distutils.core
    name = 'PyModel',
    version = '0.9',
    author = 'Jonathan Jacky',
    author_email = 'jon@u.washington.edu',
    maintainer = 'Jonathan Jacky',
    maintainer_email = 'jon@u.washington.edu',
    url = 'http://staff.washington.edu/jon/pymodel/www/',
    description = 'Model-based testing in Python',
    long_description = open('README.rst').read(),
    download_url = 'http://staff.washington.edu/jon/pymodel/www/',
    license = 'GNU General Public License (GPL)',

    keywords = 'model-based testing python model on-the-fly offline composition finite state machine harness stepper automated test run suite oracle nondeterminism synchronizing interleaving strategy coverage protocol trace scenario',

    # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ],
)
