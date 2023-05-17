# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:12:05 2023

@author: hsien
"""
import matplotlib.pyplot as plt
import sys
import random


def number_dots():
    number = int(input("Please enter how many dots are in the graph: "))
    print("The number of dots in the graph is : ", number)
    return number

def get_dots(number_dots):
    dot_list = []
    number_dots   
    for i in range (number_dots):
        variable = f"dot#{i}_x", f"dot#{i}_y"
        variable = input(f"Please enter the coordinates of dot#{1+i}, X and Y seperated by a space (e.g. 1 2):").split( )
        variable = float(variable[0]), float(variable[1])
        dot_list.append(variable)
    return(dot_list)

def draw_dots(dot_list):
    # Create a 25x25 plot
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim([0, 25])
    ax.set_ylim([0, 25])
    ax.set_aspect('equal')
    plt.grid(True, which='major', axis='both')
    
    # Add dots
    for dot in dot_list:
        ax.scatter(dot[0], dot[1], c ='blue')
        ax.text(dot[0] + 0.5, dot[1] - 1, f"#{1+dot_list.index(dot)}", fontsize=10 , c = 'blue')
                
    # Show the plot
    plt.show()

def get_lines(dot_list):
    line_list = []
    number_lines = int(input("Please enter how many lines are in the graph: "))
    for i in range(number_lines):
        line = input(f"Please enter the dots connected by line#{i+1} (e.g. '1 2' meaning dot 1 & 2 on the plot) :").split( )
        line = int(line[0]), int(line[1])      
        line_list.append(line)
    return(line_list)
    
def draw_lines(line_list, dot_list):    
    # Create a 25x25 plot
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim([0, 25])
    ax.set_ylim([0, 25])
    ax.set_aspect('equal')
    plt.grid(True, which='major', axis='both')
    
    # Add dots
    for dot in dot_list:
        ax.scatter(*dot, c ='blue')
        ax.text(dot[0] + 0.5, dot[1] - 1, f"#{1+dot_list.index(dot)}", fontsize=10 , c = 'blue')
    
    dotdot_list = []
    for i in range(len(line_list)):
        line = line_list[i]
        dot1x,dot1y = float(dot_list[line[0]-1][0]), float(dot_list[line[0]-1][1])
        dot2x, dot2y = float(dot_list[line[1]-1][0]), float(dot_list[line[1]-1][1])
        
        # ax.scatter([dot1x, dot1y], [dot2x, dot2y], color = 'blue')
        ax.plot([dot1x, dot2x], [dot1y, dot2y], color='red')

    plt.show()

def get_dotID(dot_list):
    dotID_list = []
    for dot in dot_list:
        dotID = 1 + dot_list.index(dot)
        dotID_list.append(dotID)
    
    return(dotID_list)
    
def get_vectors(line_list, dot_list):
    vector_list = []
    for i in range(len(line_list)):
        line = line_list[i]   
        dot1 = dot_list[line[0]-1]
        dot2 = dot_list[line[1]-1]
        
        vector = (dot1[0]-dot2[0], dot1[1]-dot2[1])
        vector_list.append(vector)
    return(vector_list)


'''
---below code to obtain dots and line info---
'''
 
number_dots = number_dots()
dot_list = get_dots(number_dots)
dotID_list = get_dotID(dot_list)
print(dot_list)
print(dotID_list)
drawing = draw_dots(dot_list)
print('Check on the graph and use the dot labels to describe the lines')
line_list = get_lines(dot_list)
draw_lines(line_list, dot_list)
check = str(input("Please confirm if the dots are drawed appropriately before process forward? (y/n)"))
if check == 'n':
    print("No worries, let's start over :)")
    sys.exit() #stop the program

print('Program processes forward to game solving :)')

'''
---below code to solve the game---
'''
# Create a new 25x25 plot for solution
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim([0, 25])
ax.set_ylim([0, 25])
ax.set_aspect('equal')
plt.grid(True, which='major', axis='both')

# Add dots
for dot in dot_list:
    ax.scatter(dot[0], dot[1], c ='blue')
    ax.text(dot[0] + 0.5, dot[1] - 1, f"#{1+dot_list.index(dot)}", fontsize=10 , c = 'blue')


vector_list = get_vectors(line_list, dot_list)
vector_direction =[-1, 1]
verify = 'false'
vector_list_ordered = []
dot_list_ordered = []

# randomize the order of the vectors
for i in range(len(vector_list) - 1):
    if vector_list[i] == vector_list[i+1] * -1:
        # If there are, shuffle the list and check again
        random.shuffle(vector_list)
        i = 0  # start again from the beginning of the list


while verify == 'false': # while-1
    dot_list_ordered = []
    for dot in dot_list: # get a dot to start from                        
        dot_list_ordered.append(dot)                   
        if len(vector_list_ordered) == len(line_list):
            dot_test = 'true'
            verify = 'true'
            continue
        current_dot = dot
        vector_list_temp = vector_list
        dot_test = 'false'
        
        while dot_test == 'false':
            direction_times_vector = (0,0)
            for vector in vector_list_temp:
                
                if len(vector_list_temp) == 0:
                    dot_test = 'true'
                    verify = 'true'
                    continue
                direction_check = 'false'
                for direction in vector_direction:
                    if direction_check == 'true':
                        continue
                    
                    if len(vector_list_temp) == 0:
                        dot_test = 'true'
                        verify = 'true'
                        continue
                    
                    direction_times_vector = (direction*vector[0] , direction*vector[1])
                    next_dot = (current_dot[0] + direction*vector[0] , current_dot[1] + direction*vector[1])
                    
                    if next_dot not in dot_list:
                        direction_check = 'false'
                        
                    else:
                        direction_check = 'true'
                        vector_list_temp.remove(vector)
                        vector_list_ordered.append(direction_times_vector)
                        
                        current_dot = next_dot
                        
                        if len(vector_list_temp) == 0:
                            dot_test = 'true'            
                            verify = 'true'
                            break

starting_dot_list = []                            
starting_dot = dot_list_ordered[0]                        
for v in vector_list_ordered:    
    starting_dot_list.append(starting_dot)
    ax.arrow(starting_dot[0], starting_dot[1], v[0], v[1], head_width=0.8, head_length=0.8, fc='k', ec='k')    
    starting_dot = (starting_dot[0] + v[0], starting_dot[1] + v[1])
plt.show()
starting_dot_list.append(starting_dot)


print('dot_list = ', dot_list)
print('line_list = ', line_list)
print('starting point = ', starting_dot)
print('drawing_ordered = ', starting_dot_list)






