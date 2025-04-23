# 🧠 Mental Health Companion

![Mental Health Support](https://images.unsplash.com/photo-1544027993-37dbfe43562a?w=800&auto=format&fit=crop&q=80)

A modern, AI-powered mental health companion designed to provide personalized support and guidance for individuals navigating mental health challenges in the digital age.

## 🌟 Features

### 1. Personalized Assessment
![Assessment](https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=800&auto=format&fit=crop&q=80)
- Comprehensive questionnaire
- Individual need analysis
- Tailored recommendations

### 2. AI Companion
![AI Support](https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=800&auto=format&fit=crop&q=80)
- 24/7 supportive chat
- Evidence-based guidance
- Emotional support

### 3. Goal Tracking
![Goal Tracking](https://images.unsplash.com/photo-1434626881859-194d67b2b86f?w=800&auto=format&fit=crop&q=80)
- Progress monitoring
- Customized strategies
- Regular check-ins

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mental-chatbot.git
cd mental-chatbot
```

2. Create a virtual environment (recommended):
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Watchdog for better performance (recommended):
```bash
# On macOS
xcode-select --install
pip install watchdog

# On Windows/Linux
pip install watchdog
```

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## 📱 Application Flow

1. **Home Page**
   - Welcome screen
   - Project overview
   - Quick navigation

2. **About Us**
   - Detailed project information
   - Key features
   - Goals and objectives

3. **Assessment**
   - Personal information
   - Mental health assessment
   - Support preferences

4. **Chat Interface**
   - AI-powered conversations
   - Personalized support
   - Progress tracking

## 🛠️ Project Structure

```
mental-chatbot/
├── app.py                    # Main application file
├── requirements.txt          # Project dependencies
├── README.md                # Project documentation
├── LICENSE                  # MIT License
├── data/
│   ├── questions.json       # Assessment questions
│   └── responses/           # User response storage
└── pages/
    ├── 01_AboutUs.py       # About page
    ├── 02_Assessment.py    # Assessment form
    └── 03_Chat.py          # Chat interface
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This application is not a substitute for professional mental health treatment. If you're experiencing severe distress, please contact a mental health professional or emergency services.

## 🙏 Acknowledgments

- Images from [Unsplash](https://unsplash.com)
- Built with [Streamlit](https://streamlit.io)

---

<div align="center">
Made with ❤️ for better mental health
</div> 