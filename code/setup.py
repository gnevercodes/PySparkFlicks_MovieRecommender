from setuptools import setup, find_packages

setup(
    name='movie_recommender',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyspark',
        'pandas',
        'numpy',
        # add more dependencies here accordingly to your wish...
    ],
)
