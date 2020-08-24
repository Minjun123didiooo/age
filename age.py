driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
	    print('你成功考取駕照了')
	else: 
		print('奇怪 你怎麼能開車')
elif driving == '沒有':
    if age >= 18:
        print('你可以嘗試開車喔')
    else:
        print('你再過幾年就能嘗試去考駕照了')		
