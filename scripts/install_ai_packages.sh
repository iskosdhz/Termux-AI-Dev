#!/data/data/com.termux/files/usr/bin/bash

echo "🤖 Installing AI Packages for Termux..."
echo "========================================"

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "❌ Please activate virtual environment first:"
    echo "source ai-env/bin/activate"
    exit 1
fi

# Machine Learning packages
echo "📦 Installing Machine Learning packages..."
pip install scikit-learn tensorflow-cpu keras

# NLP packages
echo "📦 Installing NLP packages..."
pip install nltk transformers torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Computer Vision packages
echo "📦 Installing Computer Vision packages..."
pkg install -y libjpeg-turbo libpng
LDFLAGS="-L/system/lib64" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install pillow opencv-python-headless

# Utilities
echo "📦 Installing utilities..."
pip install jupyterlab flask requests beautifulsoup4

echo "✅ All AI packages installed successfully!"
echo "🎉 Your Termux is now AI-powered!"


