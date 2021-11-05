from diagrams import Cluster, Diagram
from diagrams.aws.storage import S3, FsxForLustre
from diagrams.aws.ml import SagemakerNotebook, SagemakerModel, Sagemaker, SagemakerTrainingJob


with Diagram("MLOps"):
    with Cluster("SageMaker Dev"):
        notebook = SagemakerNotebook("Notebook")


    with Cluster("SageMaker Training"):
        trainingJob = SagemakerTrainingJob("Training")

    
