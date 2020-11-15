import random
import time

#Make the class

class countries:
    def __init__(self, name, language, leader):
        self.name = name
        self.language = language
        self.leader = leader
        self.wars = 0
        self.friends = []
        self.enemies = []

    def declare_war(self, country):
        if not country in self.enemies:
            self.enemies.append(country)
        for i in self.friends:
            if(i == country):
                self.friends.remove(i)
        print(self.name, "declared a war with", country.name)
        Methods = ["murder", "bisect", "hang", "quarter", "choke", "decapitate", "throttle", "defenestrate"]
        v = random.choice(Methods)
        print(f'{self.leader} wants to {v} {country.leader}')
        country.answer_war(self)
        g = random.randint(0, 2)
        if(g == 1):
            self.resolve_war(country)
        elif(g == 0):
            print(self.name, "won the war")
            self.wars += 1
            d = random.choice(Methods)
            print(f'{self.leader} managed to {d} {country.leader}')
        elif(g == 2):
            print(country.name, "won the war")
            country.wars += 1
            d2 = random.choice(Methods)
            print(f'{country.leader} managed to {d2} {self.leader}')
    def resolve_war(self, country):
        print(self.name, "resolved a war with", country.name)
        country.answer_resolve_war(self)
        q = random.randint(0, 2)
        if(q == 1):
            self.befriend(country)
        for i in self.enemies:
            if(i == country):
                self.enemies.remove(i)


    def befriend(self, country):
        if not country in self.friends:
            self.friends.append(country)
        for i in self.enemies:
            if(i == country):
                self.enemies.remove(i)
        print(self.name, "befriended", country.name)
        Methods = ["have tea with", "meet", "have cake with", "talk to", "give some missiles to"]
        v = random.choice(Methods)
        print(f'{self.leader} wants to {v} {country.leader}')
        country.answer_friend_request(self)

    def answer_friend_request(self, country):
        if not country in self.friends:
            self.friends.append(country)
        for i in self.friends:
            if(i == country):
                self.friends.remove(i)
        print(self.name, "befriended", country.name)
        Methods = ["have tea with", "meet", "have cake with", "talk to", "give some missiles to"]
        v = random.choice(Methods)
        print(f'{self.leader} wants to {v} {country.leader}')


    def answer_war(self, country):
        if not country in self.enemies:
            self.enemies.append(country)
        for i in self.friends:
            if(i == country):
                self.friends.remove(i)
        print(self.name, "accepted a war with", country.name)


    def answer_resolve_war(self, country):
        for i in self.enemies:
            if(i == country):
                self.enemies.remove(i)
        print(self.name, "resolved a war with", country.name)

#Define Countries

England = countries("England", "English", "Boris Johnson")
Russia = countries("Russia", "Russian", "Vladimir Putin")
America = countries("America", "English", "Donald Trump")
Poland = countries("Poland", "Polish", "Andrzej Duda")
Germany = countries("Germany", "German", "Frank-Walter Steinmeier")
France = countries("France", "French", "Emmanuel Macron")

#Add to list

places = []
places.append(England)
places.append(Russia)
places.append(America)
places.append(Poland)
places.append(Germany)
places.append(France)

#Declare some war

for i in range(7):
    x = random.sample(places, 2)
    x[0].declare_war(x[1])


#Print Results

for i in places:
    i.enemies = set(i.enemies)
    i.friends = set(i.friends)
    print("\n")
    print("Country:", i.name, end = '')
    print("\n")
    print("\n")
    print("    ", "Friends:", end = '')
    print("\n")
    for x in i.friends:
        print("    ", x.name, end = '')
    print("\n")
    print("\n")
    print("    ", "Enemies:", end = '')
    print("\n")
    for x in i.enemies:
        print("    ", x.name, end = '')
    print("\n")
    print("\n")
    print("    ", "Wars Won:", i.wars, end = '')
    print("\n")
    print("\n")
