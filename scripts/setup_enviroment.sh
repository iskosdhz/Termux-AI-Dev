#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 AI-Powered Termux Setup Started..."
echo "======================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Update and upgrade
echo -e "${YELLOW}[1/6] Updating packages...${NC}"
pkg update -y && pkg upgrade -y

# Install essential packages
echo -e "${YELLOW}[2/6] Installing essential packages...${NC}"
pkg install -y python nodejs git wget curl cmake make clang

# Setup Python environment
echo -e "${YELLOW}[3/6] Setting up Python environment...${NC}"
pip install --upgrade pip
pip install virtualenv

# Create virtual environment
echo -e "${YELLOW}[4/6] Creating virtual environment...${NC}"
python -m venv ai-env
source ai-env/bin/activate

# Install basic AI packages
echo -e "${YELLOW}[5/6] Installing basic AI packages...${NC}"
pip install numpy pandas matplotlib scipy jupyter

# Completion message
echo -e "${GREEN}[6/6] Setup completed!${NC}"
echo -e "${GREEN}✅ AI environment ready!${NC}"
echo -e "${YELLOW}To activate virtual environment:${NC}"
echo -e "source ai-env/bin/activate"
