# 🎬 Personalized Movie Recommendation System using PySpark & Collaborative Filtering

> 📌 Project 1 of 6 | Pushed as part of my academic + real-world ML portfolio 🚀

## 🧠 Overview
In the ever-growing jungle of streaming content, users often get lost in endless scrolls and mediocre suggestions. Our project dives into solving this problem by building a **personalized movie recommendation system** powered by **collaborative filtering** and **Apache Spark**, capable of processing massive datasets and giving spot-on suggestions based on user behavior.

## 📈 Key Features
- 💡 Personalized suggestions based on **user-item interaction**
- ⚡ Built with **PySpark** on **Apache Spark** for large-scale performance
- 🧪 Evaluated using **RMSE**, **precision**, and **recall**
- 🤝 Scalable, fast, and adaptable to various streaming platforms
- 🔒 Acknowledges **bias and privacy** issues in recommender systems

## 🛠️ Tech Stack
- **Language**: Python
- **Frameworks**: PySpark, Apache Hadoop (HDFS)
- **Tools**: MLlib, Jupyter, VS Code
- **Algorithm**: User-based Collaborative Filtering

## 📂 Dataset
- Contains over **8,000+** user interactions and movie ratings
- Publicly sourced, includes diverse genres, languages, and release years
- Preprocessing steps include handling nulls, normalization, and outlier removal

## 📊 Dataset

This project uses the ([https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset](https://www.kaggle.com/datasets/arzubesiroglu/netflix-titles)) which contains millions of user-movie interactions, ratings, and metadata.

> For quick testing, a sample dataset (`netflix_titles.csv`) is included in the `/data` folder.

To use the full dataset:
1. Sign in to Kaggle
2. Download the dataset from the link above
3. Place it in the root directory or update the path in the code accordingly


## 📊 Results
- Achieved **RMSE = 3.7725** on our baseline implementation
- Compared with benchmark paper achieving **RMSE = 1.0742**
- Insights into how **parameter tuning** (lambda, iterations, rank) affects performance

## 🔍 Research & References
We’ve drawn inspiration and technical strategies from key works including:
- [Deldjoo et al., 2015](#)
- [Shi et al., 2014](#)
- [Ekstrand et al., 2011](#)
- [Ortega et al., 2016](#)

_For the full IEEE-style paper, check the documenation folder in this repo :) 

## 🧠 Authors & Credits
Built with ❤️ by a team of graduate students as part of our coursework under the guidance of our incredible supervisor (see acknowledgments in paper). Shoutout to all contributors and cited researchers!

## 📌 Future Work
- 🧠 Incorporating **hybrid models** (content + collaborative)
- 🔒 Introducing **privacy-preserving mechanisms**
- 🎯 Deploying the system on a cloud platform for live inference

## 📎 License
feel free to fork, star, and remix with credit!

## 📁 Project Structure
'''PySparkFlicks_MovieRecommender/
│
├── code/                     # All PySpark code/scripts
│   ├── preprocessing.py
│   ├── train_model.py
│   └── utils.py
│
├── notebooks/               # Optional: Jupyter Notebooks (.ipynb)
│   └── movie_recommender.ipynb
│
├── data/                    # (optional) Add sample dataset for demo/testing
│   └── sample_ratings.csv
│
├── documentation/           # IEEE paper, diagrams, screenshots
│   ├── project_report.pdf
│   └── architecture.png
│
├── .github/
│   └── workflows/
│       └── python-package.yml
│
├── requirements.txt         # pip dependencies
├── setup.py                 # optional, for making this pip installable
├── README.md                # landing page 📄
└── LICENSE                  # add MIT license or similar if open-source
'''

