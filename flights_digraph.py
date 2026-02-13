# -*- coding: utf-8 -*-
"""
@author: ariya
"""

# libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import polars as pl  

# import data
data = pd.read_csv("BTS2025.csv")
flights = pd.DataFrame(data, columns=["ORIGIN", "DEST"])

# EDA 
origin_counts = flights.groupby("ORIGIN").size().sort_values(ascending=False)
destination_counts = flights.groupby("DEST").size().sort_values(ascending=False)
route_counts=flights.groupby(["ORIGIN", "DEST"]).size().reset_index(name="count")

# creating directed graph (DiGraph function)
G = nx.DiGraph()
for index, row in flights.iterrows():  # for each row, make an edge connecting the origin and destination
    G.add_edge(row["ORIGIN"], row["DEST"])

# plot all flights
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_size=50, font_size=8, arrowstyle="->")
plt.show()

# top routes
top_routes = route_counts.sort_values(by="count",ascending=False).head(20)

H = nx.DiGraph()

for _, row in top_routes.iterrows():
    origin=row["ORIGIN"]
    dest = row["DEST"]
    weight = row["count"]
    H.add_edge(origin, dest, weight=weight)
    
nx.draw(H, with_labels=True, node_size=50, font_size=8, arrowstyle="->")
plt.show()
