import React, { Children, useContext, useEffect, useState } from "react";
import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from "firebase/auth";
import { auth } from "../firebase"

export const AuthContext = React.createContext()

export function useAuthContext(){
    return useContext(AuthContext);
}

export function AuthProvider({children}) {
    const [activeUser, setActiveUser] = useState();
    
    function signup(email,password){
        console.log("HERE2 " + email + " " + password)
        return createUserWithEmailAndPassword(auth,email,password)
        console.log("HERE3")
    }
    function login(email,password){
        return signInWithEmailAndPassword(auth,email,password)
    }

    useEffect(() =>{
        const unsubscribe = auth.onAuthStateChanged(user => {
            setActiveUser(user)
        })
        return unsubscribe;
    }, [])
    const value = {
        activeUser,
        signup,
        login
    }
    

    return (
            <AuthContext.Provider value={value}>
                {children}
            </AuthContext.Provider>
    );
}