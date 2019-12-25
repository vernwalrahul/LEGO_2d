import numpy as np
import networkx as nx
from itertools import chain
import helper
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualize_nodes(curr_occ_grid, curr_node_posns):
    fig1 = plt.figure(figsize=(10,6), dpi=80)
    ax1 = fig1.add_subplot(111, aspect='equal')

    occ_g = curr_occ_grid.reshape(10,10)
    for i in range(10):
            for j in range(10):
                if(occ_g[i,j]==0):
                    ax1.add_patch(patches.Rectangle(
                    (i/10.0, j/10.0),   # (x,y)
                    0.1,          # width
                    0.1,          # height
                    alpha=0.6
                    ))
    curr_node_posns = np.array(curr_node_posns)
    if len(curr_node_posns)>0:
        plt.scatter(curr_node_posns[:,0], curr_node_posns[:,1], s = 50, color = 'green')
    plt.title("Visualization")
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.show()

def main():
    dense_G = nx.read_graphml("graphs/dense_graph.graphml")
    shallow_G = nx.read_graphml("graphs/shallow_graph.graphml")

    occ_grid = helper.get_random_occ_grid()
    visualize_nodes(occ_grid,[])
                
if __name__ == '__main__':
    main()