
# 🚀 AI Image API

This project provides a FastAPI application for AI image generation and manipulation, integrating with external services like Google's Vertex AI and Gradio's Hugging Face models.

***

## 📋 Prerequisites

Before you begin, ensure you have the following set up:

* **Python:** Version 3.11 or higher.
* **Google Cloud Project:** A Google Cloud project is required to use Vertex AI. You'll need to set up the following environment variables:
    ```bash
    GOOGLE_CLOUD_PROJECT="your-project-id"
    GOOGLE_CLOUD_LOCATION="your-google-server-location"
    GOOGLE_GENAI_USE_VERTEXAI=true
    ```
* **Hugging Face Account:** An account and access token from Hugging Face are needed for Gradio services. You can get a token from your settings page.
    ```bash
    GRADIO_HF_TOKEN="your-access-token"
    ```

***

## ⚙️ Installation

### 1. Create a Python Environment

It's highly recommended to use a Python environment manager like **`pyenv`** to isolate your project's dependencies.

First, create a new virtual environment. For example, to create one named `testenv` with Python 3.11.9:

```bash
pyenv virtualenv 3.11.9 testenv
```

This will create a virtual enviroment called testenv with python version 3.11.9
then set your local enviroment:

```bash
pyenv local testenv
```


## dependencies
Go to the root folder and run:
```bash
pip install -r requirements.txt
```
# Fastapi initialization 

use the command:
```bash
fastapi dev src/interfaces/main.py
```