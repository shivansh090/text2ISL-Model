import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from django.http import JsonResponse
from django.contrib.staticfiles import finders
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

# Set up NLTK data directory
NLTK_DATA_DIR = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(NLTK_DATA_DIR):
    os.makedirs(NLTK_DATA_DIR)
nltk.data.path.append(NLTK_DATA_DIR)

# Download required NLTK data
try:
    nltk.download('punkt', download_dir=NLTK_DATA_DIR)
    nltk.download('averaged_perceptron_tagger', download_dir=NLTK_DATA_DIR)
    nltk.download('stopwords', download_dir=NLTK_DATA_DIR)
    nltk.download('wordnet', download_dir=NLTK_DATA_DIR)
    print("NLTK data downloaded successfully")
except Exception as e:
    print(f"Error downloading NLTK data: {e}")

@method_decorator(csrf_exempt, name='dispatch')
class ApiAnimationView(APIView):
    def post(self, request):
        try:
            data = request.data
            text = data.get('sen', '').lower()

            # Tokenize using standard punkt tokenizer
            words = nltk.word_tokenize(text)
            
            # POS tagging using standard averaged_perceptron_tagger
            tagged = nltk.pos_tag(words)

            # Tense analysis
            tense = {
                "future": len([word for word in tagged if word[1] == "MD"]),
                "present": len([word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]]),
                "past": len([word for word in tagged if word[1] in ["VBD", "VBN"]]),
                "present_continuous": len([word for word in tagged if word[1] == "VBG"])
            }

            # Stopwords removal and lemmatization
            stop_words = set(stopwords.words('english'))
            lemmatizer = WordNetLemmatizer()
            filtered_text = [
                lemmatizer.lemmatize(w, pos='v' if p[1].startswith('V') else 'a' if p[1].startswith('J') else 'n')
                for w, p in zip(words, tagged) if w not in stop_words
            ]

            # Determine tense and prepend specific words
            if max(tense, key=tense.get) == "past" and tense["past"] >= 1:
                filtered_text.insert(0, "Before")
            elif max(tense, key=tense.get) == "future" and tense["future"] >= 1:
                if "will" not in filtered_text:
                    filtered_text.insert(0, "Will")
            elif tense["present_continuous"] >= 1:
                filtered_text.insert(0, "Now")

            # Animation file checks
            words_for_animation = []
            for w in filtered_text:
                path = f"{w}.mp4"
                if finders.find(path):
                    words_for_animation.append(w)
                else:
                    words_for_animation.extend(list(w))  # Add letters if word animation is missing

            return JsonResponse({'words': words_for_animation, 'text': text}, status=200)
        
        except Exception as e:
            print(f"Error in animation processing: {e}")
            return JsonResponse({'error': str(e)}, status=500)