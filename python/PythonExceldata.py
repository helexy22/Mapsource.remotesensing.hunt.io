# the excel list from https://docs.google.com/spreadsheets/d/1BTJMMFH9t4p5UmHj5kiC6PGfMN6yaaaZkocx0mDqTK0/edit?usp=drive_web&ouid=111878893823071965889

import pandas
travel_df = pandas.read_excel('./cities.xlsx')
cities = travel_df.to_dict('records')
cities[0] # 显示数组 cities[0] 元素所有属性 
# {'City': 'Solta', 'Country': 'Croatia', 'Population': 1700, 'Area': 59}  这是运行结果


# Here we use a library, which is some code not part of standard Python, to make this process easier
import pandas
# If we use the `import pandas` we have access to the pandas library
travel_df = pandas.read_excel('./cities.xlsx')
# We call the pandas.read_excel method and pass through the string './cities.xlsx' as the file is called cities.xlsx.  By saying './' we are saying
# go to the current folder, lists-lab, and find the 'cities.xlsx' file there
cities = travel_df.to_dict('records')

# code from  git@github.com:learn-co-students/excel-to-python-data-science-intro-000.git
