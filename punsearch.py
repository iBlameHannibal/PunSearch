import requests
import json
import time
import random
import os
from concurrent.futures import ThreadPoolExecutor


B = '\033[94m'
C = '\033[96m'
punpun = """
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⡴⠿⠿⠿⠷⣦⡀
⢀⢀⢀⢀⢀⢀⢀⢀⡞⠋⢀⢀⢀⢀⢀⠘⢻⡄
⢀⢀⢀⢀⢀⢀⢠⠘⢀⢀⢀⢀⣤⢀⢀⢀⢀⠳⡆
⠲⢶⣶⠶⠶⠶⠟⢀⢀⢀⢀⢀⣿⢀⢀⢀⢀⢀⡇
⢀⢀⠻⢧⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡇
⢀⢀⢀⠈⢻⡆⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡇
⢀⢀⢀⢀⢀⡇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡇
⢀⢀⢀⢀⢸⠃⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡇
⢀⢀⢀⢀⢸⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡇
⢀⢀⢀⢸⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡇
⢀⢀⢀⡸⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢠
"""


color_codes = {
        
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
  }
print(C + punpun)
time.sleep(1)
print("\n Punpun is stalking 😉")
time.sleep(2)
os.system('cls')
# قائمة المواقع المستهدفة
websites = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
}


def check_account(platform, url, username):
    try:
        user_url = url.format(username)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = requests.get(user_url, headers=headers, timeout=10)
        if response.status_code == 200:
            return platform, user_url
        return platform, None
    except Exception as e:
        return platform, None


def find_user(username):
    print(f"🔍 Searching for '{username}' across multiple platforms...\n")
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_platform = {
            executor.submit(check_account, platform, url, username): platform
            for platform, url in websites.items()
        }
        for future in future_to_platform:
            platform, user_url = future.result()
            if user_url:
                results[platform] = user_url
                print(f"✅ Found on {platform}: {user_url}")
            else:
                print(f"❌ Not found on {platform}.")
            
            time.sleep(random.uniform(1, 3))
    return results


def save_results(username, results):
    filename = f"{username}_results.json"
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)
    print(f"\n📁 Results saved to {filename}.")

if __name__ == "__main__":
    username = input("Enter the username to search: ").strip()
    results = find_user(username)
    
    print("\nSearch complete!")
    if results:
        print("\nAccounts found:")
        for platform, url in results.items():
            print(f"- {platform}: {url}")
        save_results(username, results)
    else:
        print("No accounts found.")



print("\n thanks for using punpun")





#--------------------------------------------------------------------------------------------------------------



