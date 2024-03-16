# This shell script should be run within backend
# Run the following command if "Permission denied"
# chmod +x dev.sh
source venv/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
flask run
