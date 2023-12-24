
import React, { useContext } from "react";
import 'firebase/compat/auth';
import { AuthContext } from "../context/AuthContext";
import firebase from 'firebase/compat/app'
import axios from "axios";
// import { auth } from "../firebase/firebase";


export const HomePage: React.FC = () => {
	const user = useContext(AuthContext);

	const getData = async () => {
		firebase.auth().onAuthStateChanged(async (user) => {
			const token = await user?.getIdToken();
			const response = await axios.get(
				"http://127.0.0.1:8000/api/todolists",
				{
					headers: {
						"Authorization": `Bearer ${token}`,
						"Content-Type": "application/json"
					}
				}
			);
			console.log(response.data)
		})
	}
	return (
		<div
			className="flex flex-col w-full h-full items-center justify-end bg-slate-300"
		>
			<p className="p-3 text-white text-xl">
				Welcome {user ? user.displayName : ""}
			</p>
			<button className="bg-green-600 text-white p-2" onClick={getData}>
				Get Data from backend
			</button>
		</div>
	);
};