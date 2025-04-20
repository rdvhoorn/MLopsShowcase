from kfp import Client
import os
import argparse

def upload_pipeline(git_sha: str = None):
    client = Client(
        host="http://localhost:8888",
    )

    pipeline_name = "iris-pipeline"
    if git_sha:
        pipeline_name = f"{pipeline_name}-{git_sha}"

    client.upload_pipeline(
        pipeline_package_path="iris_pipeline.yaml",
        pipeline_name=pipeline_name
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--git_sha", help="Version to append to pipeline name")
    args = parser.parse_args()
    
    upload_pipeline(version=args.git_sha)