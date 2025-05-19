import logging
import pandas as pd
from zenml import step


experiment_tracker = Client().active_stack.experiment_tracker


@step
def train_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Train the model on the data and return the model.
    
    Args:
        df: the data to train the model on.
    """
    pass