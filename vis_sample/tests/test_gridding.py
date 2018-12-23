from vis_sample import gridding
import numpy as np

def test_spheroid():
    assert gridding.spheroid(eta=100) == 1.e30
    assert gridding.spheroid(eta=-100) == 1.e30
    assert gridding.spheroid(eta = 1) == 0.01466325
    assert gridding.spheroid(eta = -1) == 0.01466325
    assert gridding.spheroid(eta = 0.5) == (0.01624782*(-0.75)**6 + -0.05350728*(-0.75)**5 + 0.1464354*(-0.75)**4 + -0.2347118*(-0.75)**3 + 0.2180684*(-0.75)**2 + -0.09858686*(-0.75) + 0.01466325)/(0.2177793*(-0.75) + 1)
    assert gridding.spheroid(eta = -0.5) == (0.01624782*(-1.25)**6 + -0.05350728*(-1.25)**5 + 0.1464354*(-1.25)**4 + -0.2347118*(-1.25)**3 + 0.2180684*(-1.25)**2 + -0.09858686*(-1.25) + 0.01466325)/(0.2177793*(-1.25) + 1)
