import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('titanic.csv')
data.head()


# #### Univariate Plots : Task 1


import os

def createFolder(directory):
    """
    Function to create required folders in the current working directory
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)



directories = ['Univariate_Plots','Univariate_Plots/Histogram','Univariate_Plots/LinePlot','Univariate_Plots/BoxPlot',
             'Univariate_Plots/ViolinPlot','Univariate_Plots/BarPlot','Univariate_Plots/HorizontalBarPlot','Univariate_Plots/PieChart']

for i in directories:
    createFolder('./'+ i + '/')


def generate_univariate_plots(data,remove_ids=[]):
    
    """
    This function creates univariate plots for numerical and categorical columns in a dataframe
    
    Plots for Numerical Columns are:
        - Histogram
        - Line Plot
        - Box Plot
        - Violin Plot
    Plots for Categorial Columns are:
        - Bar Plot
        - Horizontal Bar Plot
        - Pie Chart
        
    Arguments:
        - data : dtype = dataframe
        - remove_ids : dtype = list
                       remove_ids are a list of id columns that should not be considered while plotting
    """
    
    data = data.drop(columns=remove_ids)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_categorical = data.select_dtypes(exclude=numerics)
    df_numerical = data.select_dtypes(include=numerics)
    print('Descriptive Statistics')
    print(data.describe(include='all'))
    for col_name in data.columns:
        if col_name in df_numerical.columns:
            # Histogram
            hist = df_numerical[col_name].hist(bins=10)
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots/Histogram/Histogram_'+ col_name + '.png',dpi=100)
            plt.show()
            # Lineplot
            line = df_numerical[col_name].plot.line()
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots/LinePlot/Line_'+ col_name + '.png',dpi=100)
            plt.show()
            # Boxplot
            boxplot = df_numerical.boxplot(column = col_name)
            plt.savefig('Univariate_Plots/BoxPlot/BoxPlot_'+ col_name + '.png',dpi=100)
            plt.show()
            boxplot = df_numerical.boxplot(column = col_name,showfliers=False)
            plt.savefig('Univariate_Plots/BoxPlot/BoxPlot_no_outliers'+ col_name + '.png',dpi=100)
            plt.show()
            # Violin Plot
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            violinplot = ax.violinplot(df_numerical[col_name])
            plt.savefig('Univariate_Plots/ViolinPlot/ViolinPlot_'+ col_name + '.png',dpi=100)
            plt.show()
        elif col_name in df_categorical.columns:
            # Barplot
            barplot = df_categorical[col_name].value_counts().plot.bar()
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots/BarPlot/BarPlot_'+ col_name + '.png',dpi=100)
            plt.show()
            # Horizontal Barplot
            h_barplot = df_categorical[col_name].value_counts().plot(kind='barh')
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots/HorizontalBarPlot/HBarPlot_'+ col_name + '.png',dpi=100)
            plt.show()
            # Pie Chart
            pie_chart = df_categorical[col_name].value_counts().plot(kind='pie')
            plt.axis('equal')
            plt.title('Number of appearances in dataset')
            plt.savefig('Univariate_Plots/PieChart/PieChart_'+ col_name + '.png',dpi=100)
            plt.show()
        else:
            print('nothing')
    return print('Plotted')


# ### Example function call

generate_univariate_plots(data=data,remove_ids=['Name', 'PassengerId'])


# #### Univariate Plots : Task 2

# Creating a new folder "Univariate_Plots_T2" to save all the plots in different sub folders

directories = ['Univariate_Plots_T2','Univariate_Plots_T2/Histogram','Univariate_Plots_T2/LinePlot','Univariate_Plots_T2/BoxPlot',
             'Univariate_Plots_T2/ViolinPlot','Univariate_Plots_T2/BarPlot','Univariate_Plots_T2/HorizontalBarPlot','Univariate_Plots_T2/PieChart']

for i in directories:
    createFolder('./'+ i + '/')


def generate_univariate_plots_features(data,remove_ids=[],list_of_features=[]):
    
    """
    This function creates univariate plots for numerical and categorical columns in a dataframe for a given list of features/columns 
    of interest.
    
    Plots for Numerical Columns are:
        - Histogram
        - Line Plot
        - Box Plot
        - Violin Plot
    Plots for Categorial Columns are:
        - Bar Plot
        - Horizontal Bar Plot
        - Pie Chart
        
    Arguments:
        - data : dtype = dataframe
        - remove_ids : dtype = list
                       remove_ids are a list of id columns that should not be considered while plotting
        - list_of_features : dtype = list
                             list_of_features are a list of columns that are of interest while plotting
    """
        
    data = data.drop(columns=remove_ids)
    data = data[list_of_features]
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_categorical = data.select_dtypes(exclude=numerics)
    df_numerical = data.select_dtypes(include=numerics)
    print('Descriptive Statistics')
    print(data.describe(include='all'))
    for col_name in data.columns:
        if col_name in df_numerical.columns:
            # Histogram
            hist = df_numerical[col_name].hist(bins=10)
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots_T2/Histogram/Histogram_'+ col_name + '.png',dpi=100)
            plt.show()
            line = df_numerical[col_name].plot.line()
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots_T2/LinePlot/Line_'+ col_name + '.png',dpi=100)
            plt.show()
            boxplot = df_numerical.boxplot(column = col_name)
    #             print("Plotting for column {}".format(col_name))
            plt.savefig('Univariate_Plots_T2/BoxPlot/BoxPlot_'+ col_name + '.png',dpi=100)
            plt.show()
            boxplot = df_numerical.boxplot(column = col_name,showfliers=False)
            plt.savefig('Univariate_Plots_T2/BoxPlot/BoxPlot_no_outliers'+ col_name + '.png',dpi=100)
            plt.show()
            # Create a figure instance
            fig = plt.figure()
            # Create an axes instance
            ax = fig.add_axes([0,0,1,1])
            violinplot = ax.violinplot(df_numerical[col_name])
    #             print("Plotting for column {}".format(col_name))
            plt.savefig('Univariate_Plots_T2/ViolinPlot/ViolinPlot_'+ col_name + '.png',dpi=100)
            plt.show()
        elif col_name in df_categorical.columns:
            barplot = df_categorical[col_name].value_counts().plot.bar()
            print("Plotting for column {}".format(col_name))
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots_T2/BarPlot/BarPlot_'+ col_name + '.png',dpi=100)
            plt.show()
            #Plot a histogram of frequencies
            h_barplot = df_categorical[col_name].value_counts().plot(kind='barh')
            print("Plotting for column {}".format(col_name))
            plt.xlabel(''+ col_name + '')
            plt.savefig('Univariate_Plots_T2/HorizontalBarPlot/HBarPlot_'+ col_name + '.png',dpi=100)
            plt.show()
            pie_chart = df_categorical[col_name].value_counts().plot(kind='pie')
            plt.axis('equal')
            plt.title('Number of appearances in dataset')
            print("Plotting for column {}".format(col_name))
            plt.savefig('Univariate_Plots_T2/PieChart/PieChart_'+ col_name + '.png',dpi=100)
            plt.show()
        else:
            print('nothing')
    return print('Plotted')

### Example function call

generate_univariate_plots_features(data,remove_ids=['Name', 'PassengerId'],
                                   list_of_features=['Sex','Age','Fare'])


# #### Univariate Plots : Task 3

directories = ['Univariate_Plots_T3','Univariate_Plots_T3/Histogram','Univariate_Plots_T3/LinePlot','Univariate_Plots_T3/BoxPlot',
             'Univariate_Plots_T3/ViolinPlot','Univariate_Plots_T3/BarPlot','Univariate_Plots_T3/HorizontalBarPlot','Univariate_Plots_T3/PieChart']

for i in directories:
    createFolder('./'+ i + '/')


def generate_univariate_plots_and_features(data,remove_ids=[],list_of_features=[],dict_plots=[]):
    
    """
    This function creates univariate plots for numerical and categorical columns in a dataframe for a given list of features/columns 
    of interest and for the given list of dictionary of data_type and plots.
    
    Plots for Numerical Columns are:
        - Histogram
        - Line Plot
        - Box Plot
        - Violin Plot
    Plots for Categorial Columns are:
        - Bar Plot
        - Horizontal Bar Plot
        - Pie Chart
        
    Arguments:
        - data : dtype = dataframe
        - remove_ids : dtype = list
                       remove_ids are a list of id columns that should not be considered while plotting
        - list_of_features : dtype = list
                             list_of_features are a list of columns that are of interest while plotting
        - dict_plots : dtype = list
                       dict_plots is a list of dictionaries that can take data_type as key and plot name as value 
    """
        
    data = data.drop(columns=remove_ids)
    data = data[list_of_features]
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_categorical = data.select_dtypes(exclude=numerics)
    df_numerical = data.select_dtypes(include=numerics)
    print('Descriptive Statistics')
    print(data.describe(include='all'))
    for dict_ in dict_plots:
        print(dict_)
        for key in dict_.keys():
            if key == 'Continuous':
                for col_name in data.columns:
                    if col_name in df_numerical.columns:
                        # Histogram
                        print(dict_[key])
                        if dict_[key] in ["histogram","Histogram"]:
                            hist = df_numerical[col_name].hist(bins=10)
                            plt.xlabel(''+ col_name + '')
                            plt.savefig('Univariate_Plots_T3/Histogram/Histogram_'+ col_name + '.png',dpi=100)
                            plt.show()
                        elif dict_[key] in ["lineplot","Lineplot"]:
                            line = df_numerical[col_name].plot.line()
                            plt.xlabel(''+ col_name + '')
                            plt.savefig('Univariate_Plots_T3/LinePlot/Line_'+ col_name + '.png',dpi=100)
                            plt.show()
                        elif dict_[key] in ["boxplot","Boxplot"]:
                            boxplot = df_numerical.boxplot(column = col_name)
                            plt.savefig('Univariate_Plots_T3/BoxPlot/BoxPlot_'+ col_name + '.png',dpi=100)
                            plt.show()
                            boxplot = df_numerical.boxplot(column = col_name,showfliers=False)
                            plt.savefig('Univariate_Plots_T3/BoxPlot/BoxPlot_no_outliers'+ col_name + '.png',dpi=100)
                            plt.show()
                        elif dict_[key] in ["violinplot","Violinplot"]:
                            fig = plt.figure()
                            ax = fig.add_axes([0,0,1,1])
                            violinplot = ax.violinplot(df_numerical[col_name])
                            plt.xlabel(''+ col_name + '')
                            plt.savefig('Univariate_Plots_T3/ViolinPlot/ViolinPlot_'+ col_name + '.png',dpi=100)
                            plt.show()
            elif key == 'Categorical':
                for col_name in df_categorical.columns:
                    if col_name in df_categorical.columns:
                        print('yes')
                        if dict_[key] in ["barplot","Barplot"]:
                            barplot = df_categorical[col_name].value_counts().plot.bar()
                            plt.xlabel(''+ col_name + '')
                            print("Plotting for column {}".format(col_name))
                            plt.savefig('Univariate_Plots_T3/BarPlot/BarPlot_'+ col_name + '.png',dpi=100)
                            plt.show()
                        #Plot a histogram of frequencies
                        elif dict_[key] in ["HBarplot","hbarplot"]:
                            h_barplot = df_categorical[col_name].value_counts().plot(kind='barh')
                            plt.xlabel(''+ col_name + '')
                            print("Plotting for column {}".format(col_name))
                            plt.savefig('Univariate_Plots_T3/HorizontalBarPlot/HBarPlot_'+ col_name + '.png',dpi=100)
                            plt.show()
                        elif dict_[key] in ["piechart","Piechart"]:
                            pie_chart = df_categorical[col_name].value_counts().plot(kind='pie')
                            plt.axis('equal')
                            plt.title('Number of appearances in dataset')
                            print("Plotting for column {}".format(col_name))
                            plt.savefig('Univariate_Plots_T3/PieChart/PieChart_'+ col_name + '.png',dpi=100)
                            plt.show()
            else:
                print('nothing')
    return print('Plotted')


# # Example function call

generate_univariate_plots_wrapper(data,remove_ids=['PassengerId', 'Name','Ticket','Cabin'],list_of_features=['Sex','Age','Fare','Embarked'],
                                       dict_plots= [{"Continuous":'histogram'},{'Continuous':'lineplot'},{'Categorical':'Barplot'},{'Categorical':'Piechart'}])


# #### Wrapper Function

def generate_univariate_plots_wrapper(df,remove_ids=[], list_of_features=[], dict_plots=[]):
    
    """
    This function creates univariate plots for numerical and categorical columns in a dataframe for a given list of features/columns 
    of interest and for the given list of dictionary of data_type and plots.
    
    Plots for Numerical Columns are:
        - Histogram
        - Line Plot
        - Box Plot
        - Violin Plot
    Plots for Categorial Columns are:
        - Bar Plot
        - Horizontal Bar Plot
        - Pie Chart
        
    Arguments:
        - data : dtype = dataframe
        - remove_ids : dtype = list
                       remove_ids are a list of id columns that should not be considered while plotting
        - list_of_features : dtype = list
                             list_of_features are a list of columns that are of interest while plotting
        - dict_plots : dtype = list
                       dict_plots is a list of dictionaries that can take data_type as key and plot name as value
                       
    There are three different case in which this function can be utilized:
    
    1. The user can give just the dataframe and the ID columns that has to be removed/not considered during plotting.
    Output : The function will create all possible sorts of plots for each of the column in specific folders of current working
             directory
    2. The user can input just the dataframe, ID columns that has to be removed/not considered during plotting, and the list of 
       columns for plotting
    Output : the function will create all possible plots only for the list of columns given as an argument
    3. The user can input the dataframe, ID columns that has to be removed/not considered during plotting,list of 
       columns for plotting,list of dictionary of plots - key: data_type of the column. value: plot_name
    """
    
    if ((len(list_of_features)!= 0) & (len(dict_plots)==0)):
        print('Cond1')
        generate_univariate_plots_features(data,remove_ids=remove_ids,list_of_features=list_of_features)
    elif ((len(list_of_features)!= 0) & (len(dict_plots) != 0)):
        print('Cond2')
        generate_univariate_plots_and_features(data,remove_ids=[],list_of_features=list_of_features,dict_plots=dict_plots)
    elif ((len(list_of_features) == 0) & (len(dict_plots) == 0)):
        print('Cond3')
        generate_univariate_plots(df,remove_ids=remove_ids)
    else:
        print('Nothing')
    return print('Plotted')



# Example Function Call

generate_univariate_plots_wrapper(data,remove_ids=['PassengerId', 'Name','Ticket','Cabin'],list_of_features=['Sex','Age','Fare','Embarked'],
                                       dict_plots= [{"Continuous":'histogram'},{'Continuous':'lineplot'},{'Categorical':'Barplot'},{'Categorical':'Piechart'}])


# Example Function Call

generate_univariate_plots_wrapper(data,remove_ids=['PassengerId', 'Name','Ticket','Cabin'],list_of_features=['Sex','Age','Fare','Embarked'])


# Example Function Call

generate_univariate_plots_wrapper(data,remove_ids=['PassengerId', 'Name','Ticket','Cabin'])

