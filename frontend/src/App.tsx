import { useContext } from 'react';
import { AuthContext } from "./context/AuthContext";
import { AppHeader } from "./components/AppHeader";
import { Login } from "./pages/Login";
import { HomePage } from "./pages/Homepage";
import './App.css'

function App() {
  const user = useContext(AuthContext);

  return (
    <div>
      <AppHeader />
      {
      user ? 
      <HomePage />
      :
      <Login />
      }
    </div>
  )
}

export default App
