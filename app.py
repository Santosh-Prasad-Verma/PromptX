"""
Production Flask Application - Gemini Powered
Uses Google Gemini API instead of OpenAI
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from google import genai
from services import (
    detect_intent, apply_smart_template,
    analyze_quality_heatmap,
    generate_ab_variations, compare_variations,
    save_version, get_versions, get_version_diff,
    rollback_version, get_version_history_summary, compare_all_versions,
    get_client, generate_with_fallback
)

load_dotenv()

app = Flask(__name__)
CORS(app)

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
- Do not make it excessively verbose unless needed
- Use emojis strategically for visual appeal
- Structure with clear sections using headers and bullet points
- Make it visually scannable and professional"""

# ============================================================================
# CLASSIFICATION & SCORING (same as before)
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
# ENDPOINTS
# ============================================================================

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'version': '2.0.0', 'model': 'gemini-pro'})

@app.route('/api/enhance', methods=['POST'])
def enhance():
    try:
        data = request.json
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Prompt is required'}), 400
        
        prompt = data['prompt'].strip()
        if not prompt or len(prompt) > 5000:
            return jsonify({'error': 'Invalid prompt length'}), 400
        
        # Classify and score original
        classification = classify_prompt(prompt)
        original_score = score_prompt(prompt)
        
        # Use multi-model fallback
        full_prompt = f"{MASTER_PROMPT}\n\nUser prompt to enhance:\n{prompt}"
        result = generate_with_fallback(full_prompt, max_tokens=2000)
        enhanced = result['text']
        model_used = result['model']
        
        enhanced_score = score_prompt(enhanced)
        
        return jsonify({
            'success': True,
            'original': prompt,
            'enhanced': enhanced,
            'classification': classification,
            'original_score': original_score,
            'enhanced_score': enhanced_score,
            'improvement': round(enhanced_score['total'] - original_score['total'], 2),
            'model': model_used
        })
    
    except Exception as e:
        print(f"Error in enhance endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e), 'success': False}), 500

# ============================================================================
# ADVANCED FEATURES (Used by Frontend)
# ============================================================================

@app.route('/api/detect-intent', methods=['POST'])
def detect_prompt_intent():
    """Auto-detect prompt intent and suggest template"""
    try:
        data = request.json
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Prompt is required'}), 400
        
        prompt = data['prompt'].strip()
        intent_data = detect_intent(prompt)
        
        # Optionally apply template
        if data.get('apply_template', False):
            enhanced = apply_smart_template(prompt, intent_data)
            intent_data['enhanced_prompt'] = enhanced
        
        return jsonify({
            'success': True,
            'data': intent_data
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/quality-heatmap', methods=['POST'])
def quality_heatmap():
    """Get detailed quality heatmap analysis"""
    try:
        data = request.json
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Prompt is required'}), 400
        
        prompt = data['prompt'].strip()
        analysis = analyze_quality_heatmap(prompt)
        
        return jsonify({
            'success': True,
            'data': analysis
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ab-test', methods=['POST'])
def ab_test():
    """Generate 3 A/B test variations"""
    try:
        data = request.json
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Prompt is required'}), 400
        
        prompt = data['prompt'].strip()
        variations = generate_ab_variations(prompt)
        
        # Optionally include comparison
        if data.get('include_comparison', True):
            comparison = compare_variations(prompt, variations)
            return jsonify({
                'success': True,
                'data': comparison
            })
        
        return jsonify({
            'success': True,
            'data': {'variations': variations}
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# ============================================================================
# RUN
# ============================================================================

# Vercel serverless handler
app = app

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║       AI Prompt Enhancer - Gemini Powered 🌟              ║
║                   Version 2.0.0                           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

Server: http://localhost:{port}
Model: Google Gemini Pro

Endpoints:
  POST /api/enhance           - Enhance prompt
  POST /api/detect-intent     - Auto-detect intent
  POST /api/quality-heatmap   - Quality analysis
  POST /api/ab-test           - A/B variations
  GET  /health                - Health check

Press CTRL+C to stop
""")
    
    app.run(host='0.0.0.0', port=port, debug=True)
