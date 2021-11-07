import React, {useState} from "react";

import Cookies from 'universal-cookie';

const Auth = () => {
  const cookies = new Cookies();
  const [token_val, setToken] = useState();

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
    <div>
      <label htmlFor="token">Token </label>
      <div>
        <input
          type="text"
          id="token"
          value={token_val}
          onKeyDown={(e) => saveTokenByEnter(e)}
          onChange={(e) => saveToken(e)}
        />
        <button onClick={validate}>Enter</button>
      </div>
    </div>
  );
};

export default Auth;
