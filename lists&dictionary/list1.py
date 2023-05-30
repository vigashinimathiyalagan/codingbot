############## Problem  1 #################### 
#Ask first friend the colors they like. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.

shini_colors = ["black", "yellow", "green", "orange"]
reema_colors = ["black", "green", "brown", "yellow", "purple"]

common_colors = []

for color in shini_colors:
    if color in reema_colors:
        common_colors.append(color)
        print("You both like", color)

print("Common colors:", common_colors)

output:
  You both like black
You both like yellow
You both like green
Common colors: ['black', 'yellow', 'green']
  
  
