# 19.3.2014
# Päätöspuu

## Käyttäkää tätä esimerkkiä R-kurssityössä

options(digits = 10)

library(caret)
library(ggplot2)

data("iris")
names(iris)
table(iris$Species)
summary(iris)

# Jaetaan data kahteen eri datasettiin: training (sovittamiseen) ja testing (yleistämiseen)
# (Validation: sovittamisen arviointiin)

set.seed(1234)
inTrain = createDataPartition(y = iris$Species, p = 0.7, list = FALSE)
training = iris[inTrain, ]
testing = iris[-inTrain, ]

qplot(Petal.Width, Sepal.Width, colour = Species, data = training)
qplot(Petal.Length, Sepal.Length, colour = Species, data = training)

# Tehdään päätöspuumalli

malli = train(Species ~., method = "rpart", data = training)
print(malli$finalModel)

library(rattle)
fancyRpartPlot(malli$finalModel)

# Tehdään ennustus testing datasetillä
ennuste = predict(malli, newdata = testing)
confusionMatrix(ennuste, testing$Species)
