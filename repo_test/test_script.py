import logging
import numpy as np
import pandas as pd
import requests
import sys

def test_sys_requests():
    logger.info("Testing sys")
    logger.info(sys.version)

    logger.info("Testing requests")
    logger.info(requests.head)

def test_pandas_numpy():
    logger.info("Testing pandas")
    test_dataframe = pd.DataFrame(
        {
            "hw_column": ["hello","world"],
        }
    )
    logger.info(f"Test DataFrame:\n {test_dataframe}")

    logger.info("Testing numpy")
    test_dataset = [1, 2, 3, 4, 5]
    logger.info(f"Test Dataset: {test_dataset}, Mean: {np.mean(test_dataset)}")


if __name__ == "__main__":
    # Initialize logger
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Begin basic tests to verify repo functionallity 
    logger.info("Repository / Dependency Test Started:\n")
    test_sys_requests()
    test_pandas_numpy()
