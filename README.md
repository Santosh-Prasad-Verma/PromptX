<div align="center">

<img src="frontend/Public/star.gif" width="650" alt="PromptX Banner"/>

# 🎯 PromptX

### ✨ AI-Powered Prompt Enhancement Platform ✨

*Transform simple prompts into professional, AI-optimized instructions*

<br>

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Powered by Gemini](https://img.shields.io/badge/Powered%20by-Gemini%202.0-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br>

**[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📖 Usage](#-usage) • [🛠️ Tech Stack](#️-tech-stack) • [📡 API](#-api-endpoints)**

---

</div>

<br>

## 🌟 Why PromptX?

> **Stop struggling with vague prompts.** PromptX uses Google Gemini 2.0 to transform your basic prompts into professional, structured instructions that get better AI responses.

<br>

## ✨ Features

<div align="center">

<table>
<tr>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/sparkles.svg" width="48" height="48"/>
<h3>🤖 AI Enhancement</h3>
<p>Powered by Gemini 2.0 Flash for lightning-fast prompt optimization</p>
</td>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/activity.svg" width="48" height="48"/>
<h3>📊 Quality Analysis</h3>
<p>6-dimension scoring with beautiful visual heatmaps</p>
</td>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/git-compare.svg" width="48" height="48"/>
<h3>🧪 A/B Testing</h3>
<p>Generate 3 variations: Concise, Detailed & Structured</p>
</td>
</tr>
<tr>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/target.svg" width="48" height="48"/>
<h3>🎯 Intent Detection</h3>
<p>Auto-detect prompt intent, tone & confidence level</p>
</td>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/clock.svg" width="48" height="48"/>
<h3>💾 History Management</h3>
<p>Save and reuse your best prompts locally</p>
</td>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/zap.svg" width="48" height="48"/>
<h3>⚡ Lightning Fast</h3>
<p>Minimal dependencies, instant responses</p>
</td>
<td width="33%" align="center">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/shield-check.svg" width="48" height="48"/>
<h3>🔄 Auto Fallback</h3>
<p>Switches to backup AI models automatically</p>
</td>
</tr>
</table>

</div>

<br>

---

## 🚀 Quick Start

<div align="center">

### 📋 Prerequisites

```bash
✅ Python 3.8+
✅ Google Gemini API Key (Get free at ai.google.dev)
```

</div>

### 🔧 Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/PromptX.git
cd PromptX

# 2️⃣ Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# 5️⃣ Start the server
python3 app.py

# 6️⃣ Open frontend in browser
open frontend/index.html  # Or visit http://localhost:5000
```

**⚡ Or use the one-line startup:**
```bash
./start.sh
```

<br>

---

## 📁 Project Structure

```
Prompt.ai/
├── 📂 frontend/              # Frontend application
│   ├── index.html           # Main UI
│   ├── index.css            # Styles
│   ├── index.js             # JavaScript logic
│   └── Public/              # Static assets
│       ├── bob.gif          # Animated logo
│       ├── favicon.svg      # Favicon
│       └── star.svg         # Alternative icon
├── 📂 docs/                 # Documentation
│   ├── FALLBACK_GUIDE.md    # Multi-model fallback guide
│   ├── QUICK_SUMMARY.md     # Quick reference
│   └── VISUAL_GUIDE.md      # Visual diagrams
├── ⚙️ app.py                # Flask backend server
├── 🤖 services.py           # AI services & fallback logic
├── 📦 requirements.txt      # Python dependencies
├── 🧪 test_fallback.py      # Fallback system test
├── 🚀 start.sh              # Quick startup script
├── 🔐 .env.example          # Environment template
├── 📖 README.md             # Main documentation
├── 📝 CONTRIBUTING.md       # Contribution guidelines
├── 📋 CHANGELOG.md          # Version history
└── 📄 LICENSE               # MIT License
```

---

## 🎨 Usage

<div align="center">

<table>
<tr>
<td width="25%" align="center">
<h3>1️⃣</h3>
<h4>✨ Enhance</h4>
<p>Enter your basic prompt → Get AI-enhanced version</p>
</td>
<td width="25%" align="center">
<h3>2️⃣</h3>
<h4>📊 Analyze</h4>
<p>Get quality breakdown across 6 dimensions</p>
</td>
<td width="25%" align="center">
<h3>3️⃣</h3>
<h4>🧪 Compare</h4>
<p>Generate 3 A/B variations</p>
</td>
<td width="25%" align="center">
<h3>4️⃣</h3>
<h4>💾 History</h4>
<p>Browse and reuse saved prompts</p>
</td>
</tr>
</table>

</div>

<br>

---

## 📡 API Endpoints

<div align="center">

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| `GET` | `/health` | Health check | ✅ Active |
| `POST` | `/api/enhance` | Enhance prompt with AI | ✅ Active |
| `POST` | `/api/detect-intent` | Auto-detect intent & tone | ✅ Active |
| `POST` | `/api/quality-heatmap` | Quality analysis with scores | ✅ Active |
| `POST` | `/api/ab-test` | Generate 3 A/B variations | ✅ Active |

</div>

<br>

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technology |
|----------|-----------|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Backend** | Flask (Python) |
| **AI Model** | Google Gemini 2.0 Flash |
| **Storage** | LocalStorage (Browser) |
| **Icons** | Lucide Icons |
| **Fonts** | Inter, Orbitron |

</div>

---

## 📊 Quality Scoring Dimensions

<div align="center">

<table>
<tr>
<td align="center" width="33%">
<h3>🎯</h3>
<h4>Clarity</h4>
<p>Remove ambiguity</p>
</td>
<td align="center" width="33%">
<h3>🔍</h3>
<h4>Specificity</h4>
<p>Add details</p>
</td>
<td align="center" width="33%">
<h3>🏗️</h3>
<h4>Structure</h4>
<p>Organize content</p>
</td>
</tr>
<tr>
<td align="center" width="33%">
<h3>📝</h3>
<h4>Context</h4>
<p>Background info</p>
</td>
<td align="center" width="33%">
<h3>⚖️</h3>
<h4>Constraints</h4>
<p>Define boundaries</p>
</td>
<td align="center" width="33%">
<h3>📋</h3>
<h4>Format</h4>
<p>Specify output</p>
</td>
</tr>
</table>

*Each dimension scored 0-10 with actionable suggestions*

</div>

<br>

---

## 🔒 Environment Setup

Create a `.env` file in the root directory:

```env
# Primary AI Model (Required)
GEMINI_API_KEY=your_gemini_api_key_here

# Fallback Models (Optional - for automatic switching)
OPENAI_API_KEY=your_openai_key_here
DEEPSEEK_API_KEY=your_deepseek_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here

# Server Config
PORT=5000
```

**Get your free API keys:**
- **Gemini** (Primary): [ai.google.dev](https://ai.google.dev/)
- **OpenAI** (Fallback): [platform.openai.com](https://platform.openai.com/)
- **DeepSeek** (Fallback): [platform.deepseek.com](https://platform.deepseek.com/)
- **HuggingFace** (Fallback): [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 🔄 Multi-Model Fallback

PromptX automatically switches between AI models if one fails:

```
Gemini → OpenAI → DeepSeek → HuggingFace
```

**Benefits:**
- ✅ Never worry about API quota limits
- ✅ Automatic failover on errors
- ✅ See which model powered each response
- ✅ Works with just one API key (others optional)

📖 **[Read Full Fallback Guide →](docs/FALLBACK_GUIDE.md)**

---

## 🐛 Troubleshooting

<details>
<summary><b>❌ Server won't start</b></summary>

- Check if `.env` file exists with valid `GEMINI_API_KEY`
- Ensure Python 3.8+ is installed: `python3 --version`
- Install dependencies: `pip install -r requirements.txt`
</details>

<details>
<summary><b>❌ Frontend not connecting</b></summary>

- Verify backend is running on `http://localhost:5000`
- Check browser console for errors (F12)
- Ensure CORS is enabled (it is by default)
</details>

<details>
<summary><b>❌ API errors</b></summary>

- Verify your Gemini API key is valid
- Check API quota limits
- Review server logs for detailed errors
</details>

---

## 📈 Performance

<div align="center">

| Metric | Value |
|--------|-------|
| ⚡ **Response Time** | < 2 seconds average |
| 💾 **Bundle Size** | ~50KB (code only) |
| 📦 **Dependencies** | Only 4 packages |
| 🚀 **Startup Time** | < 3 seconds |

</div>

<br>

---

## 🎯 Roadmap

<div align="center">

| Feature | Status |
|---------|--------|
| 🔄 Multi-model fallback system | ✅ Complete |
| 📤 Export prompts to JSON/CSV | 🔜 Coming Soon |
| 📚 Prompt templates library | 🔜 Coming Soon |
| 🤖 Add Claude (Anthropic) support | 💡 Planned |
| 👥 Team collaboration features | 💡 Planned |
| 🔌 Chrome extension | 💡 Planned |
| 📱 Mobile app | 💡 Planned |

</div>

<br>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- 🤖 **Google Gemini** team for the amazing AI model
- 🌐 **Flask** community for the lightweight framework
- 🎨 **Lucide Icons** for beautiful icons
- 💜 **Open Source** community for inspiration

---

## 📞 Support & Contact

<div align="center">

<table>
<tr>
<td align="center">
<a href="https://github.com/yourusername/PromptX/issues">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/bug.svg" width="32" height="32"/>
<br>
<b>Report Bug</b>
</a>
</td>
<td align="center">
<a href="https://github.com/yourusername/PromptX/discussions">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/message-circle.svg" width="32" height="32"/>
<br>
<b>Discussions</b>
</a>
</td>
<td align="center">
<a href="https://github.com/yourusername/PromptX">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/git-pull-request.svg" width="32" height="32"/>
<br>
<b>Contribute</b>
</a>
</td>
</tr>
</table>

<br>

---

<br>

### ⭐ Star this repo if you find it helpful!

<br>

**Made with 💜 by the PromptX Team**

*Transform your prompts. Transform your results.*

<br>

</div>k
- 🎨 **Lucide Icons** for beautiful icons
- 💜 **Open Source** community for inspiration

---

## 📞 Support & Contact

<div align="center">

<table>
<tr>
<td align="center">
<a href="https://github.com/yourusername/Prompt.ai/issues">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/bug.svg" width="32" height="32"/>
<br>
<b>Report Bug</b>
</a>
</td>
<td align="center">
<a href="https://github.com/yourusername/Prompt.ai/discussions">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/message-circle.svg" width="32" height="32"/>
<br>
<b>Discussions</b>
</a>
</td>
<td align="center">
<a href="https://github.com/yourusername/Prompt.ai">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/git-pull-request.svg" width="32" height="32"/>
<br>
<b>Contribute</b>
</a>
</td>
</tr>
</table>

<br>

---

<br>

### ⭐ Star this repo if you find it helpful!

<br>

**Made with 💜 by the PromptX**

*Transform your prompts. Transform your results.*

<br>

</div>
