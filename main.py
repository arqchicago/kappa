import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from visualizer import arq_viz    
    
if __name__ == "__main__":
    df = pd.read_csv('data/test.csv')

    data_viz = arq_viz(df)
    data_viz.plot_title = 'Boxplot of Y vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.watermark = 'draft'
    
    # create a boxplot of variable 'x'
    data_viz.y_label = 'Y'
    data_viz.x_label = 'X'
    data_viz.boxplot('fig1.png', 'x')
    
    # create a histogram of variable 'y' vs 'x'
    data_viz.plot_title = 'Histogram of Y'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.histogram('fig2.png', 'y', 20)
    
    # create a scatterplot of variable 'y' vs 'x'
    data_viz.y_label = 'Y'
    data_viz.x_label = 'X'
    data_viz.plot_title = 'Scatterplot of Y vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.scatter('fig3.png', 'x', 'y', watermark_loc='lower_right')
    
    # create a scatterplot of variable 'y' and 'z' vs 'x'
    data_viz.y_label = 'Y and Z'
    data_viz.x_label = 'X'
    data_viz.plot_title = 'Scatterplot of Y, Z vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.scatter('fig4.png', 'x', ['y', 'z'], watermark_loc='lower_left')
    
    # create a line chart of variable 'y' vs 'x'
    data_viz.plot_title = 'Line Chart of Y vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.line_chart('fig5.png', 'x', 'y', watermark_loc='lower_right')
    
    # create a line chart of variable 'y' and 'z' vs 'x'
    data_viz.plot_title = 'Line Chart of Y, Z vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.line_chart('fig6.png', 'x', ['y', 'z'], watermark_loc='lower_left')