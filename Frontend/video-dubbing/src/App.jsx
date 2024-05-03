import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import MainPage from './components/MainPage';
import VideoUpload from './components/VideoUpload';


function App() {

  return (
   <div>
     <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/main" element={<MainPage />} />
        {/* Use Navigate to redirect to the landing page */}
        <Route path="*" element={<Navigate to="/" />} />
        <Route path="/upload" component={VideoUpload} />
      </Routes>
    </Router>
   </div>
  )
}

export default App
