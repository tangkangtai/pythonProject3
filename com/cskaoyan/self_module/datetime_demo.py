#datetime 处理日期和时间的标准库

#获取当前的日期和时间
from datetime import datetime ,timedelta ,timezone
now = datetime.now()
print(now)

print(type(now))

#用指定时间创建datetime
dt = datetime(2015,4,19,12,20)
print(dt)


#datetime转换为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
#对应的北京时间
#timestamp = 0 = 1970-1-1 08:00:00 UTC +8:00

dt = datetime(2015,4,19,12,20)#用指定日期创建datetime
dt.timestamp() #将datetime 转换为timestamp
print(dt.timestamp()) #timestamp是一个浮点数 整数位表示秒 


#----------------------------------------------
print('-------------------------')
#----------------------------------------------
t = 1429417200.0
print(datetime.fromtimestamp(t))

#--------------------------------
print('--------------------')
#--------------------------------
#转化UTC标准时区的时间

print(datetime.utcfromtimestamp(t))


#------------------------------------
print('--------------------')
#------------------------------------
#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)


#----------------------------------
print('----------------')
#----------------------------------
#datetime转换为str
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

print('--------------------------')

#datetime加减
#需要导入timedelta
now = datetime.now()
print(now)

print(now + timedelta(hours=10))

print(now - timedelta(days=1))

print(now + timedelta(days=2,hours=12))

#--------------------------------------
print('-----------------------')
#--------------------------------------

#本地时间转换为UTC时间
#datetime类型有一个时区属性tzinfo  默认为None  所以无法区分这个datetime到底是哪个时区
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
print('----------------------')

dt = now.replace(tzinfo=tz_utc_8) #强制设置为UTC+8:00
print(dt)

#--------------------------
print('----------------------')
#--------------------------
#时区转换
#拿到utc时间 并强制设置为时区为UTC +0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

#astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)



