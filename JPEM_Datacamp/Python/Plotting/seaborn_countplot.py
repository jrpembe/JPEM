import seaborn as sns
import matplotlib.pyplot as plt

height = [62, 64, 69, 75, 66, 68, 65, 71, 76, 73]
weight = [120, 136, 148, 175, 137, 165, 154, 172, 200, 187]
gender = ["female", "female", "female", "female", "male", "male", "male", "male", "male", "male"]


# sns.scatterplot(x=height, y=weight)

# plt.title = "Height vs Weight"
# plt.xlabel = "Height (in)"
# plt.ylabel = "Weight (lbs)"

sns.countplot(x=gender, hue=gender)

# plt.show()

# trying different seaborn themes

for style in ['white', 'dark', 'whitegrid', 'darkgrid', 'ticks']:
    sns.set_style(style)
    sns.countplot(x=gender, hue=gender)
    plt.show()