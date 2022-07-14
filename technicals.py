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

    def moving_std(self, n, colname, new_colname):
        self.df[new_colname] = self.df[colname].rolling(n).std().fillna(method='bfill')

    def bol_bands(self, n, m, moving_avg_colname, moving_std_colname, new_colname_lbb, new_colname_ubb):
        self.df[new_colname_lbb] = self.df[moving_avg_colname].rolling(n).std().fillna(method='bfill') - m * self.df[moving_std_colname].rolling(n).std().fillna(method='bfill')
        self.df[new_colname_ubb] = self.df[moving_avg_colname].rolling(n).std().fillna(method='bfill') + m * self.df[moving_std_colname].rolling(n).std().fillna(method='bfill')
        


if __name__ == '__main__':

    # generate random data clusters
    print('technicals.py')