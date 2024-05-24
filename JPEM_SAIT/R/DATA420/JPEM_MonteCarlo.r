library(tidyverse)

# Basic understanding of a Monte Carlo Simulation: We will look at an example where we simulate throwing darts at a dart board (circle).

# The X-Coordinates of the circle range from -1 to 1 (along the x-axis), while the Y-Coordinates range from -1 to 1 along the y-axis. We will use the runif function to randomly select a set of coordinates along each axis, wrapping this function in a for loop to allow us to run a specified number of simulated "dart throws".

# For each "dart throw" we will check whether the outcome lies within the circle by using the formula:

# X\^2 + y\^2 \<= 1

# Recall that the area of a circle is defined by pi\*radius\^2. In our example the radius is 1 so the area of the circle is pi.

# The area of the square is 2 X 2 or 4

# The ratio of the area of the circle to the area of the square is pi / 4. Depending on the level of precision you desire pi/4 = 3.14159265359 / 4 = 0.785398. This means the circle represents approximately 78.54% of the area of the square.

# As we run our Monte Carlo simulation we will begin with a small number of simulated dart throws - perhaps 1,000, and increase the number of simulations to 100,000 or 10,000,000. As the number of simulations increases, the number of randomly thrown darts hitting the circle (the model accuracy) will gradually approach the ratio of the area of the circle to the area of the square (78.54%)

# ![](images/montecarlo.png)

# Define number of simulations to run, start with 1000. Set the number of darts that randomly hit the circle to zero to begin with. We will use the runif function to randomly generate X and Y coordinates (assuming a uniform or normal distribution). Our for loop will execute until it hits the number of darts thrown that we have specified. With each iteration the for loop will also calculate whether the dart is inside the circle (X^2 + Y^2 \<= 1), if so we will increase the counter by 1. Finally we will calculate the model accuracy by dividing the number of darts in the circle to the number of darts thrown.


# Number of simulations to run
num_darts <- 1000

# Start our counter at zero
num_darts_in_circle <- 0

for (i in 1:num_darts) {
  x <- runif(n = 1, min = -1, max = 1)
  y <- runif(n = 1, min = -1, max = 1)
  if (x^2 + y^2 <= 1) {
    num_darts_in_circle = num_darts_in_circle + 1
  }
}

paste("Loop Model accuracy: ", num_darts_in_circle / num_darts * 100, "%")

# We can achieve a more accurate result by increasing the number of darts thrown - however this will significantly increase run time. We can optimize this. R can be slow when iterating through loops but can be quite fast when working with vector and matrix operations.

# We will remove the for and if loops and replace them with vectors.

# Number of simulations to run
num_darts <- 1000

# Start our counter at zero
num_darts_in_circle <- 0

# Vectors of length num_darts
x <- runif(n = num_darts, min = -1, max = 1)
y <- runif(n = num_darts, min = -1, max = 1)

# Also a vector of length num_darts
sum_squares <- x^2 + y^2
indexes_darts_in_circle <- which(sum_squares <= 1)

num_darts_in_circle2 <- length(indexes_darts_in_circle)

paste("Vector Model accuracy: ", num_darts_in_circle2 / num_darts * 100, "%")

# Depending on your computer performance, model run time can differ significantly (in my case 1,000,000 simulated dart throws took 8 seconds using for and if loops, and less than a second with vector calculation)

# Finally we will visualize the number of simulated darts hitting the circle (and square).


library(tidyverse)
# Create a data frame with the generated points

df <- data.frame(x, y, in_circle = sum_squares <= 1)

# Create a scatter plot of the points, color them based on whether they are inside the circle or not
plot <- ggplot(df, aes(x, y, color = in_circle)) +
  geom_point() +
  theme_minimal()

# Create a data frame for circle points
circle_df <- data.frame(
  x = cos(seq(0, 2 * pi, length.out = 100)),
  y = sin(seq(0, 2 * pi, length.out = 100))
)

# Add a red circle to the plot
plot <- plot +
  geom_point(data = data.frame(x = 0, y = 0), aes(x, y), color = "red", size = 2) +
  geom_path(data = circle_df, aes(x, y), color = "red") +
  labs(title=paste("Model accuracy: ", num_darts_in_circle2 / num_darts * 100, "%"))

# Set the aspect ratio to 1
plot <- plot + coord_fixed(ratio = 1)

# Display the plot
print(plot)
