import numpy
import pandas
from pandas.core.arrays.integer import Int32Dtype
from pandas.io.pytables import dropna_doc

# read the data
addhealth_data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

# convert all column names to upper case
addhealth_data.columns = map(str.upper, addhealth_data.columns)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

# get needed data
col_needed = ['H1ED11', 'H1ED12', 'H1ED13', 'H1ED14', 'H1PR1', 'H1PR2', 'H1PR3', 'H1PR4', 'H1PR5', 'H1PR6', 'H1PR7', 'H1PR8']

orig_data = addhealth_data[col_needed]
data = orig_data.copy()
# print(data.columns)

# refine data

# replace irrelevant data with NaN value
data['H1PR1'] = data['H1PR1'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR1'] = data['H1PR1'].astype(pandas.Int64Dtype())

data['H1PR2'] = data['H1PR2'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR2'] = data['H1PR2'].astype(pandas.Int64Dtype())

data['H1PR3'] = data['H1PR3'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR3'] = data['H1PR3'].astype(pandas.Int64Dtype())

data['H1PR4'] = data['H1PR4'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR4'] = data['H1PR4'].astype(pandas.Int64Dtype())

data['H1PR5'] = data['H1PR5'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR5'] = data['H1PR5'].astype(pandas.Int64Dtype())

data['H1PR6'] = data['H1PR6'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR6'] = data['H1PR6'].astype(pandas.Int64Dtype())

data['H1PR7'] = data['H1PR7'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR7'] = data['H1PR7'].astype(pandas.Int64Dtype())

data['H1PR8'] = data['H1PR8'].replace(6, numpy.nan).replace(96, numpy.nan).replace(98,numpy.nan)
data['H1PR8'] = data['H1PR8'].astype(pandas.Int64Dtype())

data['H1ED11'] = data['H1ED11'].replace(5,numpy.nan).replace(6, numpy.nan).replace(96, numpy.nan).replace(97,numpy.nan).replace(98,numpy.nan)
data['H1ED11'] = data['H1ED11'].astype(pandas.Int64Dtype())

data['H1ED12'] = data['H1ED12'].replace(5,numpy.nan).replace(6, numpy.nan).replace(96, numpy.nan).replace(97,numpy.nan).replace(98,numpy.nan)
data['H1ED12'] = data['H1ED12'].astype(pandas.Int64Dtype())

data['H1ED13'] = data['H1ED13'].replace(5,numpy.nan).replace(6, numpy.nan).replace(96, numpy.nan).replace(97,numpy.nan).replace(98,numpy.nan)
data['H1ED13'] = data['H1ED13'].astype(pandas.Int64Dtype())

data['H1ED14'] = data['H1ED14'].replace(5,numpy.nan).replace(6, numpy.nan).replace(96, numpy.nan).replace(97,numpy.nan).replace(98,numpy.nan)
data['H1ED14'] = data['H1ED14'].astype(pandas.Int64Dtype())

ref_data = data.copy()

# counts and percentages of English grades
c_eng_grade = ref_data.H1ED11.value_counts(sort=False, dropna=False)
p_eng_grade = ref_data.H1ED11.value_counts(sort=False, normalize = True, dropna=False)
print("\nEnglish Count:\n", c_eng_grade)
print("\nEnglish Percentages:\n", p_eng_grade)

# counts and percentages of Math grades
c_math_grade = ref_data.H1ED12.value_counts(sort=False, dropna=False)
p_math_grade = ref_data.H1ED12.value_counts(sort=False, normalize = True, dropna=False)
print("\nMath Count:\n", c_math_grade)
print("\nMath Percentages:\n", p_math_grade)

# counts and percentages of History grades
c_hist_grade = ref_data.H1ED13.value_counts(sort=False, dropna=False)
p_hist_grade = ref_data.H1ED13.value_counts(sort=False, normalize = True, dropna=False)
print("\nHistory Count:\n", c_hist_grade)
print("\nHistory Percentages:\n", p_hist_grade)

# counts and percentages of Science grades
c_sci_grade = ref_data.H1ED14.value_counts(sort=False, dropna=False)
p_sci_grade = ref_data.H1ED14.value_counts(sort=False, normalize = True, dropna=False)
print("\nScience Count:\n", c_sci_grade)
print("\nScience Percentages:\n", p_sci_grade)

# counts and percentages of adult support
c_adult_supp = ref_data.H1PR1.value_counts(sort=False, dropna=False)
p_adult_supp = ref_data.H1PR1.value_counts(sort=False, normalize = True, dropna=False)
print("\nAdult Support Count:\n", c_adult_supp)
print("\nAdult Support Percentages:\n", p_adult_supp)

# counts and percentages of teacher support
c_teach_supp = ref_data.H1PR2.value_counts(sort=False, dropna=False)
p_teach_supp = ref_data.H1PR2.value_counts(sort=False, normalize = True, dropna=False)
print("\nTeacher Support Count:\n", c_teach_supp)
print("\nTeacher Support Percentages:\n", p_teach_supp)

# counts and percentages of parent support
c_parent_supp = ref_data.H1PR3.value_counts(sort=False, dropna=False)
p_parent_supp = ref_data.H1PR3.value_counts(sort=False, normalize = True, dropna=False)
print("\nParent Support Count:\n", c_parent_supp)
print("\nParent Support Percentages:\n", p_parent_supp)

# counts and percentages of friend support
c_friend_supp = ref_data.H1PR4.value_counts(sort=False, dropna=False)
p_friend_supp = ref_data.H1PR4.value_counts(sort=False, normalize = True, dropna=False)
print("\nFriend Support Count:\n", c_friend_supp)
print("\nFriend Support Percentages:\n", p_friend_supp)

# counts and percentages of family understanding
c_fam_und = ref_data.H1PR5.value_counts(sort=False, dropna=False)
p_fam_und = ref_data.H1PR5.value_counts(sort=False, normalize = True, dropna=False)
print("\nFamily Understanding Count:\n", c_fam_und)
print("\nFamily Understanding Percentages:\n", p_fam_und)

# counts and percentages of wanting to run away
c_run_away = ref_data.H1PR6.value_counts(sort=False, dropna=False)
p_run_away = ref_data.H1PR6.value_counts(sort=False, normalize = True, dropna=False)
print("\nRunning Away Count:\n", c_run_away)
print("\nRunning Away Percentages:\n", p_run_away)

# counts and percentages of having fun with the family
c_fam_fun = ref_data.H1PR7.value_counts(sort=False, dropna=False)
p_fam_fun = ref_data.H1PR7.value_counts(sort=False, normalize = True, dropna=False)
print("\nFamily Fun Count:\n", c_fam_fun)
print("\nFamily Fun Percentages:\n", p_fam_fun)

# counts and percentages of family paying attention
c_fam_att = ref_data.H1PR8.value_counts(sort=False, dropna=False)
p_fam_att = ref_data.H1PR8.value_counts(sort=False, normalize = True, dropna=False)
print("\nFamily Attention Count:\n", c_fam_att)
print("\nFamily Attention Percentages:\n", p_fam_att)