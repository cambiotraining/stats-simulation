from plotnine import *
import pandas as pd
import numpy as np
import pingouin as pg
from scipy import stats
import statsmodels.api as sm
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf
import scikit_posthocs as sp
import matplotlib.pyplot as plt
from patsy import dmatrix
import random
from scipy.stats import t
import statistics
#exec(open('setup_files/dgplots_knitr.py').read())
theme_set(theme_bw())
