import "./../App.css";
import HomePage from "./Home";
import { Link } from "react-router-dom";
import {useAuthContext} from "../contexts/AuthContext"

function Nav() {
  const { activeUser } = useAuthContext()
  return (
    <nav>
      <Link to="/">
        <h3>USC MarketPlace</h3>
      </Link>
      <ul className="nav-links">
        <Link to="/">
          <li>Home</li>
        </Link>
        <li><a href="http://localhost:9080/Auction/AuctionPage.html" style={{"textDecoration":"none", "color":"white"}}>Auction</a></li>
        <Link to="/login">
          <li>Login</li>
        </Link>
        {activeUser ? 
        <Link to={`/profile/${activeUser.uid}`}>
          <li>{activeUser.email}</li>
        </Link> 
        :
          <li>Not signed In</li>
        }
        <Link to="/details">
          <li>Details</li>
        </Link>
      </ul>
    </nav>
  );
}

export default Nav;
