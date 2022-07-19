import pandas as pd

# this class loads index data
class data_load:

    # constructor
    def __init__(self, file):

        # set the mean and the standard deviation
        self.file = file
        self.file_df = pd.read_csv(file)

    def get_df(self):
        return self.file_df

    def get_size(self):
        return self.file_df.shape

    def get_file(self):
        return self.file

    def set_datetime_var(self, var):
        self.file_df[var] = pd.to_datetime(self.file_df[var])

    def get_file(self):
        return self.file


if __name__ == '__main__':

    # generate random data clusters
    sp500_file_loc = 'data//sp500.csv'
    sp500 = data_load(sp500_file_loc)
    sp500_df = sp500.get_df()
    print(sp500_df)
    print(sp500_df.columns.tolist())