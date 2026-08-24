print("Student Information System")

full_name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
programme = input("Enter your programme: ")
level = input("Enter your level: ")
age = input("Enter your age: ")
favourite_language = input("Enter your favourite programming language: ")
name_part = full_name[:3].lower()
username = name_part + student_id

domain = "@st.ug.edu.gh"
email = username + domain