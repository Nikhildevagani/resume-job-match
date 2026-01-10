from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from MLpreprocess import preprocess_text


def calculate_match_score(resume_text, job_text):
    resume_clean = preprocess_text(resume_text)
    job_clean = preprocess_text(job_text)

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),      # capture phrases
        sublinear_tf=True,       # log scaling
        smooth_idf=True,         # stable IDF
        norm="l2"                # cosine-friendly
    )

    vectors = vectorizer.fit_transform([resume_clean, job_clean])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)



if __name__ == "__main__":
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()

    with open("job_description.txt", "r", encoding="utf-8") as f:
        job = f.read()

    score = calculate_match_score(resume, job)
    print(f"Resume–Job Match Score: {score}%")
