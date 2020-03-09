##########################################################################
## Imports
#########################################################################
from setuptools import setup
from setuptools import find_packages

##########################################################################
## Package Information
##########################################################################

## Basic information
NAME         = "ML_models"
DESCRIPTION  = "creating a package of ML classification model, will printout accuracy"
VERSION      = "0.0.1"
AUTHOR       = "abcd"
EMAIL        = "abcd@abcd.com"
PACKAGE      = "classification"
URL          = "https://github.com/SurajKande/python_packaging/tree/master/sample_ML_classification_package"
KEYWORDS     = (
    'ML', 
    'python', 
    'Automate',
    'classification',
)

## Important Paths
#REQUIRE_PATH = "requirements.txt"

## Directories to ignore in find_packages
EXCLUDES     = (
    "tests", "resources", "notebooks",
)

##########################################################################
## Helper Functions
##########################################################################


##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "description": DESCRIPTION,
    "version":VERSION
    "author": AUTHOR,
    "author_email": EMAIL,
    "url": URL,
    "maintainer": AUTHOR,
    "maintainer_email": EMAIL,
    "packages": find_packages(exclude=EXCLUDES),
    "install_requires": ['pandas', 'numpy', 'matplotlib', 'seaborn', 'scipy','sklearn'],
    "keywords": KEYWORDS,
    "zip_safe": False,
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
