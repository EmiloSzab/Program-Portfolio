if __name__ == "__main__":

    students = int(input('How many students are there? '))
    group_size = int(input('What is the required group size? '))

    groups = (students//group_size)
    left_students = (students % group_size)

    if left_students == 1:
        print(f'There will be {groups} groups with {left_students} student remaining')
    else:
        print(f'There will be {groups} groups with {left_students} students remaining')