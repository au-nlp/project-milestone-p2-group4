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
- Marcus: Data handeling & overview + CTA analysis + Correlation analysis
- Mikkel: Interruption analysis + Data visualization across the analysis
- Nicoline: Sentiment analysis + Report writing + Project management

## Repo organization
The repo consists of a folder with data (stored locally and not contained in git), and a folder with all helpers stored in seperate .py files for easy management. The root folder containts the main .ipynb, the .gitignore file and the README.md (this file). A final folder notebooks stores all additional .ipynb files used for initial analysis and exploration of data, where code and content is then moved to the main .ipynb if relevant to the final analysis.

## Links and additional ressources for potential use
- https://github.com/blitt2018/SPoRC_analysis/tree/master?tab=readme-ov-file (analysis)
- https://github.com/blitt2018/SPoRC_data (data)
- https://github.com/davidjurgens/sporc/tree/main/docs/wiki (sproc library wiki)
- https://www.kaggle.com/code/josephnehrenz/nlp-sentiment-analysis-of-joe-rogan-experience (similar analysis in R)


## Interne noter til møde 4/12
Vi skal have lavet et fælles sample at køre koden på af min 1000 episoder, hvor der er balance mellem genrer og filtreret episoder uden genrer, tekst osv. fra, så de 1000 rent faktisk er 1000 brugbare. Pt. i sentiment laver jeg random sample på 100, men det giver kun 11 episoder efter oprydning, så den skal laves inden --> skal blive til en ny fil måske eller bare ligge i koden som variabel? Overvejelse. 

Tilret koden med inspection af data og statistics til det nye slice efter preprocessing (se længere nede).

Der skal ryddes op i koden - fjerne, ændre og tilføje kommentarer så alt giver mening, og ikke ser chat agtigt ud. Der skal laves overskrifter og forklaringer til de forskellige komponentet når det rykkes til main. 

Der skal laves en fælles pre-processing pipeline på sætninger, da jeg i min kode ser at f.eks. "'s a", "part." og andre skøre ting får lov at være sin egen sætning uden at det er sigende. Tænker samme problemstilling kunne afhjælpe nogle af problemerne i interruptions og CTA + at vi arbejder mere standardiseret med teksterne. 

Vi skal have lavet hypoteser + kode til correlation analysis mellem de forksellige analyser for at se sammenhænge, og det kræver nok et overblik over hvad vi egentlig har og hvordan tingene kan sammenstilles. Samle tabeller med resultater pr. sætning, episode eller genre til at lave tingene. Kræver standardisering af hvordan vi arbejder videre på sentences_df og lignende, så de namt kan joines igen. Obs på at kontrollere for ubalance i episodelængder, antal sætninger i episode. Lave nogle fede komparative plots af tingene. 

Vi skal have udvalgt og forfinet de relevante plots, så de kan bruges direkte i raportern - de skal se ens ud for alle elementerne, så vi skal standardisere brug af pakker, farver, sprog, navne osv. 

Alt koden skal køres igennem på en god computer når ovenstående rettelser er lavet, så vi får de endelige resultater klar. 

Vi skal have klare definitioner klar på de ting vi arbejder med. Hvad betyder sentiment (binær vs. labels)? Hvad er CTA (A call-to-action is an utterance that explicitly invites the listener to take an action (subscribe, donate, buy, visit, follow, rate, share…).”) - inkl. scope?

Begynde at skrive rapport:
- Introduction + research questions
- Dataset (SPoRC), sampling strategy, preprocessing
- Methods (3 sections: interruptions, CTA, sentiment) incl. Evaluation (each method: short, clear)
- Results (3 sections + combined correlation)
- Discussion (limitations, confounds, future work)
- Conclusion


Plan:
1. Fælles datagrundlag --> rydde op i episoderne så alle har genre + alle har turns (måske mere end 2) + evt. andet --> lav et random sample stratried på genrer på min. 1000 i alt
2. Fælles pre-processing pipeline --> split i turns + rengør (fjern sætninger af 1 ord eller kun tegn eller lignende) --> turn_df inkl. info om episode + genre osv. til regression
3. Fælles deskreptiv statistik afsnit tilrettes og genkøres
4. Indsætte CTA kode i main --> tilrettes turn_df datastruktur enten ved at køre pr. turn eller ved at køre pr. sætning og aggregere + proxy evaluering af udvalgte samples + inter-method agreement kohens kappa
5. Indæstte sentiment kode i main --> tilrettes til at køre pr. turn til turn_df
6. Indsætte interruptions kode i main --> tilret til turn_df + undersøg andre måder til detektion
7. Plots --> fælles ramme for hvordan de ser ud + helpers til dem hver især + udvælg for hvert område hvad der er relevant for konklusioner + overveje fælles plots på tværs (histogram, density, tidsserier)
8. Ud fra plots og intuition skal der defineres nogle hypoteser til korrelation analyse
9. Lave korrelation analyse og resultater herfra
10. Lave mini fælles-analyse om ændring i sentiment umiddelbart før og efter CTA eller interruption som support
11. Rydde op i kode --> fjerne chat kommentarer der ser chat agtige ud, følge samme kode standard (evt. pep8) + flyt evt. ting til helpers som ikke er essentielt
12. Skrive rapport

N = skriv rapport groft, lav fælles plot kode inkl. parameterstyring af visuelle ting, fikse egen kode og sætte i main

Mi = fikse egen kode, lave mini-analyse og korrelations analyse kode opstart klar til resultater

Ma = fikse egen kode, lave fælles data pipeline 

Hypoteser:
- Sammenhæng mellem negativ sentiment og afbrydelser
- Sammenhæng mellem positiv sentiment og cta
- Sammenhæng mellem genrer og sentiment/afbrydelser/cta + evt. specifikke
- Flest cta i slutningen af episode, sammenhæng mellem cta og episode progress 0-1


## Noter til møde 11/12

Måske kigge på turn.is_overlapping (turn involves multiple speakers) til interruption pipeline. 

I main skal vi da loade ALLE pakker i starten, eller loader vi nye pakker til hver analyse-del?

Hvor maget text vil vi have med i main. Har skrevet meget til CTA som jeg tænkte kunne bruges i vore rapport, men det behøver ikke nødvendigvis være med.

Jeg har inkluderet alt kode, måske skal jeg fjerne nogle funktioner? Jeg tærker dog gerne de vil se logikken?
