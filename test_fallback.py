#!/usr/bin/env python3
"""
Test script for multi-model fallback system
"""

import os
from dotenv import load_dotenv
from services import generate_with_fallback

load_dotenv()

def test_fallback():
    print("🧪 Testing Multi-Model Fallback System\n")
    print("=" * 60)
    
    # Check which API keys are available
    print("\n📋 Available API Keys:")
    keys = {
        'Gemini': os.getenv('GEMINI_API_KEY'),
        'OpenAI': os.getenv('OPENAI_API_KEY'),
        'DeepSeek': os.getenv('DEEPSEEK_API_KEY'),
        'HuggingFace': os.getenv('HUGGINGFACE_API_KEY')
    }
    
    for name, key in keys.items():
        status = "✅ Configured" if key else "❌ Missing"
        print(f"  {name}: {status}")
    
    # Test prompt
    test_prompt = "Write a short greeting message for a website."
    
    print(f"\n🎯 Test Prompt: '{test_prompt}'")
    print("\n⏳ Generating response with fallback...\n")
    
    try:
        result = generate_with_fallback(test_prompt, max_tokens=100)
        
        print("=" * 60)
        print(f"\n✅ SUCCESS!")
        print(f"\n🤖 Model Used: {result['model'].upper()}")
        print(f"\n📝 Response:\n{result['text']}")
        print("\n" + "=" * 60)
        
        return True
        
    except Exception as e:
        print("=" * 60)
        print(f"\n❌ FAILED!")
        print(f"\n⚠️  Error: {str(e)}")
        print("\n💡 Tip: Make sure at least one API key is configured in .env")
        print("\n" + "=" * 60)
        
        return False

if __name__ == "__main__":
    success = test_fallback()
    exit(0 if success else 1)
