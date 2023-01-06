//import "./../App.css";
import "./style.css";
import { useForm } from 'react-hook-form'
import { AuthContext, useAuthContext } from "../contexts/AuthContext";
import { useContext, useState } from "react";
function SignupPage() {
  const { register, handleSubmit} = useForm();
  const {signup, activeUser} = useAuthContext();
  const [status, setStatus] = useState("")
  const onSubmit = async data => {
    //save activeruser id here as temp
    //const previd = activeUser.uid;
    try {
      console.log("HERE")
      await signup(data.email, data.password);
      console.log("DID IT?")
      setStatus("Signed in successfully! Try logging in!")
    } catch (e) {
      console.log(e);
      setStatus("Sign In Failed! try again")
    }
    let payload = {
      "bio": data.bio,
      "email_address": data.email,
      "profile_pic_url": data.url,
      "name": data.name,
      "user_id": activeUser.uid
    }
    //while activeUser is equal to temp do nothing
    // while(activeUser.uid == previd){
    //   console.log("waiting");
    // }
  try {
    const requestData = {
      method: 'POST',
      headers:{
         'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    };

    const response = await fetch('http://localhost:8080/api/user/create', requestData);
    const data = await response.json();

    // do something with the data returned from the server as 
    // a result of POSt request
    // redirect
   } catch (error) {
      console.log(error);
   }
  }

  return (
    <div>
      <head>
        <script
          src="https://kit.fontawesome.com/fd33c7b4a1.js"
          crossorigin="anonymous"
        ></script>
        <meta charset="utf-8" />
      </head>
      <body>
        <div class="login-container">
            <h1>Sign Up</h1>
            <form onSubmit={handleSubmit(onSubmit)}>
                <div class="blank">
                    <div><input type="text" {...register("name")} placeholder="First Name" required></input></div>
                    <div><input type="email" {...register("email")} pattern=".+@usc\.edu" placeholder="Enter @usc.edu email" required></input></div>
                    <div><input type="password" {...register("password")} placeholder="Enter password" required></input></div>
                    <div><textarea rows="3" cols="30" {...register("bio")} placeholder="Write a bio!"></textarea></div>
                    <div><input type="text" {...register("url")} placeholder="Profile Pic URL" required></input></div>
                    <div><input class="buttons" type="submit" {...register("submit")}></input></div>
                    <div><input class="buttons" type="reset" {...register("reset")}></input></div>
                    <label>{status}</label>
                </div>
            </form>
        </div>
      </body>
    </div>
  );
}

export default SignupPage;
