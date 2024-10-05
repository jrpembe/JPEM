# Load necessary libraries
library(tidyverse)
library(caret)
library(ggplot2)
library(reshape2)

# Define column names
column_names <- c('CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV')

# Load the data
df <- read.table("C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/housing.csv", col.names = column_names, header = FALSE)

# Split data into predictor and response variables
y <- df$MEDV
x <- df %>% select(-MEDV)

################ Linear Regression ###########################

# Train linear regression model
model <- lm(MEDV ~ ., data = df)
print(coef(model))
print(model$coefficients[1])  # Intercept

################ Train Test Split ###########################

# Split the data into training and testing sets
set.seed(1234)
trainIndex <- createDataPartition(df$MEDV, p = .7, list = FALSE, times = 1)
train <- df[trainIndex, ]
test <- df[-trainIndex, ]

# Train model on training data
model <- lm(MEDV ~ ., data = train)
print(coef(model))
print(model$coefficients[1])  # Intercept

# Make predictions on test data
y_pred <- predict(model, test)

# Evaluate model performance
mse <- mean((test$MEDV - y_pred)^2)
mae <- mean(abs(test$MEDV - y_pred))
r2 <- cor(test$MEDV, y_pred)^2

print(mse)
print(mae)
print(r2)

################ Visualization of data and results ###########################

# Check dimensions of data
print(dim(df))

# Summary statistics of the data
print(summary(df))

# Boxplots for each column
df_melt <- melt(df)
ggplot(df_melt, aes(x = variable, y = value)) + 
  geom_boxplot() + 
  facet_wrap(~ variable, scales = "free") + 
  theme_bw() +
  theme(axis.text.x = element_blank(), axis.ticks.x = element_blank())

# Histograms for each column
ggplot(df_melt, aes(x = value)) + 
  geom_histogram(bins = 30) + 
  facet_wrap(~ variable, scales = "free") + 
  theme_bw()

# Correlation heatmap
cor_matrix <- cor(df)
ggplot(melt(cor_matrix), aes(Var1, Var2, fill = value)) + 
  geom_tile() + 
  geom_text(aes(label = round(value, 2))) + 
  scale_fill_gradient2(midpoint = 0, low = "blue", mid = "white", high = "red") +
  theme_minimal() + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
