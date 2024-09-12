import os
import subprocess
import xml.etree.ElementTree as ET
import yaml
import requests
import logging


class DependencyUpgrader:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.log_file = 'dependency_upgrade.log'
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
    
    def upgrade_dependencies(self):
        logging.info(f"Starting dependency upgrade for repository at: {self.repo_path}")
        try:
            for root, dirs, files in os.walk(self.repo_path):
                for file in files:
                    if file.endswith('.xml'):
                        self._update_xml_dependencies(os.path.join(root, file))
                    elif file.endswith('.yml') or file.endswith('.yaml'):
                        self._update_yaml_dependencies(os.path.join(root, file))
                    elif file.endswith('.txt') or file.endswith('.text'):
                        self._update_text_dependencies(os.path.join(root, file))
            logging.info("Dependency upgrade completed successfully.")
        except Exception as e:
            logging.error(f"Error during dependency upgrade: {str(e)}")
            print(f"Error during dependency upgrade: {str(e)}")
    
    def _update_xml_dependencies(self, file_path):
        logging.info(f"Updating XML dependencies in file: {file_path}")
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            # Assume the structure is known for Maven or similar XML-based dependency management
            for dependency in root.findall(".//dependency"):
                version = dependency.find("version")
                group_id = dependency.find("groupId").text
                artifact_id = dependency.find("artifactId").text

                if version is not None:
                    current_version = version.text
                    latest_version = self._get_latest_version(group_id, artifact_id, current_version)
                    if latest_version:
                        logging.info(f"Upgrading {artifact_id} from {current_version} to {latest_version}")
                        version.text = latest_version

            tree.write(file_path)
            logging.info(f"XML file {file_path} updated successfully.")
        except Exception as e:
            logging.error(f"Error updating XML dependencies in {file_path}: {str(e)}")

    def _update_yaml_dependencies(self, file_path):
        logging.info(f"Updating YAML dependencies in file: {file_path}")
        try:
            with open(file_path, 'r') as stream:
                data = yaml.safe_load(stream)
            
            # Assumed structure for YAML dependencies (can be tailored)
            for dependency, details in data.get('dependencies', {}).items():
                current_version = details.get('version')
                latest_version = self._get_latest_version(dependency, None, current_version)
                if latest_version:
                    logging.info(f"Upgrading {dependency} from {current_version} to {latest_version}")
                    details['version'] = latest_version
            
            with open(file_path, 'w') as stream:
                yaml.safe_dump(data, stream)
            logging.info(f"YAML file {file_path} updated successfully.")
        except Exception as e:
            logging.error(f"Error updating YAML dependencies in {file_path}: {str(e)}")

    def _update_text_dependencies(self, file_path):
        logging.info(f"Updating text dependencies in file: {file_path}")
        try:
            # Navigate to the repository path and upgrade dependencies using pip
            subprocess.run(["pip", "install", "--upgrade", "-r", file_path], check=True)
            logging.info(f"Text dependencies in {file_path} upgraded successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error upgrading text dependencies in {file_path}: {str(e)}")
    
    def _get_latest_version(self, group_id_or_package, artifact_id, current_version):
        # Example method to fetch the latest version. You can enhance this method to call:
        # 1. PyPI API for Python packages   
        # 2. Maven Central Repository API for Java dependencies
        # 3. npm API for JavaScript packages
        if group_id_or_package in ["requests", "flask"]:  # Example for Python packages
            return self._fetch_latest_version_pypi(group_id_or_package)
        elif group_id_or_package and artifact_id:  # Example for Maven/Java dependencies
            return self._fetch_latest_version_maven(group_id_or_package, artifact_id)
        return None

    def _fetch_latest_version_pypi(self, package_name):
        try:
            url = f"https://pypi.org/pypi/{package_name}/json"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['info']['version']
        except Exception as e:
            logging.error(f"Error fetching latest version for PyPI package {package_name}: {str(e)}")
        return None

    def _fetch_latest_version_maven(self, group_id, artifact_id):
        try:
            url = f"https://search.maven.org/solrsearch/select?q=g:{group_id}+AND+a:{artifact_id}&rows=1&wt=json"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['response']['docs'][0]['latestVersion']
        except Exception as e:
            logging.error(f"Error fetching latest version for Maven dependency {artifact_id}: {str(e)}")
        return None
