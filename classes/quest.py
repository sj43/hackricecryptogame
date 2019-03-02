class Quest:
    def __init__(self, date):
        self.start_month = date
        self.end_month = -1

    def generate_quest_randomly(self):
        quest_string, time_constraint = quests[random(1, 9)]
        self.end_month = self.start_month + time_constraint

    def check_quest_success(self):
        pass
