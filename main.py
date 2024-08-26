import os
from bot.dependency_upgrader import DependencyUpgrader
from bot.code_suggester import CodeSuggester
from bot.test_generator import TestGenerator
from bot.pr_creator import PullRequestCreator

REPO_PATH = '/path/to/your/repo'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = 'your-username/dependency-upgrade-bot'

def main():
    # Step 1: Upgrade Dependencies
    upgrader = DependencyUpgrader(REPO_PATH)
    upgrader.upgrade_dependencies()

    # Step 2: Suggest Code Changes
    suggester = CodeSuggester()
    changes = suggester.suggest_code_changes(dependency="example-dependency")

    # Step 3: Generate Tests
    test_generator = TestGenerator()
    tests = test_generator.generate_tests()

    # Step 4: Create a Pull Request
    pr_creator = PullRequestCreator(REPO_NAME, GITHUB_TOKEN)
    pr_url = pr_creator.create_pr(
        branch_name='dependency-upgrade',
        title='Upgrade Dependencies',
        body=f'Upgraded dependencies. Suggested changes:\n{changes}\nGenerated tests:\n{tests}'
    )
    print(f'Pull request created: {pr_url}')

if __name__ == '__main__':
    main()
