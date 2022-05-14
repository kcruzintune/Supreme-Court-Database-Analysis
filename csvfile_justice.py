# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

###############################################################################
# QUESTION 1
###############################################################################

fileref = open("SCDB_2021_01_justiceCentered_Citation.csv", encoding = 'ISO-8859-1')

scdb = pd.read_csv(fileref)

scdb_subset = scdb[scdb.term >= 2000]

# This takes all the cases from 2000 term to the most recently completed term

###############################################################################
# QUESTION 2
###############################################################################


scdb_subset.groupby('term')['caseId'].nunique()

# This calculates the number of cases for each term

f = plt.figure(figsize=(12,8))

# Variable "f" is used to set the size of the graphs

scdb_subset.groupby('term')['caseId'].nunique().plot(kind="bar", title = 'Kevin Cruz')

# This plots the number of cases for each term

###############################################################################
# QUESTION 3
###############################################################################

scdb_subset.groupby(["justiceName", "direction"])['caseId'].nunique()

# Calculates the number of votes in each "direction", for each justice

scdb_subset.groupby(["justiceName", "direction"])['caseId'].nunique().plot(kind="bar", title = 'Kevin Cruz')

# Plots the number of votes in each "direction", for each justice

###############################################################################
# QUESTION 4
###############################################################################

fileref2 = open('SCDB_2021_01_caseCentered_Docket.csv', encoding = 'ISO-8859-1')

scdb2 = pd.read_csv(fileref2)

scdb_subset2 = scdb[scdb.term >= 2008]

scdb_subset2 = scdb_subset2[scdb_subset2.term <= 2020]

# The reason for two scdb_subset2 is to take all the cases from 2008 term to 
# 2020 term.

###############################################################################
# QUESTION 5
###############################################################################

scdb_subset2.groupby("caseDisposition")['caseId'].nunique()

# Calculates the number of cases for each case Disposition type

scdb_subset2.groupby("caseDisposition")['caseId'].nunique().plot(kind="bar", title = 'Kevin Cruz')

# Plots the number of cases for each case Disposition type

###############################################################################
# Question 6
###############################################################################

scdb_subset3 = scdb[scdb.term >= 2017]

scdb_subset3 = scdb_subset3[scdb_subset3.term <= 2020]

scdb_subset3.groupby("justiceName")[["majOpinWriter", "majOpinAssigner"]].nunique()

scdb_subset3.groupby("justiceName")[["majOpinWriter", "majOpinAssigner"]].nunique().plot(kind="bar", title = 'Kevin Cruz').legend(bbox_to_anchor=(1.05, 1));

#This bar graph represents the number of majOpinWriter and majOpinAssigner for 
#each justicName. In addition, I moved the legend outside of the graph so that
#there is nothing blocking the graph. Also, I only included the years 2017-2020.

############################################################################### 
