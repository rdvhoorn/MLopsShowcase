# can be compiled by running `python pipeline/pipeline.py`
from kfp import dsl
from kfp.dsl import container_component, Input, Output, Dataset, Model, Metrics
from kfp import compiler

@container_component
def download_data_op(
    train_data: Output[Dataset],
    test_data: Output[Dataset]
):
    return dsl.ContainerSpec(
        image="ghcr.io/robinvhoorn/mlops-showcase/download_data:latest",
        command=["python", "download_data.py"],
        args=[
            "--train_data_path", train_data.path,
            "--test_data_path", test_data.path,
        ]
    )

@container_component
def train_op(
    train_data: Input[Dataset],
    model: Output[Model]
):
    return dsl.ContainerSpec(
        image="ghcr.io/robinvhoorn/mlops-showcase/train:latest",
        command=["python", "train.py"],
        args=[
            "--train_data_path", train_data.path,
            "--model_path", model.path
        ]
    )

@container_component
def evaluate_op(
    model: Input[Model],
    test_data: Input[Dataset],
    metrics: Output[Metrics]
):
    return dsl.ContainerSpec(
        image="ghcr.io/robinvhoorn/mlops-showcase/evaluate:latest",
        command=["python", "evaluate.py"],
        args=[
            "--model_path", model.path,
            "--test_data_path", test_data.path,
            "--metrics_path", metrics.path,
        ]
    )

@dsl.pipeline(
    name="iris-classification-pipeline",
    description="Pipeline that preprocesses, trains and evaluates an Iris model."
)
def iris_pipeline():
    download_step = download_data_op()
    train_step = train_op(train_data=download_step.outputs["train_data"])
    evaluate_step = evaluate_op(
        model=train_step.outputs["model"],
        test_data=download_step.outputs["test_data"]
    )

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=iris_pipeline,
        package_path="iris_pipeline.yaml"
    )
