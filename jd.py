import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load dataset
file_path = r"E:\jd\Conversation.csv"  # path to your uploaded dataset
data = pd.read_csv(file_path, encoding="utf-8")

# Step 2: Automatically find text columns
text_columns = [col for col in data.columns if data[col].dtype == "object"]

if not text_columns:
    raise ValueError("No text columns found in dataset!")

# Combine all text columns into one list
text_data = []
for col in text_columns:
    text_data.extend(data[col].dropna().tolist())

# Step 3: Clean and prepare text data
text_data = [t.strip() for t in text_data if isinstance(t, str) and len(t.strip()) > 0]

if len(text_data) == 0:
    raise ValueError("No usable text found in dataset!")

# Step 4: Create TF-IDF model
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(text_data)

print(f"✅ Loaded {len(text_data)} sentences from your dataset.")
print("🤖 AI Clone ready! Type your message below (type 'exit' to quit)\n")

# Step 5: Generate AI responses (fixed version)
def generate_response(user_input):
    # Convert user input into vector
    user_vec = vectorizer.transform([user_input])

    # Compute similarity with dataset text
    similarities = cosine_similarity(user_vec, tfidf_matrix)
    best_match_idx = similarities.argmax()
    base_sentence = text_data[best_match_idx]

    # ✅ FIX: Return full matched sentence instead of jumbled words
    response = base_sentence.strip()

    # Add punctuation if missing
    if not response.endswith(('.', '!', '?')):
        response += '.'

    return response

# Step 6: Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Clone: Goodbye! Keep exploring your digital self. 🌱")
        break

    reply = generate_response(user_input)
    print("AI Clone:", reply)
