#For easy datetime goto maya library in github
import datetime
import pytz
today=datetime.date.today()
print(today)

birth_date=datetime.date(1982,5,4)#yyyy m d
print(birth_date)

day_since_birth=(today-birth_date).days
print(day_since_birth)
#https://youtu.be/4F2m91eKmts?t=13532

print(today.day) #1-31
print(today.weekday()) #m=0 sun=6

print(datetime.time(7,13,54,56))#h,m,s,ms
print(datetime.date(2020,3,29))#y,m,d
print(datetime.datetime(2020,3,29,7,16,15,45))#y,m,d,h,m,s,ms

hours_delta=datetime.timedelta(hours=10)
print(datetime.datetime.now()+hours_delta)

#print(datetime.datetime.now(tz=pytz.UTC))
datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_pacific=datetime_today.astimezone(pytz.timezone('US/pacific'))
print(datetime_pacific)

for tz in pytz.all_timezones:
    print(tz)

#string formating with dates
#2020-3-29-->march 09,2020
#strftime(f=formatting)
print(datetime_pacific.strftime('%B %d, %Y'))

#march 09,2020-->datetime(2020,3,29)
datetime_thing=datetime.datetime.strptime('march 29,2020','%B  %d,%Y')
print(datetime_thing)