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
            quest1_check(player.asset.property)
        elif self.whichquest == 2:
            quest2_check(player.asset.property)
        elif self.whichquest == 3:
            quest3_check(player.savings)
        elif self.whichquest == 4:
            quest4_check(player.netWorth)
        elif self.whichquest == 5:
            quest5_check(player.netWorth)
        elif self.whichquest == 6:
            quest6_check(player.payments, player.salary)
        elif self.whichquest == 7:
            quest7_check(player.credit)
        else:
            quest8_check(player.savings, player.assets.investment)

    def quest1_check(self, property):
        self.info_to_check = len(property) + 1

    def quest2_check(self, property):
        self.info_to_check = len(property) + 1

    def quest3_check(self, savings):
        lost = 0.05 * savings
        self.info_to_check = savings
        savings -= lost

    def quest4_check(self, netWorth):
        self.info_to_check = netWorth + 100000

    def quest5_check(self, netWorth):
        self.info_to_check = netWorth + 1000000

    def quest6_check(self, payments, salary):
        self.info_to_check = payments - 3*salary

    def quest7_check(self, credit):
        self.info_to_check = credit + 100

    def quest8_check(self, savings, investment):
        self.info_to_check = savings
        del investment[:]

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
            return quest3_check(player.savings)
        elif whichquest == 4:
            return quest4_check(player.netWorth)
        elif whichquest == 5:
            return quest5_check(player.netWorth)
        elif whichquest == 6:
            return quest6_check(player.payments)
        elif whichquest == 7:
            return quest7_check(player.credit)
        else:
            return quest8_check(player.savings, player.investment)

    def quest1_check(self, property):
        self.info_to_check <= len(property)

    def quest2_check(self, property):
        self.info_to_check <= len(property)

    def quest3_check(self, savings):
        self.info_to_check <= savings

    def quest4_check(self, netWorth):
        self.info_to_check <= netWorth

    def quest5_check(self, netWorth):
        self.info_to_check <= netWorth

    def quest6_check(self, payments):
        self.info_to_check >= payments

    def quest7_check(self, credit):
        self.info_to_check <= credit

    def quest8_check(self, savings, investment):
        self.info_to_check <= savings
