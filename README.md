# Capstone-Production

Create the environment from the environment.yml file:

conda env create -f environment.yml

The first line of the yml file sets the new environment's name. For details see Creating an environment file manually.

Activate the new environment: conda activate myenv

Verify that the new environment was installed correctly:

conda env list
You can also use conda info --envs

For updating the enviroment use 
conda env update --prefix ./env --file environment.yml  --prune