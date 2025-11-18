import pandas as pd

# Load the dataset
df = pd.read_csv('../../../../Downloads/Titanic.csv')

# Create HTML for original data
html = "<html><head><title>Titanic Data Processing</title></head><body>"
html += "<h1>Original Titanic Dataset (First 10 Rows)</h1>"
html += df.head(10).to_html(index=False)

# Data Cleaning: Handle missing values in Age by imputing with median
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Ensure Age is numeric
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# Data Transformation: Create a new feature 'FamilySize'
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Add to HTML
html += "<h1>After Data Cleaning (Imputed Missing Age with Median: {:.1f})</h1>".format(median_age)
html += df[['PassengerId', 'Name', 'Age']].head(10).to_html(index=False)

html += "<h1>After Data Transformation (Added FamilySize)</h1>"
html += df[['PassengerId', 'Name', 'SibSp', 'Parch', 'FamilySize']].head(10).to_html(index=False)

html += "</body></html>"

# Save to HTML file
with open('titanic_result.html', 'w') as f:
    f.write(html)

print("HTML file created: titanic_result.html")
