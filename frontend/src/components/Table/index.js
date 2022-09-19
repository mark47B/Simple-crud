import React, { useState, useEffect } from 'react';
import Swal from 'sweetalert2';


import Header from './Header';
import Table from './Table';
import Add from './Add';
import Edit from './Edit';

const Dashboard = () => {
  const [Cars, setCars] = useState({});
  const [selectedCar, setSelectedCar] = useState(null);
  const [isAdding, setIsAdding] = useState(false);
  const [isEditing, setIsEditing] = useState(false);

  const getCars = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("api/car", requestOptions);
    if(!response.ok){
      console.log('ERROR: ' + response.data);
    }else{
      const data = response.json();

      data.then(function(value){setCars(value.items);})
      return data
    }
  };
  useEffect(() => {
    getCars();
  }, []);


  const handleEdit = (id) => {
    const [Car] = Cars.filter(Car => Car.license_plate === id);

    setSelectedCar(Car);
    setIsEditing(true);
  };

  const handleDelete = (id) => {
    Swal.fire({
      icon: 'warning',
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      showCancelButton: true,
      confirmButtonText: 'Yes, delete it!',
      cancelButtonText: 'No, cancel!',
    }).then(result => {
      if (result.value) {

        const requestOptions = {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          }, 
        };
        const response = fetch(`api/car/${id}`, requestOptions);
        if (!response.ok){
          console.log("Error in HandleDelete");
        }else{
          const [Car] = Cars.filter(Car => Car.id === id);

        Swal.fire({
          icon: 'success',
          title: 'Deleted!',
          text: `Car with License plate: ${Car.license_plate} been deleted.`,
          showConfirmButton: false,
          timer: 1500,
        });
        }

        const CarsCopy = Cars.filter(Car => Car.license_plate !== id);
        setCars(CarsCopy);
      }
    });
  };

  return (
    <div className="container">
      {!isAdding && !isEditing && (
        <>
          <Header
            setIsAdding={setIsAdding}
          />
          
          <Table
            cars={Cars}
            handleEdit={handleEdit}
            handleDelete={handleDelete}
          />
        </>
      )}
      {isAdding && (
        <Add
          Cars={Cars}
          setCars={setCars}
          setIsAdding={setIsAdding}
        />
      )}
      {isEditing && (
        <Edit
          cars={Cars}
          selectedCar={selectedCar}
          setCars={setCars}
          setIsEditing={setIsEditing}
        />
      )}
    </div>
  );
};

export default Dashboard;
