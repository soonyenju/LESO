"""
Free software for processing and reading LESO data.
Author: Songyan Zhu, University of Exeter (Now at University of Edinburgh)
Contact: szhu4@ed.ac.uk
Publication: https://ieeexplore.ieee.org/document/9800930
Citation: 
S. Zhu et al., "Learning Surface Ozone From Satellite Columns (LESO): A Regional Daily Estimation Framework for Surface Ozone Monitoring in China," in IEEE Transactions on Geoscience and Remote Sensing, vol. 60, pp. 1-11, 2022, Art no. 4108711, doi: 10.1109/TGRS.2022.3184629.
"""

# Install necessary libraries
pip install numpy==1.20.3
pip install pandas==1.3.3
pip install deep-forest
pip install scigeo==0.0.13
pip install sciml==00.5
pip install xarray==0.19.0
pip install scitbx
pip install matplotlib

# load libraries
from scitbx.easy_import import *
from scitbx.stutils import *

def load_leso_data(p):
    '''
    p: the full path of a LESO nc file
    '''
    nc = xr.load_dataset(p)
    return nc

# project directory
root_proj = '<LESO DATASET LOCATION>'
root_proj = Path(root_proj)
paths = root_proj.glob('*.nc') # Example of data naming: SUR-O3-2012-01-01-DF21-01.nc
# Create file index as a pandas dataframe
df_path = pd.DataFrame([[pd.to_datetime(p.stem, format = 'SUR-O3-%Y-%m-%d-DF21-01'), p] for p in paths], columns = ['DATE', 'PATH']).set_index('DATE', drop = True).sort_index()
# Select the path of file of interest, e.g.:
p = df_path.iloc[0, 0]
# Read data:
data = load_leso_data(p)
'''
Start your specified processing chain, the data is loaded in a xarray format, it can be converted to numpy array by data[<YOUR VAR>].data
Please contact me for any questions, all queries about following bespole data process are welcome, thank you.
'''