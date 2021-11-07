import React, {useState} from "react";
import './Auth.css';
import Cookies from 'universal-cookie';

const Auth = () => {
  const cookies = new Cookies();
  const [token_val, setToken] = useState();
  const info_link = "https://t.me/grit4in"

  const saveTokenByEnter = (e) => {
    if (e.key === 'Enter') {
      cookies.set('auth', e.target.value, { path: '/' });
      window.location.reload();
    }
  }

  const saveToken = (e) => {
    cookies.set('auth', e.target.value, { path: '/' });
  }

  const validate = () => {
    window.location.reload();
  }

  return (
    <div className="login">
      <h1>
        <label htmlFor="token">Token </label>
      </h1>
      <div>
        <input
          className="tokenfiled"
          type="text"
          id="token"
          value={token_val}
          onKeyDown={(e) => saveTokenByEnter(e)}
          onChange={(e) => saveToken(e)}
        />
        <button onClick={validate}>Enter</button>
        <a
          className="btn"
          href={info_link}
          target="_blank"
          rel="noreferrer"
          >Info</a>
      </div>
    </div>
  );
};

export default Auth;
