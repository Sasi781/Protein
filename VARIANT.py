import requests
import pandas as pd
class mutation:
    def __init__(self,pdb_id):
    # Define the URL for retrieving the FASTA sequence
        url = f"https://biosig.lab.uq.edu.au/thermomutdb/api/v1/VariantInformation/pdb/{pdb_id}"
        # url = f"https://www.rcsb.org/fasta/entry/{pdb_id}/display"
        
        csv_file_path = "protein_change_dataset.csv"
        df = pd.read_csv(csv_file_path)
        # Send a GET request to the URL
        response = requests.get(url)
        vari=[]
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the FASTA sequence from the response content
            data=response.json()
            if(len(data)==0):
                for i in range(len(df["PDB ID"])):
                    if(df["PDB ID"][i]==pdb_id):
                        vari.append(df["Mutation_PDB"][i])
            else:    
                for i in range(len(data)):
                    vari.append(data[i]['mutation_code'])
            self.v=vari
        else:
            print(f"Failed to retrieve FASTA sequence for PDB ID {pdb_id}. Status code: {response.status_code}")

    def Result(self):
        return self.v
