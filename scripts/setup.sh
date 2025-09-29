
## 📋 2. BUAT SCRIPTS/SETUP.SH

```bash
cat > scripts/setup.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash

# Termux-Setup-Dev Installation Script
echo "🚀 Starting Termux-Setup-Dev Installation..."
echo "============================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Function to print status
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running in Termux
if [ ! -d "/data/data/com.termux/files/usr" ]; then
    print_error "This script must be run in Termux!"
    exit 1
fi

# Main installation function
install_environment() {
    print_status "Step 1/8 - Updating system packages..."
    pkg update -y && pkg upgrade -y
    
    print_status "Step 2/8 - Installing programming languages..."
    pkg install -y python nodejs
    
    print_status "Step 3/8 - Installing development tools..."
    pkg install -y git curl wget vim nano cmake make clang
    
    print_status "Step 4/8 - Installing additional utilities..."
    pkg install -y termux-api termux-tools proot tree
    
    print_status "Step 5/8 - Setting up Python environment..."
    pip install --upgrade pip
    pip install numpy pandas matplotlib jupyter requests flask django
    
    print_status "Step 6/8 - Setting up Node.js environment..."
    npm install -g npm@latest
    npm install -g express nodemon react-native-cli
    
    print_status "Step 7/8 - Installing AI/ML packages..."
    pip install scikit-learn tensorflow-cpu keras torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    
    print_status "Step 8/8 - Finalizing setup..."
    # Create symbolic links to examples
    ln -sf ../examples/ai_development.py projects/ai-ml/ai_demo.py
    ln -sf ../examples/web_server.py projects/web/web_demo.py
    
    # Make project directories executable
    chmod +x examples/*.py
    chmod +x scripts/*.sh
}

# Run installation
install_environment

# Completion message
echo ""
print_success "Termux-Setup-Dev installation completed!"
echo ""
echo -e "${YELLOW}🎉 Your Android device is now a development workstation!${NC}"
echo ""
echo -e "${GREEN}📚 Available Commands:${NC}"
echo -e "  ${YELLOW}python examples/ai_development.py${NC}    - Test AI environment"
echo -e "  ${YELLOW}python examples/web_server.py${NC}       - Start web server"
echo -e "  ${YELLOW}cd projects/ai-ml${NC}                   - AI projects directory"
echo -e "  ${YELLOW}cd projects/web${NC}                     - Web projects directory"
echo ""
echo -e "${GREEN}🚀 Next Steps:${NC}"
echo -e "1. Check ${YELLOW}USAGE.md${NC} for detailed instructions"
echo -e "2. Explore ${YELLOW}examples/${NC} folder for code samples"
echo -e "3. Start your projects in ${YELLOW}projects/${NC} directory"
echo ""
print_success "Happy coding! 👨‍💻"
EOF
