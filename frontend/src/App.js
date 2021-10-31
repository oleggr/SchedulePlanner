import React, { useState } from "react";
import './App.css';
import Grid from "./components/grid";

function App() {
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
        <Grid
          grid={grid}
          inputCells={inputCells}
          inputRows={inputRows}
          setCells={setCells}
          setRows={setRows}
        />
    </div>
  );
}

export default App;
