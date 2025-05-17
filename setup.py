from setuptools import setup, find_packages

setup(
    name='topotrace',
    version='0.1',
    description='Topology-Aware Behavior Fingerprinting Toolkit',
    author='Anormalm',
    author_email='lifan.hnus@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-learn',
        'ripser',
        'persim',
        'gudhi',
        'streamlit',
        'torch',
        'torch-geometric',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
)