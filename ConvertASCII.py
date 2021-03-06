#!/usr/bin/python

from struct import unpack
file = "Blocks"
fileNew = file + "ASCII"
f = open(file + ".stl","rb")

header = f.read(80)
numfacets = unpack("<I",f.read(4))[0]



with open(fileNew + ".stl", 'w') as fw:
        fw.write("solid stock" + "\n")
        for i in range(1,numfacets):
            a1 = unpack("<f",f.read(4))[0]
            a2 = unpack("<f",f.read(4))[0]
            a3 = unpack("<f",f.read(4))[0]

            v11 = unpack("<f",f.read(4))[0]
            v12 = unpack("<f",f.read(4))[0]
            v13 = unpack("<f",f.read(4))[0]

            v21 = unpack("<f",f.read(4))[0]
            v22 = unpack("<f",f.read(4))[0]
            v23 = unpack("<f",f.read(4))[0]

            v31 = unpack("<f",f.read(4))[0]
            v32 = unpack("<f",f.read(4))[0]
            v33 = unpack("<f",f.read(4))[0]

            attribs = unpack("<H",f.read(2))
            fw.write("facet normal " + str(a1) + " " + str(a2) +" " + str(a3) + "\n")
            fw.write("  outer loop" + "\n")
            fw.write("    vertex " + str(v11) + " " + str(v12) + " " + str(v13) + "\n")
            fw.write("    vertex " + str(v21) + " " + str(v22) + " " + str(v33) + "\n")
            fw.write("    vertex " + str(v31) + " " + str(v32) + " " + str(v33) + "\n")
            fw.write("  endloop" + "\n")
            fw.write("endfacet" + "\n")
        fw.write("endsolid stock" + "\n")
