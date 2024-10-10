import pandas as pd
import random

# Read the Excel file
df = pd.read_excel('newname.xlsx')

# Ensure the data has the correct columns
assert all(col in df.columns for col in ['s/n', 'name', 'class']), "Excel file must contain 's/n', 'name', and 'class' columns."

# Shuffle the entire DataFrame for random selection
df = df.sample(frac=1).reset_index(drop=True)

# Create a list of halls
halls = [[] for _ in range(23)]

# Distribute students across halls
for i, student in enumerate(df.itertuples(index=False)):
    hall_index = i % len(halls)
    halls[hall_index].append(student)

# Create a new DataFrame for the output
output_data = []
for i, hall in enumerate(halls):
    for student in hall:
        output_data.append({
            'Hall': i + 1, 
            's/n': student._0,  # Use _0 for the first column (s/n)
            'name': student.name, 
            'class': student._2 # Use the correct attribute name directly
        })

output_df = pd.DataFrame(output_data)

# Export to a new Excel file
output_df.to_excel('newarranged_halls.xlsx', index=False)

print("Students randomly arranged and exported to 'arranged_halls.xlsx'")
