# Datatlas: Data Atlas

Basic functionality for data science & engineering


## Installation & Updates

Run the following to install:
```bash
pip install datatlas
```

Run one of the following to update:
```bash
pip install datatlas --upgrade

pip install datatlas -U
```


## Usage

```python
# Import the library
import datatlas as dat

# Print 'Hello Atlas!' to test if the package installation and import were successful
dat.say_hello('Atlas') 

# Generate an output df with detailed stats about the input df including warnings for data quality issues that might need to be addressed before model training
df_profile = dat.df_profiling(df) 

'''
df_profiling(df, nulls_threshold=50.0, zeroes_threshold=50.0, cardinality_threshold=50.0)
    Input(s):
        1) df: Dataframe to analyse
        2) nulls_threshold (int): Default is 50. Adds warning if >50% nulls detected
        3) zeroes_threshold (int): Default 50. Adds warning if >50% zeroes detected for numerical dtype columns
        4) cardinality_threshold (int): Default 50. Adds warning if >50% unique values for categorical dtype columns
    Output(s):
        1) Dataframe with statistics and data quality warnings about the input df
'''

# Predict the missing values in a particular column using machine learning algorithms - as an alternative to replacing missing values with the column's mean/max/etc
imputed_df, impute_model, impute_stats = dat.predict_missing_values(df, impute_column='target_column', datatype='numeric', impute_model=True, impute_stats=True, console_messages=True)

'''
predict_missing_values(df, impute_column, datatype, impute_model=True, impute_stats=True, console_messages=True)
    Input(s):
        1) df: Dataframe of all columns including the column with missing values
        2) impute_column (string): Name of the column containing missing values that you want to predict and impute using machine learning
        3) datatype (string): Choose one of the following - numeric, categoric
        4) impute_model (boolean): Default True. See outputs docstring below for more info
        4) stats (boolean): Default True. See outputs docstring below for more info
        5) console_messages (boolean): Default True. Outputs status messages in the console to indicate progress of the model training and predictions
    Output(s):
        1) Dataframe where the nulls in the column to impute are replaced with their predicted values
        2) impute_model (Sklearn estimator object) (optional): The trained model that was used to predict the missing values that can be later used to predict missing values of new live data
        3) impute_stats (dictionary) (optional): A dictionary containing stats about the impute column before and after the predictions. Also includes rmse (for numeric) or accuracy (for categoric) model performance evaluation metrics
'''
```

## Versions
Please see the release_notes.txt file

## Contributing
[section under construction]


