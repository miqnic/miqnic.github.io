import numpy
import pandas
from pandas.core.arrays.integer import Int32Dtype
from pandas.io.pytables import dropna_doc

data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

# refine support data
data['H1PR1'] = pandas.to_numeric(data['H1PR1'])
data['H1PR2'] = pandas.to_numeric(data['H1PR2'])
data['H1PR3'] = pandas.to_numeric(data['H1PR3'])
data['H1PR4'] = pandas.to_numeric(data['H1PR4'])
data['H1PR5'] = pandas.to_numeric(data['H1PR5'])
data['H1PR6'] = pandas.to_numeric(data['H1PR6'])
data['H1PR7'] = pandas.to_numeric(data['H1PR7'])
data['H1PR8'] = pandas.to_numeric(data['H1PR8'])

# refine grades data
data['H1ED11'] = pandas.to_numeric(data['H1ED11'])
data['H1ED12'] = pandas.to_numeric(data['H1ED12'])
data['H1ED11'] = pandas.to_numeric(data['H1ED13'])
data['H1ED14'] = pandas.to_numeric(data['H1ED14'])

# replace irrelevant support data with NaN value
data['H1PR1'] = data['H1PR1'].replace([6,96,98], numpy.nan)
data['H1PR1'] = data['H1PR1'].astype(pandas.Int64Dtype())

data['H1PR2'] = data['H1PR2'].replace([6,96,98], numpy.nan)
data['H1PR2'] = data['H1PR2'].astype(pandas.Int64Dtype())

data['H1PR3'] = data['H1PR3'].replace([6,96,98], numpy.nan)
data['H1PR3'] = data['H1PR3'].astype(pandas.Int64Dtype())

data['H1PR4'] = data['H1PR4'].replace([6,96,98], numpy.nan)
data['H1PR4'] = data['H1PR4'].astype(pandas.Int64Dtype())

data['H1PR5'] = data['H1PR5'].replace([6,96,98], numpy.nan)
data['H1PR5'] = data['H1PR5'].astype(pandas.Int64Dtype())

data['H1PR6'] = data['H1PR6'].replace([6,96,98], numpy.nan)
data['H1PR6'] = data['H1PR6'].astype(pandas.Int64Dtype())

data['H1PR7'] = data['H1PR7'].replace([6,96,98], numpy.nan)
data['H1PR7'] = data['H1PR7'].astype(pandas.Int64Dtype())

data['H1PR8'] = data['H1PR8'].replace([6,96,98], numpy.nan)
data['H1PR8'] = data['H1PR8'].astype(pandas.Int64Dtype())

# replace irrelevant grades data with NaN value
data['H1ED11'] = data['H1ED11'].replace([5,6,96,97,98], numpy.nan)
data['H1ED11'] = data['H1ED11'].astype(pandas.Int64Dtype())

data['H1ED12'] = data['H1ED12'].replace([5,6,96,97,98], numpy.nan)
data['H1ED12'] = data['H1ED12'].astype(pandas.Int64Dtype())

data['H1ED13'] = data['H1ED13'].replace([5,6,96,97,98], numpy.nan)
data['H1ED13'] = data['H1ED13'].astype(pandas.Int64Dtype())

data['H1ED14'] = data['H1ED14'].replace([5,6,96,97,98], numpy.nan)
data['H1ED14'] = data['H1ED14'].astype(pandas.Int64Dtype())

# add a secondary variable that adds the scores of each user for each support variable
data['SUPPORTSUM'] = data['H1PR1'].dropna() + data['H1PR2'].dropna() + data['H1PR3'].dropna() + data['H1PR4'].dropna() + data['H1PR5'].dropna() + data['H1PR6'].dropna() + data['H1PR7'].dropna() + data['H1PR8'].dropna()

# add a secondary variable that averages the grades of each user for each subject
data['GRADEAVE'] = (data['H1ED11'].dropna() + data['H1ED12'].dropna() + data['H1ED13'].dropna() + data['H1ED14'].dropna())/4

# copy needed columns into a new dataframe and drop NA 
ref_data = data[['AID', 'SUPPORTSUM', 'GRADEAVE']]
ref_data = ref_data.dropna()

# apply ranges in SUPPORTSUM
def SUPPORT_RANGE(row):
    if row['SUPPORTSUM'] <= 50 and row['SUPPORTSUM'] > 40:
        return 5
    if row['SUPPORTSUM'] <= 40 and row['SUPPORTSUM'] > 30:
        return 4
    if row['SUPPORTSUM'] <= 30 and row['SUPPORTSUM'] > 20:
        return 3
    if row['SUPPORTSUM'] <= 20 and row['SUPPORTSUM'] > 10:
        return 2
    if row['SUPPORTSUM'] <= 10 and row['SUPPORTSUM'] >= 0:
        return 1

# apply ranges in GRADEAVE
def GRADE_RANGE(row):
    if row['GRADEAVE'] <= 4 and row['GRADEAVE'] > 3:
        return 4
    if row['GRADEAVE'] <= 3 and row['GRADEAVE'] > 2:
        return 3
    if row['GRADEAVE'] <= 2 and row['GRADEAVE'] > 1:
        return 2
    if row['GRADEAVE'] <= 1 and row['GRADEAVE'] >= 0:
        return 1

ref_data['SUPPORTSUM'] = ref_data.apply(lambda row: SUPPORT_RANGE (row), axis=1)
ref_data['GRADEAVE'] = ref_data.apply(lambda row: GRADE_RANGE (row), axis=1)

# counts and percentages of SUPPORTSUM
c_supportsum = ref_data.SUPPORTSUM.value_counts(sort=False, dropna=False)
p_supportsum = ref_data.SUPPORTSUM.value_counts(sort=False, normalize = True, dropna=False)
print("\nSUPPORTSUM Count:\n", c_supportsum)
print("\nSUPPORTSUM Percentages:\n", p_supportsum)

# counts and percentages of GRADEAVE
c_gradeave = ref_data.GRADEAVE.value_counts(sort=False, dropna=False)
p_gradeave = ref_data.GRADEAVE.value_counts(sort=False, normalize = True, dropna=False)
print("\nGRADEAVE Count:\n", c_gradeave)
print("\nGRADEAVE Percentages:\n", p_gradeave)