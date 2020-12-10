# Pandas change string to new dataframe

This piece of code takes a DataFrame field that contains an array of dictionaries which is seen by Pandas as a string, and converts it into multiple entries using the instance_id as a key so that if there are multiple security groups attached to an instance they will appear as columns in a DataFrame individually preceeded with the instance_id
