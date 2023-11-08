import requests
api_url = 'https://api.github.com/users/nmadev/repos?type=public'
headers = {
    "Authorization": "Bearer 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"
  }
response = requests.get(api_url, headers=headers)
repos = response.json()

public_repos = []
for repo in repos:
    public_repos.append((repo["name"], repo["html_url"]))

for repo in public_repos:
    print (repo)

new_response = requests.get('https://files.terranceli.com/ssh.txt')
print (new_response.content)