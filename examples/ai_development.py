cat > examples/ai_development.py << 'EOF'
#!/data/data/com.termux/files/usr/bin/python3
"""
🤖 AI Development Environment Check for Termux
Author: iskosdhz
Description: Test script to verify AI/ML packages installation
"""

import sys
import platform

def check_python_environment():
    """Check Python version and environment"""
    print("🐍 Python Environment Check")
    print("=" * 40)
    
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Termux Path: {sys.prefix}")
    
    return sys.version_info >= (3, 8)

def check_ai_packages():
    """Check if essential AI packages are installed"""
    print("\n🤖 AI Package Availability")
    print("=" * 40)
    
    packages = {
        'numpy': 'Numerical computing',
        'pandas': 'Data analysis',
        'matplotlib': 'Data visualization',
        'scikit-learn': 'Machine learning',
        'tensorflow': 'Deep learning',
        'torch': 'PyTorch deep learning',
        'keras': 'Neural networks API',
        'flask': 'Web framework'
    }
    
    available = []
    missing = []
    
    for package, description in packages.items():
        try:
            __import__(package)
            available.append((package, description, '✅'))
            print(f"✅ {package:15} - {description}")
        except ImportError:
            missing.append((package, description, '❌'))
            print(f"❌ {package:15} - {description}")
    
    return available, missing

def test_basic_ai_functionality():
    """Test basic AI functionality"""
    print("\n🧪 Basic AI Functionality Test")
    print("=" * 40)
    
    try:
        import numpy as np
        # Create sample data
        X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        y = np.dot(X, np.array([1, 2])) + 3
        
        print(f"✅ NumPy test: Array shape {X.shape}")
        print(f"   Sample calculation: {y[:2]}")
        
        # Test simple ML if scikit-learn is available
        try:
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
            model.fit(X, y)
            prediction = model.predict([[3, 5]])
            print(f"✅ Scikit-learn test: Prediction = {prediction[0]:.2f}")
        except ImportError:
            print("❌ Scikit-learn not available for ML test")
            
    except Exception as e:
        print(f"❌ Basic AI test failed: {e}")

def show_ai_project_ideas():
    """Show AI project ideas for Termux"""
    print("\n💡 AI Project Ideas for Termux")
    print("=" * 40)
    
    ideas = [
        "📊 Data analysis with pandas",
        "🤖 Chatbot with transformers",
        "🖼️ Image classification with TensorFlow",
        "📈 Stock prediction model",
        "🔤 Text classification with scikit-learn",
        "🎮 Game AI with reinforcement learning",
        "📱 Mobile-optimized AI models"
    ]
    
    for idea in ideas:
        print(f"  {idea}")

def installation_commands():
    """Show installation commands for missing packages"""
    print("\n🔧 Installation Commands")
    print("=" * 40)
    
    commands = [
        "pip install numpy pandas matplotlib",
        "pip install scikit-learn tensorflow",
        "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu",
        "pip install jupyter flask requests",
        "pkg install python nodejs git",
    ]
    
    for cmd in commands:
        print(f"  {cmd}")

def main():
    """Main function"""
    print("🚀 AI Development Environment Check")
    print("=" * 50)
    print("Checking your Termux AI setup...\n")
    
    # Run checks
    py_ok = check_python_environment()
    available, missing = check_ai_packages()
    test_basic_ai_functionality()
    
    # Summary
    print("\n📊 SUMMARY")
    print("=" * 50)
    print(f"Python Environment: {'✅ Ready' if py_ok else '❌ Issues'}")
    print(f"AI Packages: {len(available)} available, {len(missing)} missing")
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join([p[0] for p in missing])}")
        installation_commands()
    
    show_ai_project_ideas()
    
    print(f"\n🎯 Next: Run 'python examples/web_server.py' to test web development")
    print("📁 Your AI projects: cd projects/ai-ml")

if __name__ == "__main__":
    main()
