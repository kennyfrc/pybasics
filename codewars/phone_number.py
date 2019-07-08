import pdb

def create_phone_number(num):
	# '12345678910'
	# join() joins elements in a list
	# map() takes a func and an iterator and uses the func on the iterator
	# '' is the string you want to join them to
    num_str = ''.join(map(str,num))

    # num_str[:3] takes the first 3 elements in a string 0-2
    # '%s'%() is the format that you want to use. s is string.
    return '(%s) %s-%s'%(num_str[:3], num_str[3:6], num_str[6:])

print(create_phone_number([1,2,3,4,5,6,7,8,9]))