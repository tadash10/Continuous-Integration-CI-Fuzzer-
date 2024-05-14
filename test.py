import subprocess
import os

def trigger_fuzzing_job(commit_hash):
    """Trigger fuzzing job in the CI pipeline."""
    try:
        # Replace 'jenkins_url' with the actual URL of the Jenkins server
        # Replace 'job_name' with the name of the fuzzing job in Jenkins
        subprocess.run(['curl', '-X', 'POST', f'jenkins_url/job/job_name/buildWithParameters?commit={commit_hash}'])
        print("Fuzzing job triggered successfully.")
    except Exception as e:
        print(f"Failed to trigger fuzzing job: {e}")

def main():
    # Get the commit hash of the latest code change
    try:
        # Replace 'git_repo_path' with the path to the Git repository
        commit_hash = subprocess.check_output(['git', '-C', 'git_repo_path', 'rev-parse', 'HEAD']).decode().strip()
    except subprocess.CalledProcessError as e:
        print(f"Failed to get commit hash: {e}")
        return

    # Trigger fuzzing job in the CI pipeline
    trigger_fuzzing_job(commit_hash)

if __name__ == "__main__":
    main()
