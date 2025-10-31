#!/bin/bash
echo "Installing Neuro AI Engine with Free Models..."

# Install Python dependencies
pip install transformers torch requests

# For faster performance (optional)
pip install accelerate

echo "✅ Neuro installation complete!"
echo "Run: python neuro_ai_engine.py"
