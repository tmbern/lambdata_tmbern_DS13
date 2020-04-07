
class Team():
    def __init__(self, name, city, sport=None, roster=[]):
        self.name = name
        self.city = city
        self.sport = sport
        self.roster = roster

    # This is a property/noun
    @property    
    def full_name(self):
        return f"{team.city} {team.name}"

    # this is a method/verb
    def advertise(self):
        print("PLEASE COME TO", self.city.upper(), "TO SEE US PLAY")

if __name__ == "__main__":

    teams = [
        {"name": "Yankees", "city": "New York"},
        {"name": "Mets", "city": "New York"},
        {"name": "Nationals", "city": "Washington"}
    ]


    # for team in teams:
    #     print(team['city'] + " " + team["name"])

    for d in teams:
        # print(full_name(team))

        team = Team(d['name'], d['city'])
        print(team.name)
        print(team.full_name)
        team.advertise()