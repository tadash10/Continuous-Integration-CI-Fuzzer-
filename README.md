# Continuous-Integration-CI-Fuzzer-

Fuzzing Job Trigger Script
Overview

This script automates the triggering of a fuzzing job in a Continuous Integration (CI) pipeline. It retrieves the latest commit hash from a Git repository and uses it to trigger the fuzzing job in Jenkins.
Prerequisites

    Python 3.x installed on the system.
    Git installed on the system.
    Access to a Jenkins server with a configured fuzzing job.

Setup

    Clone this repository to your local machine.
    Ensure Python 3.x is installed.
    Install required dependencies:

    pip install -r requirements.txt

    Configure the script:
        Set the JENKINS_URL variable to the URL of your Jenkins server.
        Set the JOB_NAME variable to the name of the fuzzing job in Jenkins.
        Set the GIT_REPO_PATH variable to the path of the Git repository.

Usage

Run the script using the following command:

python fuzzing_job_trigger.py

The script will automatically fetch the latest commit hash from the Git repository and trigger the fuzzing job in the Jenkins CI pipeline.
Error Handling

    If the script fails to retrieve the commit hash or encounters any other errors, it will log the error details.
    Error logs are generated using the Python logging module, providing detailed information for troubleshooting.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.
