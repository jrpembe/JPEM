data <- cars

plot(data)

hist(data$dist)

# to access the variables within data, we could use attach(cars), then we will have
# access to the variables by simply typing their name, without using $

attach(cars)
hist(dist)


# to view summary statistics about the data
summary(data)

# like "type" in Python, "class" will show you the data type
class(cars)
class(speed)
class(dist)

# length will tell us the number of rows
length(speed) # number of rows
length(cars) # length of the data.frame = # of columns

# return the unique values in a column
unique(speed)

# combine or concatenate values
new_data <- c(1,2,4,5,7,NA)
class(new_data)

# calculating statistics on new_data, how R handles NA values
median(new_data)

# we can call on a parameter of the median function, na.rm = TRUE
median(new_data, na.rm = TRUE)


median(dist)
mean(dist)
# median < mean, skeweed to the right

median(speed)
mean(speed)
# median ~= mean, normal distribution
