import '../App.css'

import React, { useState, useEffect } from 'react';
import * as NGL from 'ngl';
function Residues() {
        useEffect(() => {
            var stage1 = new NGL.Stage('viewport1',{ backgroundColor: 'white' });
        stage1.loadFile("src/assets/1a7v.pdb")
            .then(component => {
                component.addRepresentation('cartoon', { color: 'red' });
                component.addRepresentation('cartoon', { sele: '10-13 or 50-53', color: 'green' });
                stage1.autoView();
            });
  }, []);


  return (
    <div>
      <h1 className="mt-5">Binding Site Residues</h1>
      <div id="viewport1" style={{ width: '1170px', height: '500px' }}></div>
    </div>
  );
}

export default Residues;