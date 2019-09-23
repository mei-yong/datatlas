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

# Generate an output df with detailed stats about the input df including warnings for data quality issues that might need to be addressed for model training
df_profile = dat.df_profiling(df) 

'''
df_profiling(df, nulls_threshold=50.0, zeroes_threshold=50.0, cardinality_threshold=50.0)
    Input(s):
        1) df - dataframe to analyse
        2) nulls_threshold - int - default 50. Adds warning if >50% nulls
        3) zeroes_threshold - int - default 50. Adds warning if >50% zeroes for numerical dtype columns
        4) cardinality_threshold - int - default 50. Adds warning if >50% nulls for categorical dtype columns
    Output(s):
        1) Dataframe with statistics and data quality warnings about the input df
'''


```

## Versions
Please see the release_notes.txt file

## Contributing
[section under construction]


