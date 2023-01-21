# Capstone-Production

To run: 

1. Create or update the environment from the environment.yml file:

        conda env create -f environment.yml
    
        conda env update --prefix ./env --file environment.yml  --prune

2. Activate the new environment: 
    
        conda activate myenv

3. Run loandefault 
    
        Mac: python loandefault.py
    
        PC: py loandefault.py


Or you can run through docker in the command line using the Docker Instructions.rtf file. 

You can see how to use the API where you could input new data and get loan default predictions using the run_api notebook or python file (same content in two file types)

