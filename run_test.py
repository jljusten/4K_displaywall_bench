#!/usr/bin/env python

import os
import sys, getopt
import subprocess
import platform
import csv

local_cwd = os.path.dirname(os.path.realpath(__file__))
print local_cwd
os.chdir(local_cwd)
distname, version, Id = platform.linux_distribution()
print distname, version

csvfile = 'report.csv'
try:
  opts, args = getopt.getopt(sys.argv[1:], "hf:", ["csvfile="])
except getopt.GetoptError:
  print 'run_test.py --csvfile <outputfile>'
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
    print 'run_test.py --csvfile <outputfile>'
    sys.exit()
  elif opt in ("-f", "--csvfile"):
    csvfile = arg

number_of_tests = 7
# add one row for the column label
number_of_rows = number_of_tests + 1

rows = []
append_to_existing_data = False
if os.path.isfile(csvfile):
  with open(csvfile, 'rb') as cf:
    reader = csv.reader(cf)
    for row in reader:
      rows.append(row)
  cf.close()
  if len(rows) != 0:
    append_to_existing_data = True

with open(csvfile, 'wb') as cf:
  writer = csv.writer(cf)
  column_label = "FPS " + distname + version
  if append_to_existing_data:
    row = rows[0]
    row.append(column_label)
    writer.writerow(row)
  else:
    writer.writerow(["num images", column_label])

#basic 3x 4K viewport test
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-testmode", "fps"
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[1]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["0", data])


#1 image
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-mipmap", "true", "-layout", "true",
                                      "-testmode", "fps",
                                      "-i", "./images/bubble4K.png",
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[2]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["1", data])

#2 images
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-mipmap", "true", "-layout", "true",
                                      "-testmode", "fps",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[3]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["2", data])

#3 images
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-mipmap", "true", "-layout", "true",
                                      "-testmode", "fps",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[4]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["3", data])

#4 images
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-mipmap", "true", "-layout", "true",
                                      "-testmode", "fps",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[5]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["4", data])

#5 images
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-mipmap", "true", "-layout", "true",
                                      "-testmode", "fps",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[6]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["5", data])

#10 images
  data = subprocess.check_output(
           ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
                                      "-swap_interval", "0",
                                      "-mipmap", "true", "-layout", "true",
                                      "-testmode", "fps",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      "-i", "./images/bubble4K.png",
                                      ], cwd=local_cwd)
  if append_to_existing_data:
    row = rows[7]
    row.append(data)
    writer.writerow(row)
  else:
    writer.writerow(["10", data])


print csvfile, " has been written with test data."
