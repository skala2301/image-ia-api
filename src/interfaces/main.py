from typing import Union

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.shared import API, DEBUG

from .routers import (
    image_edit_router,
    google_router,
    gradio_router,
)

from os import getenv, path
from dotenv import load_dotenv

# --- NEW: Calculate the path to the .env file ---
# Get the absolute path of the current script (main.py)
current_script_dir = path.dirname(path.abspath(__file__))

# Go up one level (from interfaces to src)
src_dir = path.dirname(current_script_dir)

# Go up another level (from src to my_project)
project_root_dir = path.dirname(src_dir)

# Construct the path to the .env file
dotenv_path = path.join(project_root_dir, '.env')

# Load the environment variables from the .env file
# This line should be at the very top of your application's loading process.
load_dotenv(dotenv_path=dotenv_path)

app = FastAPI(
    debug=DEBUG,
    title="Shopify API",
    description="API for interacting with Shopify",
    version="0.1.0",
    default_response_class=ORJSONResponse,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)


app.include_router(router=image_edit_router, prefix=API.V1)
app.include_router(router=google_router, prefix=API.V1)
app.include_router(router=gradio_router, prefix=API.V1)
