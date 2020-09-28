# # Unlock Academy


# Homework 1 & 2


# def printDivider(name):
#     print(f'----------{name.upper()}---------------')


# initialize empty dict
# user_profile = {'name': '', 'dob': '', 'years_of_experience': '',
#                 'num_of_languages': '', 'salary_range': '', 'is_active': ''}


# def createUserProfile():
#     # assign user input to dict key/pairs
#     user_profile['name'] = input('Enter your Name: ')
#     user_profile['dob'] = input('What is your Date of Birth: ')
#     user_coding_languages = input("List coding languages: ")
#     user_languages = user_coding_languages.strip().split(',')
#     user_answer = input('Are you actively looking? Respond Y/N: ')
#     user_profile['is_active'] = False
#     if(user_answer.lower() == 'y'):
#         user_profile['is_active'] = True
#     elif(user_answer.lower() == 'n'):
#         user_profile['is_active'] = False
#     else:
#         print('[-] ERROR, please re-enter using y/n as an answer')


#     user_profile['num_of_languages'] = len(user_languages)
#     user_experience = input(
#         'How many years of development experience do you have? \n [1] < 1 year \n [2] 1 - 3 years \n [3] 3 - 8 years \n [4] 8+ years \n Enter Here:  ')

#     user_experience = int(user_experience)
#     if user_experience > 4:
#         raise ValueError

#     elif user_experience == 1:
#         user_profile['years_of_experience'] = '< 1 year'
#         min_amount = 30
#         max_amount = 60
#         if len(user_languages) < 2:
#             amount = min_amount - 10
#             amount_max = max_amount - 10
#             user_profile['salary_range'] = (
#                 f'{amount}k - {amount_max}k')
#         else:
#             amount = min_amount
#             amount_max = max_amount
#         user_profile['salary_range'] = (
#             f'{amount}k - {amount_max}k')
#         print(
#             f'Entry Level Salary ranges from {min_amount}k - {max_amount}k annually')

#     elif user_experience == 2:
#         user_profile['years_of_experience'] = '1 - 3 years'
#         min_amount = 60
#         max_amount = 80
#         if len(user_languages) < 3:
#             amount = min_amount - 10
#             amount_max = max_amount - 10
#             user_profile['salary_range'] = (
#                 f'{amount}k - {amount_max}k')
#         else:
#             amount = min_amount
#             amount_max = max_amount
#             user_profile['salary_range'] = (
#                 f'{amount}k - {amount_max}k')
#         print(
#             f"Junior Level Salary ranges from {amount}k - {amount_max}k")

#     elif user_experience == 3:
#         user_profile['years_of_experience'] = '3 - 8 years'
#         min_amount = 80
#         max_amount = 90
#         if len(user_languages) < 4:
#             amount = min_amount - 10
#             amount_max = max_amount - 10
#             user_profile['salary_range'] = (
#                 f'{amount}k - {amount_max}k')
#         else:
#             amount = min_amount
#             amount_max = max_amount
#             user_profile['salary_range'] = (
#                 f'{amount}k - {amount_max}k')
#         print(
#             f"Mid-Level Salary ranges from {amount_max}k - {amount_max}k")
#     elif user_experience == 4:
#         user_profile['years_of_experience'] = '8+ years'
#         user_profile['salary_range'] = '100k'
#         print('WELCOME TO THE PROMISE LAND OF CODE!!! SENIOR LEVEL BABY!! 100k+')
#     else:
#         print('[-] Please pick a valid value')
#         user_experience = input(
#             'How many years of development experience do you have? \n [1] < 1 year \n [2] 1 - 3 years \n [3] 3 - 8 years \n [4] 8+ years \n Enter Here:  ')


# Homework 5


# def create_user_id():
#     user_id = id(user_profile['name'])
#     user_profile.update({'id': user_id})
#     printDivider('UNIQUE ID')


# create_user_id()

# print(user_profile)

#LESSON 7
# question = input('Would you like to create another user?')
# if question.upper() == 'Y':
#     createUserProfile()
# else:
#     print('User(s) created!')

# WHILE LOOP
# printDivider('while loops')
# list_of_colors = ['red', 'yellow', 'blue']
# index = 0
# while len(list_of_colors) > index:
#     print(list_of_colors[index])
#     index += 1

# printDivider('for loops')
# for item in list_of_colors:
#     print('[x]', item)

# printDivider('range function')
# x = range(0, 11)  # print 0 - 10
# for num in x:
#     print(num)

# printDivider('range with a step of 2')
# x = range(0, 11, 2)
# for num in x:
#     print(num)

# printDivider('print odd numbers')
# x = range(0, 11)
# for num in x:
#     if (num % 2 != 0):
#         print(num)


# # Looping over Dictionaries
# printDivider('loop over dictionaries')
# dictionary_list = {'1': 100, '2': 200, '3': 300}
# print(dictionary_list.keys())
# print(dictionary_list.values())

# for key in dictionary_list:
#     print(key, ':', dictionary_list[key])


# LESSON 6
# CLASSES

class UserProfile:
    def __init__(self, dob, full_name, country, state, number_of_education_years, age, expected_salary):
        super().__init__(dob, full_name, country, state,
                         number_of_education_years, age, expected_salary)
        self.password = ''
        self.email = None
        self.is_active = True

        self.dob = dob
        self.full_name = full_name
        self.country = country
        self.state = state
        self.number_of_education_years = number_of_education_years
        self.age = age
        self.expected_salary = expected_salary

    def get_age(self):
        return self.age

    def set_age(self, new_password):
        self.password = new_password

    def get_name(self):
        return self.full_name

    def set_name(self, new_name):
        self.full_name = new_name

    def get_dob(self):
        return self.dob

    def set_dob(self, new_dob):
        self.dob = new_dob

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def get_country(self):
        return self.country

    def set_country(self, new_country):
        self.state = new_country

    def get_expected_salary(self):
        return self.expected_salary

    def set_expected_salary(self, new_expected_salary):
        self.expected_salary = new_expected_salary


#  def __init__(self, dob, full_name, country, state, number_of_education_years, age, expected_salary):
user_1 = UserProfile(
    input('Enter DOB: \n'),
    input('Enter Full Name: \n'),
    input('Enter Country: \n'),
    input('Enter State: \n'),
    input('Enter Education Years: \n'),
    input('Enter Age: \n'),
    input('Enter Expected Salary: \n'),
)

print(
    f'{user_1.get_name()} \n',
    f'{user_1.get_dob()} \n',
    f'{user_1.get_country()} \n',
    f'{user_1.get_state()} \n',
    f'{user_1.get_age()} \n',
    f'{user_1.get_expected_salary()} \n',
)


class Developer(UserProfile):
    def __init__(self):
        pass
        self.listOFLanguages = ['Angular', 'React', 'Vue']

class Designer(UserProfile):
    def __init__(self):
       pass
       self.softwarePrograms = ['Adobe Illustrator', 'Figma', 'Photo Shop']
