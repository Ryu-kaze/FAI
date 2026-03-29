from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model():
    # Sample resume data
    texts = [
        "python machine learning data analysis",
        "financial accounting auditing taxation",
        "nursing patient care hospital management",
        "software development cloud computing",
        "investment banking corporate finance"
    ]

    labels = ["technical", "finance", "health", "technical", "finance"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = MultinomialNB()
    model.fit(X, labels)

    return vectorizer, model


def classify_resume(vectorizer, model, resume):
    try:
        if not resume.strip():
            raise ValueError("Resume description cannot be empty.")

        resume_vec = vectorizer.transform([resume])
        prediction = model.predict(resume_vec)[0]

        print("\n--- Resume Screening Result ---")
        print("Input Description:", resume)
        print("Predicted Category:", prediction)

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("System Error:", e)


# --------- Main Program ---------
vectorizer, model = train_model()

while True:
    try:
        user_input = input("Enter applicant description: ")

        classify_resume(vectorizer, model, user_input)
        break

    except Exception as e:
        print("Unexpected Error:", e)
