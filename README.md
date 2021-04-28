# Webscrapper

Tocho webscrapper to get stock from shitty AMD/Nvidia releases 2020

## Requirements

### Firefox backend

```bash
sudo apt install firefox firefox-geckodriver -y
```

If you have problems to find geckodriver in your distro, do it manually:

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
tar -xvzf geckodriver*
sudo mv geckodriver /usr/bin/geckodriver
sudo chown root:root /usr/bin/geckodriver
sudo chmod +x /usr/bin/geckodriver
rm geckodriver*
```

### Chrome backend

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

### Both - Python environment

Create the tox virtual environment with the Makefile target:

```bash
make env-create
```

## Usage

To choose between chrome and firefox use the core flag `use_firefox`

```bash
source ./.tox/webscrapping/bin/activate
python bin/amd5900x.py
```
Check this repository https://github.com/EricJMarti/inventory-hunter to learn more about webscrapping and coprocessing requests
