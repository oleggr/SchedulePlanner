import React, { useState } from "react";
import axios from 'axios';

const Grid = ({
  grid,
  handleGridSize,
  inputCells,
  setCells,
  inputRows,
  setRows,
}) => {
  const field = new Array(grid.rows).fill(new Array(grid.cells).fill(0));
  const [field_arr, setField] = useState(field);

  const handleClick = (e, index_row, index_cell) => {
    let a = JSON.parse(JSON.stringify(field_arr));

    const item = e.target;
    if (item.classList.contains('selected')) {
      a[index_row][index_cell] = 0;
    } else {
      a[index_row][index_cell] = 1;
    }

    setField(a);
  };

  const sendToBackend = (e) => {
    console.log("send data to host:")
    console.log(field_arr)

    var body = {
      "field": field_arr,
      "end_x": inputCells,
    };
    
    axios.post('http://127.0.0.1:8000/api/strategy/1', body)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  return (
  
    <div className="main">
      <div className="map">
        {field_arr.map((field_row, index_row) => (
          <ul className="row" key={index_row}>
            {field_row.map((cell, index_cell) => {
              if(cell) {
                return <li key={index_cell} className="item selected" onClick={(e) => handleClick(e, index_row, index_cell)}/>
              } else {
                return <li key={index_cell} className="item" onClick={(e) => handleClick(e, index_row, index_cell)}/>
              }
            })}
          </ul>
        ))}
      </div>

      <div className="settings">
        <h1>SchedulePlanner</h1>

        <div>
          <label htmlFor="cells">Define cells in the row</label>
        </div>

        <div>
          <input
            type="text"
            placeholder="Define cells in the row"
            id="cells"
            value={inputCells}
            onChange={(e) => setCells(e.target.value)}
          />
        </div>


        <div>
          <label htmlFor="rows">Define rows</label>
        </div>
        <div>
          <input
            type="text"
            placeholder="Define rows"
            id="rows"
            value={inputRows}
            onChange={(e) => setRows(e.target.value)}
          />
        </div>

        <button onClick={handleGridSize}>Change Grid</button>
        <button onClick={sendToBackend}>Find Schedule</button>
        
        <a 
          className="btn" 
          href='https://github.com/oleggr/SchedulePlanner' 
          target="_blank" 
          rel="noreferrer"
          >Github</a>
      </div>

    </div>
  );
};

export default Grid;
