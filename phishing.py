phishing_keywords = [
    "login", "verify", "update", "free", "bank",
    "secure", "account", "confirm", "password"
]

def check_url(url):
    url = url.lower()
    for word in phishing_keywords:
        if word in url:
            print("⚠️ Phishing URL Detected!")
            return
    print("✅ Legitimate URL")
url = input("Enter a URL to check: ")
check_url(url)
