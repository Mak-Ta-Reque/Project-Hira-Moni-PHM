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

#### Enabling database
```
make a file .env inside root of the project and write 
DATABASE_URL=sqlite:///db.sqlite3 

```
Do not upload this file in git

Without this you will get key error.
#### Open the project in your IDE and start coding. 



#### Setting up the development environment (Linux)
```
# Make sure you have python3 installed in your computer.
# Python 3.7 is recomanded 

# If you don't have Python3 in your computer please follow this instruction
# [https://realpython.com/installing-python/]

```
##### Creating a virtual environment
```
python3 -m venv phm_env
```

###### It will help you to keep the project work indepedent of your system environment.

###### This command will create a director phm_env inside your current directory

##### Activate virtual environment <phm_env>
```
source phm_env/bin/activate
```



##### Deactivate virtual environment <phm_env> type
```
deactivate
```
##### Source: https://docs.python.org/3/tutorial/venv.html 

##### Connect environment with your IDE: Example PyCharm
```
Click:  Preferences -> Project Interpreter -> 
The seeting icon in the right corner -> 
Add -> Existing environment -> Locate the created <phm_env> folder
 
```
#### PyCharm can also create create a  New environment for you if you don't have one 

```
Click:  Preferences -> Project Interpreter -> 
The seeting icon in the right corner -> 
Add -> New environment -> Give the location where you want to save the new environment 
-> Chose base Python: Python3 from the list.
 
```

##### Download project from git
```
After Activating the virtual environment please clone
the project from the deafult branch. eg: 
SSH Command : git clone git@github.com:Mak-Ta-Reque/Project-Hira-Moni-PHM.git
or 
HTTP Command : git clone https://github.com/Mak-Ta-Reque/Project-Hira-Moni-PHM.git
```
SSH does't require user id and password every time.
You might need to setup SSH for that


#### After activating your virtual environment Go inside < violence-against-women-bd > directory and install requirements
```
pip3 install -r requirements.txt 
```

#### Enabling database
```
make a file .env inside root of the project and write 
DATABASE_URL=sqlite:///db.sqlite3 

```
Do not upload this file in git

Without this you will get key error.
#### Open the project in your IDE and start coding. 



