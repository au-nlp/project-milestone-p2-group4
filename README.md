[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hgNAtOO3)

# Understanding conversation dynamics - NLP analysis of sentiment, language and interruptions in podcasts

## Abstract
This project aims to analyze conversational dynamics in podcasts using the SPoRC dataset, which provides annotated podcast transcriptions with speaker and dialogue turn information. In the project, we focus on three key elements of conversational dynamics; interruptions, calls to action, and sentiment. These will be the lenses for understanding how podcast conversations differ across genres. By analyzing the existence and nature of interruptions, the use of persuasive and action oriented language toward the listeners, along with the sentiment and tone, we wish to compare and characterize how conversational patterns vary between genres of podcasts. The analysis aims at sheding light on how podcasts communicate and engage audiences differently depending on their genre.

## Contributions
The project contributes a data-driven analytical study of conversational dynamics in podcasts, offering insights into how rhetorical and emotional strategies differ across podcast genres. Specifically:

- A comparative analysis of conversation dynamics across podcast genres, focusing on:
    - Frequency and type of interruptions to understand power dynamics and conversation structure across genres
    - Identification and characterization of calls to action and persuasive language (e.g. "follow", "spread the word", "buy") to understand patterns of listerner engagement and persuasive intent
    - Sentiments to understand tone and affect across genres and temporal dimensions

## Use of additional data
The analysis is centered around the SPoRC dataset, and is supported by logical flagging and lexicon based approaches to some degree featuring additional data built in to these methods. 

## Methods
The project is centered around three different analytical components:

- Interruption analysis
     - Detection pipeline to identify interruptions through overlaps in terms of time and speaker labels
     - Unsupervised clustering of detected interruptions to find different types of interruptions
     - Genre level comparison across features, types and aggregate metrics like interruption overlap, frequency etc.
     - Graph modelling of found interruptions to discover relationsships
- Call-to-action detection
    - Detection and extraction of CTA based on e.g. logical flagging and LLM judgements
    - Analysis of frequence and positional information in the podcast episode timeline
    - Genre level comparison of patterns of use, frequency and intensity of CTA and action-oriented language
- Sentiment analysis
    - Analysis of speaker turns (at sentence level) for sentiment polarity and intensity using lexicon based (VADER) and transformers based (DistilBERT) approaches
    - Aggregation of analysis to turns, episodes and genres
    - Genre level comparison of sentiment patterns and distribution
    - Analysis of temporal dimension of sentiment across episodes and genres
    - Robustness check: Negation flip test and sample sanity checks for low- and high confidence
    - Inter-method agreement and confusion matrix to understand similarities and differences

Finally the different part of the analysis will be combined in a correlation analysis to find potential relationsships between sentiments, interruptions and CTA across genres to answer questions like; "Is emotionally charged language correlated with use of more pursaisive language and more frequent interruptions in conversation?". We also look into interesting patterns of e.g. sentiment changing just before and after a CTA or interruption to understand impact.


## Team organization and individual contributions
- Marcus: Data handling + data preprocessing pipeline + CTA analysis
- Mikkel: Interruption analysis + correlation analysis 
- Nicoline: Sentiment analysis + data visualizations + final report write up (combining parts, writing abstract, conclusion etc.)

Each group member has written the parts of the report related to their area of analysis, and we have had weekly meetings going over each analysis and the combined analysis and conclusions, so everyone has been involved at high level in all parts of the final work.

## Repo organization
The repo consists of a folder with data (some is stored locally and not contained in git due to the size), and a folder with all helpers stored in seperate .py files for easy management. Furthermore, there are folders for saved figures and the final report. The root folder containts the main .ipynb, the .gitignore file and the README.md (this file). 