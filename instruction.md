## How to launch in Ubuntu
ssh aws
tmux attach
sudo apt update
sudo apt upgrade

sudo apt install python3.10 python3-venv

cd WebChatRooms/
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements/requirements.txt
cd WebChatProject
python manage.py runserver 0.0.0.0:8000
