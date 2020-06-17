"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com
Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='/Users/hedyeherfani/Desktop/ThinkStats2-master/code/2002FemResp.dct',
                dat_file='/Users/hedyeherfani/Desktop/ThinkStats2-master/code/2002FemResp.dat.gz',
                nrows=None):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    nsfg.CleanFemResp(df)
    return df


def CleanFemResp(df):
    pass


def ValueCounts(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)
    preg.pregnum_counts().sort_index()


def main(script):
    """Tests the functions in this module.
    script: string script name
    """
    resp = ReadFemResp()

    if len(resp) == 7643 and resp.pregnum.value_counts == 1267:
        print('%s: All tests passed.' % script)

    else:
        print("Tests not passed")


if __name__ == '__main__':
    main(*sys.argv)
