
import React, { useEffect, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import 'firebase/compat/auth';
import firebase from 'firebase/compat/app'
import { auth } from "../firebase";

interface AuthProviderProps {
    children: React.ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }: AuthProviderProps) => {
    const [user, setUser] = useState<firebase.User | null>(null);


    useEffect(() => {
        const unsubscribe = auth.onAuthStateChanged((firebaseUser) => {
            setUser(firebaseUser);
        });
        3

        return unsubscribe;
    }, []);

    return <AuthContext.Provider value={user}>{children}</AuthContext.Provider>;
};