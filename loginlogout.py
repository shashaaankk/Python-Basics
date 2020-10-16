import datetime
def get_month(MM):
    months={
        "01":1,
        "02":2,
        "03":3,
        "04":4,
        "05":5,
        "06":6,
        "07":7,
        "08":8,
        "09":9,
        }
    return months.get(MM)
tday=datetime.datetime.today().date()
tday=str(tday)
YYYY,MM,DD=tday.split("-")
if(int(MM)<10):
    MONTH=get_month(MM)
#print(YYYY,MM,DD)
#print(MONTH)
def log_in():
    userip=input("Enter Log in as HH:MM:SS: ")
    #print(userip)
    HH,MM,SS=userip.split(":")
    #print(HH,MM,SS)
    logged_in_at=datetime.datetime(int(YYYY),int(MONTH),int(DD),int(HH),int(MM),int(SS))
    return logged_in_at
def log_out():
    userip=input("Enter Log out as HH:MM:SS: ")
    #print(userip)
    HH,MM,SS=userip.split(":")
    #print(HH,MM,SS)
    logged_out_at=datetime.datetime(int(YYYY),int(MONTH),int(DD),int(HH),int(MM),int(SS))
    return logged_out_at

p1_log_in=log_in()
p1_log_out=log_out()
p1delta=p1_log_out-p1_log_in
print(p1delta.total_seconds())
