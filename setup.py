"""
setup.py for PyModel, model-based testing in Python
see http://docs.python.org/distutils/packageindex.html

To create or update the PyModel page at PyPI: python setup.py register

To make distribution: python setup.py sdist -v -f --formats=gztar,zip

To upload distribution to PyPI: 
 python setup.py sdist -v -f --formats=gztar,zip upload --show-response

It is not necessary to install, you can just run out of the unpacked
distribution. In that case, it is convenient to run
PyModel/bin/pymodel_paths to set up your PATH and PYTHONPATH (run
pymodel_paths.bat on Windows).  That script assumes the distribution
directory is in your HOME directory and is named PyModel (not
PyModel-1.0, so you many need to rename it).

To optionally install the PyModel python modules and commands in
system directories (for example in /Library/Python/2.7/site-packages
and /usr/local/bin, respectively):

 sudo python setup.py install.

The distribution contents are all specified in MANIFEST.in, not in
setup.py.  Most of the distribution is in the examples under
PyModel/samples, and in the documentation under PyModel/notes, www,
and talks, and in the README files in most directories.  Installation
does not install these into any system directories
"""

from distutils.core import setup
from distutils import sysconfig

site_packages_path = sysconfig.get_python_lib()

setup(
    # Metadata for PyPI
    # from http://docs.python.org/distutils/setupscript.html#meta-data
    # also http://docs.python.org/distutils/apiref.html#module-distutils.core
    name = 'PyModel',
    version = '1.0',
    author = 'Jonathan Jacky',
    author_email = 'jon.p.jacky@gmail.com',
    maintainer = 'Jonathan Jacky',
    maintainer_email = 'jon.p.jacky@gmail.com',
    url = 'https://github.com/jon-jacky/PyModel',
    description = 'Model-based testing in Python',
    long_description = open('README.md').read(),
    download_url = 'https://pypi.python.org/pypi/PyModel',
    license = 'BSD License',

    packages = ['pymodel'],

    data_files = [(site_packages_path, ['pymodel.pth'])],

    scripts = [ 'bin/clogdiff', 
                'bin/clogdiff.bat', 
                'bin/dotpdf', 
                'bin/dotpdf.bat', 
                'bin/dotps', 
                'bin/dotps.bat', 
                'bin/dotsvg', 
                'bin/dotsvg.bat', 
                'bin/pma', 
                'bin/pmg', 
                'bin/pmt', 
                'bin/pmv', 
                'bin/pymodel_paths', 
                'bin/pymodel_paths.bat', 
                'bin/tclean', 
                'bin/tclean.bat', 
                'bin/tdiff', 
                'bin/tdiff.bat', 
                'bin/tpath', 
                'bin/tpath.bat', 
                'bin/trun', 
                'bin/wsgirunner', ],

    keywords = 'model-based testing python model on-the-fly offline composition finite state machine harness stepper automated test run suite oracle nondeterminism synchronizing interleaving strategy coverage protocol trace scenario',

    # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
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
