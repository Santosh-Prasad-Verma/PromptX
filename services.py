"""  
Minimal services for PromptX - Multi-model fallback support
"""
from google import genai
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# ============================================================================
# MULTI-MODEL FALLBACK SYSTEM
# ============================================================================

class AIModelFallback:
    """Handles automatic fallback between AI models"""
    
    def __init__(self):
        self.models = [
            {'name': 'gemini', 'priority': 1},
            {'name': 'openai', 'priority': 2},
            {'name': 'deepseek', 'priority': 3},
            {'name': 'huggingface', 'priority': 4}
        ]
    
    def generate(self, prompt, max_tokens=2000):
        """Try models in order until one succeeds"""
        errors = []
        
        for model in self.models:
            try:
                result = self._call_model(model['name'], prompt, max_tokens)
                if result:
                    return {'text': result, 'model': model['name'], 'success': True}
            except Exception as e:
                errors.append(f"{model['name']}: {str(e)}")
                continue
        
        raise Exception(f"All models failed. Errors: {'; '.join(errors)}")
    
    def _call_model(self, model_name, prompt, max_tokens):
        """Call specific model"""
        if model_name == 'gemini':
            return self._call_gemini(prompt)
        elif model_name == 'openai':
            return self._call_openai(prompt, max_tokens)
        elif model_name == 'deepseek':
            return self._call_deepseek(prompt, max_tokens)
        elif model_name == 'huggingface':
            return self._call_huggingface(prompt, max_tokens)
    
    def _call_gemini(self, prompt):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")
        
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        return response.text.strip()
    
    def _call_openai(self, prompt, max_tokens):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")
        
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={'Authorization': f'Bearer {api_key}'},
            json={
                'model': 'gpt-3.5-turbo',
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': max_tokens
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    
    def _call_deepseek(self, prompt, max_tokens):
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found")
        
        response = requests.post(
            'https://api.deepseek.com/v1/chat/completions',
            headers={'Authorization': f'Bearer {api_key}'},
            json={
                'model': 'deepseek-chat',
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': max_tokens
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    
    def _call_huggingface(self, prompt, max_tokens):
        api_key = os.getenv('HUGGINGFACE_API_KEY')
        if not api_key:
            raise ValueError("HUGGINGFACE_API_KEY not found")
        
        response = requests.post(
            'https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct',
            headers={'Authorization': f'Bearer {api_key}'},
            json={'inputs': prompt, 'parameters': {'max_new_tokens': max_tokens, 'return_full_text': False}},
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0].get('generated_text', '').strip()
        return result.get('generated_text', '').strip()

# Global fallback instance
_fallback = AIModelFallback()

def get_client():
    """Legacy function - returns Gemini client"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment")
    return genai.Client(api_key=api_key)

def generate_with_fallback(prompt, max_tokens=2000):
    """Generate text with automatic model fallback"""
    return _fallback.generate(prompt, max_tokens)

# ============================================================================
# INTENT DETECTION
# ============================================================================

def detect_intent(prompt):
    """Detect prompt intent"""
    keywords = {
        'content': ['blog', 'article', 'write', 'content'],
        'code': ['code', 'function', 'program', 'debug'],
        'analysis': ['analyze', 'research', 'study'],
        'creative': ['story', 'creative', 'design']
    }
    
    prompt_lower = prompt.lower()
    for intent, words in keywords.items():
        if any(w in prompt_lower for w in words):
            return {
                'intent': intent,
                'confidence': 0.8,
                'tone': 'professional'
            }
    
    return {'intent': 'general', 'confidence': 0.5, 'tone': 'neutral'}

def apply_smart_template(prompt, intent_data):
    """Apply template based on intent"""
    return prompt  # Simple passthrough

# ============================================================================
# QUALITY ANALYZER
# ============================================================================

def analyze_quality_heatmap(prompt):
    """Analyze prompt quality"""
    length = len(prompt)
    
    # Calculate scores
    clarity = min(10, (length / 50) * 2)
    specificity = min(10, len(prompt.split()) / 10)
    structure = 8 if '\n' in prompt else 4
    context = 7 if length > 100 else 3
    constraints = 6 if any(w in prompt.lower() for w in ['must', 'should']) else 3
    output_format = 7 if any(w in prompt.lower() for w in ['format', 'structure']) else 4
    
    overall = round((clarity + specificity + structure + context + constraints + output_format) / 6, 1)
    
    # Generate suggestions
    suggestions = []
    if clarity < 5:
        suggestions.append({
            'category': 'Clarity',
            'issue': 'Prompt is too vague',
            'fix': 'Add specific details about what you want'
        })
    if specificity < 5:
        suggestions.append({
            'category': 'Specificity',
            'issue': 'Lacks specific requirements',
            'fix': 'Specify tone, length, and format'
        })
    
    grade = 'A' if overall >= 9 else 'B' if overall >= 7 else 'C' if overall >= 5 else 'D' if overall >= 3 else 'F'
    
    return {
        'overall': overall,
        'grade': grade,
        'metrics': {
            'clarity': {'score': round(clarity, 1)},
            'specificity': {'score': round(specificity, 1)},
            'structure': {'score': round(structure, 1)},
            'context': {'score': round(context, 1)},
            'constraints': {'score': round(constraints, 1)},
            'output_format': {'score': round(output_format, 1)}
        },
        'suggestions': suggestions
    }

# ============================================================================
# A/B TESTING
# ============================================================================

def generate_ab_variations(prompt):
    """Generate 3 variations with fallback"""
    try:
        # Concise version
        concise_prompt = f"Make this prompt concise and direct (max 100 words):\n{prompt}"
        concise_result = generate_with_fallback(concise_prompt, 500)
        concise = concise_result['text']
        
        # Detailed version
        detailed_prompt = f"Expand this prompt with comprehensive details:\n{prompt}"
        detailed_result = generate_with_fallback(detailed_prompt, 1000)
        detailed = detailed_result['text']
        
        # Structured version
        structured_prompt = f"Rewrite this prompt with clear structure and sections:\n{prompt}"
        structured_result = generate_with_fallback(structured_prompt, 1000)
        structured = structured_result['text']
        
        return {
            'concise': {'text': concise, 'length': len(concise), 'model': concise_result['model']},
            'detailed': {'text': detailed, 'length': len(detailed), 'model': detailed_result['model']},
            'structured': {'text': structured, 'length': len(structured), 'model': structured_result['model']}
        }
    except Exception as e:
        return {
            'concise': {'text': prompt, 'length': len(prompt), 'model': 'fallback'},
            'detailed': {'text': prompt, 'length': len(prompt), 'model': 'fallback'},
            'structured': {'text': prompt, 'length': len(prompt), 'model': 'fallback'}
        }

def compare_variations(original, variations):
    """Compare variations and recommend best"""
    # Score each variation
    for key in variations:
        quality = analyze_quality_heatmap(variations[key]['text'])
        variations[key]['quality'] = quality
    
    # Find best
    best = max(variations.keys(), key=lambda k: variations[k]['quality']['overall'])
    
    return {
        'variations': variations,
        'recommendation': {
            'best_variation': best,
            'reason': f'{best.capitalize()} version has the highest quality score'
        }
    }

# ============================================================================
# VERSION CONTROL (Stub - not used by frontend)
# ============================================================================

def save_version(prompt_id, prompt_text, metadata):
    return {'version': 1, 'saved': True}

def get_versions(prompt_id):
    return []

def get_version_diff(prompt_id, v1, v2):
    return {'diff': 'No changes'}

def rollback_version(prompt_id, version):
    return {'rolled_back': True}

def get_version_history_summary(prompt_id):
    return {'total_versions': 0}

def compare_all_versions(prompt_id):
    return {'versions': []}
