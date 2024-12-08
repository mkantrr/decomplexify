import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { CustomThemeProvider } from '../components/ThemeContext';

import Home from "../pages/Home";
import Create from "../pages/Create";
import Data from "../pages/Data";
import Help from "../pages/Help";
import Documentation from "../pages/Documentation";
import Navbar from "../components/Navbar";
import PageNotFound from "../pages/PageNotFound";

const App = () => {
    return (
      <CustomThemeProvider>
            <Router>
              <Navbar />
              <div style={styles.content}>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path='/home' element={<Home />} />
                    <Route path='/create' element={<Create />} />
                    <Route path='/data' element={<Data />} />
                    <Route path='/docs' element={<Documentation />} />
                    <Route path='/documentation' element={<Documentation />} />
                    <Route path='/help' element={<Help />} />
                    <Route path="/github" Component={() =>{
                        window.location.href = "https://github.com/mkantrr/decomplexify";
                        return null;
                    }} />
                    <Route path="*" element={<PageNotFound />} />
                </Routes>
              </div>
            </Router>
      </CustomThemeProvider>
    );
};

const styles = {
  content: {
      //paddingTop: '50px', // Matches the navbar's height
      padding: '20px', // Adds some general padding for the content
  },
};

export default App;
