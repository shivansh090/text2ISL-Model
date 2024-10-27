# Text to Indian Sign Language (ISL) Converter API

Hello there! I've created a backend API that converts text input into Indian Sign Language (ISL) animations. This API is designed to be the engine behind a web application that displays ISL animations based on text input.

## What My API Does

My API takes in text as input, processes it using Natural Language Toolkit (NLTK), and returns the relevant Indian Sign Language animations. Here's a quick overview of what's happening under the hood:

> 1. Text preprocessing using NLTK
> 2. Mapping of processed text to pre-created 3D animations
> 3. Returning animation data for frontend rendering

## Prerequisites

To get my API up and running, you'll need:

> - Python 3.7 or higher
> -Browser supports Web Speech API
> - All required packages listed in `requirements.txt`

## Getting Started

First, make sure you have all the prerequisites installed. Then, follow these steps:

1. Clone this repository to your local machine
2. Navigate to the project directory in your terminal
3. Install the required packages: `pip install -r requirements.txt`
4. Start the server with this command: python manage.py runserver 8000

This will start the server at `http://127.0.0.1:8000/`

## API Usage

To use my API, send a POST request to the `/api/animation/` endpoint with your text in the request body. Here's an example using curl:
```
curl -X POST [http://localhost:8000/api/animation/](http://localhost:8000/api/animation/) -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -d '{"sen": "Hello, how are you?"}'
Project Demo Video: https://youtu.be/YiHhD0QGrno
```
The API will return a JSON response with the relevant animation data.

## A Note on Authentication

I've implemented token-based authentication for security. Make sure to include your authentication token in the request header as shown in the example above.

## Feedback and Contributions

I'm always looking to improve this API. If you have any suggestions or run into any issues, please open an issue in this repository. Pull requests are also welcome!

Thank you for using my Text to ISL Converter API. I hope it serves you well in your projects!

