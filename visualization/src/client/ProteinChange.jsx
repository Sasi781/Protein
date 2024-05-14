import '../App.css'

import React, { useState, useEffect } from 'react';
import * as NGL from 'ngl';
function Protein() {
  useEffect(() => {
    var stage2 = new NGL.Stage('viewport2',{ backgroundColor: 'white' });

            // Load structure using the structure ID
            stage2.loadFile("src/assets/mt_1a7v.pdb")
                .then(component => {
                  component.addRepresentation('cartoon')
                  component.addRepresentation('ball+stick',{ sele: '73' });
                  stage2.autoView();
                });
  }, []);


  return (
    <div>
      <h1>Protein Change Visualization</h1>
      <div id="viewport2" style={{ width: '1170px', height: '500px' }}></div>
    </div>
  );
}

export default Protein;