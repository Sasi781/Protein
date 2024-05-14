import { useNavigate } from 'react-router-dom';
import Button from 'react-bootstrap/esm/Button';
import Card from 'react-bootstrap/esm/Card';

function BasicExample() {
  const navigate = useNavigate();

  function DTIprediction() {
    // console.log("HII")
    navigate("/dti-residues");
  }

  function ProteinChange() {
    // console.log("HII")
    navigate("/protein-change-result");
  }

  return (
    <div className='container'>
      <div className='row'>
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>DTI-Prediction</Card.Title>
            <Button variant="primary" onClick={DTIprediction}>Predict DTI</Button>
          </Card.Body>
        </Card>
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>Protein Change Prediction</Card.Title>
            <Button variant="primary" onClick={ProteinChange}>Protein Change</Button>
          </Card.Body>
        </Card>
        {/* <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>Drug-Drug Interaction</Card.Title>
            <Card.Text>
              Content about Drug Drug Interaction
            </Card.Text>
            <Button variant="primary">DDI</Button>
          </Card.Body>
        </Card> */}
      </div>
    </div>
  );
}

export default BasicExample;
