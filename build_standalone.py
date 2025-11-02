#!/usr/bin/env python3
"""
Build standalone Neuro executable
No Python installation required to run!
"""

import subprocess
import sys
import os
from pathlib import Path

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_pyinstaller():
    """Install PyInstaller"""
    print("Installing PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print("✓ PyInstaller installed")

def build_executable():
    """Build standalone Neuro executable"""
    
    if not check_pyinstaller():
        install_pyinstaller()
    
    print("\n🔨 Building standalone Neuro executable...")
    print("This creates a .exe that works WITHOUT Python installed!")
    print("=" * 50)
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable
        "--name=neuro",                 # Output name
        "--clean",                      # Clean build
        "--noconfirm",                  # Overwrite without asking
        "--add-data=src;src",          # Include source code
        "--add-data=examples;examples", # Include examples
        "--hidden-import=dotenv",      # Include hidden imports
        "--hidden-import=neuro.interpreter",
        "--hidden-import=neuro.parser",
        "--hidden-import=neuro.ai_engine",
        "neuro"                        # Main script
    ]
    
    print(f"\nRunning: {' '.join(cmd)}\n")
    
    try:
        subprocess.check_call(cmd)
        
        print("\n" + "=" * 50)
        print("✓ BUILD SUCCESSFUL!")
        print("=" * 50)
        print("\nStandalone executable created:")
        print("  Location: dist/neuro.exe")
        print("  Size: ~10-20 MB")
        print("\nUsage:")
        print("  dist\\neuro.exe my_job_search.neuro")
        print("\nThis .exe works on ANY Windows machine")
        print("WITHOUT Python installed!")
        print("\nTo distribute:")
        print("  1. Copy dist/neuro.exe to any Windows machine")
        print("  2. Run: neuro.exe your_file.neuro")
        print("  3. That's it! No Python needed!")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure Python is in PATH")
        print("2. Try: pip install pyinstaller --upgrade")
        print("3. Run as administrator if permission errors")

if __name__ == "__main__":
    print("🧠 Neuro Standalone Builder")
    print("Creating native executable with NO Python dependency\n")
    
    build_executable()

