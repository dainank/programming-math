from expl import *

for i in range(0,100):
   a,b = random_scalar(), random_scalar()
   u,v,w = random_scalar(), random_scalar(), random_scalar()
   test(0, isclose, a,b,u,v,w)