// Import the functions you need from the SDKs you need
import { firebase ,initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB0dKxzN3JOWcZyZBchw_S33jcHo0dcq-0",
  authDomain: "usc-marketplace-11428.firebaseapp.com",
  projectId: "usc-marketplace-11428",
  storageBucket: "usc-marketplace-11428.appspot.com",
  messagingSenderId: "636402163392",
  appId: "1:636402163392:web:6d04eb934babe64c1e9725",
  measurementId: "G-C444758NDF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);
export default app;