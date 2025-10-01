# Twitter Sentiment Analysis - NLP Pipeline

A complete end-to-end NLP project for sentiment analysis on Twitter data, from preprocessing to deployment.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)


## Overview

This project implements a complete NLP pipeline for Twitter sentiment classification:
- **Preprocessing**: Regex cleaning, tokenization, lemmatization
- **Feature Engineering**: TF-IDF, Bag of Words, Word2Vec
- **Modeling**: Multiple classifiers with sklearn pipelines
- **Deployment**: REST API with Flask

**Final Model**: Logistic Regression + TF-IDF achieving **78.1% accuracy**

## Dataset

- **Source**: [Sentiment140](http://help.sentiment140.com/for-students/)
- **Size**: 20,000 tweets (sampled from 1.6M)
- **Classes**: Binary (Positive, Negative)
- **Distribution**: Balanced dataset

## Features

-  Complete text preprocessing pipeline
-  Multiple text representation methods (BoW, TF-IDF, Word2Vec)
-  Comparison of 6 different models
-  Comprehensive evaluation with confusion matrix
-  Error analysis with misclassified examples
-  REST API for predictions
-  Saved model pipeline for deployment
