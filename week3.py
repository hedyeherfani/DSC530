from __future__ import print_function

import numpy as np
import sys

import nsfg
import first
import thinkstats2
import thinkplot

def PmfMean(pmf):
    mean = 0.0
    for x, p in pmf.d.items():
        mean += p * x
    return mean

def Difference(t):
    first = t[0]
    others = t[1:]
    difference = [first - x for x in others]
    return difference


def PairWiseDifferences(live):
    live = live[live.prglngth >= 37]
    preg_map = nsfg.MakePregMap(live)

    diffs = []
    for caseid, indices in preg_map.items():
        lengths = live.loc[indices].prglngth.values
        if len(lengths) >= 2:
            diffs.extend(Diffs(lengths))

    mean = thinkstats2.Mean(diffs)
    print('Mean difference between pairs', mean)

    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf, align='center')
    thinkplot.Show(xlabel='Difference in weeks',
                   ylabel='PMF')


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    PairWiseDifferences(live)

    # test PmfMean and PmfVar
    prglngth = live.prglngth
    pmf = thinkstats2.Pmf(prglngth)
    mean = PmfMean(pmf)
    var = PmfVar(pmf)

    assert(mean == pmf.Mean())
    assert(var == pmf.Var())
    print('mean/var preg length', mean, var)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
