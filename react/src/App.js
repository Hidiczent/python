import React from 'react'
import { ToastContainer } from 'react-toastify';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-loading-skeleton/dist/skeleton.css'
import 'react-toastify/dist/ReactToastify.css';
import Router from './routes/Router';
import { Provider } from 'react-redux';
import stores from './redux/stores'
function App() {
  return (
    <Provider store={stores}>
      <Router />
      <ToastContainer autoClose={1000} theme='colored' />
    </Provider>
  )
}

export default App