#!/usr/bin/python


import sys, os, re

DIRECTORY_1=sys.argv[1] #directory with the sorted png
DIRECTORY_2=sys.argv[2] #directory with the reference pir files


if DIRECTORY_1[-1][-1] == "/":
	DIRECTORY_1=DIRECTORY_1[:-1]
	
TYPE_FOLDER=os.path.basename(DIRECTORY_1)
FILES=os.listdir(DIRECTORY_1) # uses the .png files in a given directory1
if not FILES: exit()

T0=0
T6=0
T0_to_T6=0
SEQ_NB=0

re_label = re.compile("label=\"([^\"]*)")

T0CSF_to_T6Bl=0
T0CSF_to_T6CSF=0
T0Bl_to_T6CSF=0
T0Bl_to_T6Bl=0

for PNG in FILES:
	#print (PNG)
	TOLOAD=DIRECTORY_2 + "/" + ".".join(PNG.split('.')[:-1] ) # remove the .out.png to get the source of the data (pir file)
	if not os.path.exists(TOLOAD):
		sys.stderr.write("WARNING: %s does not exists\n"%(TOLOAD))
		continue
		
	#load the network
	NETWORK=[]
	LABELS={}
	PARENTS_LIST=[]
	CHILDS_LIST=[]
	with open(TOLOAD) as handle:
		for rline in handle.readlines():
			line=rline.split("\n")[0]
			if line:
				if " -> " in line: #interraction : 7 -> 40 [fontsize=25, label="33"];
					Match = re_label.search(line) #number of mutations
					if Match:
						MUTATIONS = int(Match.group(1))
					else:
						MUTATIONS=1
					INDEX1=line.split(" ")[0]
					INDEX2=line.split(" ")[2]
					NETWORK.append( ( INDEX1, INDEX2, MUTATIONS ) ) #source, target, label (nb mutation) #here is an edge
					
					PARENTS_LIST.append(INDEX1)
					CHILDS_LIST.append(INDEX2)
					
				else:
					if re.search(r'\d', line.split(" ")[0]):
						ID = line.split(" ")[0]
						Match = re_label.search(line) #name of the sequence
						if Match:
							LAB = Match.group(1)
						else:
							LAB = ""
						LABELS[ID]=LAB #here are the nodes

	#find the root : the only source which is not a target
	LI_ROOT=[ el for el in PARENTS_LIST if el not in CHILDS_LIST ]
	if len(LI_ROOT) >1: 
		#sys.stderr.write("WARNING: Not single arrow from germline %s\n"%TOLOAD)
		pass
		
	ROOT_id=list(set(LI_ROOT))
	if len(ROOT_id) == 1:
		ROOT_id=ROOT_id[0]
		#sys.stderr.write( "germline is %s (%s) for %s\n"%(ROOT_id, LABELS[ROOT_id], TOLOAD) )
	else:
		sys.stderr.write("ERROR: problem with root %s\n"%TOLOAD)
		exit(1)
	
	#check the direct connections
	for tupl in NETWORK:
		
		# count the targets before skipping
		NAME_SOURCE=LABELS[ tupl[0] ]
		NAME_TARGET=LABELS[ tupl[1] ]
		if NAME_TARGET:
			SEQ_NB+=len(NAME_TARGET.split("\\n")) #before skipping the germline to count all sequences
			T0+=[  el.split('.')[3] for el in NAME_TARGET.split("\\n")  ].count("T0")
			T6+=[  el.split('.')[3] for el in NAME_TARGET.split("\\n")  ].count("T6")
		
		#skip count if germline (meaningless T0->T6 of tissue1->tissue2)
		if tupl[0] == ROOT_id:
			continue
		#skip when the reference is an internal node without label
		if not NAME_SOURCE or not NAME_TARGET:
			continue
		T0Bl_to_T6Bl
		#use only list of sequences, since possible to have > 1 per node
		LIST_tissue_source  = list(set([  el.split('.')[1] for el in NAME_SOURCE.split("\\n")  ]))
		LIST_celltype_source= list(set([  el.split('.')[2] for el in NAME_SOURCE.split("\\n")  ]))
		LIST_time_source    = list(set([  el.split('.')[3] for el in NAME_SOURCE.split("\\n")  ]))
		
		LIST_tissue_target  = list(set([  el.split('.')[1] for el in NAME_TARGET.split("\\n")  ]))
		LIST_celltype_target= list(set([  el.split('.')[2] for el in NAME_TARGET.split("\\n")  ]))
		LIST_time_target    = list(set([  el.split('.')[3] for el in NAME_TARGET.split("\\n")  ]))
		

		
		# count T0 to T6
		if len(LIST_time_source) == 1:
			if len(LIST_time_target) == 1:
				if LIST_time_source[0] == "T0":
					if LIST_time_target[0] == "T6":
						
						#sys.stderr.write("T0_to_T6 %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) #recheck that for the S1 Natal over CSF
						T0_to_T6+=1
						
						if len(LIST_tissue_source) == 1:
							if len(LIST_tissue_target) == 1:
								
								if LIST_tissue_source[0] == "CSF":
									if LIST_tissue_target[0] == "CSF":
										T0CSF_to_T6CSF+=1
										#sys.stderr.write("T0CSF_to_T6CSF %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) #recheck that for the S1 Natal over CSF
										
									if LIST_tissue_target[0] == "Bl":
										T0CSF_to_T6Bl+=1
										#sys.stderr.write("T0CSF_to_T6Bl %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) 
								
								
								if LIST_tissue_source[0] == "Bl":
									if LIST_tissue_target[0] == "CSF":
										T0Bl_to_T6CSF+=1
										#sys.stderr.write("T0CSF_to_T6CSF %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) #recheck that for the S1 Natal over CSF
										
									if LIST_tissue_target[0] == "Bl":
										T0Bl_to_T6Bl+=1
										#sys.stderr.write("T0CSF_to_T6Bl %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) 

print("\t".join( [ str(el) for el in [ T0, T6, T0_to_T6, T0CSF_to_T6CSF,  T0CSF_to_T6Bl, T0Bl_to_T6CSF, T0Bl_to_T6Bl, SEQ_NB, DIRECTORY_1 ] ] ))





