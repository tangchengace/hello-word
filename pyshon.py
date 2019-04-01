def dayup(df):
    dayup=1
    for i range(365)：
        if i%7 in [6,0]：
            dayup=dayup*0.99
        else：
            dayup=dayup*(1+df)
    return df
dayfactor=0.01
while dayup(dayfactor)<37.78:
    dayfactor+=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor)
