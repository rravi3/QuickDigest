import React,{useState} from 'react';
import httpClient from "../httpClient";
import {websiteUrl} from '../index.js'
import validator from 'validator';

const Register =()=>{
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")

    const handleSubmit = event => {
        event.preventDefault();
        
        if (validator.isEmail(email)) {
            registerUser();
        } else {
            alert("Please, enter valid Email!");
        }
      };

    const registerUser = async ()=>{
        await httpClient.post(websiteUrl + "/register",{
            email,
            password
        })
        .then(res=>{
            console.log("Logged in");
            window.location.href="/"
        })
        .catch(err=>{
            alert("Invalid credentials")
        })
    }
    return (
       <div class="page">
            <div class="form">
                <h1>NoteNugget</h1>
                <h1 style={{color:'white'}}>Register</h1>
                <form id="signup-form">
                    <input type="text" placeholder="email" value={email} onChange={(e)=>setEmail(e.target.value)}/>
                    <input type="password" placeholder="password" value={password} onChange={(e)=>setPassword(e.target.value)}/>
                    <button type="submit" onClick={handleSubmit}>Register</button>
                    <a href="/">
                                <p>Login</p>
                    </a>
                </form>
            </div>
        </div>
    )
}

export default Register