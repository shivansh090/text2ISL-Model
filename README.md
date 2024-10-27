> `(This MLmodel has been integrated in my repo` https://github.com/shivansh090/Neuraxis)
# Text to Indian Sign Language (ISL) Converter API

This API converts text into Indian Sign Language (ISL) animations by leveraging natural language processing (NLP) techniques. Designed as a translation engine, it interprets and maps text input to 3D ISL animations, creating an accessible and engaging experience for sign language users.

## Project Overview

The Text to ISL Converter API uses machine learning and NLP to:
 1. **Preprocess and Analyze Text Input** — Breaking down text into key tokens and grammatical structures.
 2. **Map Processed Text to ISL Animations** — Using predefined animations based on the semantic and syntactic features of the text.
 3. **Generate Responses** — Returning animation data for ISL sign sequences.

## Model & NLP Pipeline

The API leverages NLTK for preprocessing, which includes:

- Tokenization — Breaking text into words
- POS Tagging — Part-of-speech tagging to capture grammatical context
- Stop Words Removal and Lemmatization — Filtering out unimportant words and reducing words to base forms
- Based on token analysis and grammatical structure, the API maps text to ISL animations, using predefined videos to represent each token. When a token’s animation is unavailable, it defaults to a character-by-character sign animation.

## Prerequisites

To get my API up and running, you'll need:

 - Python 3.7 or higher
 - Browser supports Web Speech API
 - All required packages listed in `requirements.txt`

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

```
The API will return a JSON response with the relevant animation data.

## Future Directions
The following areas offer potential for enhancement:

- Model Refinement — Implement more complex NLP models for improved text analysis.
- Dynamic Animation Generation — Use computer vision models for real-time generation of ISL animations.
- Expansion to Other Sign Languages — Adapt the model to support other regional sign languages with minimal changes.
## Feedback and Contributions

I'm always looking to improve this API. If you have any suggestions or run into any issues, please open an issue in this repository. Pull requests are also welcome!

Thank you for using my Text to ISL Converter API. I hope it serves you well in your projects!

