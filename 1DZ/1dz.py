import numpy as np
import pandas as pd


df = pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')

#1
print(df.pivot_table(['height'], ['gender'], aggfunc='mean').head(10))

print(df['gender'].value_counts())

#2
print(df.pivot_table(['alco'], ['gender'], aggfunc='mean').head(10))

#3
print(round(df['smoke'][df['gender'] == 2].mean()/df['smoke'][df['gender'] == 1].mean()))

#4
print(round((df['age'][df['smoke'] == 0].median()-df['age'][df['smoke'] == 1].median())/30))

#5
df['age_years'] = round(df['age']/365).astype('int')

print(round(df[(df['age_years']>=60) & (df['age_years']<=64) & (df['ap_hi'] <= 160) & (df['ap_hi'] <= 180) & (df['cholesterol'] == 3) & (df['cardio'] == 1)].shape[0] / df['age_years'][(df['age_years']>=60) & (df['age_years']<=64) & (df['ap_hi'] < 120) & (df['cholesterol'] == 1) & (df['cardio'] == 1)].shape[0] ))

#6
df['BMI'] = df['weight']/((df['height']/100)*(df['height']/100))

print(df['BMI'].median())

print(df['BMI'][df['gender'] == 1].mean())
print(df['BMI'][df['gender'] == 2].mean())

print(df['BMI'][df['gender'] == 1].mean())
print(df['BMI'][df['gender'] == 2].mean())

print(df['BMI'][df['cardio'] == 0].mean())
print(df['BMI'][df['cardio'] == 1].mean())

print(df['BMI'][(df['cardio'] == 0) & (df['gender'] == 1) & (df['alco'] == 0)].mean())
print(df['BMI'][(df['cardio'] == 0) & (df['gender'] == 2) & (df['alco'] == 0)].mean())

#7
clean_df = df[(df['ap_hi']>=df['ap_lo']) & (df['height']>=df['height'].quantile(q=0.025)) & (df['height']<=df['height'].quantile(q=0.975)) & (df['weight']>=df['weight'].quantile(q=0.025)) & (df['weight']<=df['weight'].quantile(q=0.975))]
print(round(1-clean_df.shape[0]/df.shape[0], 2))
