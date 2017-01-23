from setuptools import setup, find_packages
import os

def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'alternativefacts/version.py')) as f:
        variables = {}
        exec(f.read(), variables)
        return variables.get('VERSION')
    raise RuntimeError('No version info found.')

setup(
    name='alternativefacts',
    version=get_version(),
    author='Dennis Burke',
    author_email='ikirudennis@gmail.com',
    description='An alternativefacts package for python',
    url='http://github.com/ikirudennis/alternativefacts',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='alternative facts',
    include_package_data=True,
    zip_safe=False,
)

