team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]

new_member = ['js', 10]

#team = team + new_member
team += new_member
# len(team) == 8

del(team[2]) #team[2] 삭제
# len(team) == 7

del(team[2:4])
# len(team) == 5