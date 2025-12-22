# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 17:55:01 2025

@author: manid
"""




#word search 
graph = {1:['A',{2: 'right',4: 'down'}], 2:['T',{1: 'left',3: 'right',5: 'down'}],3:['T',{2: 'left',6: 'down'}],4:['E',{1: 'up',5: 'right'}],5:['T',{2: 'up',4: 'left',6: 'right'}],6:['A',{3: 'up',5: 'left'}], } #(id: [letter, neighbor_id_list])
word = "ATE"




#assume starting at index 0 (will iterate this starting. only start at nonzero nodes/letters)
start = 6 #id=0
fringe = [(start, None, None)] #(id, direction, letter of word index)
score = 0

while(len(fringe)!=0):
    
    current_id, current_direction, first_index = fringe.pop()
    print("-----",current_id, current_direction, first_index)
    #find the next nodes to expand
    for node in graph[current_id][1]:
        if graph[current_id][0] in word:
            if current_direction == None:
                orig_index = word.index(graph[current_id][0])
                
                if orig_index < len(word) - 1:
                    #getting node's individual value
                    added_score = 0
                    if graph[node][0] == word[orig_index + 1]:
                        added_score = 1
                        first_index = orig_index + 1
                        
                    
                    if added_score > 0:
                        fringe.append((node, graph[current_id][1][node], first_index))
            else:
                
                if first_index < len(word)-1:
                    
                    if graph[current_id][1][node] == current_direction:
                        added_score = 0
                        
                        
                        if graph[node][0] == word[first_index + 1]:
                            added_score = 1
                        
                        if added_score > 0:
                            fringe.append((node, current_direction, first_index + 1))
            
        
        
    
    