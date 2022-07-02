import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']

class arq_viz:
    def __init__(self, df):
        mpl.style.use('seaborn')
        self.df = df
        self.text_watermark = ''
        self.text_plot_title = ''
        self.text_plot_suptitle = ''
        self.text_y_label = ''
        self.text_x_label = ''
        print(f'arqviz initiated')

    @property
    def y_label(self):
        return self.text_y_label
        
    @y_label.setter
    def y_label(self, text):
        self.text_y_label = text
        
    @property
    def x_label(self):
        return self.text_x_label
        
    @x_label.setter
    def x_label(self, text):
        self.text_x_label = text
        
    @property
    def plot_suptitle(self):
        return self.text_plot_suptitle
        
    @plot_suptitle.setter
    def plot_suptitle(self, suptitle):
        self.text_plot_suptitle = suptitle
        
    @property
    def plot_title(self):
        return self.text_plot_title
        
    @plot_title.setter
    def plot_title(self, text):
        self.text_plot_title = text
        
    @property
    def watermark(self):
        return self.text_watermark
        
    @watermark.setter
    def watermark(self, text):
        self.text_watermark = text

    def line_chart(self, fig_name, var_x, var_y, watermark_loc=''):
        self.fig, self.ax = plt.subplots()

        self.fig.suptitle(self.text_plot_suptitle, fontsize=16)

        for axis in ['bottom','left']:  #'top', 'right'
            self.ax.spines[axis].set_linewidth(2)
            self.ax.spines[axis].set_color('red')
        
        i = 0
        if type(var_y) == list:
            for each_var_y in var_y:
                self.ax.plot(self.df[var_x], self.df[each_var_y], color=colors[i], label=each_var_y)
                i += 1
        
        else:
            self.ax.plot(self.df[var_x], self.df[var_y], color=colors[0], label=var_y)

        self.ax.set(title=self.text_plot_title)
        self.ax.set_xlabel(self.text_x_label)
        #self.ax.set_ylabel(self.text_y_label)
        self.ax.legend()
        
        if watermark_loc=='lower_right':
            self.fig.text(0.85, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)

        elif watermark_loc=='lower_left':
            self.fig.text(0.25, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)

        #self.fig.text(0.85, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)
        plt.savefig(fig_name)
        plt.close()
        print(f'line chart created  [{fig_name}]')


    def scatter(self, fig_name, var_x, var_y, watermark_loc=''):
        self.fig, self.ax = plt.subplots()

        self.fig.suptitle(self.text_plot_suptitle, fontsize=16)

        for axis in ['bottom','left']:  #'top', 'right'
            self.ax.spines[axis].set_linewidth(2)
            self.ax.spines[axis].set_color('red')
        
        i = 0
        if type(var_y) == list:
            for each_var_y in var_y:
                self.ax.scatter(self.df[var_x], self.df[each_var_y], color=colors[i], label=each_var_y)
                i += 1
        
        else:
            self.ax.scatter(self.df[var_x], self.df[var_y], color=colors[0], label=var_y)

        self.ax.set(title=self.text_plot_title)
        self.ax.set_xlabel(self.text_x_label)
        #self.ax.set_ylabel(self.text_y_label)
        self.ax.legend()
        
        if watermark_loc=='lower_right':
            self.fig.text(0.85, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)
        elif watermark_loc=='lower_left':
            self.fig.text(0.25, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)
        
        plt.savefig(fig_name)
        plt.close()
        print(f'scatter plot created  [{fig_name}]')

    def boxplot(self, fig_name, var):
        green_diamond = dict(markerfacecolor='g', marker='s')
        fig, ax = plt.subplots()
        ax.set_title('Boxplot - variable ' + var)
        boxplot = ax.boxplot(self.df[var], notch=True, flierprops=green_diamond, patch_artist=True, showmeans=True)
        plt.xticks([1], [var])
        for patch, color in zip(boxplot['boxes'], ['pink']):
            patch.set_facecolor(color)
            
        for median in boxplot['medians']: 
            median.set(color ='red', linewidth = 3) 
            
        print(f'boxplot created  [{fig_name}]')
        
        
        plt.savefig(fig_name)
        plt.close()

    def histogram(self, fig_name, var_x, num_bins):
        self.fig, self.ax = plt.subplots()

        self.fig.suptitle(self.text_plot_suptitle, fontsize=16)

        for axis in ['bottom','left']:  #'top', 'right'
            self.ax.spines[axis].set_linewidth(2)
            self.ax.spines[axis].set_color('red')
          
        #self.ax.plot(self.df[var_x], self.df[var_y], color='b', label='test')
        self.ax.set(title=self.text_plot_title)
        self.ax.set_xlabel(self.text_x_label)
        #self.ax.set_ylabel(self.text_y_label)
        #self.ax.legend()
        self.fig.text(0.45, 0.80, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)
        self.ax.hist(self.df[var_x], bins=num_bins)
        plt.savefig(fig_name)
        plt.close()
        print(f'histogram created  [{fig_name}]')
 
        
