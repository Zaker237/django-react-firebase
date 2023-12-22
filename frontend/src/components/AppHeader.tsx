
import React, {useContext } from "react";
import 'firebase/compat/auth';
import { AuthContext } from "../context/AuthContext";
import { auth } from "../firebase";


export const AppHeader: React.FC = () => {
	const user = useContext(AuthContext);

	const signOut = async () => {
		await auth.signOut();
	};

	return (
		<div
			className="flex flex-row-reverse w-full min-h-[50px] bg-slate-600"
		>
			{
				user &&
				<button
					className="bg-red-700 text-white"
					onClick={signOut}
				>
					Logout
				</button>
			}
		</div>
	);
};