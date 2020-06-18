#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import networkx as nx


# # Loading the data
pro_network = pd.read_table('9606.protein.links.v11.0.txt', sep=' ')
pro_network.head()

pro_domain = pd.read_table('proteins_w_domains.txt', sep = '\t')
pro_domain.head()


# # Filter Network with score >= 500 
pro_network_m500 = pro_network[pro_network.combined_score >= 500]
pro_network_m500.head()


# # Network degree
network = nx.from_pandas_edgelist(pro_network_m500, source = 'protein1', target = 'protein2')
pro_degree = pd.DataFrame(network.degree, columns= ['protein', 'degree'])
pro_degree['Degree'] = np.where(pro_degree['degree'] > 100, 'High', 'Low')
pro_degree['Protein stable ID'] = [ p.replace('9606.','') for p in pro_degree['protein']]
pro_degree.head()


# # Domain Difference between group
pro_domain_count = pro_domain.groupby('Protein stable ID')['Pfam ID'].agg('count').reset_index(name = "Domain count")
pro_domain_degree = pro_domain_count.merge(pro_degree, on = 'Protein stable ID', how = 'inner')
pro_domain_degree.sort_values(by=['Domain count'], ascending=False).head()


# # Boxplot
sns.set_context("poster")
sns_plot = sns.boxplot(y="Domain count", x= "Degree", data = pro_domain_degree, showfliers = False)
sns_plot.get_figure().savefig("protein_domains_vs_string_degree.png")

