#!/data/data/com.termux/files/usr/bin/python3

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def linear_regression_demo():
    print("📊 Linear Regression Demo in Termux")
    print("=" * 40)
    
    # Generate sample data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2.5 * X + np.random.randn(100, 1) * 2 + 5
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Results
    print(f"✅ Model trained successfully!")
    print(f"📈 Coefficient: {model.coef_[0][0]:.2f}")
    print(f"📉 Intercept: {model.intercept_[0]:.2f}")
    print(f"🎯 R² Score: {model.score(X_test, y_test):.2f}")
    
    # Plot (if running in environment that supports display)
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(X_test, y_test, color='blue', alpha=0.6, label='Actual')
        plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.title('Linear Regression - Termux AI Demo')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig('regression_plot.png')
        print("📸 Plot saved as 'regression_plot.png'")
    except Exception as e:
        print(f"⚠️  Could not save plot: {e}")

if __name__ == "__main__":
    linear_regression_demo()
