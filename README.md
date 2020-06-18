# violence-against-women-bd
It is an open source project to track violence against women in sub-urban level in Bangladesh


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

#### Open the project in your IDE and start coding. 







