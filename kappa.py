from data_proc import data_load
from technicals import simple_technicals
from visualizer import arq_viz    
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


    # adding dependent variables
    # ----------------------------------------------------------------

    # 30 day return (%)
    sp500_df['ret_30day'] = sp500_df['Close'].pct_change(30)
    sp500_df['ret_30day'] = sp500_df['ret_30day'].shift(-30)  #.fillna(method='ffill')

    # 60 day return (%)    
    sp500_df['ret_60day'] = sp500_df['Close'].pct_change(60)
    sp500_df['ret_60day'] = sp500_df['ret_60day'].shift(-60)  #.fillna(method='ffill')

    # 90 day return (%)
    sp500_df['ret_90day'] = sp500_df['Close'].pct_change(90)
    sp500_df['ret_90day'] = sp500_df['ret_90day'].shift(-90)  #.fillna(method='ffill')
    #sp500_df['ret_1yr'] = sp500_df['Close'].pct_change(365)


    # adding simple technicals as features
    # ----------------------------------------------------------------    
    sp500_techs = simple_technicals(sp500_df)
    
    # 5 day moving avg and moving std deviation
    sp500_techs.moving_avg(5, 'Close', 'mavg_5')
    sp500_techs.moving_std(5, 'Close', 'mstd_5')
    sp500_techs.bol_bands(5, 2, 'mavg_5', 'mstd_5', 'lbb_5', 'ubb_5')

    # 10 day moving avg and moving std deviation
    sp500_techs.moving_avg(10, 'Close', 'mavg_10')
    sp500_techs.moving_std(10, 'Close', 'mstd_10')
    
    sp500_techs.moving_avg(200, 'Close', 'mavg_200')
    sp500_df = sp500_techs.get_df()
    #sp500_df['mavg10_mstd_10'] = sp500_df['mavg_10'] - sp500_df['mstd_10']
    
    print(sp500_df.head(225).to_string())
    print(sp500_df)
    #print(sp500_df.to_string())
    print(sp500_df.columns.tolist())
    

    # visualize
    # pick a timeframe to visualize (or create the plot for all time units)
    mask = (sp500_df['Date'] > '2005-06-01') & (sp500_df['Date'] <= '2022-06-25')

    line_chart = arq_viz(sp500_df.loc[mask])
    line_chart.plot_title = 'SP500'
    line_chart.plot_suptitle = 'Moving Averages'
    line_chart.watermark = 'draft'
    line_chart.line_chart('line_chart_sp500.png', 'Date', ['Close', 'mavg_200'], watermark_loc='lower_left')