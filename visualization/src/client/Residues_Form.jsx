import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';
import axios from 'axios';
import { Link, Navigate, useNavigate } from 'react-router-dom';

function Residues_Form() {
    const navigate = useNavigate()
    const [drugID, setDrugID] = useState("1983");
    const [proteinID, setProteinID] = useState("P00375");

    function handleChange(e) {
        setDrugID(e.target.value);
    }

    function handleChange2(e) {
        setProteinID(e.target.value);
    }

    function handleSubmit(e){
        e.preventDefault();
      
        // Update the URL with the port number
        const url = `http://localhost:5000/api/process`;
      
        axios.post(url, { drugId: drugID, proteinId: proteinID })
          .then(response => {
            console.log("--DrugID & ProteinID");
            console.log(response.data)
            
            navigate("/dti-residues-result",{state :response.data})
    
        })
          .catch(error => {
            console.error('Error:', error);
          });
    }
      
    return (
        <div className="container">
        <h1 className="mt-5">Enter Drug and UniProt ID</h1>
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="drugId">Drug ID:</label>
                <input type="text" value={drugID} className="form-control" id="drugId" placeholder="Enter Drug ID" onChange={handleChange}/>
            </div>
            
            <div className="form-group">
                <label htmlFor="uniprotId">UniProt ID:</label>
                <input type="text" value={proteinID} className="form-control" id="uniprotId" placeholder="Enter UniProt ID" onChange={handleChange2} />
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
        </form>
    </div>
    );
}

export default Residues_Form;
