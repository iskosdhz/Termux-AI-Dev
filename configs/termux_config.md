
Termux Development Configuration

Essential Packages

```bash
# Core development
pkg install python nodejs git vim

# Additional tools
pkg install curl wget termux-api
```

Python Development

```bash
pip install numpy pandas flask django
pip install jupyter notebook
```

Node.js Development

```bash
npm install -g express react-native-cli
npm install -g nodemon pm2
```

Useful Aliases (add to ~/.bashrc)

```bash
alias dev='cd ~/Termux-Setup-Dev'
alias projects='cd ~/Termux-Setup-Dev/projects'
alias py='python'
alias pi='pip install'
```

