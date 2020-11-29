import markdown2

tableHTML = markdown2.markdown("|| *Year* || *Temperature (low)* || *Temperature (high)* ||\n|| 1900 || -10 || 25 ||", extras=['wiki-tables'])

print(tableHTML)