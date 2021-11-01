import React, { useState } from "react";
import axios from 'axios';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Grid = ({
  grid,
  inputCells,
  setCells,
  inputRows,
  setRows,
}) => {
  const field = new Array(grid.rows).fill(new Array(grid.cells).fill(0));
  const [field_arr, setField] = useState(field);

  // TODO: add loading field from the file
  // TODO: add hold and move behavior for the grid

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
    var body = {
      "field": field_arr,
      "completion_time": parseInt(inputCells) - 1, // send index here (max number - 1)
    };

    axios.post('http://127.0.0.1:8000/api/strategy/1', body)
      .then(function (response) {
        toast.success("Request sended", {
          autoClose: 2000,
          hideProgressBar: true,
          pauseOnFocusLoss: false
        });        

        var schedule = response.data['result'];
        let a = JSON.parse(JSON.stringify(field_arr));

        schedule.map((schedule_row, schedule_row_index) => (
            // eslint-disable-next-line array-callback-return
            schedule_row.map((schedule_cell, schedule_cell_index) => {
              if(schedule_cell === 1) {
                a[schedule_row_index][schedule_cell_index] = 2; 
              }
            })
        ))

        setField(a);
      })
      .catch(function (error) {
        toast.error("Request failed", {
          autoClose: 2500,
          hideProgressBar: true,
          pauseOnFocusLoss: false
        });
        console.log(error);
      });
  }

  var changeGridLink = "http://localhost:3000/?cells=" + inputCells + "&rows=" + inputRows 
  var li_text = ""

  return (
  
    <div className="main">
      <div className="map">
        {field_arr.map((field_row, index_row) => (
          <ul className="row" key={index_row}>
            {field_row.map((cell, index_cell) => {
              if(index_cell === 0) {
                let index_to_show = inputRows - parseInt(index_row)
                li_text = "CPU" + index_to_show
              } else {
                li_text = ""
              }

              if(cell === 1) {
                return <li key={index_cell} className="item selected" onClick={(e) => handleClick(e, index_row, index_cell)}>{li_text}</li>
              } if(cell === 2) {
                return <li key={index_cell} className="item schedule" onClick={(e) => handleClick(e, index_row, index_cell)}>{li_text}</li>
              } else {
                return <li key={index_cell} className="item" onClick={(e) => handleClick(e, index_row, index_cell)}>{li_text}</li>
              }
            })}
          </ul>
        ))}
        <div>time</div>
      </div>

      <div className="settings">
        <h1>SchedulePlanner</h1>

        <div className="inputblock">
          <div>
            <label htmlFor="cells">Time range:</label>
            <input
              type="text"
              placeholder="Time range"
              id="cells"
              value={inputCells}
              onChange={(e) => setCells(e.target.value)}
            />
          </div>

          <div>
            <label htmlFor="rows">CPU count:</label>
            <input
              type="text"
              placeholder="CPU count"
              id="rows"
              value={inputRows}
              onChange={(e) => setRows(e.target.value)}
            />
          </div>
        </div>

        <div className="inputblock">
          <a 
            className="btn" 
            href={changeGridLink}
            >Change Grid</a>

          <button onClick={sendToBackend}>Find Schedule</button>
          
          <a 
            className="btn" 
            href='https://github.com/oleggr/SchedulePlanner' 
            target="_blank" 
            rel="noreferrer"
            >Github</a>


          <ToastContainer 
            position="bottom-right"
            />
        </div>
      </div>

    </div>
  );
};

export default Grid;
