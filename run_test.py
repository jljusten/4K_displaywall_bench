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

def run_one_test(num_images, image_file):
    args = ["./4K_displaywall_bench", "-width", "11520", "-height", "2160",
            "-testmode", "fps"]
    if num_images > 0:
        args += ["-swap_interval", "0", "-mipmap", "true", "-layout", "true"]
    for i in range(num_images):
        args += ["-i", image_file]
    if num_images == 0:
        print 'Running with 0 images'
    else:
        print 'Running with', num_images, 'copies of', image_file
    return subprocess.check_output(args, cwd=local_cwd)

def read_rows():
    rows = []
    if os.path.isfile(csvfile):
        with open(csvfile, 'rb') as cf:
            reader = csv.reader(cf)
            for row in reader:
                rows.append(row)
            cf.close()
    return rows

num_images = (0, 1, 2, 3, 4, 5, 10)

number_of_tests = len(num_images)
# add one row for the column label
number_of_rows = number_of_tests + 1

rows = read_rows()

if len(rows) != number_of_rows:
    with open(csvfile, 'wb') as cf:
        writer = csv.writer(cf)
        writer.writerow(["num images"])
        for i in num_images:
            writer.writerow([str(i)])
        cf.close()
    rows = read_rows()

def run_tests_for_size(rows, size):
    column_label = ' '.join(("FPS", distname, version, size))
    row = rows[0]
    row.append(column_label)

    #basic 3x 4K viewport test
    for i in range(len(num_images)):
        image_file = "./images/bubble" + size + ".png"
        data = run_one_test(num_images[i], image_file)
        row = rows[i + 1]
        row.append(data)

def write_csv(filename, rows):
    with open(csvfile, 'wb') as cf:
        writer = csv.writer(cf)
        for row in rows:
            writer.writerow(row)
        cf.close()

run_tests_for_size(rows, '1K')
run_tests_for_size(rows, '4K')
write_csv(csvfile, rows)

print csvfile, " has been written with test data."
