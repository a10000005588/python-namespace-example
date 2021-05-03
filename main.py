import sys
from pprint import *

# 需要先將namespace的path1與path2給引用進來
sys.path.extend(['./path1', './path2'])

pprint(sys.path)

import calculatorPackage
import utilsPackage

pprint(calculatorPackage.__path__)
pprint(utilsPackage.__path__)

pprint(calculatorPackage.calculatorModule.add(1,2))
pprint(calculatorPackage.calculatorModule.subtract(1,2))

pprint(utilsPackage.encodeModule.encoder('input'))