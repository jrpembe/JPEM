import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']

for p in palettes:
    sns.set_palette(p)
    sns.palplot(sns.color_palette())
    plt.show()
    
# there are three main types of color palettes
# circular - non-ordered data
# sequential - consistent range from high to low
# diverging - when you have interesting end members (high and low)

