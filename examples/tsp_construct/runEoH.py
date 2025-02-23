import sys
sys.path.append('/home/chenix/vscode/codepy/EoH-milp')
from eoh.src.eoh import eoh
from eoh.src.eoh.utils.getParas import Paras

# Parameter initilization #
paras = Paras() #init

# Set parameters #
paras.set_paras(method = "eoh",    # ['ael','eoh']
                problem = "tsp_construct", #['tsp_construct','bp_online']
                llm_api_endpoint = "https://api.zhizengzeng.com/v1/chat/completions", # set your LLM endpoint
                llm_api_key = "sk-zk23e45bed8bac590cf8beaf5b5f88b478667b58007df74f",   # set your key
                llm_model = "gpt-3.5-turbo",
                ec_pop_size = 4, # number of samples in each population
                ec_n_pop = 4,  # number of populations
                exp_n_proc = 4,  # multi-core parallel
                exp_debug_mode = False)

# initilization
evolution = eoh.EVOL(paras)

# run 
evolution.run()