# drive upload videos

upload files to google drive from downloads

## requirements

pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## create environment

python3 -m venv myenv

### windows

source myenv/Scripts/activate

### linux/mac

source myenv/bin/activate

## install packages

pip3 install -r requirements.txt

## client secret file

Download OAuth client json file [here](https://console.cloud.google.com/apis/credentials) and save to project directory as "client_secret_file.json".
