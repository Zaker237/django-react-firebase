
import React from "react";
import 'firebase/compat/auth';
import firebase from 'firebase/compat/app';


export const Login: React.FC = () => {
    const signIn = async () => {
        try {
            const provider = new firebase.auth.GoogleAuthProvider();
            firebase.auth().signInWithRedirect(provider);
        } catch (error) {
            console.error(error);
        }
    };
    return (
        <div
            className="flex flex-col w-full h-full items-center justify-end bg-slate-300"
        >
            <button
                className="p-3 bg-orange-300 text-white text-xl"
                onClick={signIn}
            >
                Login With Google
            </button>
        </div>
    );
};