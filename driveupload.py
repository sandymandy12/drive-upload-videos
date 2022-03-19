from turtle import up
from Google import Create_Service, upload_file
from googleapiclient.http import MediaFileUpload
from sys import platform
import os

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

home_dir = os.path.expanduser('~')
path = os.path.join(home_dir, 'Downloads')
dir_list = os.listdir(path)

results = [upload_file(service, path, x)
           for x in dir_list if x.endswith('.txt')]
# files = [upload_file(x) for x in dir_list if x.endswith('.txt')]

print(results)
