echo -e "Subject\tFolder\tSeq_total\tT0_CSF_Me\tT0_CSF_Na\tT0_CSF_PB\tT0_CSF_gc\tT0_BLOOD_Me\tT0_BLOOD_Na\tT0_BLOOD_PB\tT0_BLOOD_gc\tT6_CSF_Me\tT6_CSF_Na\tT6_CSF_PB\tT6_CSF_gc\tT6_BLOOD_Me\tT6_BLOOD_Na\tT6_BLOOD_PB\tT6_BLOOD_gc\tfilename" > count_per_tree.tsv
TOPFOLDER=over.BLOOD
SUBJECT=S1
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX/ $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX/ $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv

SUBJECT=S2
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Fingo.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv

SUBJECT=S4
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Fingo.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv

SUBJECT=S5
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv

SUBJECT=S6
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv

SUBJECT=S7
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv

SUBJECT=S8
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Fingo.over.BLOOD.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodGC-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodME-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodNA-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodPbl-BloodX $REF_DIR >> count_per_tree.tsv
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT/BloodX-CSFX $REF_DIR >> count_per_tree.tsv




TOPFOLDER=over.CSF
SUBJECT=S1
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv

SUBJECT=S2
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Fingo.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv

SUBJECT=S4
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Fingo.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv

SUBJECT=S5
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv

SUBJECT=S6
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv

SUBJECT=S7
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Natal.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv

SUBJECT=S8
REF_DIR=/mnt/MSprojectData/TREE/files.$SUBJECT.Fingo.over.CSF.2.NONE
python tree_network_count_members_v2.py $TOPFOLDER/$SUBJECT $REF_DIR >> count_per_tree.tsv
