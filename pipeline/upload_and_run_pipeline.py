from kfp import Client
import os
import argparse
from dotenv import load_dotenv

class EnvironmentError(Exception):
    """Raised when required environment variables are missing"""
    pass

def get_required_env_var(name: str) -> str:
    """Get a required environment variable or raise an error if not set"""
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Required environment variable {name} is not set")
    return value

def upload_pipeline(git_sha: str):
    # Load environment variables from .env file
    load_dotenv()
    
    # Get configuration from environment variables
    namespace = get_required_env_var('KUBEFLOW_NAMESPACE')
    host = get_required_env_var('KFP_HOST')
    
    client = Client(
        host=host,
    )

    pipeline_name = "iris-pipeline"
    pipeline_version_name = f"{pipeline_name}-{git_sha}"

    # Upload the pipeline
    client.upload_pipeline_version(
        pipeline_package_path="iris_pipeline.yaml",
        pipeline_version_name=pipeline_version_name,
        pipeline_name=pipeline_name
    )
    
    # Start a new run
    run_name = f"{pipeline_version_name}-run"
    client.create_run_from_pipeline_package(
        pipeline_file="iris_pipeline.yaml",
        run_name=run_name,
        namespace=namespace
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload pipeline to Kubeflow with version from git SHA")
    parser.add_argument("--git_sha", required=True, help="Git SHA to use as pipeline version")
    args = parser.parse_args()
    upload_pipeline(git_sha=args.git_sha)