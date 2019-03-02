class Quest:
    def __init__(self, date, success):
        self.start_month = date
        self.end_month = -1
        self.success = False
        self.whichquest = -1

    def generate_quest_randomly(self):
        self.whichquest = random(1, 9)
        quest_string, time_constraint = quests[self.whichquest]
        self.end_month = self.start_month + time_constraint

    def check_quest_overall_success(self, current_date):
        if current_date == self.end_month and check_quest_requirements_success():
            self.success = True
        else:
            False
            
    def check_quest_requirements_success(self):
