[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hgNAtOO3)

# Conversation dynamics in podcasts: An analysis of interruptions, calls to action and sentiment across genres

## Abstract
This project aims to analyze conversational dynamics in podcasts using the SPoRC dataset, which provides annotated podcast transcriptions with speaker and dialogue turn information. In the project, we focus on three key elements of conversational dynamics; interruptions, calls to action, and sentiment. These will be the lenses for understanding how podcast conversations differ across genres. By analyzing the existence and nature of interruptions, the use of persuasive and action oriented language toward the listeners, along with the sentiments and emotional tone, we wish to compare and characterize how conversational patterns vary between genres of podcasts. The analysis aims at sheding light on how podcasts communicate and engage audiences differently depending on their genre.

## Contributions
The project contributes a data-driven analytical study of conversational dynamics in podcasts, offering insights into how rhetorical and emotional strategies differ across podcast genres. Specifically:

- A comparative analysis of conversation dynamics across podcast genres, focusing on:
    - Frequency, duration, and type of interruptions (e.g. "agreement", "disagreement", "topic change") to understand power dynamics and conversation structure
    - Identification and characterization of calls to action and persuasive language (e.g. "follow", "spread the word", "buy") to understand patterns of listerner engagement and persuasive intent
    - Sentiments and emotional language use to understand tone and affect

## Use of additional data
The analysis is centered around the SPoRC dataset, however it could still be relevant to use additional sources for data related to the analysis, e.g.:
- Sentiment/emotion lexical ressources to provide assistance in classifying emotions in terms of polarity and intensity
- Call-to-action keyword lexicons, both related to podcats and more general if avaiable to support the identification of such language use

## Methods
The project is centered around three different analytical components:

- Interruption analysis
     - Detection methods to identify interruptions through overlaps and audio features
     - Feature extractionf from detected interruptions to capture duration, speaker turn etc.
     - Unsupervised clustering of detected interruptions to find different types of interruptions
     - Genre level comparison across features, types and aggregate metrics like interruption overlap, frequency etc.
- Call-to-action detection
    - Detection and extraction of CTA based on e.g. lexicons or other ressources (maybe self-crafted) aswell as action-oriented language
    - Analysis of frequence and positional information in the podcast episode timeline
    - Genre level comparison of patterns of use, frequency and intensity of CTA and action-oriented language
- Sentiment analysis
    - Analysis of speaker turns for sentiment polarity and intensity using existing libraries (e.g. RoBERTa-sentiment or others)
    - Aggregation of analysis to episodes and genres
    - Genre level comparison of sentiment patterns

Finally the different part of the analysis will be combined in a correlation analysis to find relationsships between sentiments, interruptions and CTA across genres to answer questions like; "Is emotionally charged language correlated with use of more pursaisive language and more frequent interruptions in conversation?". Beyond these main points of analysis there are also methods used for descriptive statistical analysis of the dataset, relationsship modelling in general and data visualization for the comparisons, which will be decided on a need basis throughout the project. 

## Timeline (from P2 to P3)
- Week 46: Working on the 3 analysis parts
- Week 47: Working on the 3 analysis parts
- Week 48: Working on the 3 analysis parts
- Week 49: Combination of analysis and correlation analysis
- Week 50: Final results synthesis and report writing
- Week 51: Final report writing

## Team organization
We are planning on working close together through multiple weekly meetings where tasks and milestones will be divided. The overall responsibility for the different parts will however be:
- Marcus: Call-to-action detection and analysis + Correlation analysis
- Mikkel: Interruption analysis + Data visualization across the analysis
- Nicoline: Sentiment analysis + Report writing + Project management

## Repo organization
The repo consists of a folder with data (stored locally and not contained in git), and a folder with all helpers stored in seperate .py files for easy management. The root folder containts the main .ipynb, the .gitignore file and the README.md (this file). A final folder notebooks stores all additional .ipynb files used for initial analysis and exploration of data, where code and content is then moved to the main .ipynb if relevant to the final analysis.

## Links and additional ressources for potential use
- https://github.com/blitt2018/SPoRC_analysis/tree/master?tab=readme-ov-file (analysis)
- https://github.com/blitt2018/SPoRC_data (data)
- https://github.com/davidjurgens/sporc/tree/main/docs/wiki (sproc library wiki)
- https://www.kaggle.com/code/josephnehrenz/nlp-sentiment-analysis-of-joe-rogan-experience (similar analysis in R)