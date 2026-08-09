# 🚀 Email Address Slicer

## 📝 Description
Extract username and domain from an email address.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 019: Email Address Slicer
Category: Text & Strings
Description: Extract username and domain from an email address.
"""

def run_project_19():
    print("=" * 45)
    print("      PYTHON PROJECT 019: EMAIL ADDRESS SLICER")
    print("=" * 45)
    
    email = input("Enter an email address: ").strip()
    
    if "@" not in email:
        print("Error: Invalid email address format.")
        return False
        
    try:
        username, domain = email.split('@', 1)
        
        print("\n--- Slicer Results ---")
        print(f"Email: {email}")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        return True
    except ValueError:
        print("Error parsing the email.")
        return False

if __name__ == "__main__":
    run_project_19()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 019_email_address_slicer.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Email Address Slicer in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
