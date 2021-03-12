import json
import sys, os
#import ipdb; ipdb.set_trace()
sys.path.append(os.getcwd())
file = json.load(open(os.path.dirname(__file__) + "/tabelas.json", "r"))
