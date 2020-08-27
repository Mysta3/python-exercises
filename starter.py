# # Unlock Academy

# # Homework 1 & 2

# # initialize empty dict
# # user_profile = {'name': '', 'dob': '', 'years_of_experience': '',
# #                 'num_of_languages': '', 'salary_range': '', 'is_active': ''}


# # # assign user input to dict key/pairs
# # user_profile['name'] = input('Enter your Name: ')
# # user_profile['dob'] = input('What is your Date of Birth: ')


# # user_coding_languages = input("List coding languages: ")
# # user_languages = user_coding_languages.strip().split(',')
# # user_answer = input('Are you actively looking? Respond Y/N: ')
# # user_profile['is_active'] = False
# # if(user_answer.lower() == 'y'):
# #     user_profile['is_active'] = True
# # elif(user_answer.lower() == 'n'):
# #     user_profile['is_active'] = False
# # else:
# #     print('[-] ERROR, please re-enter using y/n as an answer')


# # user_profile['num_of_languages'] = len(user_languages)


# # user_experience = input(
# #     'How many years of development experience do you have? \n [1] < 1 year \n [2] 1 - 3 years \n [3] 3 - 8 years \n [4] 8+ years \n Enter Here:  ')

# # user_experience = int(user_experience)
# # if user_experience == 1:
# #     user_profile['years_of_experience'] = '< 1 year'
# #     min_amount = 30
# #     max_amount = 60
# #     if len(user_languages) < 2:
# #         amount = min_amount - 10
# #         amount_max = max_amount - 10
# #         user_profile['salary_range'] = (
# #             f'{amount}k - {amount_max}k')
# #     print(
# #         f'Entry Level Salary ranges from {amount}k - {amount_max}k annually')

# # elif user_experience == 2:
# #     user_profile['years_of_experience'] = '1 - 3 years'
# #     min_amount = 60
# #     max_amount = 80
# #     if len(user_languages) < 3:
# #         amount = min_amount - 10
# #         amount_max = max_amount - 10
# #         user_profile['salary_range'] = (
# #             f'{amount}k - {amount_max}k')
# #     print(
# #         f"Junior Level Salary ranges from {amount}k - {amount_max}k")
# # elif user_experience == 3:
# #     user_profile['years_of_experience'] = '3 - 8 years'
# #     min_amount = 80
# #     max_amount = 90
# #     if len(user_languages) < 4:
# #         amount = min_amount - 10
# #         amount_max = max_amount - 10
# #         user_profile['salary_range'] = (
# #             f'{amount}k - {amount_max}k')
# #     print(
# #         f"Mid-Level Salary ranges from {amount_max}k - {amount_max}k")
# # elif user_experience == 4:
# #     user_profile['years_of_experience'] = '8+ years'
# #     user_profile['salary_range'] = '100k'
# #     print('WELCOME TO THE PROMISE LAND OF CODE!!! SENIOR LEVEL BABY!! 100k+')
# # else:
# #     print('[-] Please pick a valid value')
# #     user_experience = input(
# #         'How many years of development experience do you have? \n [1] < 1 year \n [2] 1 - 3 years \n [3] 3 - 8 years \n [4] 8+ years \n Enter Here:  ')


# # print(user_profile)

# # WHILE LOOP
# print('-------WHILE LOOP -------')
# list_of_colors = ['red', 'yellow', 'blue']
# index = 0
# while len(list_of_colors) > index:
#     print(list_of_colors[index])
#     index += 1

# print('-------FOR LOOP -------')
# for item in list_of_colors:
#     print('[x]', item)

# print('--- PRINT 0 to 10 ----')
# x = range(0, 11)  # print 0 - 10
# for num in x:
#     print(num)

# print('---- PRINT EVERY 2 ----')
# x = range(0, 11, 2)
# for num in x:
#     print(num)

# print('<---- PRINT ODDS ONLY --->')
# x = range(0, 11)
# for num in x:
#     if (num % 2 != 0):
#         print(num)


# # Looping over Dictionaries
# print('------ LOOP OVER DICTIONARY')
# dictionary_list = {'1': 100, '2': 200, '3': 300}
# print(dictionary_list.keys())
# print(dictionary_list.values())

# for key in dictionary_list:
#     print(key, ':', dictionary_list[key])




