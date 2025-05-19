import logging
import pandas as pd

from zenml import step


@step
def evaluate_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Evaluate the model on the data and return the evaluation metrics.
    Args:
        df: the data to evaluate the model on.
    """
    pass

