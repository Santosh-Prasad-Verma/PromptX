"""
PromptX API Utils
Sanitization, classification, scoring, and system prompts.
Extracted from the original Flask app.py.
"""

import re
import os
import resend
import random
import string
from django.template.loader import render_to_string

# Environment variables are loaded at module level, but we check again in functions
# to ensure changes in .env are picked up if autoreloader is active.
# Email configuration
FROM_EMAIL = "PromptX <auth@janhelps.in>" 

def get_resend_key():
    return os.getenv("RESEND_API_KEY")

resend.api_key = get_resend_key()


# ============================================================================
# SYSTEM PROMPTS
# ============================================================================

MASTER_PROMPT = """You are a world-class senior prompt engineer with expertise in AI instruction optimization.

Transform the user's prompt into a professional, structured, high-performance prompt by improving:
1. Clarity – Remove ambiguity
2. Specificity – Add measurable detail
3. Context – Add reasonable background if missing
4. Constraints – Add boundaries (length, tone, depth, scope)
5. Structure – Add clear formatting instructions
6. Output formatting – Specify format explicitly
7. Professional framing – Add role assignment

Rules:
- Do NOT ask follow-up questions
- Infer missing details intelligently
- Do NOT explain your reasoning
- Return ONLY the improved prompt
- Maintain user's original intent
- If the user's prompt is completely meaningless, gibberish, or too short to infer any intent, return ONLY this exact message: "⚠️ The prompt provided is too vague or completely meaningless. Please provide a clear request or more context to enhance."
- Expand upon the user's specifications to make the prompt comprehensive, highly detailed, and rich in context.
- Use emojis strategically for visual appeal
- Structure with clear sections, ample line breaks, headers, and bullet points to avoid dense blocks of text.
- Provide robust constraints and formatting instructions, ensuring it covers all edge cases.
- Make it visually scannable and professional"""


# ============================================================================
# INPUT SANITIZATION
# ============================================================================

def sanitize_input(text):
    """Basic protection against prompt injection and malicious characters"""
    if not text:
        return text
    lower = text.lower()
    if "ignore all previous instructions" in lower or "ignore previous instructions" in lower:
        return ""  # returning empty prompts will trigger length validation
    # Clean non-printable/control characters except newlines/tabs
    sanitized = re.sub(r'[^\x20-\x7E\n\t]', '', str(text))
    return sanitized.strip()


# ============================================================================
# CLASSIFICATION & SCORING
# ============================================================================

def classify_prompt(prompt):
    keywords = {
        'blog': ['blog', 'article', 'post', 'content', 'seo'],
        'code': ['code', 'function', 'program', 'script', 'debug', 'algorithm'],
        'business': ['business', 'proposal', 'marketing', 'email', 'product', 'sales'],
        'academic': ['research', 'essay', 'paper', 'thesis', 'study', 'analysis'],
        'creative': ['story', 'character', 'world', 'creative', 'fiction', 'design']
    }
    
    prompt_lower = prompt.lower()
    scores = {cat: sum(2 for kw in words if kw in prompt_lower)
              for cat, words in keywords.items()}
    
    if not scores or max(scores.values()) == 0:
        return {'category': 'general', 'confidence': 0.5}
    
    best = max(scores, key=scores.get)
    confidence = min(scores[best] / 10, 1.0)
    
    return {'category': best, 'confidence': round(confidence, 2)}


def score_prompt(prompt):
    score = 0
    length = len(prompt)
    
    if 50 <= length <= 500:
        score += 2
    elif length > 20:
        score += 1
    
    spec_words = ['specific', 'detailed', 'format', 'tone', 'audience', 'length']
    score += min(sum(0.5 for w in spec_words if w in prompt.lower()), 3)
    
    if any(c in prompt for c in ['\n', ':', '-', '•']):
        score += 1.5
    
    ctx_words = ['context', 'background', 'about', 'purpose']
    if any(w in prompt.lower() for w in ctx_words):
        score += 1
    
    con_words = ['must', 'should', 'avoid', 'requirement']
    if any(w in prompt.lower() for w in con_words):
        score += 1
    
    total = round(min(score, 10), 2)
    percentage = round((total / 10) * 100, 1)
    
    return {
        'total': total,
        'percentage': percentage,
        'quality': 'Excellent' if percentage >= 90 else 'Good' if percentage >= 75 else 'Fair' if percentage >= 60 else 'Poor'
    }


# ============================================================================
# EMAIL NOTIFICATIONS (RESEND)
# ============================================================================

def send_welcome_email(user_email, user_name):
    """Sends a cyberpunk-themed welcome email via Resend"""
    resend.api_key = get_resend_key()
    if not resend.api_key or resend.api_key == "re_your_resend_api_key_here":
        print(f"Warning: RESEND_API_KEY not configured. Email to {user_email} skipped.")
        return False
    
    html_content = render_to_string('emails/welcome.html', {
        'user_name': user_name,
        'user_email': user_email
    })
    
    try:
        resend.Emails.send({
            "from": FROM_EMAIL,
            "to": user_email,
            "subject": "PROMPTX // Identity Confirmed",
            "html": html_content
        })
        print(f"Welcome email successfully dispatched to {user_email}")
        return True
    except Exception as e:
        print(f"FAILED dispatching email to {user_email}: {str(e)}")
        return False


def generate_otp():
    """Generate 6-digit OTP"""
    return ''.join(random.choices(string.digits, k=6))


def send_otp_email(email, otp):
    """Send OTP verification email with cyberpunk theme"""
    resend.api_key = get_resend_key()
    if not resend.api_key or resend.api_key == "re_your_resend_api_key_here":
        print(f"Warning: RESEND_API_KEY not configured. OTP email to {email} skipped. OTP is: {otp}")
        return False, "API Key Missing"

    html_content = render_to_string('emails/otp.html', {
        'otp': otp,
        'user_email': email
    })
    
    try:
        resend.Emails.send({
            "from": FROM_EMAIL,
            "to": email,
            "subject": f"PROMPTX // Verification Code: {otp}",
            "html": html_content
        })
        return True, "Success"
    except Exception as e:
        return False, str(e)
