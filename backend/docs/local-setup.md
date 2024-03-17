# Setting Up the Backend

Follow these steps to set up the project:

**1. Clone the project repository**

The remote repository is hosted on GitHub. Use either of the two methods to clone to a local repository for development.

<u>HTTPS:</u>

```bash
git clone https://github.com/edisonwang03/pipeline.git
```

<u>SSH:</u>

```bash
git clone git@github.com:edisonwang03/pipeline.git
```

**2. Install backend dependencies**

The backend dependencies are stored in `pipeline/backend/requirements.txt`. Make sure to `pip freeze > requirements.txt` whenever additional dependencies are installed (within the virtual environment).

```bash
cd pipeline/backend
python -m venv venv
pip install -r requirements.txt
```

**3. Set up the database**
    
3a. Install PostgreSQL.

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

3b. Login to PostgreSQL as the `postgres` user. PostgreSQL uses peer authentication, where authentication occurs based on your operating system username. In a default PostgreSQL installation, a system user named `postgres` is created to correspond to the default PostgreSQL superuser.

```bash
sudo -u postgres -i
psql
```

3c. Create a database called `pipeline`.

```bash
CREATE DATABASE 'pipeline';
```

3d. Create a user and grant privileges to the `pipeline` database. This is the user account that our backend will use to interact with the database.

```postgresql
CREATE USER <YOUR_USERNAME_CHOICE> WITH PASSWORD '<YOUR_PASSWORD_CHOICE>';
GRANT ALL PRIVLEGES ON DATABASE 'pipeline' TO <YOUR_USERNAME_CHOICE>;
```

3e. Make checks before exiting PostgreSQL. `\du` checks that you indeed created a new user with all the necessary privileges. `\l` ensures that the database `pipeline` has actually been created. `q` quits `psql`.

```postgresql
\du
\l
\q
```

3f. Log out of the postgres user and check that the PostgreSQL server is running. If not, start the server with the second code block command.

```
exit
sudo service postgresql status
```
```
sudo service postgresql start
```

3g. Set up the environment variables in the `pipeline/backend/.env` file. Create a copy of the `.env-example` file and rename it to `.env`. Fill in the variable values with the database credentials you provided.

`pipeline/backend/.env`:
```
SECRET_KEY = "YOUR_SECRET_KEY_CHOICE"
DATABASE_USERNAME = "YOUR_USERNAME_CHOICE"
DATABASE_PASSWORD = "YOUR_PASSWORD_CHOICE"
DATABASE_NAME = "pipeline"
DATABASE_PORT = 5432
SQLALCHEMY_TRACK_MODIFICATIONS = "False"
RUN_DEBUG_MODE = "True"
```

**4. Start the backend server**

Run the command below within the `pipeline/backend` directory to start the backend server. This will start it in debug mode with all the necessary environment variables configured.

```bash
./dev.sh
```
