import React, { useState } from "react";
import './App.css';
import Grid from "./components/Grid";
import Auth from "./components/Auth";
import {expected_token} from "./Config";

import Cookies from 'universal-cookie';


function App() {
  const cookies = new Cookies();
  let client_token = cookies.get('auth');

  const queryParams = new URLSearchParams(window.location.search);

  let cells_num = queryParams.get('cells');
  cells_num = cells_num ? parseInt(cells_num) : 5;
  cells_num = cells_num < 2 ? 2 : cells_num;

  let rows_num = queryParams.get('rows');
  rows_num = rows_num ? parseInt(rows_num) : 5;
  rows_num = rows_num < 2 ? 2 : rows_num;

  const gridBase = {
    cells: cells_num,
    rows: rows_num
  };

  const [grid, setGrid] = useState(gridBase);
  const [inputCells, setCells] = useState(grid.cells);
  const [inputRows, setRows] = useState(grid.rows);

  return (
    <div className="App">
      {
        expected_token === client_token
          ?
          <Grid
            grid={grid}
            inputCells={inputCells}
            inputRows={inputRows}
            setCells={setCells}
            setRows={setRows}
          />
          :
          <Auth />
      }
    </div>
  );
}

export default App;
