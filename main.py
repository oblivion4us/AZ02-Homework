import pandas as pd

students = ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5',
            'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10']
subjects = ['Математика', 'Физика', 'Химия', 'Литература', 'История']

data = {
    'Имя': students,
    'Математика': [5, 4, 3, 4, 5, 2, 3, 4, 5, 4],
    'Физика': [4, 3, 5, 2, 4, 5, 4, 3, 4, 2],
    'Химия': [3, 5, 4, 3, 2, 4, 5, 4, 5, 3],
    'Литература': [5, 4, 3, 5, 4, 3, 2, 4, 5, 5],
    'История': [4, 5, 4, 3, 5, 4, 3, 5, 4, 2]
}

df = pd.DataFrame(data)

print(f"{df.head()}\n")

# Средние оценки по предметам
mean_Math = df['Математика'].mean()
mean_Physics = df['Физика'].mean()
mean_Chemistry = df['Химия'].mean()
mean_Literature = df['Литература'].mean()
mean_History = df['История'].mean()

# Медианы по предметам
median_Math = df['Математика'].median()

median_Physics = df['Физика'].median()

median_Chemistry = df['Химия'].median()

median_Literature = df['Литература'].median()

median_History = df['История'].median()

# Квантили и межквартальные размахи по предметам
# Квантили и межквартальные размахи по Математике
Q1_Math= df['Математика'].quantile(0.25)

Q3_Math = df['Математика'].quantile(0.75)

IQR_Math = Q3_Math - Q1_Math

# Квантили и межквартальные размахи  по Физике
Q1_Physics= df['Физика'].quantile(0.25)
Q3_Physics = df['Физика'].quantile(0.75)

IQR_Physics = Q3_Physics - Q1_Physics

# Квантили и межквартальные размахи  по Химии
Q1_Chemistry = df['Химия'].quantile(0.25)
Q3_Chemistry = df['Химия'].quantile(0.75)

IQR_Chemistry = Q3_Chemistry - Q1_Chemistry

# Квантили и межквартальные размахи  по Литературе
Q1_Literature = df['Литература'].quantile(0.25)
Q3_Literature = df['Литература'].quantile(0.75)

IQR_Literature = Q3_Literature - Q1_Literature

# Квантили и межквартальные размахи  по Истории
Q1_History = df['История'].quantile(0.25)
Q3_History = df['История'].quantile(0.75)

IQR_History = Q3_History - Q1_History

# Стандартное отклонение по Математике
std_Math = df['Математика'].std()

# Стандартное отклонение по Физике
std_Physics = df['Физика'].std()

# Стандартное отклонение по Химии
std_Chemistry = df['Химия'].std()

# Стандартное отклонение по Литературе
std_Literature = df['Литература'].std()

# Стандартное отклонение по Истории
std_History = df['История'].std()

# Вывод данных
print(f"Средние оценки по\nМатематике: {mean_Math}\nФизике: {mean_Physics}\nХимии: {mean_Chemistry}\nЛитературе: {mean_Literature}\nИстории: {mean_History}\n")

print(f"Медианы по\nМатематике: {median_Math}\nФизике: {median_Physics}\nХимии: {median_Chemistry}\nЛитературе: {median_Literature}\nИстории: {median_History}\n")

print(f"Квантили и межквартальные размахи по\nМатематике: Q1={Q1_Math}; Q3={Q3_Math}; IQR={IQR_Math}\nФизике: Q1={Q1_Physics}; Q3={Q3_Physics}; IQR={IQR_Physics}\nХимии: Q1={Q1_Chemistry}; Q3={Q3_Chemistry}; IQR={IQR_Chemistry}\nЛитературе: Q1={Q1_Literature}; Q3={Q3_Literature}; IQR={IQR_Literature}\nИстории: Q1={Q1_History}; Q3={Q3_History}; IQR={IQR_History}\n")

print(f"Стандартные отклонения по\nМатематике: {std_Math}\nФизике: {std_Physics}\nХимии: {std_Chemistry}\nЛитературе: {std_Literature}\nИстории: {std_History}")