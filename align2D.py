from modeller import *
from modeller.automodel import *

env = environ()
aln = alignment(env)
mdl = model(env, file='5ucv', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5ucv', atom_files='5ucv.pdb')
aln.append(file='TARGET.ali', align_codes='TARGET')
aln.align2d()
aln.write(file='TARGET-5ucv.ali', alignment_format='PIR')
aln.write(file='TARGET-5ucv.pap', alignment_format='PAP')
