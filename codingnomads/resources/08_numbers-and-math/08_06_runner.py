# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# speed = distance / time
# we want distance in km and time in hours

#distance in km
miles = 10 #miles
#km per mile times mile equals km
km_per_mile = 1.6
distance = miles*km_per_mile

#time in hours
mins = 30 +(30/60)
mins_per_hour = 60
time = mins / mins_per_hour

#km per hour
print("speed: ", distance/time)