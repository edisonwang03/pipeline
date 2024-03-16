# This shell script should be run within backend
# Run the following command if "Permission denied"
# chmod +x dev.sh
source venv/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
export FLASK_DEBUG=1
flask run
