# create variable name o hold hello world
# message = """hEllo world to Nkiru's world of world  """
# print(len(message))
# print(len(message))

# print(message[6:])
# print(message.find('world'))
# print(message.count('l'))

# print(message.replace('world', 'kenya'))
# or
# new_message = message.replace('world', 'kenya')
# print(new_message)
# greeting = 'hello'
# name = 'mike'
# message = greeting + ', ' + '' + name + '. ' + "welcome" + '. '
# message = f'{}, {}, Welcome'.format(greeting, name)

# print(help(str.lower))
# num = 3.14
# print(type(num))
# print (12 // 5 )
# print(3 * (2 + 1))
# num = 1
# num *= 10
# print(num)
# num_1 = 3
# num_2 = 2
# print (num_1 < num_2# )
# num_1 = '100'
# num_2 = '200'
# num_1 = int(num_1)
# num_2 = int(num_2)
# print(num_1 + num_2)

# courses.append('Art')
# courses.append('Economics')
# courses.insert(0, 'Art')
# courses.insert(2, 'geology')
#
# courses_2 = ['igbo' ,'hausa']
# courses.extend(courses_2)
# courses.remove('Math') math removed from course list
# pop also a way to remove values
courses = ['History', 'Math', 'Physics', 'CompSci']
# popped = courses.pop() #pop method will remove the last item
# wanna reverse our list?
# courses.reverse()
# wanna sort our list?
# courses.sort() # will sort it alphabetical order
nums = [2,3,4,5,6]
# nums.sort(reverse=True)
# courses.sort(reverse=True) # will not just sort but reverse it
#lets say you do not want to alter the original list and you want a sorted version
# sorted_courses = sorted(courses)
print(courses)
# print(sorted_courses)
print('Physics' in courses)
#loooping
for item in courses:
    print(item) #thisprints out each item of our list

    # now if i wanted to print the index and also the item, lets loop
    for index, course in enumerate(courses):
        print(index, course) # this will bring both the index and the item name
        #enumerate takes two argument? you can also tell it where to
        for index, course in enumerate(courses, start=1):
            print(index, course)
# how to turn our list to a string
course_str = ' - '.join(courses)
print(course_str)
# wht if you wnt to turn a string back to a list
new_list = course_str.split(' - ')
print(new_list)

# if we wanted to know the index where the physics is ?
print(courses.index('Physics'))
print(min(nums))
# print(popped)
# tupple set is immutable, starts withs ( and ends with )
#however a list is mutable and starts with square bracket, when you save into another variable, same change occurs everywhere
# what os sets ?
# sets uses curly bracket , the order or sets changes on each execution: used to test if a value is really part of a set , like if you add ada,=m, when there is also adam, it will not show the second adam
# set is optimized for :
cs_courses = {'math', "lion" 'math'}
