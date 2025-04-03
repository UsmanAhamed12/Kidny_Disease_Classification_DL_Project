import os
from cnnclassifier import logger
from cnnclassifier.utils.common import get_size
import zipfile
import gdown
from cnnclassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self)-> str:
        try:
            dataset_url = self.config.source_url
            zipdownload_url = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading Data from {dataset_url} to {zipdownload_url}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zipdownload_url)
            
            logger.info(f"Downloaded data from {dataset_url} into file {zipdownload_url}")
            
        except Exception as e:
            raise e
        
    
    def extract_zip_file(self):
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)