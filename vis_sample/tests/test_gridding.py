from vis_sample import gridding
import numpy as np

def test_spheroid():
    assert gridding.spheroid(eta=100) ==1.e30
    assert gridding.spheroid(eta=-100) ==1.e30
    assert gridding.spheroid(eta = 1) == 0.01466325
    assert gridding.spheroid(eta = -1) == 0.01466325
    assert gridding.spheroid(eta = 2) == (0.01624782*3**6 + -0.05350728*3**5 + 0.1464354*3**4 + -0.2347118*3**3 + 0.2180684*3**2 + -0.09858686*3 + 0.01466325)/(0.2177793*3 + 1)
