import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import RegisterPage from './RegsiterPage'
import LoginPage from './LoginPage'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <RegisterPage></RegisterPage>
      <LoginPage></LoginPage>
    </>
  )
}

export default App
