from pyspark.sql.functions import *
from pyspark.mllib.regression import LinearRegressionWithSGD as lrSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.sql import SparkSession
from pyspark import SparkContext
sc = SparkContext()


# """
# VARIABLE DESCRIPTIONS:
# survival        Survival
#                 (0 = No; 1 = Yes)
# pclass          Passenger Class
#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
# name            Name
# sex             Sex
# age             Age
# sibsp           Number of Siblings/Spouses Aboard
# parch           Number of Parents/Children Aboard
# ticket          Ticket Number
# fare            Passenger Fare
# cabin           Cabin
# embarked        Port of Embarkation
#                 (C = Cherbourg; Q = Queenstown; S = Southampton)
# """


spark = SparkSession \
    .builder \
    .appName("Python Spark regression example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# reading from csv file
df = spark.read.csv('titanic.csv', header=True, inferSchema=True)

# display the df
# df.show(5)

# shape of the dataframe
shape = (df.count(), len(df.columns))
print(shape)  # (891, 11)


# how many of 'Age' values are null
missing_ages = df.where(col("Age").isNull()).count()
print("Number of missing age collumns:", missing_ages)

# create a new column as gender, when Sex is female it is zero when sex is
# male it is one
df.withColumn('Gender', when(df.Sex == 'male', 1).otherwise(0)).show(5)

# checking the shape after addning new column for gender
shape = (df.count(), len(df.columns))
print(shape)  # (891, 12)

# List all of the Ages that are not null
df_not_null_ages = df.filter(df.Age.isNotNull())
df_not_null_ages.show(10)


# Slice the dataframe for those whose Embarked section was 'C'
df_only_C = df.filter(df.Embarked == 'C')
df_only_C.show(10)

# Describe a specific column
df.describe().show()

df.select('Embarked').distinct().show()
df.agg(*(countDistinct(col(c)).alias(c) for c in df.columns)).show()

print(f"MALE AND FEMALE COUNT")

# df_male_female = df.filter(df.Gender == 1)
# df_male_female.show()



genders_counter = {'male': 0, 'female': 0}

for row in df.collect():
    if row.Sex:
        genders_counter[row.Sex] += 1

print(genders_counter)

average_age_of_men = 0
average_age_of_women = 0

men_count = 0
women_count = 0

for row in df_only_C.collect():
    if row.Sex == 'female':
        if row.Age:
            women_count += 1
            average_age_of_women += row.Age
    else:
        if row.Sex == 'male':
            if row.Age:
                men_count += 1
                average_age_of_men += row.Age

average_age_of_men /= men_count
average_age_of_women /= women_count

print("Average age for men and women Who embarked on C port")
print("men: "+str((average_age_of_men)) +
      " women: "+str((average_age_of_women)))
print()


woman_ages = []
man_ages = []
max_man_age = float('-inf')
max_woman_age = float('-inf')
for row in df_only_C.collect():
    if row.Sex == 'female':
        if row.Age:
            if row.Age > max_woman_age:
                max_woman_age = row.Age
    else:
        if row.Sex == 'male':
            if row.Age:
                if row.Age > max_man_age:
                    max_man_age = row.Age

print("Maximum age for men and women Who embarked on C port")
print("men: "+str(max_man_age)+" women: "+str(max_woman_age))
