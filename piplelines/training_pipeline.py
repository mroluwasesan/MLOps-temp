from zenml.pipelines import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import model_train
from steps.evaluation import evaluation



@pipeline
def train_pipeline(data_path: str):
    """
    Args:
        ingest_data: DataClass
        clean_data: DataClass
        model_train: DataClass
        evaluation: DataClass
    Returns:
        mse: float
        rmse: float
    """
    df = ingest_data(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
