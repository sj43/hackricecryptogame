class Quest:
    def __init__(self, date, success):
        self.start_month = date
        self.end_month = -1
        self.success = False
        self.whichquest = -1
        self.quest_string = None
        self.info_to_check = None
        generate_quest_randomly()
        start_info_check()

    def generate_quest_randomly(self):
        self.whichquest = random(1, 9)
        self.quest_string, time_constraint = quests[self.whichquest]
        self.end_month = self.start_month + time_constraint


    def start_info_check(self, player):
        if self.whichquest == 1:
            return quest1_check(player.asset.property)
        elif self.whichquest == 2:
            return quest2_check(player.asset.property)
        elif self.whichquest == 3:
            return quest3_check(player)
        elif self.whichquest == 4:
            return quest4_check(player)
        elif self.whichquest == 5:
            return quest5_check(player)
        elif self.whichquest == 6:
            return quest6_check(player)
        elif self.whichquest == 7:
            return quest7_check(player)
        else:
            return quest8_check(player)

    def quest1_check(self, property):
        return

    def quest2_check(self):
        pass

    def quest3_check(self):
        pass

    def quest3_check(self):
        pass

    def quest4_check(self):
        pass

    def quest5_check(self):
        pass

    def quest6_check(self):
        pass

    def quest7_check(self):
        pass

    def quest8_check(self):
        pass

    def check_quest_overall_success(self, current_date, player):
        if current_date == self.end_month:
            if check_quest_requirements_success(player):
                self.success = True
        else:
            self.success = False

    def check_quest_requirements_success(self, player):
        if whichquest == 1:
            return quest1_check(player.asset.property)
        elif whichquest == 2:
            return quest2_check(player.asset.property)
        elif whichquest == 3:
            return quest3_check(player)
        elif whichquest == 4:
            return quest4_check(player)
        elif whichquest == 5:
            return quest5_check(player)
        elif whichquest == 6:
            return quest6_check(player)
        elif whichquest == 7:
            return quest7_check(player)
        else:
            return quest8_check(player)

    def quest1_check(self, property):
        return

    def quest2_check(self):
        pass

    def quest3_check(self):
        pass

    def quest3_check(self):
        pass

    def quest4_check(self):
        pass

    def quest5_check(self):
        pass

    def quest6_check(self):
        pass

    def quest7_check(self):
        pass

    def quest8_check(self):
        pass
