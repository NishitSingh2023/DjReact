import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { BrowserRouter as Router } from 'react-router-dom';
import CustomLayout from './containers/Layout';
import BaseRouter from './routes';

class App extends Component{
  render(){
    return ( //earlier it was articlelist instead of BaseRouter
      <div className="App">
        <Router>
          <CustomLayout>
            <BaseRouter/> 
          </CustomLayout>
        </Router>
      </div>
    );
  }
}

export default App;
