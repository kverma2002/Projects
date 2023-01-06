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

function MiniProfilePage(props) {
  //const x = activeUser.email;
  let item = props.item;
  return (
    <>
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
      <div class="cols__container">
              <div class="img__container">
                <img src={item.profile_pic_url}/>
              </div>
              <h2>{item.name}</h2>
              <p>{item.email_address}</p>
              {item.user_id &&
              <Link to={`/profile/${item.user_id}`}>
                <p>Visit my profile</p>
              </Link>}
        </div>
    </>
  );
}

export default MiniProfilePage;
