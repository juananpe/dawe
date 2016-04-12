# -*- coding: utf-8 -*-
import StringIO
import csv
from subprocess import check_output

script = "/tmp/dawe/test/jsfiddle.js"

fich = """,Práctica del Arkanoid - I  (Curso DAWE 2015-2016),,
,Sección,URL,Solución
,2,http://jsfiddle.net/f46aaocf/,http://jsfiddle.net/rx9xh97s/
,3.1,http://jsfiddle.net/juanan/e5g6wp5q/,http://jsfiddle.net/gw2tzt8t/1/
,3.2,http://jsfiddle.net/juanan/ttwc6w1a/,http://jsfiddle.net/o7g0axfh/6/
,4,http://jsfiddle.net/juanan/3rt78ujx/,http://jsfiddle.net/koLjohLj/11/
,5,http://jsfiddle.net/juanan/7fx62awb/,http://jsfiddle.net/8u8uod7c/6/
,6,http://jsfiddle.net/tmws5vzm/1/,http://jsfiddle.net/har5xhvg/4/
,6.1,http://jsfiddle.net/o9ny1qzj/,http://jsfiddle.net/vnt62s8o/3/
,7,http://jsfiddle.net/uvxdb6pb/,http://jsfiddle.net/em8s3axu/2/
,7.1,http://jsfiddle.net/tmocn6Lv/,http://jsfiddle.net/x087Lnqk/4/
,8,http://jsfiddle.net/5y9a53oy/,http://jsfiddle.net/sdo9by99/8/
,8.1,http://jsfiddle.net/qwdcr78m/,http://jsfiddle.net/L39pr3v7/3/
,8.2,http://jsfiddle.net/pwap8xea/,http://jsfiddle.net/sauncqx2/2/"""

s = StringIO.StringIO(fich)
next(s) # skip first line

input_file = csv.DictReader(s)
for line in input_file:
  output = check_output(["/tmp/phantomjs-2.1.1-macosx/bin/phantomjs", script, line['Solución']])
  print line['Sección'], line['Solución'], output,
