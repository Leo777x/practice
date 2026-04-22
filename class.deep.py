'''CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("======== ENCAPSULATION =========")
''' PYTHONDA
          public __private _protected
'''


class Account():
    # state
    description = "The class makes bank accounts"
    # construction

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
    # methods

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("LEO", 1000)
my_account.get_balance()

print("------------")

my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("-------------")


try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target State found:", err)


print("owner before:", my_account.holder)  # state

# getter vs setter
my_account.holder = "Martin"

print("owner after", my_account.holder)
