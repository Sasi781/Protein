import requests
import pandas as pd
class fasta:
    def __init__(self,pid):
        url = "https://data.rcsb.org/graphql"
        # Updated form data
        form_data = {
            "operationName": "structure",
            "query": "query structure ($id: String!) {\n  entry(entry_id:$id){\n      polymer_entities {\n          entity_poly {\n            pdbx_seq_one_letter_code_can\n          }\n        }\n  }\n}\n",
            "variables": {"id": ""}
        }
        form_data["variables"]["id"]=pid
        # Sending POST request
        response = requests.post(url, json=form_data)

        # Extracting JSON response
        json_response = response.json()
        # print(json_response)
        self.fasta_sequence=""
        max=-1
        for i in json_response["data"]["entry"]["polymer_entities"]:
            if(len(i["entity_poly"]["pdbx_seq_one_letter_code_can"])>max):
                max=len(i["entity_poly"]["pdbx_seq_one_letter_code_can"])
                self.fasta_sequence=i["entity_poly"]["pdbx_seq_one_letter_code_can"]
        
        url1 = f"https://biosig.lab.uq.edu.au/thermomutdb/api/v1/VariantInformation/pdb/{pid}"
        # url = f"https://www.rcsb.org/fasta/entry/{pdb_id}/display"
        
        csv_file_path = "protein_change_dataset.csv"
        df = pd.read_csv(csv_file_path)
        # Send a GET request to the URL
        response = requests.get(url1)
        vari=[]
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the FASTA sequence from the response content
            data=response.json()
            if(len(data)==0):
                for i in range(len(df["PDB ID"])):
                    if(df["PDB ID"][i]==pid):
                        vari.append(df["Mutation_PDB"][i])
            else:    
                for i in range(len(data)):
                    vari.append(data[i]['mutation_code'])
        fasta=str(self.fasta_sequence)
        # print(vari)
        for i in range(len(vari)):
            s=""
            for j in range(len(vari[i])):
                if(vari[i][j].isdigit()):
                    s=s+vari[i][j]
                if(j!=0 and vari[i][j].isalpha()):
                    index=int(s)-1
                    # print("index ",index)
                    break
            if(index<len(fasta)):
                self.fasta_sequence=fasta[:index]+vari[i][0]+fasta[index+1:]
                fasta=self.fasta_sequence
        
    def __str__(self):
        return self.fasta_sequence
        # Printing JSON response
        