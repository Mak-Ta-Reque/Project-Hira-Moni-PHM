# Project Hira Moni
## Overview
It is an open source project to track violence against women in sub-urban level in Bangladesh.

## Environment Setup

### Windows
Open command prompt in a folder of your local machine.   
Run 
```
git clone https://github.com/Mak-Ta-Reque/Project-Hira-Moni-PHM
```
 to download the project in a your local machine.


#### Setup Python
To check if python is already installed and added in your path. Run
```
python --version
```
Please make sure you are 
using version **3.7.7 or newer**.   
If python is already installed in your machine please go to the next step **Install virtualenv**.

##### Installing python and pip
Go to the python [official website](https://www.python.org/downloads/windows/) to download python installer.
Go through the installer window. If prompted check to install pip and add python in PATH variable.
After installation, open a new CMD window and check the above way if python is successfully installed or not.

#### Setup `virtualenv`
To check if *virtualenv* is already installed.

```
virtualenv --version
```

To install 
`pip install virtualenv`

To create a virtual environment
```
cd Project-Hira-Moni-PHM
virtualenv venv
```

To activate the virtual environment
```
.\venv\Scripts\activate
```
Make sure working directory of you CMD is leading by `(venv)` keyword.

#### Install the requirements
Notice there is a *requirements.txt* file in your project root folder containing all the packages required for 
running this project.
Run the following command to install the requirements
```
pip install -r requirements.txt
```

Wait for several minutes depending on your stability of connection.

##### Exiting from virtualenv
```
deativate
```

#### Run Django server
```
python violance_analytics\manage.py runserver
```