# -*- coding: utf-8 -*-
"""
🔒 PRIVATE BOT - OWNED BY FAHID MEHAR  
📞 Contact: 03016412628 (Authorized Access Only)  
⚠️ Unauthorized Use = Legal Action  
"""

# ==================== ACCESS CONTROL ==================== #
AUTHORIZED_USERS = {
    "fahid": "MeharCrypto@123",  # Tumhara personal login
    "trusted_user": "Pass456"     # Jisko access dena ho
}

def verify_login(username, password):
    if username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == password:
        print("Access Granted! ✅")
        return True
    print("""
    🚫 UNAUTHORIZED!  
    Contact Fahid Mehar (03016412628)
    """)
    exit()

# ==================== LOGIN CHECK ==================== #
print("""  
╔════════════════════════════════════╗
║                                    ║
║   FAHID MEHAR EXCLUSIVE BOT v1.0   ║
║   (Restricted Access)              ║
║                                    ║
╚════════════════════════════════════╝""")

username = input("Username: ")
password = input("Password: ")
verify_login(username, password)

# ==================== BOT CODE ==================== #
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Quotex Automation
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://quotex.com/login")

# Login Credentials (Tumhare details daalo)
email = "your_login@quotex.com"
password = "your_password"

# Auto-Login
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)

# Trading Logic (Yahan se tumhara strategy code shuru hoga)
print("\n Bot Live! Trading signals yahan dikhenge...")

while True:
    # Add your strategy here (SuperTrend/RSI/MACD)
    time.sleep(60)  # Check every 1 minute
