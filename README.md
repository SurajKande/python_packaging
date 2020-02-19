# python Packaging
this repository is based on how to create packages and distribute the pacakges.  

# what is packaging
A python package is a directory of python modules( python files are also modules) with a file named __init__.py

### example of package structure:

   ![example1](https://www.python-course.eu/images/packages.png)
 

### real time example of a project package of creating a game:
 
   ![example of package](https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg)
- an alternate for packaging, you should [freeze your application](https://docs.python-guide.org/shipping/freezing/#freezing-your-code-ref)

# how to create a basic package:
[example_of a_sample_package](https://github.com/SurajKande/python_packaging/tree/master/package_example)

   ### steps to create a basic package with some Python modules and submodules:
      step1: create a dictionary, The name of this directory will be the name of the package, which we want to create 

      step2: This directory needs to contain a file with the name "__init__.py". This file can be empty, or it can contain valid Python code. This code will be executed when a package will be imported, so it can be used to initialize a package,

      step3: Now we can add the Python files and modules into this package 

* the package is created which we can use locally by:
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
 server in a text file named ***.pypirc***, commonly placed in your home folder. Create it, and text it as demonstrated below:
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

   ## 2. pypi server on local system:
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
   
      
   ## 3. pypi server using docker on local system :
   To run the most recent release of pypiserver with Docker, simply:
   
          docker run pypiserver/pypiserver:latest 
          
   > This starts pypiserver serving packages from the /data/packages directory inside the container, listening on the container port 8080.

  The container takes all the same arguments as the normal pypi-server executable, with the exception of the internal container  port (-p), which will always be 8080.

  To map port 80 on the host to port 8080 on the container:

         docker run -p 80:8080 pypiserver/pypiserver:latest
         You can now access your pypiserver at localhost:80 in a web browser.
  
  ## 4. pypi server on AWS-S3:
  There are a few prerequisites when setting up a Python package repository on S3:

   * An AWS account.
   * A domain or subdomain, e.g. pypi.example.com. You should be able to create or modify the DNS record for the (sub)domain you want to use.
   * An SSL certificate for the domain you’re using.
   
   In your AWS account, you need to setup an S3 bucket configured for website hosting, as well as a Cloudfront distribution for serving the content in your S3 bucket over a secure (HTTPS) connection, which is required by pip (by default).
   
   Install the s3pypi command line tool by running
       ```$ (sudo) pip install -U s3pypi``` 

   in your console. If everything goes well, you should be able to run the s3pypi command line tool now:
       ```$ s3pypi -v```
   
   In order to upload your package to your repository, cd to the root directory of your project, and run:
       ```$ s3pypi --bucket pypi.example.com```
   
   Install your packages using pip by pointing the --extra-index-url to your subdomain:
      ```$ pip install my-project --extra-index-url https://pypi.example.com/```
 [source](https://www.novemberfive.co/blog/opensource-pypi-package-repository-tutorial):
 
   ## 5. pypi server on AWS EC2:
   After setting up the instance on EC2 and successfully able to connect to the instance using SSH
   See if python3 is already pre-installed:
   
   ```sudo yum list | grep python3```
   
   If not, install the version you would like to use:
   
   ```sudo yum install python36```
   
 * install docker
 
   ```sudo yum install docker```
      start the service
      
      ```sudo service docker start```
      give docker permission to run without using sudo every time
      
      ```sudo usermod -a -G docker ec2-user```
      > note: if you chose an ubuntu AMI instead, username would be ubuntu@IPv4Address
      exit the instance to make sure the changes take effect 
      
 * SSH back into the instance and test if the changes have taken effect:
      check if you can run docker without the sudo command
      
      ```docker info```
      if not, debug the previous steps. If so, run a test image
      
      ```docker run hello-world```
      > you should see a hello message from docker after running the last command
   
 * install docker-compose:
   run the below steps:
   
       step1: sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
        
       step2: sudo chmod +x /usr/local/bin/docker-compose  #give the proper permission for docker-compose
       
       step3: sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose   #create a symbolic link so you can run docker-compose by just typing docker-compose
       
       step4: docker-compose --version     # you should see docker-compose version x.xx.x, build xxxxxxx
   
  
 * to set up a directory to store usernames and passwords that the pypi server will use to authenticate upload or download requests. We used the “htapasswd” package for this.
 
   install httpd-tools with yum
   
   ```sudo yum install httpd-tools```
   switch to the user's home directory
   
   ```cd```
   make a new directory called auth
   
   ```mkdir auth```
   cd into the auth directory
   
   ```cd auth```
   create a new .htpasswd file
   
   ```htpasswd -sc .htpasswd <username>```
   > it will prompt you to enter a new password. Follow the prompts
   
   > to add users
   
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

to upload your package to the pypi server created earlier in this guide.

`twine upload --repository-url http://(ec2 IPv4 IP address):8081 dist/*`

to install packages from your pypi server

`pip install --extra-index-url http://(EC2 IPv4 IP Address):8081 YourPackageName --trusted-host (EC2 IPv4 IP Address)`

> If you don’t want to type the extra url and trusted host additions to the pip command, you may set up a .pip directory in your $HOME directory with a file called pip.conf like so:
   `[global]
   extra-index-url = http://(EC2 IPv4 IP Address):8081/
    trusted-host = (EC2 IPv4 IP Address)`
 
# dev-pi server
DevPI is a PyPI-compatible server you can run locally. It will not, and does not try, to scale to PyPI-like levels. In return, running it locally is simple and no frills.

* devpi-server: for serving a pypi.python.org consistent caching index as well as local github-style overlay indexes.
* devpi-web: plugin for devpi-server that provides a web and search interface
* devpi-client: command line tool with sub commands for creating users, using indexes, uploading to and installing from indexes, as well as a “test” command for invoking tox.


