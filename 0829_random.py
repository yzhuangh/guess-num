import random #使用別人寫好的功能
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
#standard library 標準化函式庫
while True:
	count += 1 #與count = count + 1相同
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
