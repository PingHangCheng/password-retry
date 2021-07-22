''' 
密碼重設程式
password = 'a123456'
讓使用者重複輸入密碼
最多輸入3次
如果正確，就印出 "登入成功！"
如果不正確，就印出 "密碼錯誤！ 還有__次機會！"
'''
password = 'a123456'
number = 0
left_chance = 3-number #剩於機會
while left_chance > 0:
    user_pwd = input('請輸入密碼(最多3次): ')
    number += 1
    left_chance = 3 - number
    if user_pwd == password:
        print('登入成功')
        break #逃出迴圈
    else:
        print('密碼錯誤! 還有', left_chance, '次機會')
        
