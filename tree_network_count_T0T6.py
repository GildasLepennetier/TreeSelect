#!/usr/bin/python


import sys, os, re

DIRECTORY_1=sys.argv[1] #directory with the sorted png
DIRECTORY_2=sys.argv[2] #directory with the reference pir files


if DIRECTORY_1[-1][-1] == "/":
	DIRECTORY_1=DIRECTORY_1[:-1]
	
TYPE_FOLDER=os.path.basename(DIRECTORY_1)
FILES=os.listdir(DIRECTORY_1) # uses the .png files in a given directory1
if not FILES: exit()

pattern_name = re.compile(">(.*)")   #to match the pir/fasta id

T0=0
T6=0
SEQ_NB=0
for PNG in FILES:
	TOLOAD=DIRECTORY_2 + "/" + ".".join(PNG.split('.')[:-3]) # remove the .out.png to get the source of the data (pir file)
	if not os.path.exists(TOLOAD):
		sys.stderr.write("WARNING: %s does not exists\n"%(TOLOAD))
		continue
	with open(TOLOAD) as fi:
		for rline in fi.readlines():
			if pattern_name.match(rline):
				MATCH=pattern_name.search(rline).group(1)
				if "G.L." not in MATCH: #skip germline
					SEQ_NB+=1
					TISSUE=MATCH.split('.')[1].upper()
					CELLTYPE=MATCH.split('.')[2].upper()
					TIMEPOINT=MATCH.split('.')[3].upper()
					
					
					if CELLTYPE not in ["ME","NA","PB","GC"]: 
						sys.stderr.write("WARNING: cell type not recognized %s %s\n"%(CELLTYPE,TOLOAD))
					if TIMEPOINT not in ["T0","T6"]: 
						sys.stderr.write("WARNING: time not recognized %s %s\n"%(TIMEPOINT,TOLOAD))
					if TISSUE not in ["BL","CSF"]: 
						sys.stderr.write("WARNING: tissue not recognized %s %s\n"%(TISSUE,TOLOAD))
					
					
					if TIMEPOINT == "T0":
						T0+=1
					if TIMEPOINT == "T6":
						T6+=1
print("\t".join([str(el) for el in [T0,T6,SEQ_NB,DIRECTORY_1]]))

	






