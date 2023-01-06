import "./../App.css";
import ListingBox from "../listing/ListingBox";
import { useState } from "react";
import { Link, useParams } from "react-router-dom";
function HomePage() {
  const { id } = useParams();
  console.log(id + "FUUUUUCK");
  return (
    <div id="homeDiv" className="App container-fluid">
      <h1>HomePage</h1>
      <div class="btn-group">
        <button>Home</button>
        <Link to='/Electronics'>
        <button>Electronics</button>
        </Link>
        <Link to="/Ticket">
        <button>Tickets</button>
        </Link>
        <Link to="/Clothes">
        <button>Clothes</button>
        </Link>
        <Link to="/Furniture">
        <button>Furniture</button>
        </Link>
        <Link to="/Supplies">
        <button>Supplies</button>
        </Link>
        
      </div>
      <div className="row">
        <div>
          { id ?
          <ListingBox url={'http://localhost:8080/api/listing/all'.concat(id ? `/of_category?category=${id}` : "")}/>
          : <ListingBox url={'http://localhost:8080/api/listing/all'.concat(id ? `/of_category?category=${id}` : "")}/>
          }
        </div>
      </div>
    </div>
  );
}

export default HomePage;
