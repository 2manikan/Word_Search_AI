# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 17:55:01 2025

@author: manid
"""




#word search 
graph = {1:['A',{2: 'right',4: 'down'}], 2:['E',{1: 'left',3: 'right',5: 'down'}],3:['E',{2: 'left',6: 'down'}],4:['E',{1: 'up',5: 'right'}],5:['E',{2: 'up',4: 'left',6: 'right'}],6:['E',{3: 'up',5: 'left'}], } #(id: [letter, neighbor_id_list])
word = "ATE"




#assume starting at index 0 (will iterate this starting. only start at nonzero nodes/letters)
start = 1 #id=0
fringe = [(start, None, None, [])] #(id, direction, letter of word index)
largest_substring_path = []

while(len(fringe)!=0):
    prev_fringe_len = len(fringe)
    current_id, current_direction, first_index, current_path = fringe.pop()
    
    #find the next nodes to expand
    for node in graph[current_id][1]:
        if graph[current_id][0] in word:
            if current_direction == None:
                orig_index = word.index(graph[current_id][0])
                current_path = [current_id]
                
                if orig_index < len(word) - 1:
                    #getting node's individual value
                    added_score = 0
                    if graph[node][0] == word[orig_index + 1]:
                        added_score = 1
                        first_index = orig_index + 1
                        
                    
                    if added_score > 0:
                        current_path.append(node)
                        fringe.append((node, graph[current_id][1][node], first_index, current_path))
                    
            
            else:
                
                if first_index < len(word)-1:
                    
                    if graph[current_id][1][node] == current_direction:
                        added_score = 0
                        
                        
                        if graph[node][0] == word[first_index + 1]:
                            added_score = 1
                        
                        if added_score > 0:
                            current_path.append(node)
                            fringe.append((node, current_direction, first_index + 1, current_path))
     
    new_fringe_len = len(fringe)                    
    if prev_fringe_len >  new_fringe_len: #This means that no new nodes have been added. That means the full substring has been found for that direction.
        #check for largest path
        if len(largest_substring_path) < len(current_path):
            largest_substring_path = current_path



print(largest_substring_path)
        
        
    
    