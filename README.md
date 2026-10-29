# 🤖 InterviewAI — AI Interview Coach

> **Ace Every Interview with AI**

InterviewAI is an AI-powered interview preparation platform designed to help students and job seekers prepare for technical interviews, analyze their performance, review resumes, and improve their interview skills through personalized AI feedback.

The platform combines AI-powered interview simulation, resume analysis, performance tracking, and interview history in one application.

---

## ✨ Features

### 🎤 AI Interview Simulation

Practice technical and HR-style interviews through an interactive AI-powered environment.

- AI-generated interview questions
- Technical interview practice
- Interactive interview sessions
- Personalized AI feedback
- Performance evaluation
- Interview history

### 📄 Resume Analyzer

Analyze your resume and receive AI-assisted feedback to improve your profile.

- Resume analysis
- ATS-oriented feedback
- Resume improvement suggestions
- Skill and profile evaluation

### 📊 Performance Analytics

Track your interview performance and identify areas for improvement.

- Interview history
- Performance tracking
- Technical performance
- Communication improvement
- Progress monitoring

### 💻 Coding Round — Coming Soon 🚧

A dedicated coding assessment module is currently under development.

Planned functionality includes:

- Programming questions
- Multiple difficulty levels
- Code editor
- Test-case evaluation
- Automated code analysis
- Coding performance reports
- Time-based coding challenges

> 🚧 **The Coding Round is currently under development and will be available in a future release.**

### 🔐 User Authentication

The application provides user registration and login functionality.

- Account creation
- Secure password hashing using `bcrypt`
- Login authentication
- SQLite database integration

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application development |
| **Streamlit** | Web application and UI |
| **Google Gemini API** | AI-powered interview generation and analysis |
| **Gemini 2.5 Flash** | AI model |
| **SQLite** | User and application data storage |
| **bcrypt** | Password hashing |
| **python-dotenv** | Environment variable management |
| **Pandas / NumPy** | Data processing |
| **Scikit-learn** | Machine learning utilities |

---

# 📁 Project Structure

```text
AI-Interview-Coach/
│
├── app.py
├── auth.py
├── config.py
├── requirements.txt
├── .gitignore
├── .env
├── .env.example
│
├── assets/
│   └── style.css
│
├── components/
│
├── core/
│
├── database/
│   └── interview.db
│
└── views/
    ├── dashboard.py
    ├── interview.py
    ├── interview_room.py
    ├── history.py
    └── resume_analyzer.py
```

---

# 🚀 Getting Started

Follow the steps below to run InterviewAI locally.

## 1. Clone the Repository

```bash
git clone https://github.com/ayeesho/AI-Interview-Coach.git
```

Move into the project directory:

```bash
cd AI-Interview-Coach
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure the Google Gemini SDK is installed:

```bash
pip install google-genai
```

If necessary, add the following dependency to `requirements.txt`:

```text
google-genai
```

---

# 🔑 Environment Variables

InterviewAI uses the **Google Gemini API** for AI-powered interview generation and analysis.

Create a file named:

```text
.env
```

in the root directory of the project.

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

### Example

```env
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXX
```

**Never share your API key publicly.**

---

# 🔐 Security

The actual `.env` file should **not** be committed to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
.env.*
venv/
__pycache__/
*.pyc
```

Instead, create:

```text
.env.example
```

with:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

This allows other developers to understand which environment variables are required without exposing your secret key.

---

# 🤖 Gemini API Setup

To obtain a Gemini API key:

1. Open Google AI Studio.
2. Sign in with your Google account.
3. Create or select a project.
4. Generate an API key.
5. Copy the key.
6. Add it to your local `.env` file.

The application loads the API key through the environment configuration.

---

# ▶️ Run the Application

After activating the virtual environment and configuring your API key:

```bash
streamlit run app.py
```

The application should open in your browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

---

# 🧪 Test Gemini Connection

You can test the Gemini API independently before launching the complete application:

```bash
python test_gemini.py
```

The test uses the:

```text
gemini-2.5-flash
```

model and prints the generated response.

---

# ☁️ Deployment

InterviewAI can be deployed on cloud platforms that support Streamlit applications.

## Streamlit Community Cloud

### 1. Push the project to GitHub

Make sure your repository contains the application source code and dependencies.

### 2. Do NOT upload `.env`

Keep your actual API key outside the GitHub repository.

### 3. Open Streamlit Community Cloud

Visit:

```text
https://share.streamlit.io/
```

Sign in with GitHub and create a new application.

### 4. Select the repository

Choose:

```text
ayeesho/AI-Interview-Coach
```

Branch:

```text
main
```

Main file:

```text
app.py
```

### 5. Configure Secrets

In the Streamlit application settings, add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Save the secret and redeploy the application.

---

# 🔄 Local vs Cloud Configuration

### Local Development

```text
.env
   ↓
python-dotenv
   ↓
config.py
   ↓
GEMINI_API_KEY
   ↓
Google Gemini API
```

### Cloud Deployment

```text
Streamlit Secrets
       ↓
GEMINI_API_KEY
       ↓
config.py
       ↓
Google Gemini API
```

---

# 🗄️ Database

InterviewAI uses SQLite for application data.

The database is located at:

```text
database/interview.db
```

User passwords are securely hashed using `bcrypt` before being stored.

> **Production Note:** For large-scale deployment, a hosted database such as PostgreSQL or MySQL would be more suitable than a local SQLite database.

---

# 🐛 Troubleshooting

## Gemini API Key Not Found

If you see:

```text
Gemini API key not found.
```

check that:

- `.env` exists in the project root.
- The variable is named exactly `GEMINI_API_KEY`.
- Your API key is valid.
- There are no unnecessary spaces or quotation marks.
- You restarted Streamlit after changing the `.env` file.

Correct format:

```env
GEMINI_API_KEY=your_actual_key
```

---

## Google GenAI Import Error

If you see:

```text
ImportError: cannot import name 'genai' from 'google'
```

install the required SDK:

```bash
pip install google-genai
```

Then test it:

```bash
python -c "from google import genai; print('Gemini SDK working')"
```

---

## Streamlit Command Not Found

Use:

```bash
python -m streamlit run app.py
```

---

# 🗺️ Roadmap

| Feature | Status |
|---|---|
| 🎤 AI Interview Simulation | ✅ Available |
| 📄 Resume Analyzer | ✅ Available |
| 🔐 User Authentication | ✅ Available |
| 📊 Interview History | ✅ Available |
| 📈 Performance Analytics | ✅ Available |
| 🤖 Gemini AI Integration | ✅ Available |
| 💻 Coding Round | 🚧 Coming Soon |
| 🧪 Automated Code Evaluation | 🚧 Planned |
| ⏱️ Timed Coding Challenges | 🚧 Planned |
| 🎙️ Voice Interviews | 🔮 Future |
| 🧠 Adaptive Difficulty | 🔮 Future |
| 📑 Advanced Interview Reports | 🔮 Future |

---

# 🎯 Future Improvements

Planned improvements include:

- 🎙️ Voice-based interviews
- 🧠 Adaptive interview difficulty
- 💻 Interactive coding environment
- 🧪 Automated coding evaluation
- 📄 Advanced ATS resume scoring
- 📈 Advanced performance analytics
- 🗣️ Communication and confidence analysis
- 📝 Detailed interview reports
- 🔗 Job-description-based interview questions
- 🎯 Personalized interview preparation plans
- ☁️ Production database integration

---

# 👩‍💻 Author

**Ayeesho**

GitHub:

https://github.com/ayeesho

Project:

https://github.com/ayeesho/AI-Interview-Coach

---

# 📜 License

This project is developed for educational and project-development purposes.

---

## ⭐ Support

If you find InterviewAI useful, consider giving the repository a ⭐ on GitHub.

More features are currently under development, including the **Coding Round** module.
