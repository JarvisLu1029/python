while True:
    num = int(input('猜數字1~100: '))
    if num == 28:
        print('恭喜中獎')
        break
    elif num > 100 or num < 1:
        print('請輸入1~100的數字')
    else:
        print('輸入錯誤')