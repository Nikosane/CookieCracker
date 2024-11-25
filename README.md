# CookieCracker

## Exploiting Cookies and Sessions

This project demonstrates various web security vulnerabilities related to cookies and sessions. It includes examples of how session fixation, cookie theft, and Cross-Site Scripting (XSS) attacks can be exploited in web applications.

## Vulnerabilities Covered:
1. **Session Fixation**: An attacker sets a known session ID for the victim and gains access to their session.
2. **Cookie Theft**: Exploiting insecure cookies (without `HttpOnly` or `Secure` flags).
3. **Cross-Site Scripting (XSS)**: Injecting malicious scripts that can steal session cookies.

## Requirements:
- Python 3.x
- Flask
- Requests

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/Exploiting-Cookies-and-Sessions.git
```
2. Install the dependencies:
```
pip install -r requirements.txt
```
3. Run the Flask app:
```
python index.py
```
