# -*- coding: utf-8 -*-
import StringIO
import csv
import urllib2
from subprocess import check_output

script = "/tmp/dawe/test/jsfiddle.js"
phantomjs = "/tmp/phantomjs-2.1.1-macosx/bin/phantomjs" 
export ="/export?format=csv"

with open("/tmp/urls_nombre.txt") as f:
   for line in f:
      url = line.split(' ')[0]
      nombre = ' '.join(line.split(' ')[1:])
      print " ", url, " ", nombre,
      csvf = "{0}{1}".format(url,export)
      # print csvf
      # raw_input("Press Enter to continue...")
      fich = urllib2.urlopen(csvf).read()

      s = StringIO.StringIO(fich)
      next(s) # skip first line

      input_file = csv.DictReader(s)
      for line in input_file:
          url = line['Solución']
          if not url.startswith("http://"):
             url = "{0}{1}".format("http://",url)

          output = check_output([phantomjs, script, url])
          print line['Sección'], url, output,
