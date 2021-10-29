import React, { useEffect, useState } from "react";
import './App.css';
import Grid from "./components/grid";

function App() {
  const gridBase = {
    cells: 5,
    rows: 5
  };

  const [grid, setGrid] = useState(gridBase);
  const [inputCells, setCells] = useState(grid.cells);
  const [inputRows, setRows] = useState(grid.rows);

  const handleGridSize = () => {
    const res = {
      cells: parseInt(inputCells),
      rows: parseInt(inputRows)
    };
    setGrid({ ...res });
  };

  return (
    <div className="App">        
        <Grid
          grid={grid}
          handleGridSize={handleGridSize}
          inputCells={inputCells}
          inputRows={inputRows}
          setCells={setCells}
          setRows={setRows}
        />
    </div>
  );
}

export default App;
