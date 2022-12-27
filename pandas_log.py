import logging
import numpy as np
import pandas as pd

LOG = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(filename='example_pandas.log',
                        encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    logging.info('dataframe head - {}'.format(df.describe().to_string()))