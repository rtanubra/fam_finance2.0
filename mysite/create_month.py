#================Import this module to create the month's Expense==============
"""
Expense sheet should be {
    exp1: $$,
    exp2: $$,
    exp3: $$
}
"""

cassandra_id= 2

def create_monthly_expenses(expenses_sheet,month,year,person_id):
    expenses = ["credit_card"]
    expected_spendings = [0]
    import datetime 
    from categories.models import Category
    from people.models import People 
    
    my_person = People.objects.get(id=person_id)

    for exp in expenses_sheet:
        expenses.append(exp)
        expected_spendings.append(expenses_sheet[exp])
    for i in range(len(expenses)):
        Category.objects.create(
            category_person = my_person,
            category_name = expenses[i]+str(month)+"_"+str(year),
            category_expected = expected_spendings[i],
            category_date = datetime.datetime(year,month,1)
        )

def create_rey(month,year):
    rey_expense = {
    "groceries":187,
    "pay_erick":700,
    "gas":150,
    "go_transit":260,
    "phone":65,
    "gym":120,
    "living":405
    }
    rey_id = 1 
    create_monthly_expenses(rey_expense,month,year,rey_id)
    
