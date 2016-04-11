import urllib2
 
export ="/export?format=csv"

with open("/tmp/urls_nombre.txt") as f:
   for line in f:
      url = line.split(' ')[0] 
      nombre = ' '.join(line.split(' ')[1:])
      print " ", url, " ", nombre,
      csv = "{0}{1}".format(url,export)
      print csv
      raw_input("Press Enter to continue...")
      print urllib2.urlopen(csv).read()

