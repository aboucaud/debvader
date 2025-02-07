from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "tensorflow==2.1.0",
    "tensorflow-probability==0.9.0",
    "matplotlib",
    "jupyter",
    "scikit-image>=0.17.2"
    # ,"numpy>=1.17.4", scipy
]

setup(
    name="debvader",
    version="0.0.100104",
    author="Bastien Arcelin, Cyrille Doux, Thomas Sainrat, Biswajit Biswas, Alexandre Boucaud",
    author_email="arcelin@apc.in2p3.fr",
    description="Galaxy deblender from variational autoencoders",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/BastienArcelin/debvader",
    include_package_data=True,
    packages=['data','debvader'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
)
