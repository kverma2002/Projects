import "./../App.css";
import "./profilestyle.css";
import tshirt from "./../img/tshirt.jpeg";
import bed from "./../img/bed.jpg";
import desk from "./../img/desk.jpg";
import josh from "./../img/josh.jpg";
import lamp from "./../img/lamp.jpg";
import set from "./../img/set.jpg";
import shoe from "./../img/shoe.jpg";
import shopping from "./../img/shopping.jpg";
import usc from "./../img/usc.jpg";
import React, {useState, useEffect} from 'react';
import {useAuthContext} from "../contexts/AuthContext"
import ListingBox from "../listing/ListingBox";
import {
  useParams
} from "react-router-dom";
import { Link } from "react-router-dom";

function ProfilePage(props) {
  //const x = activeUser.email;
  let { id } = useParams();
  useEffect(() => {
    fetchItem();
  }, []);
  const { activeUser } = useAuthContext(); 
  const [item, setItem] = useState({});
  const fetchItem = async () => {
    
    const data = await fetch(
      'http://localhost:8080/api/user/get/by_id?userId='.concat(id)
    );

    const itemx = await data.json();
    console.log("hey" + itemx);
    setItem(itemx);
  };
  return (
    
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Profile Page</title>

        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
        />

        <link rel="stylesheet" href="css/profilestyle.css" />
      </head>
      <body>
        <div class="header__wrapper">
          <header></header>
          <div class="cols__container">
            <div class="left__col">
              <div class="img__container">
                <img src={item &&item.profile_pic_url} alt="Josh Williams" />
              </div>
              <h2>{item && item.name}</h2>
              <p>Welcome to my profile!</p>
              <p>{item && item.email_address}</p>

              <div class="content">
                <p>
                  {item && item.bio}
                </p>
              </div>
              <div class="content">
                <p>
                  {item && item.email_address && activeUser && activeUser.email == item.email_address && 
                    <Link to={`/createlisting`}><p style={{"textDecoration":"none", "color":"yellow"}}>Add a Listing</p></Link>
                  }
                </p>
              </div>
            </div>
            <div class="right__col">
              {/* <div class="photos">
                <img src={tshirt} alt="" />
                <img src={desk} alt="Photo" />
                <img src={lamp} alt="Photo" />
                <img src={set} alt="Photo" />
                <img src={usc} alt="Photo" />
                <img src={shoe} alt="Photo" />
              </div> */}
              {item.user_id && <>
              <ListingBox url={`http://localhost:8080/api/listing/all/from_owner?ownerId=${item.user_id}`}/>
              </>}
            </div>
          </div>
        </div>
      </body>
    </html>
  );
}

export default ProfilePage;
