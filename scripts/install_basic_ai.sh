#!/data/data/com.termux/files/usr/bin/bash

echo "🤖 Installing Basic AI Packages..."

# Install fundamental AI libraries
pip install numpy pandas matplotlib scikit-learn jupyter

# Install TensorFlow (CPU version for Termux compatibility)
pip install tensorflow

# Install PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo "✅ Basic AI packages installed!"
