# Python Packaging

this repository is based on how to create packages and distribute the pacakges.

### Contents of repository:

1. [how_to_create_a_package](https://github.com/SurajKande/python_packaging/tree/master/how_to_create_a_package): shows the simple package structure   
    * **main.py**           : main code is here
    * **sample_package_1**  : coontains the code/function which can be imported into main.py
      - \_\_init__.py   : initilization file of the package
      - file1.py        : its a pytohn module, contains the code 
      - file2.py        : its a python module, contains the code
    
     
2. [creating_distribution_of_a_package](https://github.com/SurajKande/python_packaging/tree/master/creating_distribution_of_a_package): it contains a basic example of how to create a basic source distribution (sdist) and build distribution (bdist_wheel) of the package 
    - **setup.py**         :  it contains the information about the package 
    - **readme.md**        :  it contains the details of the folder
    - **src**              :  it is the package to be distributed     
      * \_\_init__.py    : initialization file of the package 
      * addition.py      : it the module to be distributed by creating a package of it

3. [example_ML_classifiaction_models_package](https://github.com/SurajKande/python_packaging/tree/master/sample_ML_classification_package):it contains a basic example of ML classification which i tried to package 
     * **setup.py**   :  it contains the information about the package
     * **classification** :  it is the package to be distributed 
       - \_\_init__.py : initialization file of the package 
       -  decision_tree_classifier.py
       -  knn_classifier.py    
       -  logistic_regression.py
       -  svm_classifier.py
     * [readme.md](https://github.com/SurajKande/python_packaging/blob/master/sample_ML_classification_package/readme.md)      
     
5. README.md: file contains the details on packaging.     

# What is package?

A package is a collection of Python modules. Packages are a way of structuring both, modules as well as multiple packages which eventually leads to a well-organized hierarchy of data set, making the directories and modules easy to access.

- has a file named \_\_init__.py
   
# Python modules

A Python file, provided it only relies on the standard library, can be redistributed and reused. You will also need to ensure it’s written for the right version of Python, and only relies on the standard library.

This is great for sharing simple scripts and snippets between people who both have compatible Python versions. There are even some entire Python libraries that offer this as an option, such as [bottle.py](https://bottlepy.org/docs/dev/) and [boltons](https://boltons.readthedocs.io/en/latest/architecture.html#architecture)

# Why packaging ?
   
The easiest way to organize the code of big applications is to split them into several packages. This makes the code simpler, easier to understand, maintain, and change. It also maximizes the reusability of your code. Separate packages act as components that can be used in various programs.
   How to share these modules between people, it becomes harder to share every single file seperately, it’s usually organized into a directory structure. if your code consists of multiple Python files Any directory containing Python files can comprise an package.
   
### example of package structure:
   ![example1](https://www.python-course.eu/images/packages.png)
 
### real time example of a project package of creating a game:
   ![example of package](https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg)


- An alternate for packaging, you should [freeze your application](https://docs.python-guide.org/shipping/freezing/#freezing-your-code-ref)

___

## creating a basic package:
[example_of a_sample_package](https://github.com/SurajKande/python_packaging/tree/master/package_example)

    step1: create a dictionary, The name of this directory will be the name of the package, which we want to create 

    step2: This directory needs to contain a file with the name "__init__.py". 
    	   - This file can be empty, or it can contain valid Python code. 
	   - This code will be executed when a package will be imported, so it can be used to initialize a package,

    step3: Now, we can add the Python files and modules into this package 

* the package has been created, to import the package, we can:
  - place the package in the same root directory of the main code
  - (or) place this package in the lib folder of the main python folder

-------------

For working with distributed packages, we need few Tools which are divided into the following two groups:
	- Tools for installing packages
	- Tools for package creation and distribution.

Utilities recommended by PyPA( Python Packaging authority ):
     -Use pip for installing packages from PyPI.
     -Use virtualenv or venv for application-level isolation of the Python runtime environment.

The Python Packaging User Guide recommends few tools for package creation and distribution:
     -Use setuptools to define projects and create source distributions.
     -Use wheels instead of eggs to create built distributions.
     -Use twine to upload package distributions to PyPI.

## creating package for distribution:

1.***source distribution (sdist):***

Python’s sdists are compressed archives (.tar.gz files) containing one or more packages or modules. If your code is pure-Python, and you only depend on other Python packages

It contains setup.py (which contains information about module/metadata), the source files of module/script (.py files or .c/.cpp for binary modules), data files, etc. 
   
* use the sdist command to create a source distribution of the package: `python setup.py sdist`
	
(assuming you haven’t specified any sdist options in the setup script or config file), sdist creates the archive of the default format for the current platform. The default format is a gzip’ed tar file (.tar.gz) on Unix, and ZIP file on Windows.

* You can specify as many formats as you like using the --formats option, for example:

   `python setup.py sdist --formats=gztar,zip`
   
2.***build distribution (bdist):***

The result is an archive that is specific to a platform (for example linux-x86_64) and to a version of Python. That can be installed and then used directly by extracting it into the root of your filesystem 

So much of Python’s practical power comes from its ability to integrate with the software ecosystem, in particular libraries written in C, C++, Fortran, Rust, and other languages.

Not all developers have the right tools or experiences to build these components written in these compiled languages, so Python created the wheel, a package format designed to ship libraries with compiled artifacts. In fact, Python’s package installer, pip, always prefers wheels because installation is always faster, so even pure-Python packages work better with wheels.

* to create a build distribution of the package: `python setup.py bdist_wheel`

[source](https://packaging.python.org/overview/)

#### Steps to create a package for distribution:

	STEP1: create a dictionary, The name of this directory will be the name of the package, which we want to create. 
	
	STEP2: The directory needs to contain a file with the name "__init__.py". 
	       - This file can be empty, or it can contain valid Python code. 
	       - This code will be executed when a package will be imported, so it can be used to initialize a package.
   
	STEP3: Now add the Python files and modules into this package which are to be distributed.
   
	STEP4: create a setup.py file in the root folder,
	       - it acts as the entrypoint to the package
	       - it contains the actual instructions used when building and distributing the package.
   
	STEP5: Python packages are built into distribution packages, which are then uploaded to a server 
	       — usually uploaded to the global PyPI server, from which every person can access it and download.
   
	STEP6: to build the distribution files simply run the following command in the root folder where your setup.py is located: `python setup.py sdist bdist_wheel              # creates source and build distribution files.`

----------

#### 1. setup.py

The root directory of a package that has to be distributed contains a setup.py script. It defines all metadata as described in the distutils module. 
  * Package metadata is expressed as arguments in a call to the standard setup() function.
  * Despite distutils being the standard library module provided for the purpose of code packaging, it is actually recommended to use the setuptools instead. The setuptools package provides several enhancements over the standard distutils module.
  * setup.py is a cli( command line interface ).
  * herefore, the minimum content for this file is as follows:       
  
     ``` 
	  from setuptools import setup, find_packages
         setup(
                 name="HelloWorld",
                 version="0.1",
                 packages=find_packages(),
              )
      ```

- for more options enter the command : `python setup.py --help`
  
      Common commands: (see '--help-commands' for more)

        setup.py build      will build the package underneath 'build/'
        setup.py install    will install the package

      Global options:
        --verbose (-v)      run verbosely (default)
        --quiet (-q)        run quietly (turns verbosity off)
        --dry-run (-n)      don't actually do anything
        --help (-h)         show detailed help message
        --no-user-cfg       ignore pydistutils.cfg in your home directory
        --command-packages  list of packages that provide distutils commands

      Information display options (just display information, ignore any commands)
        --help-commands     list all available commands
        --name              print package name
        --version (-V)      print package version
        --fullname          print <package name>-<version>
        --author            print the author's name
        --author-email      print the author's email address
        --maintainer        print the maintainer's name
        --maintainer-email  print the maintainer's email address
        --contact           print the maintainer's name if known, else the author's
        --contact-email     print the maintainer's email address if known, else the
                            author's
        --url               print the URL for this package
        --license           print the license of the package
        --licence           alias for --license
        --description       print the package description
        --long-description  print the long package description
        --platforms         print the list of platforms
        --classifiers       print the list of classifiers
        --keywords          print the list of keywords
        --provides          print the list of packages/modules provided
        --requires          print the list of packages/modules required
        --obsoletes         print the list of packages/modules made obsolete

      usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
         or: setup.py --help [cmd1 cmd2 ...]
         or: setup.py --help-commands
         or: setup.py cmd --help

where:

***name*** is the name of the package. This can be any name as long as only contains letters, numbers, _ , and -. It also must not already taken on pypi.org.

***version*** is the package version

***author*** and ***author_email*** are used to identify the author of the package.

***description*** is a short, one-sentence summary of the package.

***long_description*** is a detailed description of the package. This is shown on the package detail package on the Python Package Index. In this case, the long description is loaded from README.md which is a common pattern.

***long_description_content_type*** tells the index what type of markup is used for the long description. In this case, it’s Markdown.

***url*** is the URL for the homepage of the project.

***packages*** is a list of all Python import packages that should be included in the distribution package. Instead of listing each package manually, we can use find_packages() to automatically discover all packages and subpackages.

***classifiers*** tell the index and pip some additional metadata about your package. https://pypi.org/classifiers/.

***namespace_packages*** see Python - Namespace Package

> [new and changed setup keywords](https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords): All of them are optional; you do not have to supply them unless you need the associated setuptools feature.

   ##### Classifers:
   
   Each project's maintainers provide PyPI with a list of "trove classifiers" to categorize each release, describing who it's for, what systems it can run on, and how mature it is.
   
   These standardized classifiers can then be used by community members to find projects based on their desired criteria. Currently, there are 667 classifiers available on PyPI that are grouped into the following nine major categories:

 - Development status
 - Environment
 - Framework
 - Intended audience
 - License
 - Natural language
 - Operating system
 - Programming language
 - Topic

   ##### Managing Dependencies:
   
   Many projects require some external packages to be installed in order to work properly. When the list of dependencies is very long, it becomes difficult to manage it. Keep it simple and provide the list of dependencies explicitly in your setup.py script using install_requires.

   ``` 
   from setuptools import setup
    	 setup(
             	name='some-package', 
             	install_requires=['falcon', 'requests', 'delorean']  # to list dependencies
             	# ... 
              )
    ```

#### 2. [setup.cfg](https://docs.python.org/3/distutils/configfile.html):

The setup.cfg file contains default options for commands of the setup.py script. This is very useful if the process for building and distributing the package is more complex and requires many optional arguments to be passed to the setup.py script commands.

 * This setup.cfg file allows you to store such default parameters together with your source code on a per project basis. This will make your distribution flow independent from the project and also provides transparency about how your package was built/distributed to the users and other team members.
 
* The setup configuration file is a useful middle-ground between the setup script—which, ideally, would be opaque to installers and the command-line to the setup script, which is outside of your control and entirely up to the installer.

* setup.cfg are processed after the contents of the setup script, but before the command-line. This has several useful consequences:
    1. installers can override some of what you put in setup.py by editing setup.cfg
    2. you can provide non-standard defaults for options that are not easily set in setup.py
    3. installers can override anything in setup.cfg using the command-line options to setup.py
    
The basic syntax of the configuration file is simple:

`[command]
 option=value
 ...`
 
 where
    - command is one of the Distutils commands
    - option is one of the options that command supports
  
an example of the setup.cfg configuration file that provides some global, sdist, and bdist_wheel commands defaults:

        [global] 
        quiet=1 

        [sdist] 
        formats=zip,tar 

        [bdist_wheel] 
        universal=1


#### 3. [MANIFEST.in](https://packaging.python.org/guides/using-manifest-in/):

Often packages will need to depend on files which are not .py files: e.g. images, data tables, documentation, etc. Those files need special treatment in order for setuptools to handle them correctly.

The mechanism that provides this is the MANIFEST.in file. This is relatively quite simple: MANIFEST.in is really just a list of relative file paths specifying files or globs to include

   By default distutils will include the following:
1. All Python source files implied by the py_modules, packages, and scripts arguments
2. All C source files listed in the ext_modules argument
3. Files that match the glob pattern test/test*.py
4. Files named README, README.txt, setup.py, and setup.cfg

the sdist will create a MANIFEST file that lists all files and will include them in the final archive.

Let's say you are not using any extra extensions, and you need to include in your package distribution some files that are not captured by default. You can define a template called MANIFEST.in in your package root directory (the same directory as setup.py file). This template directs the sdist command on which files to include.

This MANIFEST.in template defines one inclusion or exclusion rule per line:
1. include HISTORY.txt 
2. include README.txt 
3. include CHANGES.txt 
4. include CONTRIBUTORS.txt 
5. include LICENSE 
6. recursive-include *.txt *.py

there is a library [check_manifest](https://pypi.org/project/check-manifest/) which helps to create MANIFEST.in
You can ask the script to help you update your MANIFEST.in:
```$ check-manifest -u -v```
 
 > If you have your project in source control, the question “which files constitute the source code of this project?”, as opposed to “which files are local to a particular developer’s environment?” is already answered: the files under source control constitute the source code. 
   - This is also the position setuptools seems to take, since it introduced automatic inclusion of files under source control. This behavior was later generalized to be able to support arbitrary version control systems using plugins.
   
   -  If you read this in 2019, your VCS is most likely be git, in which case the package [setuptools_scm] provides the plugins you need. Add the following incantation to setup.py to ensure that files you have under source control are packaged:
   
   ``` setup(
  		...,
    		use_scm_version=True,
    		setup_requires=['setuptools_scm'],
    		...,
		)
```
And no more need for MANIFEST.in

# Distributing the package 
    
## publish the package in opensource:
   
If you’re writing an open source Python module and upload its package, **PyPI** (python packaging index) , more properly known as The ***Cheeseshop***, is the place to host it.
to publish create a distributed package and follow the steps below
 
    STEP1: create a distribution package
 
    STEP2: to upload you packages to the global PyPI server you’ll have to register to the PyPI website.
           - to authenticate with the PyPI server save the username and password of PyPI in a text file named ***.pypirc***, placed in your home folder. Create it, and text it as demonstrated below:
	   
             `  [distutils]
                 index-servers =
                   pypi
                   testpypi
                [pypi]
                  username: teapot48
                  password: myPYPIpassword `
		  
    STEP3: use twine, a utility for uploading Python packages. 
           - Simply run : `twine upload dist/* `                 # dist is the folder created which contains the packaged files.
      
   >note: you should see one progress bar as your .whl file is uploaded, and a second when the .tar.gz archive is uploaded, after which the upload will be complete.

## create a private repo for internal or personal use 

### 1. Personal pypi:
	
If you want to install packages from a source other than PyPI (say, if your packages are proprietary), you can do it by hosting a        simple HTTP server, running from the directory which holds those packages which need to be installed.
   
For example, if you want to install a package called MyPackage.tar.gz, and assuming this is your directory structure:
	
   hosting_package     	        # directory folder
   |
   |-- MyPackage                # folder inside the directory
      |
      |-- MyPackage.tar.gz      # package to be shared
   
   Go to your command prompt and type:
   ```
   $ cd hosting_package
   $ python -m http.server 9000
   ```
   
   This runs a simple HTTP server running on port 9000 and will list all packages (like MyPackage). Now you can install MyPackage using    any Python package installer. Using pip:
   ```
   $ pip install --extra-index-url http://127.0.0.1:9000/ MyPackage
   ```
    But if you feel that creating a folder called MyPackage and keeping MyPackage.tar.gz inside that is redundant, you can still install MyPackage using:
   ```
   $ pip install http://127.0.0.1:9000/MyPackage.tar.gz
   ```

### 2. Using pypiserver package on local system:
	
[pypiserver](https://pypi.org/project/pypiserver/) is a minimal PyPI compatible server. It can be used to serve a set of packages to    easy_install or pip. It includes helpful features like an administrative command (-U) which will update all its packages to their        latest versions found on PyPI.
   pypiserver > 1.2.x works with Python 2.7 and 3.4+
  
    STEP 1 : Install pypiserver with this command:   `pip install pypiserver`
       
    STEP 2 : Copy some packages into your ~/packages folder and then get your pypiserver up and running: `pypi-server -p 8080 ~/packages` 
   
    STEP 3 : To download the packages from another system
     
             # Download and install hosted packages.
               `pip install --extra-index-url http://localhost:8080 ...` 
     
             # Search hosted packages.
               `pip search --index http://localhost:8080 ...` 
	       
    > NOTE:  pypiserver redirects pip/easy_install to the pypi.org index if it doesn’t have a requested package
    
      |------------------------------|
    1.|  Client-Side Configurations  |
      |------------------------------| 
      
    Always specifying the the pypi url on the command line is a bit cumbersome. Since pypiserver redirects pip/easy_install to the pypi.org index if it doesn’t have a requested package, it is a good idea to configure them to always use your local pypi index. 
    
    - For pip command this can be done by setting the environment variable PIP_EXTRA_INDEX_URL in your .bashr/.profile/.zshrc: 
    `export PIP_EXTRA_INDEX_URL=http://localhost:8080/simple/ `
		
		or by adding the following lines to ~/.pip/pip.conf:
			```
            [global]
			extra-index-url = http://localhost:8080/simple/
            ```
      Instead of copying packages directly to the server’s folder, you may use python tools for the task,
      e.g. python setup.py sdist bdist_wheel upload
      
      to make the pipy server search for the packages in hosted server by adding the following lines to ~/.pip/pip.conf: 
              [global]
               extra-index-url=http://localhost:8080/simple/
      
      to upload the pacakges to PyPI using SETUPTOOLS
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
        
      |----------------------------------|
    2.|   Managing the Package Directory |
      |----------------------------------| 

    The pypi-server command has the -U option that searches for updates of available packages. It scans the package directory for available packages and searches on pypi.org for updates. Without further options pypi-server -U will just print a list of commands which must be run in order to get the latest version of each package. Output looks like:

    ```
    $ ./pypi-server -U
    checking 106 packages for newer version

    .........u.e...........e..u.............
    .....e..............................e...
    ..........................

    no releases found on pypi for PyXML, Pymacs, mercurial, setuptools

    # update raven from 1.4.3 to 1.4.4
    pip -q install --no-deps  --extra-index-url https://pypi.org/simple/ -d /home/ralf/packages/mirror raven==1.4.4

    # update greenlet from 0.3.3 to 0.3.4
    pip -q install --no-deps  --extra-index-url https://pypi.org/simple/ -d /home/ralf/packages/mirror greenlet==0.3.4
    ```
    
    It first prints for each package a single character after checking the available versions on pypi. A dot(.) means the package is up-to-date, 'u' means the package can be updated and 'e' means the list of releases on pypi is empty. After that it shows a pip command line which can be used to update a one package. Either copy and paste that or run pypi-server -Ux in order to really execute those commands. You need to have pip installed for that to work however.

    Specifying an additional -u option will also allow alpha, beta and release candidates to be downloaded. Without this option these releases won’t be considered. 
    
      |--------------------------------|
    3.|  serving thousands of Packages |
      |--------------------------------| 
    
    By default, pypiserver scans the entire packages directory each time an incoming HTTP request occurs. This isn’t a problem for a small number of packages, but causes noticeable slow-downs when serving thousands of packages. 
    If you run into this problem, significant speedups can be gained by enabling pypiserver’s directory caching functionality. The only requirement is to install the watchdog package, or it can be installed during pypiserver installation, by specifying the cache extras option: 
    
    `pip install pypiserver[cache]`
    
    > There are a variety of options for handling the automated starting of pypiserver upon system startup. Two of the most common are systemd and supervis
        
	
### 3. pypi server using docker on local system :
   
To run the most recent release of pypiserver with Docker, simply:

```docker run pypiserver/pypiserver:latest``` 
 > This starts pypiserver serving packages from the /data/packages directory inside the container, listening on the container port 8080.

The container takes all the same arguments as the normal pypi-server executable, with the exception of the internal container port (-p), which will always be 8080.

To map port 80 on the host to port 8080 on the container:
`docker run -p 80:8080 pypiserver/pypiserver:latest     #You can now access your pypiserver at localhost:80 in a web browser.`
  
  
### 4. pypi server on AWS-S3:
There are a few prerequisites when setting up a Python package repository on S3:
   * An AWS account.
   * A domain or subdomain, e.g. pypi.example.com. You should be able to create or modify the DNS record for the (sub)domain you want to use.
   * An SSL certificate for the domain you’re using.
   
In your AWS account, you need to setup an S3 bucket configured for website hosting, as well as a Cloudfront distribution for serving the content in your S3 bucket over a secure (HTTPS) connection, which is required by pip (by default).
   
- Install the s3pypi command line tool by running :  
	`$ (sudo) pip install -U s3pypi` 

- in your console. If everything goes well, you should be able to run the s3pypi command line tool now : 
	`$ s3pypi -v`
   
- In order to upload your package to your repository, cd to the root directory of your project, and run : 
	```$ s3pypi --bucket pypi.example.com```
 
- Install your packages using pip by pointing the --extra-index-url to your subdomain :
	`$ pip install my-project --extra-index-url https://pypi.example.com/`
	
 [source](https://www.novemberfive.co/blog/opensource-pypi-package-repository-tutorial):
 
### 5. pypi server on AWS EC2:
   
After setting up the instance on EC2 and successfully able to connect to the instance using SSH
 - See if python3 is already pre-installed :
     `sudo yum list | grep python3`
   
 - If not, install the version you would like to use :
     `sudo yum install python36`
   
 - install docker : 
      `sudo yum install docker`
      
 - start the service :
      `sudo service docker start`
      
      give docker permission to run without using sudo every time : 
      `sudo usermod -a -G docker ec2-user`
      > note: if you chose an ubuntu AMI instead, username would be ubuntu@IPv4Address
      exit the instance to make sure the changes take effect 
      
 * SSH back into the instance and test if the changes have taken effect:
      
    - check if you can run docker without the sudo command :
       `docker info`
      
    - if not, debug the previous steps. If so, run a test image :
        `docker run hello-world`
      > you should see a hello message from docker after running the last command
   
 * install docker-compose:
    run the below steps:
   
       STEP1 : sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
        
       STEP2 : sudo chmod +x /usr/local/bin/docker-compose  #give the proper permission for docker-compose
       
       STEP3 : sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose   #create a symbolic link so you can run docker-compose by just typing docker-compose
       
       STEP4 : docker-compose --version     # you should see docker-compose version x.xx.x, build xxxxxxx
  
 * to set up a directory to store usernames and passwords that the pypi server will use to authenticate upload or download requests. We used the “htapasswd” package for this.
 
   install httpd-tools with yum :  
   `sudo yum install httpd-tools`
   
   switch to the user's home directory :
   `cd`
   
   make a new directory called auth :
   `mkdir auth`
   
   cd into the auth directory :
   `cd auth`
   
   create a new .htpasswd file :
   `htpasswd -sc .htpasswd <username>` 
   
   > it will prompt you to enter a new password. Follow the prompts
   
   > to add users :
      `htpasswd -s .htpasswd <NewUsername>`

* create a new docker-compose.yml file with the following contents
  
        version: '3.3'
      services:
        pypi-server:
          image: pypiserver/pypiserver:latest
          ports:
            - "8081:8080"
          container_name: pypi-server
          volumes:
            - type: bind
              source: /home/ec2-user/auth
              target: /data/auth
            - type: volume
              source: pypi-server
              target: /data/packages
          command: -P /data/auth/.htpasswd -a update,download,list /data/packages
          restart: always
      volumes:
        pypi-server:
     
      1. First, the port mapping is import, because we can’t make requests directly to the docker container. Instead, we will be making requests to the host EC2 instance we have, so we mapped the host 8081 port to the docker container 8080 port.
     
      2. Next, we gave the container an easy to remember name via “container_name”. This way, we can easily find and work with this container in the future by using pypi-server instead of the long id docker assigns the container.
      
      3. We also mapped the host directory we created, which contains our .htpasswd file to the container volume at /data/auth. This allows our pypi-server in the docker container to handle authentication using the host file we created to validate incoming credentials.
      
      4. Then, we created a named volume “pypi-server” to map to the /data/packages volume in the docker container. This allows packages we upload to the pypi server within the docker container to persist in the named docker volume we created on the host machine. You can check this volume by typing: docker volume ls
      Otherwise, if the container goes down for some reason, the packages uploaded already would be lost.
      
      5. Finally, we specify the restart field as “always”. This ensures that if the container goes down by accident, it will always restart.

now the private pypi server is up and running on the AWS.

to upload your package to the pypi server created earlier in this guide :
  `twine upload --repository-url http://(ec2 IPv4 IP address):8081 dist/*`
  

to install packages from your pypi server :
  `pip install --extra-index-url http://(EC2 IPv4 IP Address):8081 YourPackageName --trusted-host (EC2 IPv4 IP Address)`
  

> If you don’t want to type the extra url and trusted host additions to the pip command, you may set up a .pip directory in your $HOME directory with a file called pip.conf like so:

   `[global]
   extra-index-url = http://(EC2 IPv4 IP Address):8081/
    trusted-host = (EC2 IPv4 IP Address)`
 
## dev-pi server

DevPI is a PyPI-compatible server you can run locally. It will not, and does not try, to scale to PyPI-like levels. In return, running it locally is simple and no frills.

* devpi-server: for serving a pypi.python.org consistent caching index as well as local github-style overlay indexes.
* devpi-web: plugin for devpi-server that provides a web and search interface
* devpi-client: command line tool with sub commands for creating users, using indexes, uploading to and installing from indexes, as well as a “test” command for invoking tox.

We want to run the full devpi system on our laptop:

`$ pip install -U devpi-web devpi-client`

> Note: that the devpi-web package will pull in the core devpi-server package. If you don’t want a web interface you can just install the latter only.

So let’s first initialize devpi-server:
`$ devpi-init`

To start devpi-server in the background we use supervisor as an example. First we create the config file for it:
`$ devpi-gen-config`

Then we start supervisord using a config which includes the generated file
`$ supervisord -c gen-config/supervisord.conf`

Then we point the devpi client to it:
`$ devpi use http://localhost:3141`

Then we add our own user
`$ devpi user -c testuser password=123`

Then we login:
`$ devpi login testuser --password=123`

And create a “dev” index, telling it to use the root/pypi cache as a base so that all of pypi.org packages will appear on that index:
`$ devpi index -c dev bases=root/pypi`

Finally we use the new index:
`$ devpi use testuser/dev`

We can now use the devpi command line client to trigger a pip install of a pypi package using the index from our already running server:
`$ devpi install pytest`

> NOTE: The devpi install command configured a pip call, using the pypi-compatible +simple/ page on THE testuser/dev index for finding and downloading packages. The pip executable was searched in the PATH and found in docenv/bin/pip.

We are going to use devpi command line tool facilities for performing uploads
Now go to the directory of a setup.py file of one of your projects (we assume it is named example) to build and upload your package to our testuser/dev index:
`example $ devpi upload`

> There are three triggered actions:
  * detection of a VCS (git/hg/svn/bazaar) repository, leading to copying all versioned files to a temporary work dir. If you are not using mercurial, the copy-step is skipped and the upload operates directly on your source tree.
  * registering the example release as defined in setup.py to our current index
  * building and uploading a gztar formatted release file from the workdir to the current index (using a setup.py invocation under the hood).

We can now install the freshly uploaded package:
`$ devpi install example`

> NOTE: devpi upload allows to simultanously upload multiple different formats of your release files such as sdist.zip or bdist_egg. The default is sdist.tgz.

If you have a package which uses tox for testing you may now invoke:
`$ devpi test example  # package needs to contain tox.ini`

> Here is what happened:

  * devpi got the latest available version of example from the current index

  * it unpacked it to a temp dir, found the tox.ini and then invoked tox, pointing it to our example-1.0.tar.gz, forcing all installations to go through our current testuser/dev/+simple/ index and instructing it to create a json report.

  * after all tests ran, we send the toxreport.json to the devpi server where it will be attached precisely to our release file.

Once you are happy with a release file you can push it either to another devpi-managed index or to an outside pypi index server.
Let’s create another staging index:
   `$ devpi index -c staging volatile=False`
   
> We created a [non-volatile index](https://devpi.net/docs/devpi/devpi/stable/+doc/userman/devpi_concepts.html#non-volatile-indexes) which means that one can not overwrite or delete release files.

We can now push the example-1.0.tar.gz from above to our staging index:
`$ devpi push example==1.0 testuser/staging`

> This will determine all files on our testuser/dev index belonging to the specified example==1.0 release and copy them to the testuser/staging index.

## How i hosted repository:
For the custom server/repository I have used [pypi-server](https://pypi.org/project/pypiserver/) and hosted it from [AWS EC2 instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html). i have put below the process i followed in steps for clear understanding:

##### server side configurations
After setting up the instance on EC2 and successfully able to connect to the instance using SSH

- See if python3 is already pre-installed :

     `sudo yum list | grep python3`
   
- If not, install the version you would like to use :

     `sudo yum install python36`

- Install pypiserver :

     `sudo pip3 install pypiserver[passlib,watchdog]`

We used the “htapasswd” package to store usernames and passwords that the pypi server will use to authenticate upload or download requests
- Install apache http tools :

      ` sudo yum install httpd-tools`
     
- to store the username and password 
  
      ` htpasswd -sc htpasswd.txt <username>`
    it will promt for password, enter the password 

- Created a new folder to host packages:

      ` mkdir packages`
      
- to host the pypi server: 
      
      ` pypi-server -p 8080 --server auto -P htpasswd.txt packages &`



##### client side configurations
placed a .pypirc file in the home directory with the following contents
[distutils]
index-servers =
	aws-repo
[aws-repo]
repository: http://<ip-address-of-ec2-instance>:8080/     # it is the address of the repository
username: <username>                        # username registered using htpasswd
password: <password>
	
- To install the packages in the client system:

      ` pip install --extra-index-url http://<ip-address-of-ec2-instance>:8080/simple/ <package-name>
      
- To upload the package to the repository i have used twine:

      ` twine upload -r aws-repo <location-of-distributed-package>
      
I hade to make/add few rules of the ec2 instance to make my server accessable for uploading the packages.

1. go to the security group of the hosted ec2 instance 

2. go to inbound rules and press add/edit
![inbound rules1](https://github.com/SurajKande/python_packaging/blob/master/misc/Screenshot%20(55).png)

3. add the following rules listed below in the image 
![inbound rules](https://github.com/SurajKande/python_packaging/blob/master/misc/Screenshot%20(57).png)

# GLOSSARY

1. [setup.py](https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords) : setup.py is a python file, which usually tells you that the module/package you are about to install has been packaged and distributed with Distutils or setuptools

2. Distutils :  standard for distributing Python Modules.

3. setuptools:  standard for distributing Python Modules.

4. MANIFEST.IN:
   [reference](https://www.remarkablyrestrained.com/python-setuptools-manifest-in/)
   [reference2]((https://docs.python.org/2.0/dist/manifest.html))
