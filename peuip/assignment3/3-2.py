dust = int(input())

if dust >= 76:
    print("매우 나쁨")
elif 35 < dust & dust < 76:
    print("나쁨")
elif 15 < dust & dust < 36:
    print("보통")
else:
    print("좋음")