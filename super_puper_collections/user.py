from collections import namedtuple

User = namedtuple("User", ["name", "surname", "email", "plan"])

users = [
    User("Mary", "Griffin", "sonnen@yahoo.com", "Basic"),
    User("Brenda", "Young", "retoh@outlook.com", "Silver"),
    User("Kathleen", "Lyons", "balchen@att.net", "Gold"),
    User("Pamela", "Hicks", "corrada@sbcglobal.net", "Silver"),
    User("William", "Townsend", "kosact@verizon.net", "Gold"),
    User("Clayton", "Morris", "berserk@yahoo.com", "Silver"),
    User("Dorothy", "Dennis", "sequin@live.com", "Gold"),
    User("Tyler", "Walker", "noahb@comcast.net", "Basic"),
    User("Joseph", "Moore", "ylchang@sbcglobal.net", "Silver"),
    User("Kenneth", "Richardson", "tbusch@me.com", "Bronze"),
    User("Stephanie", "Bush", "neuffer@live.com", "Gold"),
    User("Gregory", "Hughes", "juliano@att.net", "Basic"),
    User("Tracy", "Wallace", "sblack@me.com", "Silver"),
    User("Russell", "Smith", "isaacson@comcast.net", "Bronze"),
    User("Megan", "Patterson", "hoangle@outlook.com", "Basic"),
]
users.sort(key=lambda x: x.email)
d = {"Gold": 0, "Silver": 1, "Bronze": 2, "Basic": 3}
users.sort(key=lambda x: d[x.plan])
for u in users:
    print(f"{u.name} {u.surname}\n  Email: {u.email}\n  Plan: {u.plan}\n")
