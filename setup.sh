#!/bin/bash

# PromptX Setup Script
# This script helps you set up PromptX quickly

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║                  🎯 PromptX Setup Script                      ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Setup .env file
if [ ! -f ".env" ]; then
    echo "🔐 Setting up environment variables..."
    cp .env.example .env
    echo "✅ .env file created from .env.example"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys!"
    echo "   At least one API key is required (GEMINI_API_KEY recommended)"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

# Test fallback system
echo "🧪 Testing fallback system..."
python3 test_fallback.py
TEST_RESULT=$?
echo ""

if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ Fallback system is working!"
else
    echo "⚠️  Fallback test failed. Make sure you have valid API keys in .env"
fi
echo ""

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║                  ✅ Setup Complete!                           ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 To start the server:"
echo "   python3 app.py"
echo ""
echo "🌐 Then open frontend/index.html in your browser"
echo ""
echo "📚 Documentation: docs/QUICK_SUMMARY.md"
echo ""
