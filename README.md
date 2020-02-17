# python Packaging
this repository is based on packaging in python 

# what is packaging
A python package is a directory of python modules(files are also modules) with a file named __init__.py

### example of package structure:

   ![example1](https://www.python-course.eu/images/packages.png)
 

### for example consider a project of creating a game:
 
   ![example of package](https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg)
- an alternate for packaging, you should [freeze your application](https://docs.python-guide.org/shipping/freezing/#freezing-your-code-ref)

# how to create a basic package:
[example_of a_sample_package](https://github.com/SurajKande/python_packaging/tree/master/package_example)

   ### steps to create a basic package with some Python modules and submodules:
      step1: create a dictionary, The name of this directory will be the name of the package, which we want to create 

      step2: This directory needs to contain a file with the name "__init__.py". This file can be empty, or it can contain valid Python code. This code will be executed when a package will be imported, so it can be used to initialize a package,

      step3: Now we can add the Python files and modules into this package 

   the package is created which we can use locally by
   - placing the package in the same root directory of the main code
   - (or) place this package in the lib folder of the main python folder


> note: we need to add few more files to make it into a distributed package 

# types of packaging for distribution:
  
   Because packages consist of multiple files, they are harder to distribute. Most protocols support transferring only one file at a time (when was the last time you clicked a link and it downloaded multiple files?). It’s easier to get incomplete transfers, and harder to guarantee code integrity at the destination.

   1. ### ***source distribution (sdist):***
      If code contains nothing but pure Python code, and you know your deployment environment supports your version of Python, then you can use Python’s native packaging tools to create a source distribution package, or sdist for short.

   Python’s sdists are compressed archives (.tar.gz files) containing one or more packages or modules. If your code is pure-Python, and you only depend on other Python packages

   It contains setup.py (which contains information about module/metadata), the source files of module/script (.py files or .c/.cpp for binary modules), data files, etc. 

   2. ### ***build distribution (bdist):***
      The result is an archive that is specific to a platform (for example linux-x86_64) and to a version of Python. That can be installed and then used directly by extracting it into the root of your filesystem 

   So much of Python’s practical power comes from its ability to integrate with the software ecosystem, in particular libraries written in C, C++, Fortran, Rust, and other languages.

   Not all developers have the right tools or experiences to build these components written in these compiled languages, so Python created the wheel, a package format designed to ship libraries with compiled artifacts. In fact, Python’s package installer, pip, always prefers wheels because installation is always faster, so even pure-Python packages work better with wheels.

[source](https://packaging.python.org/overview/)

# create a distribution package:

   ### steps to create a basic package with some Python modules and submodules:
      step1: create a dictionary, The name of this directory will be the name of the package, which we want to create 

      step2: This directory needs to contain a file with the name "__init__.py". This file can be empty, or it can contain valid Python              code. This code will be executed when a package will be imported, so it can be used to initialize a package,

      step3: Now we can add the Python files and modules into this package 
      
      step4: create a setup.py file, it contains the actual instructions used when building and distributing the package.
      
      step5: Python packages are built into build distribution files, which are then uploaded to a server — usually the global PyPI server — from which they can be downloaded by everybody.
      
      step6: Now, to build the distribution files simply run the following command in the root folder where your setup.py is located:
              ``` python setup.py sdist bdist_wheel ```
             The two files we’re going to upload are located in the dist folder


# publish the package in opensource
If you’re writing an open source Python module and upload its package, **PyPI** (python packaging index) , more properly known as The ***Cheeseshop***, is the place to host it.
to publish create a distributed package and follow the steps below
 
 step1: create a districution package (as mentioned above )
 
 step2: to upload you packages to the global PyPI server you’ll have to register to the PyPI website to authenticate with the PyPI
 server — in a text file named .pypirc, commonly placed in your home folder. Create it, and populate it as demonstrated below:
                ```  [distutils]
                  index-servers =
                    pypi
                    testpypi
                  [pypi]
                  username: teapot48
                  password: myPYPIpassword ```
 step3: use twine, a utility for uploading Python packages. Simply run: twine upload dist/* 
      
 >note: you should see one progress bar as your .whl file is uploaded, and a second when the .tar.gz archive is uploaded, after which the upload will be complete.

# create a private repo for internal or personal use 

   ## 1. Personal pypi:
   If you want to install packages from a source other than PyPI (say, if your packages are proprietary), you can do it by hosting a        simple HTTP server, running from the directory which holds those packages which need to be installed.
   
   For example, if you want to install a package called MyPackage.tar.gz, and assuming this is your directory structure:

   archive
   MyPackage
   MyPackage.tar.gz
   Go to your command prompt and type:
   ```
   $ cd archive
   $ python -m http.server 9000
   ```
   This runs a simple HTTP server running on port 9000 and will list all packages (like MyPackage). Now you can install MyPackage using    any Python package installer. Using pip, you would do it like:
   ```
   $ pip install --extra-index-url=http://127.0.0.1:9000/ MyPackage
   ```
    But if you feel that creating a folder called MyPackage and keeping MyPackage.tar.gz inside that is redundant, you can still install MyPackage using:
   ```
   $ pip install  http://127.0.0.1:9000/MyPackage.tar.gz
   ```

   ## 2. pypi server:
   [pypiserver](https://pypi.org/project/pypiserver/) is a minimal PyPI compatible server. It can be used to serve a set of packages to    easy_install or pip. It includes helpful features like an administrative command (-U) which will update all its packages to their        latest versions found on PyPI.
   pypiserver > 1.2.x works with Python 2.7 and 3.4+
   
      step1: Install pypiserver with this command:
   
             pip install pypiserver
             mkdir ~/packages        # Copy packages into this directory.
      step2: Copy some packages into your ~/packages folder and then get your pypiserver up and running:
   
             pypi-server -p 8080 ~/packages &   
   
      step3: To download the packages from another system
   
             # Download and install hosted packages.
               pip install --extra-index-url http://localhost:8080 ... 
   
             # Search hosted packages.
               pip search --index http://localhost:8080 ... 
   
      >***NOTE***:  pypiserver redirects pip/easy_install to the pypi.org index if it doesn’t have a requested package
   
      step4: to make the pipy server search for the packages in hosted server by adding the following lines
   
              ~/.pip/pip.conf:
   
              [global]
               extra-index-url = http://localhost:8080/simple/
   
      step5: to upload the pacakges
   
            1. upload using setuptools:
                     create a  ~/.pypirc file
   
                        [distutils]
                        index-servers =
                          pypi
                          local
   
                        [pypi]
                        username:<your_pypi_username>
                        password:<your_pypi_passwd>
   
                        [local]
                        repository: http://localhost:8080
                        username: <some_username>
                        password: <some_passwd>
   
      
   ## 3. pypi server using docker:
   To run the most recent release of pypiserver with Docker, simply:
   
          docker run pypiserver/pypiserver:latest 
          
   > This starts pypiserver serving packages from the /data/packages directory inside the container, listening on the container port 8080.

  The container takes all the same arguments as the normal pypi-server executable, with the exception of the internal container  port (-p), which will always be 8080.

  To map port 80 on the host to port 8080 on the container:

         docker run -p 80:8080 pypiserver/pypiserver:latest
         You can now access your pypiserver at localhost:80 in a web browser.
  
  ## 4. [pypi server on AmazonS3](https://www.novemberfive.co/blog/opensource-pypi-package-repository-tutorial):
   
