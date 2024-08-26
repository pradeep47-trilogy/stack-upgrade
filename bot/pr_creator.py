from github import Github
import os

class PullRequestCreator:
    def __init__(self, repo_name, token):
        self.repo_name = repo_name
        self.github = Github(token)
    
    def create_pr(self, branch_name, title, body):
        repo = self.github.get_repo(self.repo_name)
        head = branch_name
        base = "main"
        pr = repo.create_pull(title=title, body=body, head=head, base=base)
        return pr.url
