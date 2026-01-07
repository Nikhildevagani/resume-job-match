import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

if __name__ == "__main__":
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()
    with open("job_description.txt", "r", encoding="utf-8") as f:
        job = f.read()

    print("Processed Resume:\n", preprocess_text(resume))
    print("\nProcessed Job Description:\n", preprocess_text(job))
