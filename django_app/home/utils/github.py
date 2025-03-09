import requests
import base64
import uuid
from .ai_agent import analyze_code_with_llm




# https://api.github.com/repos/aarav345/Microservices/pulls/1/files


def get_owner_repo(repo_url):
    url_list = list(filter(lambda x: x.strip(), repo_url.split("/")))
    if len(url_list) >= 2:
        return url_list[-2], url_list[-1]
    return None, None



def fetch_pr_files(repo_url, pr_number, github_token):
    owner, repo = get_owner_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {
        "Authorization" : f"token {github_token}"
    } if github_token else {}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status() #handles error
    return response.json()



def fetch_file_content(repo_url, file_path, github_token):
    owner, repo = get_owner_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {
        "Authorization" : f"token {github_token}"
    } if github_token else {}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status() #handles error
    content = response.json()['content']
    return base64.b64decode(content).decode()


def analyze_pr(repo_url, pr_number, github_token):
    task_id = str(uuid.uuid4())

    try:
        pr_files = fetch_pr_files(repo_url, pr_number, github_token)
        analysis_results = []
        for file in pr_files:
            filename = file['filename']
            raw_content = fetch_file_content(repo_url, filename, github_token)
            analysis_result = analyze_code_with_llm(raw_content, filename)
            analysis_results.append({"results": analysis_result, "file_name": filename})

        return {"task_id": task_id, "results": analysis_results}
    
    except Exception as e:
        print(e)
        return {"task_id": task_id, "results" : []}