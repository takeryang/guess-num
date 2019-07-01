print('這是一個猜數字的遊戲程式')
import random
start = input('請決定開始數字: ')
end = input('請決定結束數字: ')
start = int(start)
end = int(end)
print('遊戲開始')
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大!!')
	elif num < r:
		print('比答案小!!')
	print('這是你猜的第', count, '次')
