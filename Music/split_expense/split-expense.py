group_name = input("Enter name of group ")
num_of_mem = int(input("Enter total number of members "))
members = []

list_of_expense = []

num = 0

while num < num_of_mem:
    name = input("Enter menbers name " )
    members.append(name)
    num = num + 1

for people in members:
    expense = {"name": "","total_expense": 0,"payers":[]}
    expense['name'] = people
    list_of_expense.append(expense)

for mem in list_of_expense:
    for people in members:
        if mem['name'] == people:
            pass
        else:
            pay = {'name': '', 'money': 0}
            pay['name'] = people
            mem['payers'].append(pay)

print("group name ",group_name)
print("num of mem ",num_of_mem)

print("list of members ",members)
#print("list_of_expense ",list_of_expense)

def calculate_expense(who_paid,how_much):
    for people in list_of_expense:
            if who_paid in people.values():
                how_much = how_much + int(people['total_expense'])
                people['total_expense'] = how_much
                individual_expense = people['total_expense']/num_of_mem
                for pay in people['payers']:
                    pay['money'] = individual_expense
                break

    #print("final list ",list_of_expense)


def optimise_pay():

    num = 0
    for current_pay in list_of_expense[num]['payers']:
        next_num = num +1
        try:
            while next_num < len(list_of_expense):
                for pay in list_of_expense[next_num]['payers']:
                    if list_of_expense[num]['name'] == pay['name']:
                        for pay_mem in list_of_expense[num]['payers']:
                            if list_of_expense[next_num]['name'] == pay_mem['name']:
                                actual_pay = pay_mem['money'] - pay['money']
                            if actual_pay > 0 and list_of_expense[next_num]['name'] == pay_mem['name']:
                                pay_mem['money'] = actual_pay
                                pay['money'] = 0
                            elif actual_pay < 0 and list_of_expense[next_num]['name'] == pay_mem['name']:
                                pay['money'] = abs(actual_pay)
                                pay_mem['money'] = 0
                            elif actual_pay == 0 and list_of_expense[next_num]['name'] == pay_mem['name']:
                                pay_mem['money'] = 0
                                pay['money'] = 0
                next_num = next_num +1
        except:
            pass
        num = num +1
        next_num = num +1

    #print("optimise list ",list_of_expense)

def show_expense():
    for people in list_of_expense:
        print("============================================")
        print(f"Total expense of {people['name']} is {people['total_expense']}")
        for payer in people['payers']:
            print(f"{payer['name']} will pay {payer['money']} to {people['name']}")

total_expense = 0

while True:
    choice = input("Select one 1.Show expenses  2.Enter expense ")
    print("choise is ",choice)
    if choice == '2':
        who_paid = input("who paid? ")
        how_much = int(input("how much money was paid "))
        #print("list ",list_of_expense)
        calculate_expense(who_paid,how_much)
        optimise_pay()

    elif choice == '1':
        show_expense()
        #print("expense list ",final_expence)

