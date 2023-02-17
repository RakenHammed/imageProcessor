# Image processor

A flask app that accept one post request at http://tech-test-3.picsellia.com:5000/imageProcessor and saves it in a directory images on the host server.

```bash
  curl --location --request POST 'http://tech-test-3.picsellia.com:5000/imageProcessor' \
--form 'image=@"/home/rhammed/Téléchargements/test.jpg"'
```

Logs are saved in file on the host server in
```bash
/home/ubuntu/imageProcessor/logs/main.log
```
## Configuration
On the host server you can set the allowed image extension in the .env file
or change where you can upload the image

## Development
To use the app locally you can run the script setup_dev_env.sh in the terminal
```bash
source setup_dev_env.sh #use source to activate venv
```
This will setup all your dependencies and install the pre-commit features
you need to have python3.10 and poetry 1.2.1 to be able to use this script then you can run
```bash
flask run
```
Or you can directly use if you don't wont to install things

```bash
docker compose up --build
```
## Build and deployment
Any push action will build the new image and deploy it using the github actions pipeline.


## Missing from the app
implementation of remove_background method and get_coordinates_outline
as it demand a deeper undestanding of the subject.
