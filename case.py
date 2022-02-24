import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')
print(df)


#У учащихся каких уровней образования результаты лучше?

highschool_math = df[df['parental level of education'] == 'high school']['math score'].mean()
somecollege_math = df[df['parental level of education'] == 'some college']['math score'].mean()
highschool_reading = df[df['parental level of education'] == 'high school']['reading score'].mean()
somecollege_reading = df[df['parental level of education'] == 'some college']['reading score'].mean()
highschool_writing = df[df['parental level of education'] == 'high school']['writing score'].mean()
somecollege_writing = df[df['parental level of education'] == 'some college']['writing score'].mean()

print(highschool_math)
print('Результаты по математике:', 'Старшая школа:', round(highschool_math, 2), 'Студенты коледжа:', round(somecollege_math, 2))
print('Результаты по чтению:', 'Старшая школа:', round(highschool_reading, 2), 'Студенты коледжа:', round(somecollege_reading, 2))
print('Результаты по письму:', 'Старшая школа:', round(highschool_writing, 2), 'Студенты коледжа:', round(somecollege_writing, 2))

parlev = df['parental level of education'].value_counts()
parlev.plot(kind = 'barh')
plt.show()
s = pd.Series(data= [highschool_math, somecollege_math, highschool_reading, somecollege_reading, highschool_writing, somecollege_writing],
index = ['Мат.старш', 'Мат.кол', 'Чт.старш', 'Чт.кол', 'Письмо.старш', 'Письмо.кол'])
s.plot(kind = 'barh', grid = True)
plt.show()

parlev = df['parental level of education'].value_counts()
parlev.plot(kind = 'pie')
plt.show()
s = pd.Series(data= [highschool_math, somecollege_math],
index = ['Мат.старш', 'мат.кол'])
s.plot(kind = 'pie')
plt.show()


