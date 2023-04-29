def add_time(start, duration, day = None):
  amPm = start[len(start)-2 :]
  daysLater = 0
  dt = {
    "saturday" : 0,
    "sunday" : 1,
    "monday" : 2,
    "tuesday" : 3,
    "wednesday" : 4,
    "thursday" : 5,
    "friday" : 6
  }

  new_time = ""
  dayNew = ""
  
  c1 = start.index(":")
  h1 = int(start[:c1])
  m1 = int(start[c1+1 : c1+3])

  c2 = duration.index(":")
  h2 = int(duration[:c2])
  m2 = int(duration[c2+1:])

  daysLater = int(h2 / 24)

  if(h1 + (h2 % 24) >= 12 and amPm == "PM"):
    daysLater = daysLater + 1
  if(m1+m2 >= 60 and h1 == 11 and amPm == "PM"):
    daysLater = daysLater + 1

  h3 = 0
  m3 = m1 + m2
  
  if m3 >= 60:
    m3 = m3 % 60
    h3 = h3 + 1

  if m3 < 10:
    m3 = str(m3)
    m3 = "0" + m3 
  
  if h1+(h2%24)+h3 >= 12 and h1+(h2%24)+h3 < 24:
    if amPm == "AM": amPm = "PM"
    else: amPm = "AM"
      
  h3 = h3 + (h1+ (h2%24)) % 12
  
  if(day != None):
    day = day.lower()
    x = dt[day]
    x = (x + daysLater) % 7
    dayNew = list(dt.keys())[list(dt.values()).index(x)]
    dayNew = dayNew[0].upper() + dayNew[1:]
    
  if daysLater == 0: 
    new_time = new_time + str(h3) + ":" + str(m3) + " " + amPm
    if day != None:
      new_time = new_time + ", " + dayNew
  
  else: 
    new_time = new_time + str(h3) + ":" + str(m3) + " " + amPm
    if day != None:
      new_time = new_time + ", " + dayNew
    if daysLater == 1 : new_time = new_time + " (next day)"
    else:
      new_time = new_time + " (" + str(daysLater) + " days later)"
  
  return new_time


print(add_time("11:06 PM", "2:02"))
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
