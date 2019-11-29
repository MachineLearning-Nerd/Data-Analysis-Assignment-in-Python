# CMT114 Coursework
# student number:

import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

def report(nobelprizeDict):
    year = []
    category = []
    awarded_or_not = []
    for data in nobelprizeDict:
        if 'laureates' in data.keys():
            year.append(data['year'])
            category.append(data['category'])
            awarded_or_not.append(True)
        else:
            year.append(data['year'])
            category.append(data['category'])
            awarded_or_not.append(False)
    n_data = {'year':year, 'category':category, 'awarded_or_not':awarded_or_not}
    df = pd.DataFrame(n_data)
    return df

def get_laureates_and_motivation(nobelprizeDict, year, category):
    n_data = {'category':[], 'year':[], 'id':[], 'laureate':[], 'motivation':[], 'overall_motivation':[]}
    for data in nobelprizeDict:
        # print(data.keys())
        if data['year'] == year and data['category'] == category:
            if 'laureates' in data.keys():
                print(data)
                for i in range(len(data['laureates'])) :
                    n_data['year'].append(int(data['year']))
                    n_data['category'].append(data['category'])
                    n_data['id'].append(int(data['laureates'][i]['id']))
                    Name = data['laureates'][i]['firstname'] + ' ' + data['laureates'][i]['surname']
                    n_data['laureate'].append(Name)
                    n_data['motivation'].append(data['laureates'][i]['motivation'])
                    if 'overallMotivation' in data.keys():
                        n_data['overall_motivation'].append(data['laureates'][i]['overallMotivation'])
                    else:
                        n_data['overall_motivation'].append('NaN')
    print(n_data)
    df = pd.DataFrame(n_data)
    return df


    # return df

def plot_freqs(nobelprizeDict):
    # your code here
    #
    white_list_words = []
    with open('whitelist.txt', 'r') as file:
        data = file.readlines()
    for val in data:
        white_list_words.append(val.strip('\n'))

    n_data = {}
    for data in nobelprizeDict:
        if 'laureates' in data.keys():
            for i in range(len(data['laureates'])) :
                list_val = data['laureates'][i]['motivation']
                list_val = list_val.split(' ')
                for value in list_val:
                    if value in white_list_words:
                        if data['category'] in n_data.keys():
                            if value in n_data[data['category']].keys():
                                n_data[data['category']][value] += 1
                            else:
                                n_data[data['category']][value] = 1
                        else:
                            n_data[data['category']] = {}

    top_50_words = {}
    for key, val in n_data.items():
        top_50_words[key] = {'words':[], 'frequency':[]}
        words = np.array([])
        f_words = np.array([])
        for tkey, tval in val.items():
            words = np.append(words, tkey)
            f_words = np.append(f_words, tval)
        index = np.argsort(-f_words)
        index_50 = index[:50]
        words_50 = words[index_50]
        f_words_50 = f_words[index_50]
        top_50_words[key]['words'] = words_50
        top_50_words[key]['frequency'] = f_words_50
        
    
    i = 1
    # fig = plt.figure(figsize=(10,70))
    # fig.tight_layout()
    fig = plt.figure(figsize=(16,12))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    index = np.append(0,np.arange(9,50,step=10))
    for key, val in top_50_words.items():
        # plt.subplot(3, 2, i)
        ax = fig.add_subplot(3,2,i)
        # plt.xticks(np.append(0,np.arange(9,50,step=10)), rotation=10)
        plt.xticks(rotation=10)
        plt.plot(val['words'][index], val['frequency'][index], 'bo')
        plt.ylabel('frequency')
        plt.title(key)
        i = i+1
    plt.show()

file = 'nobelprizes.json'
with open(file) as file_object:
    d = json.load(file_object)
df = report(d)
print(df.head())

df = get_laureates_and_motivation(d, '2019', 'chemistry')
print(df.head())

plot_freqs(d)
