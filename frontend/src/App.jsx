import React from 'react';
import { 
  BrowserRouter as Router,
  Routes,
  Route} from 'react-router-dom'
import Dashboard from './components/Table';
import OneCar from './components/carPage'

const App = () => {
  return (
    <>
    <Router>
      <Routes>
        <Route path={'/'} element={<Dashboard />} exact />
        <Route path={'/car/:id'} element={<OneCar />} exact />
      </Routes>
    </Router>
    </>
  );
};


export default App;
