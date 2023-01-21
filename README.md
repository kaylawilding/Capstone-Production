# Capstone-Production

To run the training file and to re-create the model:

1. Create or update the environment from the environment.yml file:

        conda env create -f environment.yml
    
        conda env update --prefix ./env --file environment.yml  --prune

2. Activate the new environment: 
    
        conda activate myenv

3. Run loandefault 
    
        Mac: python loandefault.py
    
        PC: py loandefault.py
        
Or you can run through docker in the command line using the Docker Instructions.rtf file. You can see the repository on my dockerhub page : https://hub.docker.com/repository/docker/wildingka/loandefault/general

There is an API provided where you can input a dataset of loan applications and predict their default status as output. You can see an example of how to use the API in the run_api notebook/python file (same content in two file types).





