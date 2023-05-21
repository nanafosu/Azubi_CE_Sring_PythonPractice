
my_story = ["Azubi Africa", "Cloud Engineering", "Spring23"]
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
experience = input('How was your experience as a cloud engineer trainee\nin Azubi Africa during the first 2 weeks in one word? ')
training_session = input('How do you see the tutorials and check sessions? ')
skill_01_week1 = input("What did you learn about in your first week? ")
skill_01_use = input("What is " + skill_01_week1 + " used for? For: ")
skill_01_capable1 = input('What has your knowledge in ' + skill_01_week1 + ' made you cabable to do? \nI am capable in ')
skill_01_capable2 = input('I am also capable in ')
skill_02_week2 = input('What have you started learning in your second week? ')
skill_02_use = input('What is ' + skill_02_week2 + '? ')
feeling_possibilities = input('How do you feel about the possibilities? ')
python_knowledge01 = input('What have you learnt in ' + skill_02_week2 + ' so far? State one: ')
python_knowledge02 = input('And what else? State one: ')
cloud_role = input('What cloud engineering role do you hope to focus on? ')
output1 = f"Hi, I'm {first_name.capitalize()} {last_name.upper()} a cloud trainee at {my_story[0]} and this is my story:"
output2 = ('As a Cloud Engineer trainee I have learnt ' + skill_01_week1 + ' for ' 
           + skill_01_use + ' and started my journey in \nlearning ' + skill_02_week2 + 
           ', a ' + skill_02_use + ' with vast applications in ' + my_story[1] + '.\nWith ' + skill_01_week1 + 
           ', I have gained proficiency in ' + skill_01_capable1 + ' and ' + skill_01_capable2 + 
           '\nMy introduction to ' + skill_02_week2 + ' included ' + python_knowledge01 + 
           ',' + python_knowledge02 + '. ') 
print('\n')
print (output1)
print('\n')
print (output2)
print('\n')
