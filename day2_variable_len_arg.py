def student_info(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

student_info(name="Anand", age=22, course="python")