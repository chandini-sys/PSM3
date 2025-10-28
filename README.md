👇

🤖 AI Clone – Adaptive Digital Self
📘 Overview

AI Clone is an intelligent conversational system that learns from your digital footprint — such as messages, writing style, or datasets — to simulate your reasoning, communication, and values.
This project demonstrates how an AI-powered digital self can interact naturally with users while ensuring ethical handling of data and privacy.

🚀 Features

🧠 Text Understanding: Uses TF-IDF and cosine similarity to find the most contextually relevant sentence from your dataset.

💬 Dual Modes:

Chat Mode: Gives short, human-like replies for everyday conversation.

Story Mode: Generates creative stories (e.g., horror, thriller, fantasy) using GPT-2.

⚙️ AI Model: Integrates Hugging Face’s GPT-2 Medium model for creative, context-aware text generation.

🔒 Privacy Safe: Works offline, using only anonymized text data.

📊 Accuracy Display: Shows similarity percentage between input and dataset.

🧩 Architecture

Dataset Loading: Reads text data from a CSV file (Conversation.csv).

Preprocessing: Cleans and merges all text columns into a unified corpus.

Feature Extraction: Builds a TF-IDF model to represent textual semantics.

Similarity Matching: Finds the dataset sentence most related to the user’s query.

Response Generation: Uses GPT-2 to create coherent, human-like responses.

Mode Selection: User chooses between Chat or Story mode for different outputs.

🛠️ Tech Stack
Component	Technology Used
Language	Python 3
Libraries	pandas, scikit-learn, torch, transformers
Model	GPT-2 Medium (Hugging Face Transformers)
Interface	Command Line (IDLE/Terminal)
📂 Project Structure
AI_Clone/
│
├── Conversation.csv            # Dataset file
├── ai_clone.py                 # Main Python script
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation

🧠 How It Works

User provides a dataset (e.g., Conversation.csv) containing text samples.

TF-IDF finds semantic similarity between user input and dataset sentences.

GPT-2 generates a coherent reply or story continuation.

The output is displayed with a similarity accuracy percentage.

▶️ How to Run
Step 1: Install Dependencies
pip install pandas scikit-learn torch transformers

Step 2: Run the Script
python ai_clone.py

Step 3: Choose Mode

Type chat or story when prompted:

Choose mode ('chat' for short replies, 'story' for creative writing): chat


Then start interacting:

You: hello
AI Clone (71.6% match): Hey there! How are you today?

📈 Sample Outputs
🗣️ Chat Mode
You: how are you?
AI Clone (73.4% match): I'm doing great! Just training my neural networks 😊

👻 Story Mode
