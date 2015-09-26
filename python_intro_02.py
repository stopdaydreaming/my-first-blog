#define function
# def hi():
# 	print('hi there!')
# 	print('how are you?')
# hi()

#define function
# def hi(name):
# 	if name == 'ola':
# 	 	print('hi ola')
# 	elif name == 'sonja':
# 		print('hi sonja')
# 	else: #name is not defined
# 		print('hi anonymous')
# hi('ola')

#define function
# def hi(name):
# 	print('hi ' + name + '!')
# hi('rachel')

def hi(name):
	print('hi' + name + '!')
girls = ['rachel','monica','phoebe','ola','you']
for name in girls:
	hi(name)
	print('next girl')
