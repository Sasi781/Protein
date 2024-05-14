import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';
import Protein from './Protein.jsx';
import Residues from './Residues.jsx';
import { useLocation } from 'react-router-dom';

function Residues_Result() {
    const { state } = useLocation();
    
    const brandNames = state['brandNames'];
    const sequence = state['sequence'];
    const smiles = state['smiles'];
    const dti_score = state['DTIScore']
    const residue_index = state['ResidueIndex']
    
    // Split the sequence into two parts: before "P" and after "P"

    const seq_arr=[]
    let index = 120;
    const len = sequence.length
    const mod=len%index
    const sep=Math.floor(len/index)
    const bnames=brandNames.slice(0,len-2)
    let f=0
    let s=0
    let index_arr=[]
    for(let i=0; i<sep; i++){
        seq_arr.push(sequence.slice(s, index))
        s=index
        index=index+120
    }
    index=index-120
    seq_arr.push(sequence.slice(index,index+mod))
    
    for(let i=0; i<2; i++){
        let arr=[]
        for(let j=0; j<2; j++){
            arr.push(residue_index[i][j])
        }
        index_arr.push(arr)
    }
    console.log("index: ",index_arr)
    let ind_arr=residue_index.slice(0,2).toString()
    ind_arr
    let c=0
    for(let i=0; i<ind_arr.length; i++){
        if(ind_arr[i]==','){
            c++
        }
        if(c==3){
            ind_arr=ind_arr.substring(0, i) + ' || ' + ind_arr.substring(i + 1);
            break
        }
    }
    // CSS styles for the sequence cell
    const sequenceCellStyle = {
        whiteSpace: 'nowrap', // Prevent line breaks within the cell
    };


    return (
        <div className="container">
            <h1 className="mt-5">Drug Target Prediction with Residues</h1>
            <table className="table table-striped table-bordered mt-3 col-sm-5">
                <thead className="thead-dark">
                    <tr>
                        <th>Attribute</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Smiles</td>
                        <td>{smiles}</td>
                    </tr>
                    <tr>
                        <td>Brand Names</td>
                        <td>{bnames}</td>
                    </tr>
                    <tr>
                        <td>Sequence</td>
                        <td style={sequenceCellStyle}>
                            {seq_arr.map((segment, index) => (
                                <div key={index}>{segment}</div>
                            ))}
                        </td>
                    </tr>
                    <tr>
                        <td>DTI Score</td>
                        <td>{dti_score}</td>
                    </tr>
                    <tr>
                        <td>Binding Indices(CS)</td>
                        <td>{ind_arr}</td>
                    </tr>
                </tbody>
            </table>
            <Protein />
            <Residues />
        </div>
    );
}

export default Residues_Result;
