import datetime

x=datetime.datetime.now()
w=x.replace(microsecond=0)

print(w)