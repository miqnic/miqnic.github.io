import numpy
import pandas

# read the data
addhealth_data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

# convert all column names to upper case
addhealth_data.columns = map(str.upper, addhealth_data.columns)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

# get needed data
col_needed = ['H1ED11', 'H1ED12', 'H1ED13', 'H1ED14', 'H1PR1', 'H1PR2', 'H1PR3', 'H1PR4', 'H1PR5', 'H1PR6', 'H1PR7', 'H1PR8']

data = addhealth_data[col_needed]
# print(data.columns)

# refine data
# compile all valid data from grades and support data
valid_5 = [1,2,3,4]
valid_35 = [1,2,3,4,5]

# filter the dataframe - make sure that respondents have answered all 12 questions
ref_data = data[data.H1ED11.isin(valid_5) & data.H1ED12.isin(valid_5) & data.H1ED13.isin(valid_5) & data.H1ED14.isin(valid_5) & data.H1PR1.isin(valid_35) & data.H1PR2.isin(valid_35) & data.H1PR3.isin(valid_35) & data.H1PR4.isin(valid_35) & data.H1PR5.isin(valid_35) & data.H1PR6.isin(valid_35) & data.H1PR7.isin(valid_35) & data.H1PR8.isin(valid_35)]

# counts and percentages of English grades
c_eng_grade = ref_data.H1ED11.value_counts(sort=False)
p_eng_grade = ref_data.H1ED11.value_counts(sort=False, normalize = True)
print("\nEnglish Count:\n", c_eng_grade)
print("\nEnglish Percentages:\n", p_eng_grade)

# counts and percentages of Math grades
c_math_grade = ref_data.H1ED12.value_counts(sort=False)
p_math_grade = ref_data.H1ED12.value_counts(sort=False, normalize = True)
print("\nMath Count:\n", c_math_grade)
print("\nMath Percentages:\n", p_math_grade)

# counts and percentages of History grades
c_hist_grade = ref_data.H1ED13.value_counts(sort=False)
p_hist_grade = ref_data.H1ED13.value_counts(sort=False, normalize = True)
print("\nHistory Count:\n", c_hist_grade)
print("\nHistory Percentages:\n", p_hist_grade)

# counts and percentages of Science grades
c_sci_grade = ref_data.H1ED14.value_counts(sort=False)
p_sci_grade = ref_data.H1ED14.value_counts(sort=False, normalize = True)
print("\nScience Count:\n", c_sci_grade)
print("\nScience Percentages:\n", p_sci_grade)

# counts and percentages of adult support
c_adult_supp = ref_data.H1PR1.value_counts(sort=False)
p_adult_supp = ref_data.H1PR1.value_counts(sort=False, normalize = True)
print("\nAdult Support Count:\n", c_adult_supp)
print("\nAdult Support Percentages:\n", p_adult_supp)

# counts and percentages of teacher support
c_teach_supp = ref_data.H1PR2.value_counts(sort=False)
p_teach_supp = ref_data.H1PR2.value_counts(sort=False, normalize = True)
print("\nTeacher Support Count:\n", c_teach_supp)
print("\nTeacher Support Percentages:\n", p_teach_supp)

# counts and percentages of parent support
c_parent_supp = ref_data.H1PR3.value_counts(sort=False)
p_parent_supp = ref_data.H1PR3.value_counts(sort=False, normalize = True)
print("\nParent Support Count:\n", c_parent_supp)
print("\nParent Support Percentages:\n", p_parent_supp)

# counts and percentages of friend support
c_friend_supp = ref_data.H1PR4.value_counts(sort=False)
p_friend_supp = ref_data.H1PR4.value_counts(sort=False, normalize = True)
print("\nFriend Support Count:\n", c_friend_supp)
print("\nFriend Support Percentages:\n", p_friend_supp)

# counts and percentages of family understanding
c_fam_und = ref_data.H1PR5.value_counts(sort=False)
p_fam_und = ref_data.H1PR5.value_counts(sort=False, normalize = True)
print("\nFamily Understanding Count:\n", c_fam_und)
print("\nFamily Understanding Percentages:\n", p_fam_und)

# counts and percentages of wanting to run away
c_run_away = ref_data.H1PR6.value_counts(sort=False)
p_run_away = ref_data.H1PR6.value_counts(sort=False, normalize = True)
print("\nRunning Away Count:\n", c_run_away)
print("\nRunning Away Percentages:\n", p_run_away)

# counts and percentages of having fun with the family
c_fam_fun = ref_data.H1PR7.value_counts(sort=False)
p_fam_fun = ref_data.H1PR7.value_counts(sort=False, normalize = True)
print("\nFamily Fun Count:\n", c_fam_fun)
print("\nFamily Fun Percentages:\n", p_fam_fun)

# counts and percentages of family paying attention
c_fam_att = ref_data.H1PR8.value_counts(sort=False)
p_fam_att = ref_data.H1PR8.value_counts(sort=False, normalize = True)
print("\nFamily Attention Count:\n", c_fam_att)
print("\nFamily Attention Percentages:\n", p_fam_att)