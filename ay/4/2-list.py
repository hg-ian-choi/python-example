# List Type

states_of_america = ["Delaware", "Pennsylvania"]

print(states_of_america)  # ['Delaware', 'Pennsylvania']
print(states_of_america[0])  # Delaware
print(states_of_america[1])  # Pennsylvania
print(states_of_america[-1])  # Pennsylvania
print(states_of_america[-2])  # Delaware

states_of_america[1] = "Iowa"
print(states_of_america[1])  # Iowa
print(states_of_america)  # ['Delaware', 'Iowa']

states_of_america.append("Florida")
print(states_of_america)  # ['Delaware', 'Iowa', 'Florida']
print(states_of_america[2])  # Florida

states_of_america.extend(["Arizona", "Alaska"])
# ['Delaware', 'Iowa', 'Florida', 'Arizona', 'Alaska']
print(states_of_america)


# 2-D Array
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
