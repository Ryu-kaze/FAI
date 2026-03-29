from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model():
    # Sample enterprise documents
    documents = [
        "cloud computing deployment architecture",
        "financial quarterly earnings report",
        "hospital patient treatment protocols",
        "software engineering development lifecycle",
        "corporate finance investment strategy"
    ]

    labels = ["technical", "finance", "health", "technical", "finance"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)

    model = MultinomialNB()
    model.fit(X, labels)

    return vectorizer, model


def classify_query(vectorizer, model, query):
    try:
        if not query.strip():
            raise ValueError("Query cannot be empty.")

        query_vec = vectorizer.transform([query])
        prediction = model.predict(query_vec)[0]

        print("\n--- Document Retrieval Result ---")
        print("Query:", query)
        print("Predicted document category:", prediction)

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("System Error:", e)


# --------- Main Program ---------
vectorizer, model = train_model()

while True:
    try:
        user_query = input("Enter SharePoint search query: ")

        classify_query(vectorizer, model, user_query)
        break

    except Exception as e:
        print("Unexpected Error:", e)
