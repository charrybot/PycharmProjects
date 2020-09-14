# Exercise 1
from collections import Counter
import numpy as np


def marginal_prob(chars):
    value_list = list(chars.values())
    value_dict = Counter(value_list)
    key_list = list(value_dict.keys())
    result = {}
    for i in range(len(key_list)):
        x = value_dict[key_list[i]] / sum(value_dict.values())
        result[key_list[i]] = x
    return result


def chance_homophily(chars):
    value_list = list(chars.values())
    value_dict = Counter(value_list)
    key_list = list(value_dict.keys())
    result = {}
    for i in range(len(key_list)):
        x = value_dict[key_list[i]] / sum(value_dict.values())
        result[key_list[i]] = x

    key_list = list(result.keys())
    for k in range(len(result)):
        y = result[key_list[k]] ** 2
        result[key_list[k]] = y
    return sum(list(result.values()))


favorite_colors = {
    "ankit": "red",
    "xiaoyu": "blue",
    "mary": "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)


# Exercise 2
import pandas as pd
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df1 = df.loc[df.village == 1]
df2 = df.loc[df.village == 2]

df1["resp_gend"].head()


# Exercise 3
sex1 = df1.set_index("pid")["resp_gend"].to_dict()
caste1 = df1.set_index("pid")["caste"].to_dict()
religion1 = df1.set_index("pid")["religion"].to_dict()

sex2 = df2.set_index("pid")["resp_gend"].to_dict()
caste2 = df2.set_index("pid")["caste"].to_dict()
religion2 = df2.set_index("pid")["religion"].to_dict()


# Exercise 4
chance_homophily(sex1)
chance_homophily(caste1)
chance_homophily(religion1)

chance_homophily(sex2)
chance_homophily(caste2)
chance_homophily(religion2)


# Exercise 5
def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)


# Exercise 6
data_filepath1 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_1.csv"
data_filepath2 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_2.csv"

pid1 = pd.read_csv(data_filepath1)
pid2 = pd.read_csv(data_filepath2)

pid1.iloc[100]


# Exercise 7
import networkx as nx
A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

pid1 = pd.read_csv(data_filepath1, dtype=int)['0'].to_dict()
pid2 = pd.read_csv(data_filepath2, dtype=int)['0'].to_dict()

homophily(G1, sex1, pid1)
chance_homophily(sex1)

homophily(G1, caste1, pid1)
chance_homophily(caste1)

homophily(G1, religion1, pid1)
chance_homophily(religion1)

homophily(G2, sex2, pid2)
chance_homophily(sex2)

homophily(G2, caste2, pid2)
chance_homophily(caste2)

homophily(G2, religion2, pid2)
chance_homophily(religion2)





