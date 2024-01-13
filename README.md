# 🌸 The ANIMEndation System

This project explores different methods of building a recommendation engine for animes, from feature-based recommendations to collaborative filtering. The analysis can be accessed [here](analysis/the-animendation-system.ipynb).

**Author**: Po-Hsun (Ben) Chen

## Summary

In this project, I constructed a comprehensive recommendation system for animes by combining feature-based and collaborative filtering approaches. Leveraging user preferences and anime attributes, the feature-based model facilitated personalized suggestions, while collaborative filtering enhanced recommendations based on similar users' viewing habits. The integration of these techniques provided a robust and diversified anime recommendation engine, catering to individual tastes and fostering an enriched user experience within the anime community.

## Data Source

The dataset used in this analysis contains data from 320,0000 users and more than 16,000 animes at myanimelist.net. The dataset includes metadata about animes, viewer ratings, and anime synopsis. The dataset used in this analysis is sourced from Kaggle. You can access the dataset [here](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020).

## Dependencies

All required dependencies are listed in this [conda environment file](environment.yaml).

## How to Reproduce the Analysis

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/phchen5/the-animendation-system.git
   cd the-animendation-system
   ```

2. **Download the Dataset from the Source:**
   You may need to register for a Kaggle account. After you've downloaded the dataset, place the `anime.csv`, `rating_complete.csv` and `anime_with_synopsis` files within a `data/` folder located in the root. You may also place it anywhere else in the repository as you like, just be sure to edit the data source path within the analysis.
3. **Set Up and Activate Environment:**

   ```bash
   conda env create -f environment.yaml
   conda activate animendation-system
   ```

4. **Open the Notebook:**

   ```bash
   jupyter lab analysis/the-animendation-system.ipynb
   ```

5. **Run the Cells and Have Fun Exploring!**

## Files

- `analysis/the-animendation-system.ipynb`: Jupyter notebook containing the EDA code.
- `environment.yaml`: Conda environment file listing required dependencies.
