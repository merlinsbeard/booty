
cd /home/pi/booty
source ../venv/bin/activate
gunicorn -b 0.0.0.0 booty.wsgi

