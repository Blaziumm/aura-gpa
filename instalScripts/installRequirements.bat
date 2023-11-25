@ECHO OFF
TITLE Aura Requirements Download

ECHO Please wait... Downloading Requirements Now.

python -m pip install --upgrade pip

pip install -r requirements.txt

PAUSE