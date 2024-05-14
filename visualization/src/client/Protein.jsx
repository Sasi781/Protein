import '../App.css'

import React, { useState, useEffect } from 'react';
import * as NGL from 'ngl';
function Protein() {
  useEffect(() => {
    var stage = new NGL.Stage('viewport',{ backgroundColor: 'white' });

            // Load structure using the structure ID
            stage.loadFile("src/assets/1a7v.pdb")
                .then(component => {
                  component.addRepresentation('cartoon')
                  stage.autoView();
                });
  }, []);


  return (
    <div>
      <h1 className="mt-5">Protein Visualization</h1>
      <div id="viewport" style={{ width: '1170px', height: '500px' }}></div>
    </div>
  );
}

export default Protein;