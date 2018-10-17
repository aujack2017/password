password = 'a123456'
inputpass = input('請輸入密碼：')
x = 1
while inputpass != password:
#	x = 1
#	if x == 3:
#	    break
#	else:
	print('密碼錯誤喔!!請重新輸入')
	x = x + 1
	print(x)
	inputpass = input('請輸入密碼：')
	if x == 3:
		break

