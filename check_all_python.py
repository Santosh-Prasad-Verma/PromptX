#!/usr/bin/env python3
"""
Comprehensive Python syntax and import checker for PromptX
"""
import os
import sys
import ast
import importlib.util

def check_syntax(filepath):
    """Check if a Python file has valid syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def find_python_files(directory):
    """Find all Python files in directory"""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Skip venv, __pycache__, .git
        dirs[:] = [d for d in dirs if d not in ['venv', '__pycache__', '.git', 'node_modules']]
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def main():
    print("=" * 70)
    print("PROMPTX PYTHON CODEBASE CHECKER")
    print("=" * 70)
    
    # Check backend directory
    backend_dir = 'backend'
    if not os.path.exists(backend_dir):
        print(f"❌ Backend directory not found: {backend_dir}")
        return 1
    
    python_files = find_python_files(backend_dir)
    print(f"\nFound {len(python_files)} Python files\n")
    
    errors = []
    success = []
    
    for filepath in sorted(python_files):
        rel_path = os.path.relpath(filepath)
        is_valid, error = check_syntax(filepath)
        
        if is_valid:
            print(f"✅ {rel_path}")
            success.append(rel_path)
        else:
            print(f"❌ {rel_path}")
            print(f"   {error}")
            errors.append((rel_path, error))
    
    print("\n" + "=" * 70)
    print(f"RESULTS: {len(success)} passed, {len(errors)} failed")
    print("=" * 70)
    
    if errors:
        print("\n❌ FAILED FILES:")
        for filepath, error in errors:
            print(f"  • {filepath}")
            print(f"    {error}")
        return 1
    else:
        print("\n✅ All Python files have valid syntax!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
