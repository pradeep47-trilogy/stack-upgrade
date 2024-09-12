**Tech Stack update - AI Project**

Objective of this document is to explain the implementation of an AI bot tool that updates the dependency modules of any given Github repository. Also the tool should have an option to prompt and evaluate the pros and cons of updating the dependencies.

**Approach**

**Evaluate**
The tool will upgrade the dependency version, for example upgrade Java 17 to 21 and update the code and create a pull request, which the developer can review and decide whether it’s reasonable to update or not.

**Decide**

The tool should provide options for the user to decide which version of the dependency can be updated. For example, updating from Java 8 to 17 might break the environment, so the user can choose to upgrade from Java 8 to 11 and then 11 to 17.

**Impact**

This implies the risk of upgrading the dependencies and support of the OS (windows server, linux) and database (postgres, sql). And also the unit and integration testing might be impacted because of the upgrade, so the tool should assist in fixing the issue in test mocks, dependency libraries.

**Change**
This step is where the developer applies the suggested change to the repository. And identify and add any missing unit / integration test for the new changes to prevent the application running to issues. AI bot should automatically add unit tests during the upgrade.

**Testing**

Check whether the upgrade has broken the application, a complete QA of the end-to-end flows is important to identify the runtime issues, so we can safely revert the changes.

## Installation

1. Clone the repository: `git clone https://github.com/pradeep47-trilogy/stack-upgrade.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your GitHub token: `export GITHUB_TOKEN=your_token_here`
4. Set up the Repository Path: `export REPO_PATH=repo_path`
5. Set up the Repository Name: `export REPO_NAME=repo_name`

## Configuration

- Set the `REPO_PATH` variable to the path of your repository.
- Set the `GITHUB_TOKEN` variable to your GitHub token.
- Set the `REPO_NAME` variable to the name of your repository.

## Usage

1. Run the script: `python main.py`
2. The script will upgrade dependencies, suggest code changes, generate tests, and create a pull request on GitHub.

## Troubleshooting

- If you encounter issues with the script, check the GitHub API documentation for error codes and solutions.
- If you encounter issues with the dependency upgrade process, check the Maven or pip documentation for error codes and solutions.
