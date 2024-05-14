import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from './App.jsx'
import './index.css'
import ResiduesForm from './client/Residues_Form.jsx'
import NotFoundPage from './client/NotFoundPage.jsx'
import ResiduesResult from './client/Residues_Result.jsx'
import ProteinChange from './client/Protein_Change_Result.jsx'

export default function Routing() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}/>
          <Route path="/dti-residues" element={<ResiduesForm />} />
          <Route path="/dti-residues-result" element={<ResiduesResult />} />
          <Route path="/protein-change-result" element={<ProteinChange />} />
          <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  );
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Routing />);
