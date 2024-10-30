import nltk
import os

# Set the NLTK data path to a writable directory in your deployment environment
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
except Exception as e:
    print(f"Error downloading NLTK data: {e}")