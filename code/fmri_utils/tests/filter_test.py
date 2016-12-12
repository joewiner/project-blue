""" Test script for filter module

Test with ``py.test filter.py``.
"""
import numpy as np
from fmri_utils import filter

def test_slice_timing_corr():
    """
    Test pulls the first subject file and puts through the filter code

    """
    TR = 2
    filepath = 'data/sub-01/func/sub-01_task-visualimageryfalsememory_run-01_bold.nii.gz'

    filter.filter(filepath, TR)

    return
