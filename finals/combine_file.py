import glob

# Combine all fines and write to out.txt
for num in xrange(0, 10000):
  number = '{0:04}'.format(num)

  read_files = glob.glob("./graph_data_files/*")
  with open("out.txt", "wb") as outfile:
    for f in read_files:
      with open(f, "rb") as infile:
        outfile.write(infile.read())

