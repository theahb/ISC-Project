def read():
  f = open("input", 'r')
  line = f.readline()
  split = line.split()
  c =float(split[2])

  line = f.readline()



  for line in f:
    print(line)


  #clean up
  f.close()

