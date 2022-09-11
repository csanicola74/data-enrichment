import pandas as pd

########################
# load in the data
########################
sparcs = pd.read_csv('data/SPARCS.csv')
sparcs

neighborhood_atlas = pd.read_csv('data/the_Neighborhood_Atlas.csv')
neighborhood_atlas

sparcs.columns
neighborhood_atlas.columns

########################
# cleaning up columns
########################
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')  # regex
list(sparcs)
# seeing what the column types are
sparcs.dtypes
neighborhood_atlas.dtypes

# storing first 3 letters of name as username
neighborhood_atlas['Zip_3'] = neighborhood_atlas['ZIPID'].str.slice(1, 4)
neighborhood_atlas

sparcs['Zip_Code_3_digits']
neighborhood_atlas['Zip_3']


########################
# add the neighborhood atlas data to the sparcs data
########################
neighborhood_atlas_small = neighborhood_atlas[[
    'Zip_3',
    'ADI_NATRANK',
    'ADI_STATERNK']]
sparcs_small = sparcs[[
    'Zip_Code_3_digits',
    'Health_Service_Area',
    'Hospital_County',
    'Facility_Name',
    'Age_Group',
    'Gender',
    'Race',
    'Ethnicity',
    'Length_of_Stay',
    'Type_of_Admission',
    'Patient_Disposition',
    'Discharge_Year',
    'CCS_Diagnosis_Code',
    'CCS_Procedure_Code',
    'Total_Charges',
    'Total_Costs']]

print(neighborhood_atlas_small.sample(10).to_markdown())
neighborhood_atlas_small.shape

print(sparcs_small.sample(10).to_markdown())
sparcs_small.shape

combined_sparcs = neighborhood_atlas_small.merge(
    sparcs_small, how='left', left_on='Zip_3', right_on='Zip_Code_3_digits')
combined_sparcs = pd.merge(neighborhood_atlas_small, sparcs_small,
                           how='left', left_on='Zip_3', right_on='Zip_Code_3_digits')

combined_sparcs.columns

########################
# save file to new .csv
########################
combined_sparcs.to_csv('data/combined_sparcs.csv')
combined_sparcs.shape
