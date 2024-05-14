import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';
import Protein from './Protein.jsx';
import ProteinChange from './ProteinChange.jsx';

function Protein_Change_Result() {

    return (
        <div class="container">
        <h1 class="mt-5">Protein Sequence Change</h1>
        <table class="table table-striped table-bordered mt-3">
            <thead class="thead-dark">
                <tr>
                    <th>###</th>
                    <th>###</th>
                </tr>
            </thead>
            <tbody>
                <tr class="table-primary">
                    <td>Smiles</td>
                    <td>COC1=CC2=C(C=C1)N(C3CCN(CC3)C(=O)C4=C2NC5=CC=CC=C54)C</td>
                </tr>
                <tr class="table-success">
                    <td>Sequence</td>
                    <td>MAGPGVWTVKLLKGNHTHVAGDVGALVNAFKHVFLIEYSYPSLSDREHTAVSKYYPHYLGKGSYSGQGSTVTVSS</td>
                </tr>
                <tr class="table-danger">
                    <td>Protein Sequence Change</td>
                    <td>MAHPGVWTVKLLKGNHTHVAGDVGALVNAFKHVFLIEYSYPSLSDREHTAVSKYYPHYLGKGSYSGQGSTVTVSS</td>
                </tr>
            </tbody>
        </table>
        <Protein/>
        <ProteinChange/>
    </div>
    );
}

export default Protein_Change_Result;
