import os
import numpy as np
from vis_sample.file_handling import import_data_ms

def test_import_data_ms():
    msname = os.path.join(os.path.dirname(__file__), 'testfile.ms')
    #the current code assumes that the measurement set only has one SPW, but will still operate on an MS with multiple SPWs. This needs to be addressed. 
    data_vis = import_data_ms(msname)
    pass

