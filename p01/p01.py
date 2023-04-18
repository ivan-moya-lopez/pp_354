import csv
from collections import Counter

#
def media (lista):
    print(lista)
    sumar = list(map(lambda x: round(float(x), 2), lista))
    return sum(sumar) /len(lista)

#
with open('../diabetes_sub_sample1500x17.csv',newline='') as csvfile:
    lector_archivo= csv.DictReader(csvfile)
    type_col={'Type':[]}
    hbp_col = {'HighBP':[]}
    bmi_col = {'BMI':[]}
#
#
    for fila in lector_archivo:
        type_col['Type'].append(fila['Diabetes_012'])
        hbp_col['HighBP'].append(fila['HighBP'])
        bmi_col['BMI'].append(fila['BMI'])

type_list=list(type_col.values())
res_type=Counter(type_list[0])


high_b_p_list= list(hbp_col.values())
res_hbp=Counter(high_b_p_list[0])

#0 = no diabetes 1 = prediabetes 2 = diabetes
print(res_type)
#0 = no high BP 1 = high BP
print(res_hbp)
#0 = no high cholesterol 1 = high cholesterol
#Body Mass Index

print(media(list(bmi_col.values())[0]))
#media mediana y moda percentiles

#Stroke (Ever told) you had a stroke. 0 = no 1 = yes
#physical activity in past 30 days - not including job 0 = no 1 = yes
#Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) 0 = no 1 = yes
#Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor
#Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? scale 1-30 days
#Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? scale 1-30 days
#Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes
#0 = female 1 = male
#13-level age category (_AGEG5YR see codebook) 1 = 18-24 9 = 60-64 13 = 80 or older
#media mediana y moda percentiles
#Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = Grades 1 through 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED (High school graduate) 5 = College 1 year to 3 years (Some college or technical school) 6 = College 4 years or more (College graduate)
#Income scale (INCOME2 see codebook) scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more
#media mediana y moda percentiles





