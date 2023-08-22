import requests
import os
import sys

def create_github_issue(title, body, labels):
    url = f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/issues"
    headers = {
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }

    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: create_issue.py <GITHUB_TOKEN>")
        sys.exit(1)
    
    github_token = sys.argv[1]
    
    title = "Test Failure"
    body = "Tests failed. Check the test results."
    labels = ["pytest", "test-failure"]
    
    response = create_github_issue(title, body, labels)
    print(f"Issue creation status code: {response.status_code}")
    print(response.text)
