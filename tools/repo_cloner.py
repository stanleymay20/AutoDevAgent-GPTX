import subprocess
import sys

def clone_repo(url):
    if not url:
        print("❌ No URL provided.")
        return
    print(f"🔁 Cloning repository: {url}")
    subprocess.run(["git", "clone", url])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python repo_cloner.py <repo_url>")
    else:
        clone_repo(sys.argv[1])
