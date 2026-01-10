📄 Resume–Job Match Scorer (Explainable AI)

👤 Team

VectorMind
Solo developer – AIML student
Focused on practical, explainable ML systems.
Hackathon: TechSprint 2026 – Open Innovation Track


🚀 Project Overview
The Resume–Job Match Scorer is an AI-powered system that evaluates how well a resume aligns with a given job description.
It uses classical Machine Learning for similarity scoring and an explainable AI layer to provide human-readable insights, missing skills, and resume improvement suggestions.
This project focuses on honest, explainable, and industry-relevant ATS-style matching, rather than black-box predictions.

🎯 Problem Statement⬇️
➡️ Recruiters and job seekers often struggle to understand:
1.How well a resume matches a job role
2.Why a resume gets shortlisted or rejected
3.Which skills are missing or need improvement
4.Most systems provide only a score, without transparency.

💡 Our Solution⬇️
1.We built an Explainable Resume–Job Matching System that:
2.Computes a raw ML similarity score
3.Generates a final compatibility score for better user understanding
4.Explains why the score was given
5.Highlights missing skills
6.Appreciates strong resumes when compatibility is high

🧠 System Architecture
Resume Text + Job Description
        ↓
Text Preprocessing (Cleaning, Stopwords Removal)
        ↓
TF-IDF Vectorization + Cosine Similarity
        ↓
Raw ML Match Score
        ↓
Confidence-based Normalization
        ↓
Final Compatibility Score
        ↓
Explainable AI Layer
(Missing Skills, Suggestions, Appreciation)



🔬 Technologies Used

⭐Python

⭐Scikit-learn

⭐NLTK

⭐TF-IDF Vectorizer

⭐Cosine Similarity

⭐Google Gemini (Explainable AI – API-ready design)

⭐Git & GitHub

⚠️ Note: Due to API availability constraints, the project demonstrates an offline Gemini-style explainability layer and is fully ready for live Gemini API integration.

📊 Key Features
1.Honest ML-based similarity scoring
2.Explainable skill overlap analysis
3.Resume improvement suggestions
4.Appreciation system for strong matches
5.Clean, modular, and version-controlled code


🧪 Example Output
Raw ML Match Score: 55.66%
Final Compatibility Score: 80.66%
🌟 Excellent Resume! Your profile strongly aligns with the job requirements.


Along with:-
1.Overlapping skills
2.Missing skills
3.Actionable suggestions

🏆 Why This Project Stands Out ⬇️
1.Separates ML prediction and AI explanation
2.Avoids inflated or fake scores
3.Demonstrates real ATS behavior
4.Easy to explain to judges and interviewers
5.Built incrementally with daily Git commits

🔮 Future Enhancements :-
1.PDF & image resume parsing using OCR
2.Semantic embeddings (Sentence-BERT / Gemini embeddings)\
3.Web or mobile application interface
4.Deployment using Google Cloud Run
5.Live Gemini API-powered explanations

