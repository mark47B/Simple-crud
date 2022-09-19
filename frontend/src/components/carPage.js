import {Link, useParams} from "react-router-dom";
import React, {useState, useEffect} from 'react';

  const OneCar = () => {
    const [car, setCar] = useState({});
    let { id } = useParams();

    const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      };

      useEffect(() => {
        async function getData() {
            const response = await fetch("/api/car/"+id, requestOptions)
            let data = await response.json();
            setCar(data)
          }
          getData()
       }, []);
  return (<>
  <div className="container">
    <h1>Car card</h1>
    <table className="contain-table">
        <thead>
          <tr>
            <th>License Plate</th>
            <th>Model</th>
            <th>Owner</th>
            <th>Vehicle Mileage</th>
          </tr>
        </thead>
        <tbody>
              <tr key={car.license_plate}>
                <td>{car.license_plate}</td>
                <td>{car.model}</td>
                <td>{car.owner}</td>
                <td>{car.vehicle_mileage}</td>
              </tr>
        </tbody>
      </table>
      <Link to="/">
      <button >Home</button>
      </Link>
      </div>
    </>
  );
};

export default OneCar;
