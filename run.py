import logging
import numpy as np
import pandas as pd
from tqdm import trange
from tqdm.contrib.logging import logging_redirect_tqdm
from tqdm.auto import tqdm


LOG = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(filename='example.log',
                        encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    #with logging_redirect_tqdm():
    #    for i in trange(9):
    #        if i == 4:
    #            LOG.info("console logging redirected to `tqdm.write()`")
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    logging.info('dataframe head - {}'.format(df.to_string()))
    tqdm.pandas(desc="my bar!")
    df.progress_apply(lambda x: x**2)
