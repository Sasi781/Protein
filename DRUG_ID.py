import requests

class drug_id:
    def __init__(self,pid):
        url = "https://data.rcsb.org/graphql"
        # Updated form data
        form_data ={"operationName": "structure",
        "query": "query structure ($id: String!) {\n  entry(entry_id:$id){\n        nonpolymer_entities {\n          rcsb_nonpolymer_entity_container_identifiers{\n            nonpolymer_comp_id\n          }\n          \n        }\n      \n  }\n}\n",
        "variables":{"id": ""}}
        form_data["variables"]["id"]=pid 
        # Sending POST request
        response = requests.post(url, json=form_data)

        # Extracting JSON response
        json_response = response.json()
        res=json_response["data"]["entry"]["nonpolymer_entities"]
        self.cid=""
        if(res!=None):
            for i in range(0,len(res)):
                if(res[i]["rcsb_nonpolymer_entity_container_identifiers"]["nonpolymer_comp_id"]!="NA"):
                    self.cid=res[i]["rcsb_nonpolymer_entity_container_identifiers"]["nonpolymer_comp_id"]
        else:
            self.cid=pid
    
    def __str__(self):
        return self.cid