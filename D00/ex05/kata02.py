date = (3, 30, 2019, 9, 25)
#  print(str(date[3]) + "/" + str(date[4]) +)

print(str("{0:0=2d}".format(date[3])) + "/" +
      str("{0:0=2d}".format(date[4])) + "/" +
      str("{0:0=4d}".format(date[2])) + " " +
      str("{0:0=2d}".format(date[0])) + ":" +
      str("{0:0=2d}".format(date[1])))
