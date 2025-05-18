import logging

import pandas as pd
from zenml import step


class IngestData:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self, data_path:str):
        
        """Initialize the data ingestion class."""
        self.data_path = data_path
        

    def get_data(self):
        logging.info(f"Igesting data from {self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingest_data():
    """
    Injesting the data from data_path
    
    Args:
        None
    Returns:
        df: pd.DataFrame
    """
    try:
        ingest_data = IngestData()
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(e)
        raise e
