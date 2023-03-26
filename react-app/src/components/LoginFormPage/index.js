import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { Redirect } from "react-router-dom";
import './LoginForm.css';

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const history = useHistory();

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      console.log(data)
      setErrors([data[0]]);
    }
  };

  const signUp = (e) => {
    e.preventDefault()
    history.push('/signup')
  }

  const demo = async (e) => {
    e.preventDefault()
    const data = await dispatch(login('demo@aa.io', 'password'))
  }

  return (
    <div className="loginForm">
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <div className="input-form">
          <input
            placeholder="Email"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
            <input
              placeholder="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
        </div>
        <div>
          <button className="loginFormButton" type="submit">Log In</button>
        </div>
        <div>
          <button className="loginFormButton" onClick={demo}>Demo User</button>
        </div>
        <div>
          <button className="loginFormButton" onClick={signUp}>Sign Up</button>
        </div>
      </form>
    </div>
  );
}

export default LoginFormPage;
