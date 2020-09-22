#!/usr/bin/python


import sys, os, re

FILE=sys.argv[1] #.vsdot file

OVER_OPTION=sys.argv[2]
if OVER_OPTION not in ['over','auto']:
	sys.stderr.write("Error: give second argument: over or auto\n")
	exit(1)

if not os.path.exists(FILE):
	sys.stderr.write("WARNING: %s does not exists\n"%(FILE))
	exit(1)






FILE_BASENAME=os.path.basename(FILE)
FILE_BASENAME_SPLIT=FILE_BASENAME.split('.')
pattern_overlapType=re.compile("((over)|(auto))")

OVERLAPTYPE=pattern_overlapType.search( FILE_BASENAME ).group(1)

if OVERLAPTYPE != OVER_OPTION:
	sys.stderr.write("Warning: It seem that second argument %s is not in file name (detected: %s)\nThis may be the reason of a crash\n\n"%(OVER_OPTION,OVERLAPTYPE) )


#S8.t6.Fingo.auto.CSF.BLOOD.seqs_grp6
if OVER_OPTION == "auto":
	PATIENT =FILE_BASENAME_SPLIT[0]
	TIME    =FILE_BASENAME_SPLIT[1]
	OVERLAPTYPE=FILE_BASENAME_SPLIT[3]
	TISSUE_1=FILE_BASENAME_SPLIT[4]
	TISSUE_2=FILE_BASENAME_SPLIT[5]
	GRP_NB=FILE_BASENAME_SPLIT[6].split('_')[1]
	
	CSF_to_Bl,CSF_to_CSF,Bl_to_CSF,Bl_to_Bl=0,0,0,0

	
#S7.Natal.over.BLOOD.seqs_grp127
elif OVER_OPTION == "over":
	PATIENT =FILE_BASENAME_SPLIT[0]
	OVERLAPTYPE=FILE_BASENAME_SPLIT[2]
	TISSUE=FILE_BASENAME_SPLIT[3]
	GRP_NB=FILE_BASENAME_SPLIT[4].split('_')[1]
	
	T0,T6,T0_to_T6,T6_to_T0=0,0,0,0
	T0CSF_to_T6Bl,T0CSF_to_T6CSF,T0Bl_to_T6CSF,T0Bl_to_T6Bl=0,0,0,0
	T6CSF_to_T0Bl,T6CSF_to_T0CSF,T6Bl_to_T0CSF,T6Bl_to_T0Bl=0,0,0,0
	
	#T0_ME,T0_NA,T0_PLB,T0_DN=0,0,0,0
	#T6_ME,T6_NA,T6_PLB,T6_DN=0,0,0,0
	
SEQ_NB=0

#print("\t".join([PATIENT,GRP_NB,OVERLAPTYPE,FILE]))


re_label = re.compile("label=\"([^\"]*)")
############################################################
#load the network
NETWORK=[]
LABELS={}
PARENTS_LIST=[]
CHILDS_LIST=[]
with open(FILE) as handle:
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

ERROR_TREE=[]

############################################################
#find the root : the only source which is not a target
LI_ROOT=[ el for el in PARENTS_LIST if el not in CHILDS_LIST ]
if len(LI_ROOT) >1: 
	sys.stderr.write("WARNING: Not single arrow from germline %s\n"%FILE)
	ERROR_TREE.append("2arrowsFromGermline")
ROOT_id=list(set(LI_ROOT)) #but only 1 germline
if len(ROOT_id) == 1:
	ROOT_id=ROOT_id[0]
	#sys.stderr.write( "germline is %s (%s) for %s\n"%(ROOT_id, LABELS[ROOT_id], FILE) )
else:
	sys.stderr.write("ERROR: problem with root %s\n"%FILE)
	exit(1)
	### ### -> tree with a sequence put with germline !! S7 Natal over BLOOD grp134




############################################################
#check the tree
for tupl in NETWORK:
	
	# count the targets before skipping
	INDEX_SOURCE=tupl[0]
	INDEX_TARGET=tupl[1]
	MUTATIONS=tupl[1]
	
	NAME_SOURCE=LABELS[ INDEX_SOURCE ]
	NAME_TARGET=LABELS[ INDEX_TARGET ]
	
	if NAME_TARGET:
		SEQ_NB+=len(NAME_TARGET.split("\\n")) #before skipping the germline to count all sequences
			
	if OVERLAPTYPE == "over":
		if NAME_TARGET:
			T0+=[  el.split('.')[3] for el in NAME_TARGET.split("\\n")  ].count("T0")
			T6+=[  el.split('.')[3] for el in NAME_TARGET.split("\\n")  ].count("T6")
		
	#skip count if germline (meaningless T0->T6 of tissue1->tissue2)
	if tupl[0] == ROOT_id:
		continue
	#skip when the reference is an internal node without label
	if not NAME_SOURCE or not NAME_TARGET:
		continue

	#use only list of sequences, since possible to have > 1 per node
	LIST_tissue_source  = list(set([  el.split('.')[1] for el in NAME_SOURCE.split("\\n")  ]))
	LIST_celltype_source= list(set([  el.split('.')[2] for el in NAME_SOURCE.split("\\n")  ]))
	LIST_time_source    = list(set([  el.split('.')[3] for el in NAME_SOURCE.split("\\n")  ]))
	
	LIST_tissue_target  = list(set([  el.split('.')[1] for el in NAME_TARGET.split("\\n")  ]))
	LIST_celltype_target= list(set([  el.split('.')[2] for el in NAME_TARGET.split("\\n")  ]))
	LIST_time_target    = list(set([  el.split('.')[3] for el in NAME_TARGET.split("\\n")  ]))
		



	if OVERLAPTYPE == "over":
		
		# count T0 to T6 - direct links
		
		if len(LIST_time_source) == 1:
			if len(LIST_time_target) == 1:
				
				if LIST_time_source[0] == "T0":
					if LIST_time_target[0] == "T6": #sys.stderr.write("T0_to_T6 %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) #recheck that for the S1 Natal over CSF
						T0_to_T6+=1
						if len(LIST_tissue_source) == 1:
							if len(LIST_tissue_target) == 1:
								
								
								if LIST_tissue_source[0] == "CSF":
									if LIST_tissue_target[0] == "CSF":
										T0CSF_to_T6CSF+=1 #sys.stderr.write("T0CSF_to_T6CSF %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) #recheck that for the S1 Natal over CSF
									elif LIST_tissue_target[0] == "Bl":
										T0CSF_to_T6Bl+=1 #sys.stderr.write("T0CSF_to_T6Bl %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) 
								elif LIST_tissue_source[0] == "Bl":
									if LIST_tissue_target[0] == "CSF":
										T0Bl_to_T6CSF+=1 #sys.stderr.write("T0CSF_to_T6CSF %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) #recheck that for the S1 Natal over CSF
									elif LIST_tissue_target[0] == "Bl":
										T0Bl_to_T6Bl+=1 #sys.stderr.write("T0CSF_to_T6Bl %s -> %s \n"%(NAME_SOURCE, NAME_TARGET)) 
				
				elif LIST_time_source[0] == "T6":
					if LIST_time_target[0] == "T0":
						T6_to_T0+=1
						ERROR_TREE.append("T0->T0")
						if len(LIST_tissue_source) == 1:
							if len(LIST_tissue_target) == 1:

								if LIST_tissue_source[0] == "CSF":
									if LIST_tissue_target[0] == "CSF":
										T6CSF_to_T0CSF+=1 
									elif LIST_tissue_target[0] == "Bl":
										T6CSF_to_T0Bl+=1 
								elif LIST_tissue_source[0] == "Bl":
									if LIST_tissue_target[0] == "CSF":
										T6Bl_to_T0CSF+=1 
									elif LIST_tissue_target[0] == "Bl":
										T6Bl_to_T0Bl+=1 
										
		
	elif OVERLAPTYPE == "auto":
		
		# count cell type change, tissue change
		if len(LIST_time_source) == 1:
			if len(LIST_time_target) == 1:
				if len(LIST_tissue_source) == 1:
					if len(LIST_tissue_target) == 1:
						
						if LIST_tissue_source[0] == "CSF":
							if LIST_tissue_target[0] == "CSF":
								CSF_to_CSF+=1
							elif LIST_tissue_target[0] == "Bl":
								CSF_to_Bl+=1
						elif LIST_tissue_source[0] == "Bl":
							if LIST_tissue_target[0] == "CSF":
								Bl_to_CSF+=1
							elif LIST_tissue_target[0] == "Bl":
								Bl_to_Bl+=1
				
		pass
	
if OVERLAPTYPE == "over":
	print("\t".join( [ str(el) for el in [ PATIENT,TISSUE,GRP_NB,OVERLAPTYPE,  ",".join(list(set(ERROR_TREE))),  T0,T6,T0_to_T6,T6_to_T0,     T0CSF_to_T6CSF,T0CSF_to_T6Bl,T0Bl_to_T6CSF,T0Bl_to_T6Bl,      T6CSF_to_T0CSF,T6CSF_to_T0Bl,T6Bl_to_T0CSF,T6Bl_to_T0Bl,    SEQ_NB,    FILE ] ] ))
elif OVERLAPTYPE == "auto":
	print("\t".join( [ str(el) for el in [ PATIENT,TIME,TISSUE_1,TISSUE_2,GRP_NB,OVERLAPTYPE,  ",".join(list(set(ERROR_TREE))), CSF_to_CSF,CSF_to_Bl,Bl_to_CSF,Bl_to_Bl,    SEQ_NB,    FILE ] ] ))
	




