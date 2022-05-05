import datetime

import numpy as np
import pandas as pd 
import os
# for visualizations

import seaborn as sns
import squarify

import warnings
warnings.filterwarnings('ignore')

# Global Variables
MY_PATH = os.path.abspath(os.getcwd())
data = pd.read_csv("test.csv")

data['PdDistrict'].fillna(data['PdDistrict'].mode()[0], inplace = True)
data.isnull().any().any()




def Major_Crimes_in_Sanfrancisco():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')

    plt.rcParams['figure.figsize'] = (20, 15)
    # plt.style.use('dark_background')

    sns.countplot(data['Category'], palette = 'gnuplot')

    plt.title('Major Crimes in Sanfrancisco', fontweight = 30, fontsize = 20)
    plt.xticks(rotation = 90)
    name = "foo" + str(datetime.datetime.now().strftime("%f")) + ".png"
    plt.savefig(MY_PATH + '\\static\\img\\' + name)
    plt.close()
    return name

def District_with_Most_Crime():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    plt.rcParams['figure.figsize'] = (20, 9)
    plt.style.use('seaborn')

    color = plt.cm.spring(np.linspace(0, 1, 15))
    data['PdDistrict'].value_counts().plot.bar(color = color, figsize = (15, 10))

    plt.title('District with Most Crime',fontsize = 30)

    plt.xticks(rotation = 90)
    name = "foo"+str(datetime.datetime.now().strftime("%f"))+".png"
    plt.savefig(MY_PATH + '\\static\\img\\'+name)
    plt.close()
    return name

def Top_15_Regions_in_Crime():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    plt.rcParams['figure.figsize'] = (20, 9)
    plt.style.use('seaborn')

    color = plt.cm.ocean(np.linspace(0, 1, 15))
    data['Address'].value_counts().head(15).plot.barh(color = color, figsize = (15, 10))

    plt.title('Top 15 Regions in Crime',fontsize = 20)

    plt.xticks(rotation = 90)
    name = "foo" + str(datetime.datetime.now().strftime("%f")) + ".png"
    plt.savefig(MY_PATH + '\\static\\img\\' + name)
    plt.close()
    return name

def Crime_count_on_each_day():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    plt.style.use('seaborn')

    total = sum( data['DayOfWeek'].value_counts().head(15))
    data['DayOfWeek'].value_counts().head(15).plot.pie(figsize = (15, 8), explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1), 
    autopct=lambda p: '{:.0f}'.format(p * total / 100))

    plt.title('Crime count on each day',fontsize = 20)
    plt.ylabel("")
    # plt.xticks(rotation = 90)
    plt.yticks(rotation=90)
    print()
    name = "foo" + str(datetime.datetime.now().strftime("%f")) + ".png"
    plt.savefig(MY_PATH + '\\static\\img\\' + name)
    plt.close()
    return name

def Crimes_in_each_Months():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    print(data.columns)
    data['Dates'] = pd.to_datetime(data['Dates'])

    data['Month'] = data['Dates'].dt.month

    plt.style.use('fivethirtyeight')
    plt.rcParams['figure.figsize'] = (15, 8)

    sns.countplot(data['Month'], palette = 'autumn',)
    plt.title('Crimes in each Months', fontsize = 20)
    name = "foo" + str(datetime.datetime.now().strftime("%f")) + ".png"
    plt.savefig(MY_PATH + '\\static\\img\\' + name)
    plt.close()
    return name

def get_count(district):
    store = data[data["PdDistrict"] == district]
    return len(store)

def get_crime_count(crime):
    ans = len(data[data["Descript"]==crime])
    return ans


def getReport():
    count_crimes_district = data.groupby(['PdDistrict']).size().reset_index()
    district_crimes = count_crimes_district.loc[count_crimes_district[0].idxmax()].values
    area = district_crimes[0]
    count_area = district_crimes[1]

    # <======================================================================================================>
    count_crimes_category = data.groupby(['Category']).size().reset_index()
    category_crimes = count_crimes_category.loc[count_crimes_category[0].idxmax()].values
    category = category_crimes[0]
    count_category = category_crimes[1]

    # <====================================================================================================>

    count_crimes_day = data.groupby(['DayOfWeek']).size().reset_index()
    day_crimes = count_crimes_day.loc[count_crimes_day[0].idxmax()].values
    day = day_crimes[0]
    count_day = day_crimes[1]
    # <========================================================================================================>
    resoluted_crimes = len(data[data.Resolution=='NONE'])
     
    return [district_crimes,category_crimes,day_crimes,resoluted_crimes]

def run(key):
    key = key[0]
    name = ""
    if key == "Major Crimes in Sanfrancisco":
        name = Major_Crimes_in_Sanfrancisco()
    
    if key == "District with Most Crime":
        name = District_with_Most_Crime()

    if key == "Top 15 Regions in Crime":
        name = Top_15_Regions_in_Crime()

    if key == "Crime count on each day":
        name = Crime_count_on_each_day()

    if key == "Crimes in each Months":
        name = Crimes_in_each_Months()

    return name



# print(data.columns)
# print(len(data["Descript"].unique()))
# print(data["Descript"].value_counts())