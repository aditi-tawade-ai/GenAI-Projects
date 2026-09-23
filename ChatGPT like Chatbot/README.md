# 🤖 ChatGPT-like Chatbot

A simple **ChatGPT-like chatbot** built using **Python, OpenAI API, and Streamlit**. 🚀

This project demonstrates how to connect a Python application with the OpenAI API and create an interactive chatbot interface using Streamlit.

---

## ✨ Features

- 💬 Interactive chat interface
- 🤖 Uses OpenAI API to generate responses
- 🧠 Maintains conversation history during the session
- ⚡ Streaming responses for a ChatGPT-like experience
- 🔐 Secure API key management using `.env`
- 🖥️ Simple and beginner-friendly Streamlit interface

---

## 🛠️ Technologies Used

- 🐍 Python
- 🤖 OpenAI API
- 🎈 Streamlit
- 🔑 python-dotenv

---

## 📂 Project Structure

```text
ChatGPT-like-chatbot/
│
├── 🐍 4_chatbot_OpenAI.py
├── 📦 requirements.txt
├── 🚫 .gitignore
└── 📖 README.md

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
```

### 2️⃣ Navigate to the Chatbot Folder

```bash
cd ChatGPT-like-chatbot
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 4️⃣ Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

Create a `.env` file inside the project folder.

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Never upload your `.env` file or expose your API key publicly.**

---

## ▶️ Run the Application

Run the following command:

```bash
streamlit run 4_chatbot_OpenAI.py
```

🌐 The Streamlit application will open in your browser.

---

## 🧠 How It Works

The application follows these steps:

1. 🔑 Loads the OpenAI API key from the `.env` file.
2. 🔌 Creates an OpenAI client.
3. 💾 Initializes chat history using Streamlit session state.
4. 💬 Accepts user input through the chat interface.
5. 📤 Sends the conversation history to the OpenAI model.
6. ⚡ Streams the generated response to the user.
7. 💾 Stores the response in the conversation history.

---

## 🤖 Model Used

The chatbot uses:

```text
gpt-4o-mini
```

---

## 🎯 Learning Objectives

This project helped me understand the basics of:

- 🤖 OpenAI API integration
- 🔐 API key management
- 🌱 Environment variables
- 🎈 Streamlit chat components
- 💾 Session state
- 💬 Conversation history
- ⚡ Streaming LLM responses

---

## 🚀 Future Improvements

Possible improvements include:

- 🧹 Add a **Clear Chat** button
- 🤖 Add **model selection**
- 🎯 Add customizable **system prompts**
- 📁 Add **file upload** functionality
- 💾 Add conversation export
- 🌐 Deploy the chatbot online

---

## 👩‍💻 Author

**Aditi Tawade**

🎓 GenAI Learning Project  
🤖 Exploring Generative AI, LLMs & AI Applications
