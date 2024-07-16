import React from 'react'
import Login from './components/Login'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Signup from './components/Signup'

const App = () => {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />}/>
        </Routes>  {/* Wrap your routes in Routes component */}
      </Router>
    </div>
  )
}

export default App
