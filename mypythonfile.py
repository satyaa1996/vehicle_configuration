speed = int(raw_input("what is your speed?"))

if (speed < 10):
    print "first gear"
elif (speed >= 10 and speed < 30):
    print "second gear"
elif (speed >= 30 and speed < 40):
    print "third gear"
elif (speed >= 40 and speed < 60):
    print "fourth gear"
# elif (speed > 60):
#         print "fifth gear"
else:
   print "get lost"
