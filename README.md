# Stationd-Restart

A python code that restarts Stationd service on ubuntu and sends it on telegram

first of all, create a bot on Telegram using botFather and then write bot token in tg.py as Token variable

then find your user chat id which is a numeric variable and then save it to tg.py as chat_id


## install python and screen
```
sudo apt-get update
sudo apt-get install python3.10
sudo apt install screen
sudo apt install git
```
```
sudo apt install python3-pip
```
```
git clone https://github.com/Theshaho/stationd-restart/
```
```
cd stationd-restart
```
## Change bot token and chat_id 
```
nano tg.py
```
Ctrl+X / Y / Enter
### Run script
```
screen -S stationd-restart
```
```
python3 restart.py
```
CTRL + A + D

