import React from 'react';

  const Table = ({ cars, handleEdit, handleDelete }) => {
  
  return (
    <div className="contain-table">
      <table className="striped-table">
        <thead>
          <tr>
            <th>License Plate</th>
            <th>Model</th>
            <th>Owner</th>
            <th>Vehicle Mileage</th>
            <th colSpan={2} className="text-center">
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          {cars.length > 0 ? (
            cars.map((car) => (
              <tr key={car.license_plate}>
                <td><a href={"car/"+car.license_plate} >{car.license_plate}</a></td>
                <td>{car.model}</td>
                <td>{car.owner}</td>
                <td>{car.vehicle_mileage}</td>
                <td className="text-right">
                  <button
                    onClick={() => handleEdit(car.license_plate)}
                    className="button muted-button"
                  >
                    Edit
                  </button>
                </td>
                <td className="text-left">
                  <button
                    onClick={() => handleDelete(car.license_plate)}
                    className="button muted-button"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={7}>No Cars</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
