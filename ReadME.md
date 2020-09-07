### Student health information management

Student health information management is a simple web application for managing 
student health record to be used for analysis regarding to their performance 

Pre-requisiste

- Apache server should be installed an running
- Python 3.6 or above
- Install Pip3 to help you install other python packages which are in requirements.txt
- Mysql server installed and running

Steps:

1. Apache and mysql server setup:
	- Install Xampp on Windows machine start apache and mysql service
	- For Linux
		sudo apt install apache2
		sudo apt install mysql-server
		
2. Python 3.6 or above installation
	- On windows machine download from https://www.python.org/downloads (remember during installation check add python path in variable names)
	- On linux distro python is pre-installed
	- Install pip3 (download from internet)
	
3. Install Virtual environment & Flask framework (https://flask.palletsprojects.com/en/1.1.x/installation/)
	- Activate virtual environment
		
4. Install packages to run project(in project root folder)
	-pip3 install -r requirements.txt
	
5. Import mysql database from SQL file
	- On Windows
		- cd C:\xampp\mysql\bin
		- mysql -u root -p
		- CREATE DATABASE shealthmis
		- mysqldump -h localhost -u root -p -d shealthmis < shealthmis/Database/filename.sql
		- Change database user from config.py

	
6. Run project go to project root directory (C:\..\shealthmis) 
	- python3 app.py

#### Users credentials
	Administrator Phone:	 0784360416
	Administrator password: 12345
	
	Nurse phone	: 	0726183049
	Nurse Password  :	12345
	
