<<<<<<< HEAD
# Contributing to PromptX

Thank you for your interest in contributing to PromptX! 🎉

## How to Contribute

### 1. Fork the Repository
Click the "Fork" button at the top right of this page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/Prompt.ai.git
cd Prompt.ai
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Write clean, readable code
- Follow existing code style
- Test your changes thoroughly

### 5. Commit Your Changes
```bash
git add .
git commit -m "Add: your feature description"
```

### 6. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request
Go to the original repository and click "New Pull Request"

## Code Style

- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused
- Follow PEP 8 for Python code

## Reporting Bugs

Open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## Feature Requests

Open an issue with:
- Clear description of the feature
- Use case and benefits
- Possible implementation approach

## Questions?

Feel free to open an issue for any questions!

Thank you for contributing! 💜
=======
<div align="center">

<img src="frontend/Public/star.gif" width="400" alt="Contributing to PromptX"/>

# 🤝 Contributing to PromptX

### *Help us build the future of AI prompt engineering!*

<br>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![First Timers](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=for-the-badge)](https://www.firsttimersonly.com/)
[![Contributors](https://img.shields.io/github/contributors/yourusername/PromptX?style=for-the-badge)](https://github.com/yourusername/PromptX/graphs/contributors)

<br>

**Thank you for considering contributing to PromptX!** 🎉  
Every contribution, no matter how small, makes a difference.

---

</div>

<br>

## 📋 Table of Contents

- [🌟 Ways to Contribute](#-ways-to-contribute)
- [🚀 Getting Started](#-getting-started)
- [💻 Development Workflow](#-development-workflow)
- [📝 Commit Guidelines](#-commit-guidelines)
- [🎨 Code Style Guide](#-code-style-guide)
- [🧪 Testing](#-testing)
- [🐛 Bug Reports](#-bug-reports)
- [✨ Feature Requests](#-feature-requests)
- [📖 Documentation](#-documentation)
- [👥 Community](#-community)

<br>

---

## 🌟 Ways to Contribute

<div align="center">

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/code.svg" width="48" height="48"/>
<h3>💻 Code</h3>
<p>Fix bugs, add features, improve performance</p>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/book-open.svg" width="48" height="48"/>
<h3>📖 Docs</h3>
<p>Improve documentation, write tutorials</p>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/bug.svg" width="48" height="48"/>
<h3>🐛 Testing</h3>
<p>Report bugs, test features</p>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/lightbulb.svg" width="48" height="48"/>
<h3>💡 Ideas</h3>
<p>Suggest features, share feedback</p>
</td>
</tr>
</table>

</div>

<br>

---

## 🚀 Getting Started

### 📦 Prerequisites

```bash
✅ Python 3.8+
✅ Git
✅ Code editor (VS Code recommended)
✅ Basic knowledge of Flask & JavaScript
```

### 🔧 Setup Development Environment

```bash
# 1️⃣ Fork the repository
# Click "Fork" button at https://github.com/yourusername/PromptX

# 2️⃣ Clone your fork
git clone https://github.com/YOUR_USERNAME/PromptX.git
cd PromptX

# 3️⃣ Add upstream remote
git remote add upstream https://github.com/yourusername/PromptX.git

# 4️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 5️⃣ Install dependencies
pip install -r requirements.txt

# 6️⃣ Set up environment variables
cp .env.example .env
# Add your API keys to .env

# 7️⃣ Run the application
python3 app.py

# 8️⃣ Open frontend
# Visit http://localhost:5000 or open frontend/index.html
```

<br>

---

## 💻 Development Workflow

### 🌿 Branch Strategy

```bash
# Create a feature branch
git checkout -b feature/amazing-feature

# Create a bugfix branch
git checkout -b fix/bug-description

# Create a docs branch
git checkout -b docs/update-readme
```

**Branch Naming Convention:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions/updates
- `style/` - UI/UX improvements

### 🔄 Keep Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream changes
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

### ✅ Before Submitting PR

<div align="center">

| Step | Command | Description |
|------|---------|-------------|
| 1️⃣ | `git pull upstream main` | Sync with upstream |
| 2️⃣ | `python3 app.py` | Test locally |
| 3️⃣ | Check console | No errors |
| 4️⃣ | Test all features | Everything works |
| 5️⃣ | Review changes | Clean code |

</div>

<br>

---

## 📝 Commit Guidelines

### 🎯 Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 📌 Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(api): add quality heatmap endpoint` |
| `fix` | Bug fix | `fix(frontend): resolve loading spinner issue` |
| `docs` | Documentation | `docs(readme): update installation steps` |
| `style` | Code style/formatting | `style(css): improve button hover effects` |
| `refactor` | Code refactoring | `refactor(services): optimize AI fallback logic` |
| `test` | Add/update tests | `test(fallback): add unit tests for model switching` |
| `chore` | Maintenance | `chore(deps): update Flask to 3.0.0` |
| `perf` | Performance improvement | `perf(api): reduce response time by 30%` |

### ✨ Good Commit Examples

```bash
✅ feat(ab-test): add structured variation generator
✅ fix(api): handle empty prompt edge case
✅ docs(contributing): add commit guidelines section
✅ style(ui): improve mobile responsiveness
✅ refactor(services): extract prompt validation logic
```

### ❌ Bad Commit Examples

```bash
❌ fixed stuff
❌ update
❌ changes
❌ WIP
❌ asdfasdf
```

<br>

---

## 🎨 Code Style Guide

### 🐍 Python (Backend)

```python
# ✅ Good
def enhance_prompt(user_prompt: str, model: str = "gemini") -> dict:
    """
    Enhance user prompt using AI model.
    
    Args:
        user_prompt: Original user input
        model: AI model to use (default: gemini)
        
    Returns:
        dict: Enhanced prompt with metadata
    """
    if not user_prompt or not user_prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    return {
        "enhanced": enhanced_text,
        "model_used": model,
        "timestamp": datetime.now().isoformat()
    }

# ❌ Bad
def enhance(p,m="gemini"):
    if not p:return None
    return {"e":enhanced_text,"m":m}
```

**Python Guidelines:**
- ✅ Follow PEP 8
- ✅ Use type hints
- ✅ Write docstrings for functions
- ✅ Use meaningful variable names
- ✅ Keep functions under 50 lines
- ✅ Use f-strings for formatting

### 🌐 JavaScript (Frontend)

```javascript
// ✅ Good
async function enhancePrompt(userPrompt) {
    if (!userPrompt?.trim()) {
        showError('Prompt cannot be empty');
        return null;
    }
    
    try {
        const response = await fetch('/api/enhance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: userPrompt })
        });
        
        return await response.json();
    } catch (error) {
        console.error('Enhancement failed:', error);
        throw error;
    }
}

// ❌ Bad
async function enhance(p){
    let r=await fetch('/api/enhance',{method:'POST',body:JSON.stringify({prompt:p})})
    return r.json()
}
```

**JavaScript Guidelines:**
- ✅ Use `const`/`let`, avoid `var`
- ✅ Use async/await over callbacks
- ✅ Handle errors gracefully
- ✅ Use template literals
- ✅ Add JSDoc comments
- ✅ Use meaningful function names

### 🎨 CSS (Styling)

```css
/* ✅ Good */
.prompt-card {
    padding: 1.5rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease;
}

.prompt-card:hover {
    transform: translateY(-2px);
}

/* ❌ Bad */
.pc{padding:1.5rem;border-radius:12px;background:#667eea;}
```

**CSS Guidelines:**
- ✅ Use meaningful class names
- ✅ Follow BEM naming convention
- ✅ Group related properties
- ✅ Use CSS variables for colors
- ✅ Mobile-first approach
- ✅ Add comments for complex styles

<br>

---

## 🧪 Testing

### 🔍 Manual Testing Checklist

<div align="center">

| Feature | Test Case | Expected Result |
|---------|-----------|-----------------|
| ✨ Enhance | Enter prompt → Click enhance | Enhanced prompt appears |
| 📊 Quality | Click quality analysis | Heatmap with 6 scores |
| 🧪 A/B Test | Generate variations | 3 variations displayed |
| 💾 History | Save prompt | Appears in history panel |
| 🔄 Fallback | Disable Gemini API | Switches to OpenAI |

</div>

### 🤖 Testing Fallback System

```bash
# Run fallback tests
python3 test_fallback.py

# Expected output:
# ✅ Gemini test passed
# ✅ OpenAI fallback works
# ✅ DeepSeek fallback works
# ✅ HuggingFace fallback works
```

### 📝 Adding Tests

```python
# tests/test_services.py
def test_enhance_prompt_empty_input():
    """Test that empty prompts raise ValueError"""
    with pytest.raises(ValueError):
        enhance_prompt("")

def test_enhance_prompt_success():
    """Test successful prompt enhancement"""
    result = enhance_prompt("Write a blog post")
    assert "enhanced" in result
    assert len(result["enhanced"]) > 0
```

<br>

---

## 🐛 Bug Reports

### 📋 Before Reporting

- ✅ Search existing issues
- ✅ Test on latest version
- ✅ Check if it's already fixed
- ✅ Reproduce the bug

### 🎯 Bug Report Template

```markdown
## 🐛 Bug Description
Clear description of what the bug is.

## 📝 Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## ✅ Expected Behavior
What should happen.

## ❌ Actual Behavior
What actually happens.

## 📸 Screenshots
If applicable, add screenshots.

## 🖥️ Environment
- OS: [e.g., macOS 13.0]
- Browser: [e.g., Chrome 120]
- Python: [e.g., 3.11.0]
- PromptX Version: [e.g., 1.0.0]

## 📋 Additional Context
Any other relevant information.
```

<br>

---

## ✨ Feature Requests

### 💡 Feature Request Template

```markdown
## 🚀 Feature Description
Clear description of the feature.

## 🎯 Problem It Solves
What problem does this solve?

## 💭 Proposed Solution
How should it work?

## 🔄 Alternatives Considered
Other approaches you've thought about.

## 📊 Benefits
- Benefit 1
- Benefit 2

## 🎨 Mockups/Examples
Visual examples if applicable.
```

### 🌟 Feature Priority

| Priority | Label | Description |
|----------|-------|-------------|
| 🔥 | `priority: critical` | Security, data loss, crashes |
| ⚡ | `priority: high` | Major features, important bugs |
| 📌 | `priority: medium` | Nice-to-have features |
| 💡 | `priority: low` | Minor improvements |

<br>

---

## 📖 Documentation

### 📚 Documentation Types

<div align="center">

| Type | Location | Purpose |
|------|----------|---------|
| 📖 README | `README.md` | Project overview |
| 🤝 Contributing | `CONTRIBUTING.md` | Contribution guide |
| 📋 Changelog | `CHANGELOG.md` | Version history |
| 🔄 Fallback Guide | `docs/FALLBACK_GUIDE.md` | Multi-model setup |
| 📊 API Docs | `docs/API.md` | API reference |

</div>

### ✍️ Writing Guidelines

- ✅ Use clear, simple language
- ✅ Add code examples
- ✅ Include screenshots/diagrams
- ✅ Keep it up-to-date
- ✅ Use proper markdown formatting
- ✅ Add table of contents for long docs

<br>

---

## 👥 Community

### 💬 Communication Channels

<div align="center">

<table>
<tr>
<td align="center">
<a href="https://github.com/yourusername/PromptX/discussions">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/message-circle.svg" width="48" height="48"/>
<br>
<b>GitHub Discussions</b>
</a>
<br>
<sub>General questions & ideas</sub>
</td>
<td align="center">
<a href="https://github.com/yourusername/PromptX/issues">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/bug.svg" width="48" height="48"/>
<br>
<b>GitHub Issues</b>
</a>
<br>
<sub>Bug reports & features</sub>
</td>
<td align="center">
<a href="https://github.com/yourusername/PromptX/pulls">
<img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/git-pull-request.svg" width="48" height="48"/>
<br>
<b>Pull Requests</b>
</a>
<br>
<sub>Code contributions</sub>
</td>
</tr>
</table>

</div>

### 🎖️ Recognition

All contributors will be:
- ✅ Listed in README.md
- ✅ Mentioned in release notes
- ✅ Added to CONTRIBUTORS.md
- ✅ Credited in commit history

### 📜 Code of Conduct

We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/):

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers
- ✅ Accept constructive criticism
- ✅ Focus on what's best for the community
- ❌ No harassment or trolling
- ❌ No spam or self-promotion

<br>

---

## 🎁 First-Time Contributors

### 🌱 Good First Issues

Look for issues labeled:
- `good first issue` - Perfect for beginners
- `help wanted` - We need your help!
- `documentation` - Improve docs
- `beginner friendly` - Easy to start

### 📚 Resources for Beginners

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Contributions](https://github.com/firstcontributions/first-contributions)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Markdown Guide](https://www.markdownguide.org/)

<br>

---

## 🏆 Top Contributors

<div align="center">

<!-- This will be auto-generated -->
<a href="https://github.com/yourusername/PromptX/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/PromptX" />
</a>

<br><br>

**Thank you to all our amazing contributors!** 🎉

</div>

<br>

---

## 📄 License

By contributing to PromptX, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

<div align="center">

<br>

## 🙏 Thank You!

<br>

**Your contributions make PromptX better for everyone.** 💜

<br>

*Questions? Open an issue or start a discussion!*

<br>

---

<br>

**Made with 💜 by the PromptX Community**

<br>

</div>
