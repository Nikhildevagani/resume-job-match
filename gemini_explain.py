from MLpreprocess import preprocess_text
from similarity import calculate_match_score


# ---------- Utility Functions ----------

def extract_keywords(text):
    return set(preprocess_text(text).split())


def adjusted_score(raw_score):
    """
    Confidence-based normalization for user-facing score.
    Raw ML score remains untouched.
    """
    if raw_score >= 50:
        return min(raw_score + 25, 95)
    elif raw_score >= 30:
        return raw_score + 15
    else:
        return raw_score


def appreciation_message(final_score):
    if final_score >= 80:
        return "🌟 Excellent Resume! Your profile strongly aligns with the job requirements and demonstrates solid technical relevance."
    elif final_score >= 60:
        return "✅ Good Resume! Your profile matches many of the job requirements, with minor scope for improvement."
    else:
        return "⚠️ Resume needs improvement to better align with the job requirements."


# ---------- Explainable AI Logic ----------

def explain_match(resume_text, job_text, raw_score):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    common_skills = resume_keywords & job_keywords
    missing_skills = job_keywords - resume_keywords

    explanation = f"""
Explanation:
The resume matches {raw_score}% of the job requirements based on TF-IDF and cosine similarity.
The overlapping skills include: {', '.join(list(common_skills)[:5]) if common_skills else 'very few common skills'}.

Missing Skills:
{chr(10).join(['- ' + skill for skill in list(missing_skills)[:5]]) if missing_skills else '- No major skills missing'}

Suggestions:
- Add projects related to missing skills
- Highlight relevant technical keywords
- Include measurable ML results and evaluation metrics
"""
    return explanation


# ---------- Main Execution ----------

if __name__ == "__main__":
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()

    with open("job_description.txt", "r", encoding="utf-8") as f:
        job = f.read()

    # Raw ML score
    raw_score = calculate_match_score(resume, job)

    # Adjusted user-facing score
    final_score = adjusted_score(raw_score)

    # Generate explanation & appreciation
    explanation = explain_match(resume, job, raw_score)
    appreciation = appreciation_message(final_score)

    # ---------- Output ----------
    print("\n=== Resume–Job Match Result ===\n")
    print(f"Raw ML Match Score: {raw_score}%")
    print(f"Final Compatibility Score: {final_score}%\n")
    print(appreciation)

    print("\n=== Explainable AI Output ===\n")
    print(explanation)
