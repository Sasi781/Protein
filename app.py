from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS from flask_cors
from visualization.Retrivel.FASTA import *
import os

from BR.model.hots import *
from BR.Feature_Extraction.build_features import *


app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

PORT = 5000
CLIENT_BUILD_DIR = os.path.join(os.path.dirname(__file__), 'client', 'build')

@app.route('/api/process', methods=['POST'])
def process_endpoint():
    if request.is_json:
        # define input feature
        prot_vec = "Sequence"
        drug_vec = "Morgan"
        drug_len = 2048
        radius = 2
        protein_encoder = ProteinEncoder(prot_vec)
        compound_encoder = CompoundEncoder(drug_vec, radius=radius, n_bits=drug_len)

        data = request.get_json()
        drug_id = data.get('drugId')
        protein_id = data.get('proteinId')

        smiles = get_smiles_from_cid(int(drug_id))
        sequence = get_seq_from_uniprot_acc(protein_id)
        brand_names = get_synonyms(drug_id)
        s = ""
        for i in brand_names:
            s += i + ", "

        # Prediction Process
        br_model = HoTS()
        # load model
        br_model.load_model("./Model/Model_config.json")
        # Encode Process
        drugs_fp = [compound_encoder.encode(smiles)]
        targets_encoded = [protein_encoder.encode(sequence)]

        protein_encoder = ProteinEncoder(prot_vec)
        target_encoded = protein_encoder.pad(targets_encoded)

        br_predictions = br_model.HoTS_prediction(drugs_fp, target_encoded)
        dti_score=str(br_predictions[0][0][0])
        residue_index=br_predictions[1][0]
        print("dti_score ",dti_score)
        return jsonify({'brandNames': s, 'smiles': smiles, 'sequence': sequence,'DTIScore':dti_score,'ResidueIndex':residue_index}), 200
    else:
        # Return an error response if the request does not contain JSON data
        return jsonify({'error': 'Request must be JSON'}), 415

@app.route('/residues-result')
def residues_result():
    return send_from_directory(CLIENT_BUILD_DIR, 'index.html')

# Serve the static files (JS, CSS, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(CLIENT_BUILD_DIR, 'static'), filename)

if __name__ == '__main__':
    # Run the app on the defined port
    app.run(port=PORT)
