from bs4 import BeautifulSoup
import requests

#we will give the url of the page we want to scrape - in this case, a hockey team website
#and we will provide the basic setup as below to get the html code of the page
url = f"https://www.scrapethissite.com/pages/forms/"
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")

#Answer the following five questions with data scraped from the website url given above.
#There is not necessarily one correct way to do this so feel free to experiment with different approaches.
#Hint: inspect the html code of the elements to find the tags and classes you need to scrape.

#######################
#Question 1: How many items/teams are shown on the first page? Only return the number as an integer. (Hint: 25 items) 
num_items = #YOUR CODE HERE
print(num_items)

#######################
#Question 2: What are the column titles of the table? Return the column names in a list.
column_titles = []
for c in #YOUR CODE HERE :
    column_titles.append(#YOUR CODE HERE) 
print(column_titles)

#######################
#Question 3: What are the names of the top 5 teams on the first page? 
#Return the team names in LOWER CASE in a list.
teams = []
for t in #YOUR CODE HERE:
    teams.append(#YOUR CODE HERE)
print(teams)

#######################    
#Question 4: Among the 25 teams on the first page, which team has the highest number of wins? How many wins does it have?
#Break the tie arbitrarily. Return the team name and it's number of wins formated in JSON format.
current_max_win = 0
current_max_win_team = ""
for t in #YOUR CODE HERE:
    team_win = #YOUR CODE HERE  
    if team_win > current_max_win:
        current_max_win = #YOUR CODE HERE 
        current_max_win_team = #YOUR CODE HERE 

json = {
    "team": #YOUR CODE HERE,
    "wins": #YOUR CODE HERE
}
print(json)

#######################
#Question 5: Among the 25 teams shown on the first page, which teams have win percentages of over 50% (the ones whose win % are green)? 
#Return the team names and their win percentages in JSON format in a list.
teams_win_over_50 = []
for t in #YOUR CODE HERE:
    team_name = #YOUR CODE HERE
    win_percentage = #YOUR CODE HERE

    if #YOUR CODE HERE:
        json = {
            #YOUR CODE HERE
        }
        teams_win_over_50.append(json)
print(teams_win_over_50)