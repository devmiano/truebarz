# truebarz

An entertainment app that gets the latest music and current playlist. You get to search songs by having our app listen to audio and get who has sang it.

## instructions

After cloning the repository run
`python -m pip install -r requirements.txt`

Next, make sure to create a new database
in the terminal run `psql`

Then `CREATE DATABASE truebarz;`

Ater that change your username and password in the `config.py` file in line 22

Before Running the application run `chmod a+x start.sh`
use the shell command to create all tables `db.create_all()`
the use the server command to run the application `./start.sh`

The required colors are in the colors.txt file
Write all your CSS in the file in `assets/styles/global.css`

Images are in the `assets/images/` folder
