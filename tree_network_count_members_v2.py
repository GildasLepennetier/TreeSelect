#!/usr/bin/python

#
# Program to count timepoint, tissue and cell type
# uses the .png files in a given directory1
# remove the .out.png to get the source of the data (pir file)
# search this pir file in another directory2
# ignore the germline, but count the celltype, tissue and timepoint
#

import sys, os, re

pattern_name = re.compile(">(.*)")
pattern_patient=re.compile("(S\d+)")

DIRECTORY_1=sys.argv[1] #directory with the sorted png
DIRECTORY_2=sys.argv[2]


if DIRECTORY_1[-1][-1] == "/":
	DIRECTORY_1=DIRECTORY_1[:-1]
TYPE_FOLDER=os.path.basename(DIRECTORY_1)
FILES=os.listdir(DIRECTORY_1) # uses the .png files in a given directory1
if not FILES: exit()
PATIENT=pattern_patient.search(DIRECTORY_1).group(1)
for PNG in FILES:
	TOLOAD=DIRECTORY_2 + "/" + ".".join(PNG.split('.')[:-3]) # remove the .out.png to get the source of the data (pir file)
	if not os.path.exists(TOLOAD):
		sys.stderr.write("WARNING: %s does not exists\n"%(TOLOAD))
		continue
	T0_CSF_count_CellType={"ME":0,"NA":0,"PB":0,"GC":0}
	T0_BLOOD_count_CellType={"ME":0,"NA":0,"PB":0,"GC":0}
	T6_CSF_count_CellType={"ME":0,"NA":0,"PB":0,"GC":0}
	T6_BLOOD_count_CellType={"ME":0,"NA":0,"PB":0,"GC":0}
	SEQ_NB=0
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
						if TISSUE == "CSF":
							T0_CSF_count_CellType[CELLTYPE]+=1
						if TISSUE == "BL":
							T0_BLOOD_count_CellType[CELLTYPE]+=1
					if TIMEPOINT == "T6":
						if TISSUE == "CSF":
							T6_CSF_count_CellType[CELLTYPE]+=1
						if TISSUE == "BL":
							T6_BLOOD_count_CellType[CELLTYPE]+=1
	print ("\t".join( [ str(el) for el in [ PATIENT,TYPE_FOLDER, SEQ_NB, 
					 T0_CSF_count_CellType["ME"],
					 T0_CSF_count_CellType["NA"],
					 T0_CSF_count_CellType["PB"],
					 T0_CSF_count_CellType["GC"],
					 T0_BLOOD_count_CellType["ME"],
					 T0_BLOOD_count_CellType["NA"],
					 T0_BLOOD_count_CellType["PB"],
					 T0_BLOOD_count_CellType["GC"],
					 T6_CSF_count_CellType["ME"],
					 T6_CSF_count_CellType["NA"],
					 T6_CSF_count_CellType["PB"],
					 T6_CSF_count_CellType["GC"],
					 T6_BLOOD_count_CellType["ME"],
					 T6_BLOOD_count_CellType["NA"],
					 T6_BLOOD_count_CellType["PB"],
					 T6_BLOOD_count_CellType["GC"],
					 os.path.basename(TOLOAD) ] ] ))

#summary at folder level possible here


