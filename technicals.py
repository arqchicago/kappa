import pandas as pd

# this class loads index data
class simple_technicals:

    # constructor
    def __init__(self, df):

        # set df
        self.df = df

    def get_df(self):
        return self.df

    def moving_avg(self, n, colname, new_colname):
        self.df[new_colname] = self.df[colname].rolling(n).mean().fillna(method='bfill')


if __name__ == '__main__':

    # generate random data clusters
    print('technicals.py')