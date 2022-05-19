import pandas

# TODO HOW TO CREATE DATAFRAME FROM SCRATCH
student_dict = {
    "name_of_student": ["Shakeeb Khan", "Hassan Khan", "Zain Khan", "Wahid Malik", "Shahzad Aslam"],
    "scores": [85, 80, 89, 93, 76]
}

my_created_dataframe = pandas.DataFrame(student_dict)
print(my_created_dataframe)
my_created_dataframe.to_csv("new_csvfile.csv")
