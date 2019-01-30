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
        -model_name: People
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

Application level project views:
    A lot of the views and templates used during the creation and outline of the
    application ended up not being used. The following are the templates that ended
    up being used:

    1.Categories:
        1. Person level summary:
            template name = index_person
            view name = index_person
        2. Group level summary:
            template name = index_team
            view name = index_team
        3. Expense Report (person view) with functionality:
            template name = index
            view name = index
        4. Edit category:
            template name=  edit_category
            view name = editCategory
        5. Delete category:
            template name = delete_category
            view name = deleteCategory
    2.Expenses
        1. Add expenses 
            template name= add_expense
            view name = add_expense
        2. Expense list for a given category:
            template name= category_expense_detail.html
            view name=category_expense_list
    3.Bases
        1.header.html
    4.People:
        1. Login - not yet created
        2. Edit -need to be corrected to name only.

    To prevent users from accidentally going into templates created during 
    development we can proceed with two rememdies:
        1. delete views,templates,urls not served up to the user.
            cleaner approach -best approach
        2. comment out urls so they are not accessible by the user.
            easier approach
