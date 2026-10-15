from skbuild import setup
from setuptools import find_packages


setup(
    name='loopfit',
    description='Superconducting resonator IQ loop fitting optimized for '
                'speed',
    version='0.0.7',
    author='Nicholas Zobrist',
    license='GPLv3',
    url='https://github.com/zobristnicholas/loopfit',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['numpy', 'scipy']
)
