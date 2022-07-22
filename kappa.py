from data_proc import data_load
from technicals import simple_technicals
from visualizer import arq_viz    
import datetime as dt
import numpy as np


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

    # 90 day return (%)
    sp500_df['ret_90day'] = sp500_df['Close'].pct_change(90)
    sp500_df['ret_90day'] = sp500_df['ret_90day'].shift(-90)  #.fillna(method='ffill')

    # 180 day return (%)    
    sp500_df['ret_180day'] = sp500_df['Close'].pct_change(180)
    sp500_df['ret_180day'] = sp500_df['ret_180day'].shift(-180)  #.fillna(method='ffill')

    # 1 yr return (%)
    sp500_df['ret_1yr'] = sp500_df['Close'].pct_change(365)
    sp500_df['ret_1yr'] = sp500_df['ret_1yr'].shift(-365)  #.fillna(method='ffill')

    # 2 yr return (%)
    sp500_df['ret_2yr'] = sp500_df['Close'].pct_change(730)
    sp500_df['ret_2yr'] = sp500_df['ret_2yr'].shift(-730)  #.fillna(method='ffill')


    # adding simple technicals
    # ----------------------------------------------------------------    
    sp500_techs = simple_technicals(sp500_df)
    
    # 10 day moving avg and moving std deviation
    sp500_techs.moving_avg(10, 'Close', 'mavg_10')
    sp500_techs.moving_std(10, 'Close', 'mstd_10')
    sp500_techs.bol_bands(10, 2, 'mavg_10', 'mstd_10', 'lbb_10', 'ubb_10')

    # 20 day moving avg and moving std deviation
    sp500_techs.moving_avg(20, 'Close', 'mavg_20')
    sp500_techs.moving_std(20, 'Close', 'mstd_20')
    sp500_techs.bol_bands(20, 2, 'mavg_20', 'mstd_20', 'lbb_20', 'ubb_20')

    # 30 day moving avg and moving std deviation
    sp500_techs.moving_avg(30, 'Close', 'mavg_30')
    sp500_techs.moving_std(30, 'Close', 'mstd_30')
    sp500_techs.bol_bands(30, 2, 'mavg_30', 'mstd_30', 'lbb_30', 'ubb_30')

    # 60 day moving avg and moving std deviation
    sp500_techs.moving_avg(60, 'Close', 'mavg_60')
    sp500_techs.moving_std(60, 'Close', 'mstd_60')
    sp500_techs.bol_bands(60, 2, 'mavg_60', 'mstd_60', 'lbb_60', 'ubb_60')

    # 180 day moving avg and moving std deviation
    sp500_techs.moving_avg(180, 'Close', 'mavg_180')
    sp500_techs.moving_std(180, 'Close', 'mstd_180')
    sp500_techs.bol_bands(180, 2, 'mavg_180', 'mstd_180', 'lbb_180', 'ubb_180')
    
    sp500_techs.moving_avg(200, 'Close', 'mavg_200')

    
    # features
    # ----------------------------------------------------------------   
    sp500_df = sp500_techs.get_df()

    sp500_df['mavg10_lbb20'] = sp500_df['mavg_10'] - sp500_df['lbb_20']  # 10 day moving avg - lbb 20
    sp500_df['mavg10_lbb30'] = sp500_df['mavg_10'] - sp500_df['lbb_30']  # 10 day moving avg - lbb 30
    sp500_df['mavg10_lbb60'] = sp500_df['mavg_10'] - sp500_df['lbb_60']  # 10 day moving avg - lbb 60
    sp500_df['mavg10_lbb180'] = sp500_df['mavg_10'] - sp500_df['lbb_180']  # 10 day moving avg - lbb 180

    sp500_df['mavg10_ubb20'] = sp500_df['ubb_20'] - sp500_df['mavg_10']  # ubb 20 - 10 day moving avg
    sp500_df['mavg10_ubb30'] = sp500_df['ubb_30'] - sp500_df['mavg_10']  # ubb 30 - 10 day moving avg
    sp500_df['mavg10_ubb60'] = sp500_df['ubb_60'] - sp500_df['mavg_10']  # ubb 60 - 10 day moving avg
    sp500_df['mavg10_ubb180'] = sp500_df['ubb_180'] - sp500_df['mavg_10']  # ubb 180 - 10 day moving avg
    

    sp500_df = sp500_techs.get_df()
   
    print(sp500_df.head(225).to_string())
    print(sp500_df)
    #print(sp500_df.to_string())
    print(sp500_df.columns.tolist())
    

    # visualize
    # ----------------------------------------------------------------   
    # pick a timeframe to visualize (or create the plot for all time units)
    mask = (sp500_df['Date'] > '2005-06-01') & (sp500_df['Date'] <= '2022-06-25')

    ma_bb_60day = arq_viz(sp500_df.loc[mask])
    ma_bb_60day.plot_title = 'SP500'
    ma_bb_60day.plot_suptitle = 'Moving Averages'
    ma_bb_60day.watermark = 'draft'
    ma_bb_60day.line_chart('charts//line_chart_sp500.png', 'Date', ['Close', 'lbb_60', 'ubb_60', 'mavg_60', 'mavg_200'], watermark_loc='lower_left')

    mask2 = (sp500_df['Date'] > '2020-01-01') & (sp500_df['Date'] <= '2022-06-25')

    ma_bb_30day = arq_viz(sp500_df.loc[mask2])    
    ma_bb_30day.plot_suptitle = '30 day MABB'
    ma_bb_30day.watermark = 'draft'
    ma_bb_30day.line_chart('charts//30day_bb_sp500.png', 'Date', ['Close', 'lbb_30', 'ubb_30', 'mavg_30', 'mavg_200'], watermark_loc='lower_left')

    
    # save data for model development
    # ----------------------------------------------------------------
    
    # modeling 1 year return classifier and regressor
    # classifier is if 1 year return > 0.15, then 1 else 0
    conditions = [(sp500_df['ret_1yr']>0.15), (sp500_df['ret_1yr']<=0.15)]
    choices = [1,0]
    sp500_df['ret_1yr_ind'] = np.select(conditions, choices, default=0)

    save_vars = ['Date', 'ret_1yr', 'ret_1yr_ind'] + \
                ['mavg10_lbb20', 'mavg10_lbb30', 'mavg10_lbb60', 'mavg10_lbb180', 'mavg10_ubb20', 'mavg10_ubb30', 'mavg10_ubb60', 'mavg10_ubb180']
    df = sp500_df[save_vars].copy()   
    df = sp500_df[save_vars]    
    df.to_csv('output//sp500_processed.csv', index=False)