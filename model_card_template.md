# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model leverages scikit-learn's RandomForestClassifier machine learning algorithm, and is trained to predict whether or not, based on various demographic features, an individual's income is:
- Less than or equal to $50k/year
- Greater than $50k/year

## Intended Use

This model is intended to classify individuals by predicted income (that is, does this individual make less than or equal to $50k/year, or do they make greater than $50k/year?) based on various demographic features, and may be used in various industries, including marketing and financial services.

## Training Data

This model is trained on data publicly available from the US Census database. The dataset used contains demographic information from the 1994 Census such as age, education, marital-status, race, sex, etc. and can be found at <a href="https://archive.ics.uci.edu/dataset/20/census+income">the UC Irvine Machine Learning Repository</a>.

## Evaluation Data

To test this model's performance, the original dataset was split at random and without stratified sampling, and **25%** of the original dataset was set aside for testing purposes.

## Metrics

Following are the model's performance metrics with respect to:

- Precision: **0.7406**
- Recall: **0.6310**
- F1: **0.6814**

## Ethical Considerations

As the dataset contains historical demographic information gathered by the 1994 US Census, it is important to be aware of the potential for biases present in the methods used to gather this information.  As such, the inherent biases present in the dataset used to train this model may lead to predictions which themselves contain biases.

## Caveats and Recommendations

As this model was trained on a dataset containing information from 1994, it may be advantageous to consider gathering similar Census data, but for more recent years, to better align with present-day trends in income and demographics.