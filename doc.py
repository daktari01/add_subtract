try:
    from setuptools import setup
except:
    from distutils.core import setup


dependencies = ['docopt', 'termcolor']


setup(
    name = 'add_subtract', #name of application
    version = '0.0.1', #app version
    description = 'Add or subtract integers', #small inline description
    url = 'https://github.com/daktari01/add_subtract', #where it can be found
    author = 'daktari01',
    author_email = 'dindijjames@gmail.com',
    install_requires = dependencies, #specify which apps your app depends on
    packages = ['add_subtract'], #how many packages the app contains
    entry_point = {    #specific to command line applications. what get called when the app runs from the commandline
        'console_script': [
            'add_subtract = add_subtract.main:start'
        ],
    },
    classifiers = (
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
)



