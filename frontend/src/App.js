import React, { useState } from "react";
import './App.css';
import Grid from "./components/grid";

function App() {
  const queryParams = new URLSearchParams(window.location.search);
  
  var cells_num = queryParams.get('cells');
  cells_num = cells_num ? parseInt(cells_num) : 5;
  var rows_num = queryParams.get('rows');
  rows_num = rows_num ? parseInt(rows_num) : 5;

  const gridBase = {
    cells: cells_num,
    rows: rows_num
  };

  const [grid, setGrid] = useState(gridBase);
  const [inputCells, setCells] = useState(grid.cells);
  const [inputRows, setRows] = useState(grid.rows);

  const handleGridSize = () => {
    // TODO: fix grid resize
    const res = {
      cells: parseInt(inputCells),
      rows: parseInt(inputRows)
    };
  };

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
