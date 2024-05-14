import requests
import pandas as pd
class drug_smiles:
    def __init__(self,cid):
        url = "https://data.rcsb.org/graphql"
        csv_file_path = "protein_change_dataset.csv"
        df = pd.read_csv(csv_file_path)
        # Updated form data
        form_data = {
            "operationName": "molecule",
            "query": "query molecule ($id: String!) {\n chem_comp(comp_id:$id){\n chem_comp {\n id\n name\n }\n      rcsb_chem_comp_descriptor {\n SMILES\n }\n  drugbank {\n drugbank_info {\ndrugbank_id\n  }\n }\n }\n}\n",
            "variables": {"id": ""}
        }
        form_data["variables"]["id"]=cid
        # Sending POST request
        response = requests.post(url, json=form_data)

        # Extracting JSON response
        json_response = response.json()
        if(json_response["data"]["chem_comp"]!=None):
            self.smiles=json_response["data"]["chem_comp"]["rcsb_chem_comp_descriptor"]["SMILES"]
        else:
            for i in range(len(df["PDB ID"])):
                    if(df["PDB ID"][i]==cid):
                        self.smiles=df["SMILES"][i]
                        break
    def __str__(self):
        return self.smiles
        # Printing JSON response
        