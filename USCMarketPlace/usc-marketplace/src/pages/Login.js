//import "./../App.css";
import "./style.css";
import SignupPage from "./Signup"
import { Link } from "react-router-dom";
import { useForm } from 'react-hook-form'
import { AuthContext, useAuthContext } from "../contexts/AuthContext";
import { useContext, useState } from "react";

function LoginPage() {
  const {register, handleSubmit} = useForm()
  const {login, activeUser} = useAuthContext()
  const [status, setStatus] = useState("")
  const onSubmit = async data => {
    console.log(data)
    try {
      await login(data.email, data.password);
      setStatus("Login Success")
    } catch (e) {
      setStatus("Login Failed, try again")
    }
    
  }
  return (
    <>
      <head>
        <script
          src="https://kit.fontawesome.com/fd33c7b4a1.js"
          crossorigin="anonymous"
        ></script>
        <meta charset="utf-8" />
      </head>
      <body>
        <div className="App">
          <div class="login-container">
            <h1>Login</h1>
            <form onSubmit={handleSubmit(onSubmit)}>
              <div class="txt_field">
                <label>Email</label>
                <input {...register("email")} type="text" required />
              </div>
              <div class="txt_field">
                <label>Password</label>
                <input {...register("password")} type="password" required />
              </div>

              <input class="login-button" type="submit" value="Login"></input>
              <div class="signup_link">
                Not a member? 
                <Link to="/signup">
                  <ul id="signup">Signup</ul>
                </Link>
              </div>
            </form>
          </div>
        </div>
      </body>
    </>
  );
}

export default LoginPage;
