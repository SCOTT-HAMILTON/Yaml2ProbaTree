from setuptools import setup, find_packages

setup(
    name='Yaml2ProbaTree',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules = [ 'yaml2probatree' 'cli' ],

    install_requires=['pyyaml', 'Click'],

    entry_points='''
        [console_scripts]
        yaml2probatree=Yaml2ProbaTree.cli:cli
    ''',

    # metadata to display on PyPI
    author='Scott Hamilton',
    author_email='sgn.hamilton+python@protonmail.com',
    description='Converts a yaml structure to a LaTeX/TiKZ probability tree',
    keywords='convert translation latex tikz maths tree probability',
    url='https://github.com/SCOTT-HAMILTON/Yaml2ProbaTree',
    project_urls={
        'Source Code': 'https://github.com/SCOTT-HAMILTON/Yaml2ProbaTree',
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)
