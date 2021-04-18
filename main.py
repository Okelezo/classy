##Budget App  Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories


class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


    # methods
    def deposit(self, deposit_amount):
        self.amount = self.amount + deposit_amount
        return self.amount


    def check_balance(self):
        return self.amount


    def withdraw(self, withdraw_amount):
        if self.amount >= withdraw_amount:
            self.amount = self.amount - withdraw_amount
        else:
            print("you do not have enough money in your budget")
        #ensure there is sufficient funds to withdraw
        #fail if trying to overdraw


    def transfer(self, another_budget, transfer_amount):
        if self.amount >= transfer_amount:
            self.amount = self.amount - transfer_amount
            another_budget.deposit(transfer_amount)



category_1 = Budget("Clothing", 1000)
category_2 = Budget("Food", 1000)
category_3 = Budget("Entertainment", 1000)

print("You now have {} in your {} budget".format(category_1.deposit(400), category_1.category) )
print("Your {} budget balance is {}".format(category_2.category, category_2.check_balance()) )

category_1.transfer(category_2, 666)
print(category_2.check_balance())
print(category_1.check_balance())


#superclass and subclass




