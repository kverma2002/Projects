import logo from "./logo.svg";
import "./App.css";
import HomePage from "./pages/Home";
import Nav from "./pages/Nav";
import LoginPage from "./pages/Login";
import ProfilePage from "./pages/Profile";
import SignupPage from "./pages/Signup";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider, useAuthContext } from "./contexts/AuthContext";

import DetailsPage from "./pages/Details";
import CreateListingPage from "./pages/CreateListing";

function App() {
  const { activeUser } = useAuthContext()
  return (
      <Router>
        <div className="App">
          <Nav />
          <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route path="/:id" element={<HomePage />} />
            <Route path="/createlisting" element={<CreateListingPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/profile/:id" element={<ProfilePage />} />
            <Route path="/signup" element={<SignupPage />} />
            <Route path="/details/:id" element={<DetailsPage />} />
          </Routes>
        </div>
      </Router>

  );
}

export default App;
