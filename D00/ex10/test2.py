import time
from test1 import progressbar

for i in progressbar(range(15), "Computing: ", 40):
    time.sleep(0.1) # long computation