
import React, {useContext} from "react";
import 'firebase/compat/auth';
import { AuthContext } from "../context/AuthContext";
//import firebase from 'firebase/compat/app'
// import { auth } from "../firebase/firebase";


export const HomePage: React.FC = () => {
    const user = useContext(AuthContext);
	return (
		<div
			className="flex flex-col w-full h-full items-center justify-end bg-slate-300"
		>
            <p className="p-3 text-white text-xl">
                Welcome { user ? user.displayName: ""}
            </p>
		</div>
	);
};