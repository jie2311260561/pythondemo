#A B 相比较

def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup

dayfactor = 0.01

while dayup(dayfactor) < 37.78:
    dayfactor += 0.01

print('{:.4f}'.format(dayfactor))