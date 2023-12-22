import React from "react";
import 'firebase/compat/auth';
import firebase from 'firebase/compat/app'

export const AuthContext = React.createContext<firebase.User | null>(null);