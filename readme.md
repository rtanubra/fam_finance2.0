Goal:
This project is created to help couples or teams keep track of their combined and individual budgets.

Applications:
The project contains multiple mini applications that will enable us to do so:

    1.pages:
        -maintains the header navbar for each of subsequent templates
        -utilizes static bootstrap and js so should work with or without internet.
        -considerations during production would be to move to cdn for speed considerations

    2.groups:
        -maintains the database of groups 
        -functionality allows for editing,creating, listing groups
        -Each group will contain one or more people.
        -model_name: Group
            -group_name
            -group_location

    3.people:
        -maintains the database of people. 
        -functionality allows for editing,creating, listing people
        =model_name: People
            -group_couple - linked to the group database one to many relationship
            -group_name 
            -username

    4.categories:
        -maintains the database of expense categories 
        -functionality allows for editing, creating , listing categories
        -model_name : Category
            -category_person - linked to the people database one to many relationship 
            -category_name
            -category_expected
            -category_spent
            -category_date - used to group expenses into month

    5.expenses:
        -maintains the database of expenses for each category
        -functionality allows for creating and listing expenses
        -model_name : Expense
            -expense_category -linked to the category database on to many relationship.
            -expense_description
            -expense_amount
            -expense_date