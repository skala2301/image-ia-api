
#install project
To start the project you'll to create a google cloud proyect if you want to use the vertes AI

GOOGLE_CLOUD_PROJECT="project-id"
GOOGLE_CLOUD_LOCATION="google-server-location"
GOOGLE_GENAI_USE_VERTEXAI=true

You'll also need a gradio account and access token https://huggingface.co/

GRADIO_HF_TOKEN="access-token"


#create an python enviroment
i recommend using a python enviroment link: https://github.com/pyenv/pyenv
pyenv is my personal recommendation

#after creating python enviroment
create a virtual enviroment, as an example:

pyenv virtualenv 3.11.9 testenv

this will create a virtual enviroment called testenv with python version 3.11.9
then set your local enviroment:

pyenv local testenv



#dependencies
go to the root folder and run:

pip install -r requirements.txt

#Fastapi initialization 

use the command:

fastapi/src/interfaces/main.py