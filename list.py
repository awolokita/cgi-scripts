#! /usr/bin/python
#
import os

path = "/home/httpd/lib"

lof = []
for (dirpath, dirnames, filenames) in os.walk(path):
  for filename in sorted(filenames):
    if filename.endswith('.so'):
      lof.append(filename)

print "Content-Type: text/html\n\n"
print '<html><head>'
print '<title>Python GCI libcheck</title>'
print '<body>'
print '<h3>Lib files found:</h3>'
for item in lof:
  print "%s <br>" % (item)
print '</body>'
print '</html>'
