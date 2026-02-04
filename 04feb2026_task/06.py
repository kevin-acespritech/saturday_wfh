'''6. Store employee data and display row-wise.
        Input:
        {'name':['Rohit','Sneha'],'salary':[50000,60000]}
        Output:
        Rohit 50000
        Sneha 60000'''


data = {'name':['Rohit','Sneha'],'salary':[50000,60000]}
keys = list(data.keys())

for key_index,key in enumerate(data):
    for value_index in range(len(data['name'])):

        print(data[keys[value_index]][key_index], end=" ")

    print()