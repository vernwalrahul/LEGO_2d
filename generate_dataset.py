import numpy as np
import networkx as nx
from itertools import chain
import helper
import astar
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualize_nodes(curr_occ_grid, curr_node_posns, start_pos, goal_pos):
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
    plt.scatter(start_pos[0], start_pos[1], color="red", s=100, edgecolors='black', alpha=1, zorder=10) # init
    plt.scatter(goal_pos[0], goal_pos[1], color="blue", s=100, edgecolors='black', alpha=1, zorder=10) # goal

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

    occ_grid, row, col = helper.get_random_occ_grid()
    print(row, col)
    start_n, goal_n = helper.get_valid_start_goal(dense_G, occ_grid, row, col, inc = 0.02)
    start_pos = helper.state_to_numpy(dense_G.node[start_n]['state'])
    goal_pos = helper.state_to_numpy(dense_G.node[goal_n]['state'])

    path_nodes = astar.astar(dense_G, start_n, goal_n, occ_grid, row, col)
    points_x = []
    points_y = []
    count_h = 1
    print("path_nodes = ", path_nodes)
    for node in path_nodes:
        s = helper.state_to_numpy(dense_G.node[node]['state'])
        points_x.append(s[0])
        points_y.append(s[1])
        count_h += 1
    visualize_nodes(occ_grid,np.array(list(zip(points_x,points_y))), start_pos, goal_pos)
    
if __name__ == '__main__':
    main()