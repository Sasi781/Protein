from FASTA import fasta
from VARIANT import mutation
from DRUG_ID import drug_id
from DRUG_SMILES import drug_smiles
import numpy as np

class Prediction:
    def predict(self,feature,pdb_id):
        self.pdb_id=pdb_id
        variations=mutation(pdb_id)
        var_list=variations.Result()
        pred_result=[]
        for i in range(0,len(var_list)):
            print(i)
            f=self.featureize_mutation_chain(var_list[i])
            pred_result.append(f)
        return pred_result
    
    def featureize_mutation_chain(self,mutation_chain):
    # Convert amino acid symbols to one-hot encoding
        amino_acids = str(fasta(self.pdb_id))
        aa_to_index = {aa: i for i, aa in enumerate(amino_acids)}
        num=""
        for i in range(len(mutation_chain)):
            if(mutation_chain[i].isdigit()):
                num=num+mutation_chain[i]
            if(i!=0 and mutation_chain[i].isalpha()):
                break
    
        mutation_position = int(num)  # Extract the position (e.g., 73)
            
        mutated_aa = mutation_chain[-1] 
        # Featureize mutation position
        position_feature = np.zeros(len(amino_acids))
        position_feature[mutation_position - 1] = 1  # Set the position to 1 in the one-hot encoding
        # print(position_feature)
        # Featureize mutated amino acid
        mutated_aa_feature = np.zeros(len(amino_acids))
        mutated_aa_index = aa_to_index.get(mutated_aa, -1)
        if mutated_aa_index != -1:
            mutated_aa_feature[mutated_aa_index] = 1  # Set the mutated amino acid to 1 in the one-hot encoding

        # print(mutated_aa_feature)
        # Combine features
        features = np.concatenate([position_feature, mutated_aa_feature])

        return features


