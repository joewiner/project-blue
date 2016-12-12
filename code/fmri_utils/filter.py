import os
import numpy as np
import nitime.fmri.io as io
# Import the time-series objects:
from nitime.timeseries import TimeSeries
# Import the analysis objects:
from nitime.analysis import SpectralAnalyzer, FilterAnalyzer, NormalizationAnalyzer

"""
This script uses a Finite Impulse Response (FIR) digital filter on nifti files
to remove signal that is not related to physiological processes.

The lower and upper bounds of the filter can be set with the variables
f_lb and f_ub - currently set to default based on
http://nipy.org/nitime/examples/filtering_fmri.html

The code creates a FIR filtered time series object based on a nifti file, then
makes a new nifti file based on the filtered data.

I have included a line that creates an unfiltered time series object of the data,
and also lines looking at spectral information of the time series,
but these are commented out since we don't need them for the project.
"""

def filter(filepath, TR):

    data = nib.load(filepath)
    volume_shape = data.shape[:-1]
    coords = list(np.ndindex(volume_shape))
    coords = np.array(coords).T

    #define limits of bandpass filter
    f_lb = 0.02
    f_ub = 0.15

    #unfiltered time series object
    #T_unfiltered = io.time_series_from_file(filepath, coords, TR=TR, normalize='percent')

    #create filtered time series object based on nifti file
    T_fir = io.time_series_from_file(filepath, coords, TR=TR, normalize='percent', filter=dict(lb=f_lb, ub=f_ub, method='fir', filt_order=10))

    #create spectral objects for unfiltered & filterered data to plot
    #S_unfiltered = SpectralAnalyzer(T_unfiltered).spectrum_multi_taper
    #S_fir = SpectralAnalyzer(T_fir).spectrum_multi_taper

    """
    The 'nifti_from_time_series' function is what I'm not sure about...
    I will check with Matthew about this
    """

    filt_data = io.nifti_from_time_series(volume_shape, coords, S_fir, filepath + '_filt')

    return filt_data
