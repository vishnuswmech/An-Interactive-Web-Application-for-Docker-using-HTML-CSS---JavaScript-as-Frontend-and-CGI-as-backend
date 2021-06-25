#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type:text/html")
print()

s=cgi.FieldStorage()
cmd=s.getvalue("x")

output=sp.getoutput("sudo {}".format(cmd))
print(output)


