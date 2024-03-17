# This shell script should be run within backend

# Run the following command if "Permission denied"
# chmod +x dev.sh

# The server will be running at http://localhost:5000/

# The flask server will only restart if changes to the app directory are made

source venv/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
export FLASK_DEBUG=1
export PYTHONDONTWRITEBYTECODE=1
flask run

