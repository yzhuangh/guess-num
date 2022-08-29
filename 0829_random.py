import random #使用別人寫好的功能
r = random.randint(1, 100)
#standard library 標準化函式庫
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
