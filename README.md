# Self-Organizing Maps for Data Purchase Support in Data Marketplaces

Data marketplaces have become popular in recent years, in particular for enterprises who want to enrich their own data with novel data from outside in order to improve their decision-making. A data marketplace is a platform that brings data producers and data consumers together; the platform itself provides the necessary infrastructure. Since producers want to maximize their revenue, while consumers want to minimize their spending, data pricing is among the central problems for a data marketplace. We investigate an approach in which the amount of data purchased is potentially minimized due to an indication of redundancy within the data or similarities between parts of the data. Thus, it is difficult for a buyer to decide whether all or just parts of the data should be paid for. The approach described utilizes Self-Organizing Maps and shows how they can be used to support a purchase decision.

# General Structure

- `componentplanes.ipynb` is the main code file including examples and results.
- `adultdataset_transformation.ipynb` includes data preprocessing steps used to wrangle the original adult dataset extracted from https://raw.githubusercontent.com/jbrownlee/Datasets/master/adult-all.csv. 
- `src` directory includes utility functions and class definitions used in the notebooks.
- `requirements.txt` includes references to required Python packages.
