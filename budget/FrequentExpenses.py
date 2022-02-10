# 4. Count Categories with a Counter Collection
import collections
# 7. Plot the Top 5 Most Common Categories
import matplotlib.pyplot as plt
# 1. Import the Expense Module
import Expense

# 2. Read in the Spending Data
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

# 3. Create a List of the Spending categories
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# # 4. Count Categories with a Counter Collection
spending_counter = collections.Counter(spending_categories)

# # 5. Get the Top 5 Categories
top5 = spending_counter.most_common(5)
print("Number of categories = " + str(spending_counter.__len__()))

# # 6. Convert the Dictionary to 2 Lists
categories, count = zip(*top5)

# # 7. Plot the Top 5 Most Common Categories
fig, ax = plt.subplots()

# # 8. Create the bar chart
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

# # 9. Display the graph
plt.show()