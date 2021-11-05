from diagrams import Cluster, Diagram
from diagrams.aws.storage import S3, FsxForLustre
from diagrams.aws.analytics import LakeFormation, Athena, Glue, GlueCrawlers, GlueDataCatalog
from diagrams.aws.storage import StorageGateway
from diagrams.aws.network import VPC, DirectConnect
from diagrams.aws.ml import Sagemaker
from diagrams.aws.integration import Eventbridge

from diagrams.onprem.compute import Server

with Diagram("Data Lake and Machine Learning", show=False):
    dc = DirectConnect("HNB DC")

    with Cluster("OnPrem"):
        onprem_server = Server("onprem")


    with Cluster("AWS"):
        with Cluster("VPC"):
            raw_bucket = S3("Raw")
            transformed_bucket = S3("Transformed")
            event = Eventbridge("S3 Put Trigger")
            with Cluster("Glue -- Ingest"):
                raw_crawler = GlueCrawlers("Ingest Crawler")
                raw_catalog = GlueDataCatalog("Ingested Catalog")
                transformer = Glue("ETL")
            with Cluster("Glue -- Transform"):
                transformed_crawler = GlueCrawlers("Transformed Crawler")
            
                transformed_catalog = GlueDataCatalog("Transformed Catalog")
            
            

    onprem_server >> dc \
        >> raw_bucket >> event >> raw_crawler >> raw_catalog >> transformer \
        >> transformed_bucket >> transformed_crawler >> transformed_catalog 
    
