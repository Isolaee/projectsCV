# Päätöspuu tehtävä
# 16.4.2024

# Käyttäkää tätä esimerkkiä R-kurssityössä.

options(digits = 10)

library(caret)
library(ggplot2)

# Luetaan data
data = read.csv("peli_data.csv")
summary(data)

# Poistetaan pelaajat joilla 0 ostoa
data = data[data$laskuri_ostot != 0,]

# Lisätään "kategorisointi" sarake
data$Profile = ifelse(data$avg_hinta > 5.0, "Tuhlari", "Penninvenyttaja")

# Tehdään "puhdas data" kentillä jolla voidaan kuvitella olevan väliä.
cleanData = data[c("alustaTyyppi", "laskuri_ostot", "Profile")]

# Jaetaan data kahteen eri datasettiin: training (sovittamiseen) ja testing (yleistämiseen)
# (validation: sovittamisen arviointiin)

set.seed(123)
inTrain <- createDataPartition(y = cleanData$Profile, p = 0.7, list = FALSE)
training <- cleanData[inTrain, ]
testing  <- cleanData[-inTrain, ]

# Dimensions check
dim(testing)
dim(training)

# Tehdään päätöspuumalli

malli <- train(Profile ~., method = "rpart", data = training)
print(malli$finalModel)

library(rattle)
fancyRpartPlot(malli$finalModel)

# Tehdään ennustus testing datasetillä
ennuste = predict(malli, newdata = testing)
confusionMatrix(ennuste, testing$Profile)

