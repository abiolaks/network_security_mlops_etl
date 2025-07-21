# network_security_mlops_etl
# Mlops project and ETL pipeline


## Network Security Projects for Phising Data
### Step 1
### Create Proeject repo on git, with readme and gitignore
*clone to local machine
### setup project structure following the structure below:
* data_folder - to store the data
* .github/workflows/main.yml - for github actions for deployment
* src - this folder contain other sub folder like components, pipeline, utils, constants, entity, cloud, logging, exception, notebooks.
* in the subfolders in the src, create __init__.py in each subfolders. making the folder a package
* create files Dockerfile, .env, setup.py

## step 2:
* create the setup script in setup.py
* setup the logging in logging/logger.py and exception 

## step 3
* create an etl pipeline: that will take the data transform it and save as json object in mongodb
* First setup mongodb for the etl pipeline







