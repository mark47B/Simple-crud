import React, { useState } from 'react';
import Swal from 'sweetalert2';

const Edit = ({ cars, selectedCar, setCars, setIsEditing }) => {
  const id = selectedCar.license_plate;

  const [license_plate, setLicense_plate] = useState(selectedCar.license_plate);
  const [model, setModel] = useState(selectedCar.model);
  const [owner, setOwner] = useState(selectedCar.owner);
  const [vehicle_mileage, setVehicle_mileage] = useState(selectedCar.vehicle_mileage);

  const handleUpdate = e => {
    e.preventDefault();

    if (!license_plate || !model || !owner || !vehicle_mileage) {
      return Swal.fire({
        icon: 'error',
        title: 'Error!',
        text: 'All fields are required.',
        showConfirmButton: true,
      });
    }

    const car = {
      license_plate,
      model,
      owner,
      vehicle_mileage,
    };

    for (let i = 0; i < cars.length; i++) {
      if (cars[i].license_plate === id) {
        cars.splice(i, 1, car);
        break;
      }
    }

    const requestOptions = {
      method: "PUT",
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
      console.log("Error in HandleUpdate");
    }else{
      Swal.fire({
        icon: 'success',
        title: 'Updated!',
        text: `Car with licens plate: ${car.license_plate} has been updated.`,
        showConfirmButton: false,
        timer: 1500,
      });
    }

    setCars(cars);
    setIsEditing(true);
  };

  return (
    <div className="small-container">
      <form onSubmit={handleUpdate}>
        <h1>Edit Car</h1>
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
          type="text"
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
          <input type="submit" value="Update" onClick={() => setIsEditing(true)} />
          <input
            style={{ marginLeft: '12px' }}
            className="muted-button"
            type="button"
            value="Cancel"
            onClick={() => setIsEditing(false)}
          />
        </div>
      </form>
    </div>
  );
};

export default Edit;
