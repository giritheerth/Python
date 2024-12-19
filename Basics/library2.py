import pandas as pd
import numpy as np
# read the file and print info
df = pd.read_csv('C:\\Users\\theer\\Downloads\\saraniyaa.csv')
print(df.info)


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'rating': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# read json
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)

''' cleaning data:
1. Empty cells
new_df = df.dropna()
new_df = df.dropna(inplace = True)
new_df = df.filena(value=130, inplace= True)
df["Calories"].fillna(130, inplace = True)
2. Data in wrong format
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
3. Wrong data
df.loc[7, 'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
4. Duplicates
print(df.duplicated())
df.drop_duplicates(inplace = True)
'''

# correlation in python
'''
df.corr()
The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
'''

'''
statistical terms:
1. Mean - The average value
2. Median  - The mid point value
3. Mode - The value that appears most frequently
4. standard deviation - A low standard deviation means that most of the numbers are close to the mean (average) value. A high standard deviation means that the numbers are spread out.
5. Variance - The variance is the average number of the squared differences from the Mean.
6. Percentiles - The percentiles can be used to compare where a number is situated compared to other numbers.
7. Normal Data Distribution - In a normal distribution, the graph will be shaped like a bell.
8. scatter plot - A scatter plot is a diagram where each value in the data set is represented by a dot.
9. Histogram - A histogram is a diagram consisting of rectangles whose area is proportional to the frequency of a variable and whose width is equal to the class interval.
10. Regression - Regression is used to investigate the relationship between two or more variables.
11. Outliers - An outlier is a point which falls more than 1.5 times the interquartile range above the third quartile or below the first quartile.
12. Confidence Interval - The Confidence Interval is a range of values we are fairly sure our true value lies in.
13. kurtosis - Kurtosis is a measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution.
14. skewness - Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean.
15. z-score - The Z-Score is the number of standard deviations from the mean a data point is.
16. IQR - The Interquartile Range (IQR) is a measure of statistical dispersion, or how scattered, spread out the values in a data set are.
17. Covariance - Covariance is a measure of how much two random variables vary together.
18. ANOVA - ANOVA (Analysis of Variance) is a statistical method used to test differences between two or more means.
19. p-value - The P-value is the probability that you would have found the current result if the null hypothesis were true.
20. Chi-Squared - The Chi-Squared test is used to determine whether there is a significant association between the two variables.
21. Bayesian - Bayesian statistics is a theory in the field of statistics based on the Bayesian interpretation of probability where probability expresses a degree of belief in an event.
22. A/B Testing - A/B testing is a way to compare two versions of a single variable typically by testing a subject's response to variant A against variant B, and determining which of the two variants is more effective.
23. Time Series - A time series is a series of data points indexed (or listed or graphed) in time order.
24. Survival Analysis - Survival analysis is a branch of statistics for analyzing the expected duration of time until one or more events happen, such as death in biological organisms and failure in mechanical systems.
25. Factor Analysis - Factor analysis is a method used to describe variability among observed, correlated variables in terms of a potentially lower number of unobserved variables called factors.
26. Principal Component Analysis - Principal Component Analysis, or PCA, is a dimensionality-reduction method that is often used to reduce the dimensionality of large data sets, by transforming a large set of variables into a smaller one that still contains most of the information in the large set.
27. Machine Learning - Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.
28. Deep Learning - Deep learning is a subset of machine learning where artificial neural networks, algorithms inspired by the human brain, learn from large amounts of data.
29. Reinforcement Learning - Reinforcement learning is an area of machine learning concerned with how software agents ought to take actions in an environment in order to maximize the notion of cumulative reward.
30. Natural Language Processing - Natural Language Processing (NLP) is a field of artificial intelligence that gives the machines the ability to read, understand and derive meaning from human languages.
31. Computer Vision - Computer vision is an interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos.
32. Supervised Learning - Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs.
'''
