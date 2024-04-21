import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

dogs = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/ShelterDogs.csv")

dogs["coat"] = dogs["coat"].astype("category")
dogs["coat"].value_counts(dropna=False)

# dogs.cat.method_name

dogs["coat"] = dogs["coat"].cat.set_categories(new_categories=["short", "medium", "long"])
dogs["coat"].value_counts(dropna=False)

# setting order
dogs["coat"] = dogs["coat"].cat.set_categories(new_categories=["short", "medium", "long"], ordered=True)

dogs["coat"].head(3)

# missing categories
dogs["likes_people"].value_counts(dropna=False)

# adding categories
dogs["likes_people"] = dogs["likes_people"].astype("category")
dogs["likes_people"] = dogs["likes_people"].cat.add_categories(new_categories=["did not check", "could not tell"])
dogs["likes_people"].cat.categories
dogs["likes_people"].value_counts(dropna=False)

# Removing categories
dogs["coat"] = dogs["coat"].astype("category")
dogs["coat"] = dogs["coat"].cat.remove_categories(removals=["wirehaired"])
dogs["coat"].cat.categories

# Updating categories using Series.cat.rename_categories(new_Categories=dict)
dogs["breed"] = dogs["breed"].astype("category")
dogs["breed"].value_counts()

# first create a dictionary
my_changes = {"Unknown Mix": "Unknown"}
dogs["breed"] = dogs["breed"].cat.rename_categories(my_changes)
dogs["breed"].value_counts()

# renaming categories using a lambda function
dogs["sex"] = dogs["sex"].astype("category")
dogs["sex"] = dogs["sex"].cat.rename_categories(lambda c: c.title())
dogs["sex"].cat.categories

# Collapsing categories
dogs["color"] =dogs["color"].astype("category")
print(dogs["color"].cat.categories)

# start by creating a distionary and use .replace
update_colors = {
    "black and brown": "black",
    "black and tan": "black",
    "black and white": "black"
}

dogs["main_color"] = dogs["color"].replace(update_colors)
dogs["main_color"].dtype

# convert back to categorical
dogs["main_color"] =dogs["main_color"].astype("category")
print(dogs["main_color"].cat.categories)

# reordering categories
dogs["coat"] = dogs["coat"].cat.reorder_categories(
    new_categories = ['short', 'medium', 'wirehaired', 'long'],
    ordered=True
    # inplace=True
)

dogs.groupby(['coat'])['age'].mean()

# Cleaning and accessing categorical columns
# use .value_counts() or .cat.categories 
dogs["get_along_cats"] =dogs["get_along_cats"].astype("category")
dogs["get_along_cats"].value_counts()

# fixing whitespace - use str + .strip()
dogs["get_along_cats"] = dogs["get_along_cats"].str.strip()
dogs["get_along_cats"].value_counts()

# fixing capitalization - use str + .upper() or lower() or title()
dogs["get_along_cats"] = dogs["get_along_cats"].str.title()

# fixing typos - use .replace()
replace_map = {"Noo": "No"}

# dogs["get_along_cats"].replace(replace_map, inplace=True)

dogs["get_along_cats"].replace({"Noo": "No"}, inplace=True)
dogs["get_along_cats"].value_counts()

# accessing data with loc and iloc
dogs.loc[dogs["get_along_cats"] == "Yes", "size"]
dogs.loc[dogs["get_along_cats"] == "Yes", "size"].value_counts(sort=True)