# ********************************************* Test usage *********************************************

# ***************************** Author: Dimitrios Mamakas for www.aueb.gr ******************************

# Import datasets
from datasets import load_dataset
# Import nlp-bow
from nlp-bow import *

# Load datasets
datasetEcthrA = load_dataset("lex-glue", "ecthr_a")
datasetEcthrB = load_dataset("lex-glue", "ecthr_b")
datasetScotus = load_dataset("lex_glue", "scotus")
datasetEurlex = load_dataset("lex-glue", "eurlex")
datasetLedgar = load_dataset("lex-glue", "ledgar")
datasetUnfairTos = load_dataset("lex-glue", "unfair_tos")
datasetCaseHold = load_dataset("lex-glue", "case_hold")

# Showcase 1 updated dataset for ecthr_a
updatedDatasetEcthrA = datasetEcthrA.map(updateDatasetTextField)

# Showcase 1 updated dataset for ecthr_b
updatedDatasetEcthrB = datasetEcthrB.map(updateDatasetTextField)

# Showcase 1 updated dataset for scotus
updatedDatasetScotus = datasetScotus.map(updateDatasetTextField)

# Showcase 1 updated dataset for eurlex
updatedDatasetEurlex = datasetEurlex.map(updateDatasetTextField)

# Showcase 1 updated dataset for ledgar
updatedDatasetLedgar = datasetLedgar.map(updateDatasetTextField)

# Showcase 1 updated dataset for unfair_tos
updatedDatasetUnfairTos = datasetUnfairTos.map(updateDatasetTextField)

# Showcase 1 updated dataset for case_hold
updatedDatasetCaseHold = datasetCaseHold.map(updateDatasetTextField)