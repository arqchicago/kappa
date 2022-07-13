from data_proc import data_load
from technicals import simple_technicals
import datetime as dt

if __name__ == '__main__':

    # generate random data clusters
    sp500_file_loc = 'data//sp500.csv'
    sp500 = data_load(sp500_file_loc)
    sp500.set_datetime_var('Date')
    sp500_df = sp500.get_df()
    sp500_df_size = sp500.get_size()
    #print(sp500_df)
    #print(sp500_df.columns.tolist())
    #print(sp500_df_size)
    
    # adding in more variables
    sp500_df['quarter'] = sp500_df['Date'].dt.quarter
    sp500_df['ret_90day'] = sp500_df['Close'].pct_change(90)
    sp500_df['ret_180day'] = sp500_df['Close'].pct_change(180)
    sp500_df['ret_270day'] = sp500_df['Close'].pct_change(270)
    sp500_df['ret_1yr'] = sp500_df['Close'].pct_change(365)
    
    sp500_techs = simple_technicals(sp500_df)
    sp500_techs.moving_avg(5, 'Close', 'ma_5')
    sp500_techs.moving_avg(200, 'Close', 'ma_200')
    sp500_df = sp500_techs.get_df()
    
    print(sp500_df.head(250).to_string())
    print(sp500_df.to_string())
    print(sp500_df.columns.tolist())