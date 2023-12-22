
import React, {useContext} from "react";
import 'firebase/compat/auth';
import { AuthContext } from "../context/AuthContext";
import firebase from 'firebase/compat/app'
// import { auth } from "../firebase/firebase";


export const HomePage: React.FC = () => {
    const user = useContext(AuthContext);

	const getData = () => {
		firebase.auth().onAuthStateChanged(async (user) => {
			const token = await user?.getIdToken();
			fetch("http://127.0.0.1:8000/api/todolists?format=json", {
				headers: {
					"Authotization": `Bearer ${token}`
				}
			}
			)
			.then((response) => response.json())
			.then((data) => {
				console.log(data);
			})
		})
	}
	return (
		<div
			className="flex flex-col w-full h-full items-center justify-end bg-slate-300"
		>
            <p className="p-3 text-white text-xl">
                Welcome { user ? user.displayName: ""}
            </p>
			<button className="bg-green-600 text-white p-2" onClick={getData}> 
				Get Data from backend
			</button>
		</div>
	);
};