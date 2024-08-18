# Load necessary libraries
# Install once if needed
# install.packages("tidyverse")
# install.packages("caTools")

library(tidyverse)   # For data manipulation (includes read_csv)
library(caTools)     # For train-test split
library(Metrics)     # For evaluation metrics

# Read the CSV file into a data frame
df <- read_csv("C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/boston.csv")

# Drop the 'TOWN' column
df <- df %>% select(-TOWN)

# Define response variable 'y' and predictor variables 'x'
y <- df$MEDV
x <- df %>% select(-MEDV)

# Fit the linear regression model
regressor <- lm(MEDV ~ ., data = df)

# Print coefficients and intercept
print(coef(regressor))

# Train-test split
set.seed(1234)  # For reproducibility
split <- sample.split(df$MEDV, SplitRatio = 0.7)
train <- subset(df, split == TRUE)
test <- subset(df, split == FALSE)

# Fit the linear regression model on the training data
regressor_train <- lm(MEDV ~ ., data = train)

# Print coefficients and intercept
print(coef(regressor_train))

# Make predictions on the test data
y_pred <- predict(regressor_train, newdata = test)

# Evaluation metrics
mse <- mse(test$MEDV, y_pred)
mae <- mae(test$MEDV, y_pred)
r2 <- summary(regressor_train)$r.squared

# Print evaluation metrics
print(mse)
print(mae)
print(r2)