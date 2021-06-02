from setuptools import setup, find_packages

def read_reqs():
    with open('reqs.txt') as req:
        content = req.read()
        reqs = content.split('\n')

    return reqs

setup(
    name='Nekopy',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_reqs(),
    entry_points='''
        [console_scripts]
        Nekopy=Nekopy.cli:cli
    '''
)