# truebarz

An entertainment app that gets the latest music and current playlist. You get to search songs by having our app listen to audio and get who has sang it.

## Updated instructions

After you have cloned the repository using `git clone git@github.com:devmiano/truebarz.git`

> Step 1: Create virtual environment `python3 -m venv --without-pip env`

> Step 2: Activate virtual environment `source env/bin/activate`

> Step 3: Install pip in the virtual environment `curl https://bootstrap.pypa.io/get-pip.py | python3`

> Step 4: Install all packages in the requirements.txt file `python -m pip install -r requirements.txt`

> Step 5: Change your username and password for the database config in the `config.py` file

> Step 6: Run `chmod a+x start.sh` to give privileges to the start.sh script

> Step 7: Start the database shell using the command `./start.sh` by uncommenting `python3 manage.py shell` in the `start.sh` file and comment out all other commands before running the command

> Step 8: Run `db.create_all()` to create all database tables

> Step 9: Start the application shell using the command `./start.sh` by uncommenting `python3 manage.py server` in the `start.sh` file and comment out all other commands before running the command
