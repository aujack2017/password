password = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功!!')
		break
	elif i == 1:
		break
	else:
		i -= 1
		print('')
		print('密碼錯誤 , 還有' , i , '次機會')
