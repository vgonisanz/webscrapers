# Webscrapper

Tocho webscrapper to get stock from shitty AMD/Nvidia releases 2020

## Requirements

Using Firefox:

```bash
sudo apt install firefox firefox-geckodriver -y
```

Using Chrome:

```bash
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

```bash
make env-create
```

## Usage

```bash
source ./.tox/webscrapping/bin/activate
python bin/amd5900x.py
```
