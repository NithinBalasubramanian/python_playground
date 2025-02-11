import pandas as pd

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, 4, 5, 2, 4.5, 8, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, labels)

print("Data")
print(df)
# df.info()
# df.describe()

filtered_df_1 = df.loc[:, ['animal']]
print(filtered_df_1)

filtered_by_visit = df[(df["visits"] > 1) & (df["priority"] == 'yes')]
print(filtered_by_visit)


sum_of_visits = df["visits"].sum()
print("SUm of visits", sum_of_visits)

print(df.groupby("animal")["age"].mean())

print(df["animal"].value_counts().reset_index())

print(df.sort_values(["age", "animal"], ascending=[True, False]))

df["priority_flag"] = df["priority"].map({'yes': True, 'no': False})

print(df)

print(df.pivot_table(index="animal", columns="visits", values="age", aggfunc="mean"))