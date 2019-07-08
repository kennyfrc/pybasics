import pdb

def pascal(p):
	tri = []
	tri_range = range(p)
	for tri_level in tri_range:
		new_level = []
		new_level_range = range(tri_level + 1)
		for element in new_level_range:
			if element == 0 or element == tri_level:
				new_level.append(1)
			else:
				prev_row = tri[tri_level-1]
				new_level.append(prev_row[element - 1] + prev_row[element])
		tri.append(new_level)
	return tri

print(pascal(10))

# initialize triangle
# initialize range
# for each level in the range
# 	initialize the level
# 	initialize the range of the new level
#	for each k_element in the new_level_range
#		if starting_element or end_element
#			use 1
# 		else
#			get the previous row
#			initilize the new level with the previous row's k-1 elemeent and the preview's row's k lemeent
# 	append the new_level to the triangle
# return the triangle