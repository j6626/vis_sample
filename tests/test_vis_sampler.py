import os
import numpy as np
from vis_sample import vis_sample
from vis_sample.file_handling import import_data_ms

"""
def uvgaussian(u,v):
"""
"""
    Calculates Gaussian model in uv plane corresponding to test gaussian image
"""
"""
    arcsec_to_rad = 3600*180/np.pi
    pixel = 0.01 #pixel size in arcseconds
    sig1 = 0.375 #standard deviation of gaussian in east-west direction in arcsec
    sig2 = 0.75 #standard deviation of gaussian in north-south direction in arcsec
    a = (arcsec_to_rad/sig1)**2 
    b = (arcsec_to_rad/sig2)**2
    scale = 1.e-5
    
    vis = scale*(arcsec_to_rad/pixel)**2*2*np.pi/np.sqrt(a*b)*np.exp(-2*np.pi**2*u**2/a-2*np.pi**2*v**2/b) #need to account for intensity conversion to Jy/sr in prefactor 

    exactflux = scale*2*np.pi*np.sqrt(sig1**2*sig2**2/pixel**4)

    return vis.astype(complex)
"""

def uvgaussian(u,v):
    """
    Calculates Gaussian model in uv plane corresponding to test gaussian image
    """
    arcsec_to_rad = 3600*180/np.pi
    pixel = 0.01 #pixel size in arcseconds
    #sig1 = 0.75 #standard deviation of gaussian in east-west direction in arcsec
    #sig2 = 0.75 #standard deviation of gaussian in north-south direction in arcsec
    sig1 = 0.5
    sig2 = 0.5
    a = (arcsec_to_rad/sig1)**2 
    b = (arcsec_to_rad/sig2)**2
    #scale = 4.5e-5
    scale = 0.2/(2*np.pi*sig1**2/pixel**2)
    
    vis = scale*(arcsec_to_rad/pixel)**2*2*np.pi/np.sqrt(a*b)*np.exp(-2*np.pi**2*u**2/a-2*np.pi**2*v**2/b) #need to account for intensity conversion to Jy/sr in prefactor 
 
    exactflux = scale*2*np.pi*np.sqrt(sig1**2*sig2**2/pixel**4)
    print(exactflux)

    return vis.astype(complex)
    

def test_vis_sample():
    msname = os.path.join(os.path.dirname(__file__), 'testfile.ms')
    #imagename =  os.path.join(os.path.dirname(__file__), 'gaussiantestmodel.fits')
    imagename =  os.path.join(os.path.dirname(__file__), 'model.fits')
    data_vis = import_data_ms(msname)
    interp_vis = vis_sample(imagefile = imagename, uvfile = msname, mu_RA = 0, mu_DEC = 0)
    print(interp_vis[10:20])
    print(uvgaussian(data_vis.uu[10:20], data_vis.vv[10:20]))



