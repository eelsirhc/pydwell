#!/usr/bin/env python

filename="nist_table"

input = open(filename)
skiplines = 9
for i in range(skiplines):
    input.readline()

output = open("__init__.py",'w')
output.write("{\n")
for line in input:
#    print line
    data={  "Quantity": line[0:55].rstrip(),
            "Value": line[55:77].replace(" ","").replace("...",""),
            "Uncertainty": line[77:99].replace(" ","").replace("(exact)","0.0"),
            "Unit": line[99:].rstrip()
            }
    output.write("\"{0}\":".format(data["Quantity"]))
    output.write("{")
    output.write("\"Value\": {0}, \"Uncertainty\": {1}, \"Unit\": \"{2}\"".format(data["Value"] , data["Uncertainty"], data["Unit"]))
    output.write("},\n")
output.write("}\n")    
output.close()
