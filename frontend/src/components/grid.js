import React from 'react';

const Grid = ({
  grid,
  handleGridSize,
  inputCells,
  setCells,
  inputRows,
  setRows,
}) => {
  const field = new Array(grid.rows).fill(new Array(grid.cells).fill(0));

  const handleClick = (e) => {
    const item = e.target;
    if (item.classList.contains('selected')) {
      item.classList.remove('selected');
    } else {
      item.classList.add('selected');
    }
  };

  const sendToBackend = (e) => {
    console.log("send data to host:")
    console.log(field)
  }

  return (
  
    <div className="main">
      <div className="map">
        {field.map((field_row, index_row) => (
          <ul className="row" key={index_row}>
            {field_row.map((cell, index_cell) => {
              if(cell) {
                return <li key={index_cell} className="item selected" custom_x={index_cell} onClick={handleClick}/>
              } else {
                return <li key={index_cell} className="item" onClick={handleClick}/>
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
