## Initial Downloads and Local Repository Setup
1. Download VS Code if you haven't, as the terminal is extremely important. I'm assuming on Windows it emulates bash.
https://code.visualstudio.com/

2. Download Docker and Docker-compose
https://www.docker.com/get-started
https://docs.docker.com/compose/install/

3. If you don't have python, install it.
https://www.python.org/downloads/

4. Clone the repository to whatever folder you want, you don't need the frontend for now.

5. use the following git command, and create a new branch for yourself. For now. We'll change it later.

> git checkout -b aeseop-setup

## Python and Docker
1. navigate to the directory you cloned the project in, i guess in... powershell somehow?

2. Create a python virtual environment. If you don't know what this does it allows us to work with certain dependecies (addons) without affecting other projects. You should create one for every python project you make tbh.

> python3 -m venv /path/to/your/project/root/directory

> source /path/to/your/project/root/directory/venv/bin/activate.sh

This will activate the python virtual environment. You should notice the venv beside your username in the terminal (or command prompt? idfk).

5. after it's activated, run the the following to install all of our necessary depenencies. Should handle everything form django to pythons lib for working with SQL.

> pip install -r requirements.txt and this will download all of our necessary dependencies.

6. Run the command to build the project.

> docker build

7. after that's done run docker-compose. You'll be using this from here on out.

> docker-compose up.

> (run docker-compose down if you ever need to stop it.)

The project will set itself up and start running.

8. In the VS Code terminal, you'll want to run

> docker-compose exec django python manage.py makemigrations

> docker-compose exec django python manage.py migrate

If neither of those things work. Flip them and migrate first then make migrations.

From there, the database will be populated with the tables you need.


## Setting up VS Code.
At the top, file, save workspace as. Save it osmewhere outside of the project.

* Docker
* Django
* Django Template
* Python
* Pylance
* Python Environment Manager
* YML
