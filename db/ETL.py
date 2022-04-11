from sqlalchemy import create_engine
import pandas as pd

"""
Transforms the conversion factor data from the excel sheet and loads it into an sqlite database
"""

df = pd.read_excel('unit_conversion_table.xlsx')
df.columns = ['Unit_input', 'Unit_output', 'Conversion_ratio']
df['Unit_input'] = df['Unit_input'].apply(lambda x: x.lower())
df['Unit_output'] = df['Unit_output'].apply(lambda x: x.lower())

engine = create_engine(r'sqlite:///units_of_measure.db')

df.to_sql('CONVERSION_FACTOR', engine, if_exists='replace', index=False)