from selenium import webdriver
from time import sleep
import csv
# my driver path directory
robot = webdriver.Firefox(executable_path = r'C:\Users\FaridbGodar\Desktop\MonsterCode_practice\geckodriver.exe')
print('Robot is ON')
# go on login page
robot.get('https://www.instagram.com/accounts/login/?hl=en')
print('come login page and wait 3 second')
sleep(3)
# fonction of click on Accept and send username && password
def login(username, password):
    # click Accept 
    try:    
        Accept = robot.find_element_by_class_name('bIiDR')
        Accept.click()
        print('click on Accept and wait for 3 second')
        sleep(3)
        # username find element
        Username = robot.find_element_by_name('username')
        Username.send_keys(username)
        print('username send')
        # password find element
        Password = robot.find_element_by_name('password')
        Password.send_keys(password)
        print('password send')
        # login find element
        Login = robot.find_element_by_xpath('//button[@type = "submit"]')
        Login.click()
        print('click on login button and wait for 5 second')
        sleep(5)
    except:
        # username find element
        Username = robot.find_element_by_name('username')
        Username.send_keys(username)
        print('username send')
        # password find element
        Password = robot.find_element_by_name('password')
        Password.send_keys(password)
        print('password send')
        # login find element
        Login = robot.find_element_by_xpath('//button[@type = "submit"]')
        Login.click()
        print('click on login button and wait for 5 second')
        sleep(5)
# read my password from txt file
with open('My_Password.txt', 'r') as file:
    password = file.readline()
    print('read password from My_Password.txt file')
username = 'faridbgodar'
login(username, password)
# come in my home page
robot.get(f'https://www.instagram.com/{username}')
print('come in my home page and wait for 3 second')
sleep(3)
# information of my home page
def information():      
    Post = str(robot.find_elements_by_tag_name('li')[0].text)
    Followers = str(robot.find_elements_by_tag_name('li')[1].text)
    Following = str(robot.find_elements_by_tag_name('li')[2].text)
    print('The Count of', Post, Followers, Following)
information()
# hashtag 
hashtag = []
add = int(input('how many hashtag do you enter ? '))
for name_of_hashtag in range(0, add):
    name_of_hashtag = input('enter your hashtag name : ')
    hashtag.append(name_of_hashtag)
    print(hashtag) 
    # robot go first hashtag
    tag = -1
for i in hashtag:
    tag += 1
    robot.get(f'https://www.instagram.com/explore/tags/{hashtag[tag]}')
    print(f'robot come in {hashtag[tag]} and wait 3 second')
    sleep(3)
    # open first ceramic
    first_ceramic = robot.find_element_by_xpath('//div[@class="_9AhH0"]')
    first_ceramic.click()
    print('first ceramic opened and wait for 3 second')
    sleep(3)
    # like && follow && give id of followed
    count = int(input('how many like follow && post?'))
    i = 0
    id_followed_list = []
    while i != count:
        like = robot.find_element_by_css_selector('.fr66n > button:nth-child(1)')
        like.click()
        follow = robot.find_element_by_css_selector('.bY2yH > button:nth-child(2)')
        follow.click()
        id_followed = str(robot.find_element_by_css_selector('.e1e1d > span:nth-child(1) > a:nth-child(1)').text)
        id_followed_list.append(id_followed)
        print(id_followed, 'followed and like')
        next_post = robot.find_element_by_css_selector('._65Bje')
        next_post.click()
        sleep(3)
        print(id_followed_list)
        file = csv.writer(open(r'C:\Users\FaridbGodar\Desktop\MonsterCode_practice\output.csv', 'w'))
        file.writerow(id_followed_list)
        i += 1
        