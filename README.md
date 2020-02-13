# python Packaging
this repository is based on packaging in python 

# what is packaging
A python package is a directory of python modules(files are also modules) with a file named __init__.py

### example of package structure:

   ![example1](https://www.python-course.eu/images/packages.png)
 

### for example consider a project of creating a game:
 
   ![example of package](https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg)
- an alternate for packaging, you should [freeze your application](https://docs.python-guide.org/shipping/freezing/#freezing-your-code-ref)

# how to create a package:
[example_of a_sample_package](https://github.com/SurajKande/python_packaging/tree/master/package_example)

### steps to create a package with some Python modules and submodules:

   step1: create a dictionary, The name of this directory will be the name of the package, which we want to create 
   
   step2: This directory needs to contain a file with the name "__init__.py". This file can be empty, or it can contain valid Python code.          This code will be executed when a package will be imported, so it can be used to initialize a package,
   
   step3: Now we can add the Python files and modules into this package 

# types of packaging for distribution:
  
   Because packages consist of multiple files, they are harder to distribute. Most protocols support transferring only one file at a time (when was the last time you clicked a link and it downloaded multiple files?). It’s easier to get incomplete transfers, and harder to guarantee code integrity at the destination.

1. ### ***source distribution:***
   If code contains nothing but pure Python code, and you know your deployment environment supports your version of Python, then you can use Python’s native packaging tools to create a source distribution package, or sdist for short.

Python’s sdists are compressed archives (.tar.gz files) containing one or more packages or modules. If your code is pure-Python, and you only depend on other Python packages

It contains setup.py (which contains information about module/metadata), the source files of module/script (.py files or .c/.cpp for binary modules), data files, etc. 

2. ### ***build distribution:***
   The result is an archive that is specific to a platform (for example linux-x86_64) and to a version of Python. That can be installed and then used directly by extracting it into the root of your filesystem 

So much of Python’s practical power comes from its ability to integrate with the software ecosystem, in particular libraries written in C, C++, Fortran, Rust, and other languages.

Not all developers have the right tools or experiences to build these components written in these compiled languages, so Python created the wheel, a package format designed to ship libraries with compiled artifacts. In fact, Python’s package installer, pip, always prefers wheels because installation is always faster, so even pure-Python packages work better with wheels.

[source](https://packaging.python.org/overview/)
# publish the package in opensource


# create a private repo for internal use 

#
