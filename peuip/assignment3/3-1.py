my = input()
other = input()

if my == other:
    print("무승부")
elif my == "가위":
    if other == "바위":
        print("패배")
    else:
        print("승리")
elif my == "바위":
    if other == "보":
        print("패배")
    else:
        print("승리")
else:
    if other == "가위":
        print("패배")
    else:
        print("승리")