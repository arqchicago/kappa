from data_proc import data_load

if __name__ == '__main__':

    # generate random data clusters
    sp500_file_loc = 'data//sp500.csv'
    sp500 = data_load(sp500_file_loc)
    sp500.set_datetime_var('Date')
    sp500_df = sp500.get_df()
    sp500_df_size = sp500.get_size()
    #print(sp500_df)
    #print(sp500_df.columns.tolist())
    print(sp500_df_size)