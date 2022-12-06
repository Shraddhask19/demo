#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import collections


def caldistance(raw_data):
    distance = np.zeros(shape=(len(raw_data), len(raw_data)))
    for i in range(len(raw_data)):
        for j in range(len(raw_data)):
            if i > j:
                distance[i][j] = distance[j][i]
            elif i < j:
                distance[i][j] = np.sqrt(np.sum(np.power(raw_data[i] - raw_data[j], 2)))
    return distance



def chose_epsilon(distance, t):
    temp = []
    for i in range(len(distance[0])):
        for j in range(i + 1, len(distance[0])):
            temp.append(distance[i][j])
   
    temp.sort()
    epsilon = temp[int(len(temp) * t / 100)]
    return epsilon



def get_core_point(distance, epsilon, M):
    
    density_dict = {}
    core_point = []
    for index, node in enumerate(distance):
        epsilon_neib = np.squeeze(np.argwhere(node < epsilon))
      
        if epsilon_neib.size == 0:
            node_density_set = []
       
        elif epsilon_neib.size == 1:
            node_density_set = [int(epsilon_neib)]
        
        else:
            node_density_set = list(epsilon_neib)
            
            if epsilon_neib.size >= M:
                core_point.append(index)
        density_dict[index] = node_density_set
    return density_dict, core_point


def get_border_and_noise_point(density_dict, core_point, data_length):
    noncore_point = set(range(data_length)) - set(core_point)
    border_point = []
    noise_point = []
    for point in noncore_point:
        if len(set(density_dict[point]) & set(core_point)) != 0:
            border_point.append(point)
        else:
            noise_point.append(point)
    return border_point, noise_point


def assign_class(density_dict, core_point, border_point, data_length, class_list):
    for core in core_point:
       
        if class_list[core] == -1:
            class_list[core] = core
            density_propagation(density_dict, core, class_list, core_point, border_point)
    return class_list



def density_propagation(density_dict, core, class_list, core_point, border_point):
    
    for epsilon_neib in density_dict[core]:
        
        if epsilon_neib and class_list[epsilon_neib] == -1:
            if epsilon_neib in border_point:
                class_list[epsilon_neib] = 'border'
            else:
                class_list[epsilon_neib] = class_list[core]
                density_propagation(density_dict, epsilon_neib, class_list, core_point, border_point)


def show_result(class_list, raw_data):
    colors = [
              '#FF0000', '#FFA500', '#FFFF00', '#00FF00', '#228B22',
              '#0000FF', '#FF1493', '#EE82EE', '#000000', '#FFA500',
              '#00FF00', '#006400', '#00FFFF', '#0000FF', '#FFFACD',
              ]

    
    use_color = {}
    total_color = list(dict(collections.Counter(class_list)).keys())
    if 'border' in total_color:
        total_color.remove('border')
    elif -1 in total_color:
        total_color.remove(-1)
    for index, i in enumerate(total_color):
        use_color[i] = index
    plt.figure(num=1, figsize=(15, 10))
    for node, class_ in enumerate(class_list):
        if class_ != 'border' and class_ != -1:
            plt.scatter(x=raw_data[node, 0], y=raw_data[node, 1], c=colors[use_color[class_]], s=5, marker='o', alpha=0.73)
        elif class_ == 'border':
            plt.scatter(x=raw_data[node, 0], y=raw_data[node, 1], c='g', s=20, marker='^',
                        alpha=0.8)
        else:
            plt.scatter(x=raw_data[node, 0], y=raw_data[node, 1], c='b', s=20, marker='+',
                        alpha=0.8)
    plt.title('The Result Of Cluster')
    plt.show()


def main(raw_data):

    M = 4
    
    t = 2
    data_length = len(raw_data)
    class_list = [-1 for _ in range(data_length)]
    distance = caldistance(raw_data)
    epsilon = chose_epsilon(distance, t)
    density_dict, core_point = get_core_point(distance, epsilon, M)
    border_point, noise_point = get_border_and_noise_point(density_dict, core_point, data_length)
    class_list = assign_class(density_dict, core_point, border_point, data_length, class_list)
    show_result(class_list, raw_data)

if __name__ == '__main__':
    Compound = r'D:\DM\6\Compound.txt'
    raw_data = np.loadtxt(Compound, delimiter='	', usecols=[0, 1])
    main(raw_data)