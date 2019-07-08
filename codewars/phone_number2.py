

def phone_number(num):
	num_str = ''.join(map(str,num))
	return '(%s) %s-%s'%(num_str[:3],num_str[3:6],num_str[6:])

print(phone_number([1,2,3,4,5,6,7,8,9]))