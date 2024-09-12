import os
from bot.dependency_upgrader import DependencyUpgrader
from bot.code_suggester import CodeSuggester
from bot.test_generator import TestGenerator
from bot.pr_creator import PullRequestCreator


def main():
    repo_path = os.getenv('REPO_PATH')
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('REPO_NAME')

    # Step 1: Upgrade Dependencies
    upgrader = DependencyUpgrader(repo_path)
    upgrader.upgrade_dependencies()

    # Step 2: Suggest Code Changes
    suggester = CodeSuggester()
    changes = suggester.suggest_code_changes(dependency="maven")

    # Step 3: Generate Tests
    test_generator = TestGenerator()
    tests = test_generator.generate_tests()

    # Step 4: Create a Pull Request
    pr_creator = PullRequestCreator(repo_name, github_token)
    pr_url = pr_creator.create_pr(
        branch_name='dependency-upgrade',
        title='Upgrade Dependencies',
        body=f'Upgraded dependencies. Suggested changes:\n{changes}\nGenerated tests:\n{tests}'
    )
    print(f'Pull request created: {pr_url}')

if __name__ == '__main__':
    main()
