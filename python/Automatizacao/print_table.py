table_data = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

table_withs =[0] * len(table_data)
for i in range(len(table_data)):
    table_withs[i] = max(len(item) for item in table_data[i])

rows = len(table_data)
cols = len(table_data[0])

for col in range(cols):
    rows_items = []
    for row in range(rows):
        justify_text = table_data[row][col].rjust(table_withs[row])
        rows_items.append(justify_text)
    print(" ".join(rows_items))

