import React, { useState } from 'react';
import Swal from 'sweetalert2';

const Add = ({ Cars, setCars, setIsAdding }) => {
  const [license_plate, setLicense_plate] = useState('');
  const [model, setModel] = useState('');
  const [owner, setOwner] = useState(0);
  const [vehicle_mileage, setVehicle_mileage] = useState(0);

  const cleanFormData = () => {
    setLicense_plate("");
    setModel("");
    setOwner("");
    setVehicle_mileage(""); 
  };
  const handleAdd = e => {
    e.preventDefault();

    if (!license_plate || !model || !owner || !vehicle_mileage ) {
      return Swal.fire({
        icon: 'error',
        title: 'Error!',
        text: 'All fields are required.',
        showConfirmButton: true,
      });
    }

    const newCar = {
      license_plate,
      model,
      owner,
      vehicle_mileage,
    };

    

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        license_plate: license_plate, 
        model: model, 
        owner: Number(owner), 
        vehicle_mileage: Number(vehicle_mileage)}),
    };

    const response = fetch("/api/car", requestOptions);
    if (!response.ok){
      console.log("Error in HandleAdd!!!");
    }else{
      Cars.push(newCar);
      cleanFormData();
      Swal.fire({
        icon: 'success',
        title: 'Added!',
        text: `${license_plate} ${model}'s data has been Added.`,
        showConfirmButton: false,
        timer: 1500,
      });
    }

    setCars(Cars);
    setIsAdding(false);

    
  };

  return (
    <div className="small-container">
      <form onSubmit={handleAdd}>
        <h1>Add Car</h1>
        <label htmlFor="license_plate">License Plate</label>
        <input
          id="license_plate"
          type="text"
          name="license_plate"
          value={license_plate}
          onChange={e => setLicense_plate(e.target.value)}
        />
        <label htmlFor="model">Model</label>
        <input
          id="model"
          type="text"
          name="model"
          value={model}
          onChange={e => setModel(e.target.value)}
        />
        <label htmlFor="owner">Owner</label>
        <input
          id="owner"
          type="number"
          name="owner"
          value={owner}
          onChange={e => setOwner(e.target.value)}
        />
        <label htmlFor="vehicle_mileage">Vehicle Mileage</label>
        <input
          id="vehicle_mileage"
          type="number"
          name="vehicle_mileage"
          value={vehicle_mileage}
          onChange={e => setVehicle_mileage(e.target.value)}
        />
        <div style={{ marginTop: '30px' }}>
          <input type="submit" value="Add" onClick={() => setIsAdding(true)}/>
          <input
            style={{ marginLeft: '12px' }}
            className="muted-button"
            type="button"
            value="Cancel"
            onClick={() => setIsAdding(false)}
          />
        </div>
      </form>
    </div>
  );
};

export default Add;
