
import './../App.css';
import './CreateListing.css';
import { Link } from "react-router-dom";
import { useForm } from 'react-hook-form'
import { AuthContext, useAuthContext } from "../contexts/AuthContext";
import { useContext, useState } from "react";
function CreateListingPage() {
    const {register, handleSubmit} = useForm()
    const {login, activeUser} = useAuthContext()
    const [status, setStatus] = useState("")
    const onSubmit = async event => {
        event.preventDefault;
        let payload = {
            "id": Math.floor(Math.random() * 1000) + 1,
            "title": event.iName,
            "price": parseFloat(event.price),
            "description": event.description,
            "category": event.category,
            "imageUrl": event.url,
            "owner_id": activeUser.uid,
        }
        try {
          const requestData = {
            method: 'POST',
            headers:{
               'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
          };
    
          const response = await fetch('http://localhost:8080/api/listing/create', requestData);
          const data = await response.json();
    
          // do something with the data returned from the server as 
          // a result of POSt request
          setStatus("Listing Created");
          // redirect
         } catch (error) {
            console.log(error);
         }
    }
  return (
    <div id="main">
            <form onSubmit={handleSubmit(onSubmit)} name="newListing">
                <div id="form">
                    <div class="inputs"><p>Item Name: </p><input type="text" {...register("iName")} placeholder="Ex. Used backetball" required/></div>
                    <div class="inputs"><p>Selling Price ($): </p><input type="text" {...register("price")} placeholder="Ex. 20.99" required/></div>
                    <div class="inputs"><p>Category :</p><input type="text" {...register("category")} placeholder="Ex. Electronics" required/></div>
                    <div class="inputs"><p>Item Description: </p><textarea {...register("description")} rows="3" maxlenghth="200" placeholder="Ex. Nike Adult Indoor Basketball" required></textarea></div>
                    <div class="inputs"><p>Image URL: </p><input type="text" {...register("url")} placeholder="Ex. Paste the link to your image" required/></div>    
                    <div class="inputs">
                        <input type="submit" name="submit" value="Post" id="submit"/>
                        <input type="reset" name="reset" value="Clear" id="reset"/>
                    </div>
                    <p>{status}</p>
                </div>
            </form>
        </div>
  );
}

export default CreateListingPage;
