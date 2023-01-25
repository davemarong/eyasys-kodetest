// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  // usestate for setting a javascript
  // object for storing and using data
  const [data, setdata] = useState([
    {
      name: "",
      age: 0,
      programming: "",
    },
  ]);

  // Using useEffect for single rendering
  useEffect(() => {
    // Using fetch to fetch the api from
    // flask server it will be redirected to proxy
    fetch("http://localhost:5000/phones").then((res) =>
      res.json().then((data) => {
        console.log(data);
        // Setting a data from api
        setdata(data);
      })
    );
  }, []);

  let dataa = {
    name: "Flask Room",
    description: "Talk about Flask here.",
  };
  fetch("http://localhost:5000/phones", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dataa),
  }).then((res) => {
    console.log(res);
  });
  return (
    <div className="App">
      <header className="App-header">
        <h1>React and flask</h1>
        {data.map((phone) => {
          return (
            <ul key={phone.Modell}>
              <li>{phone.Merke}</li>
              <li>{phone.Modell}</li>
              <li>{phone.Phone}</li>
            </ul>
          );
        })}
      </header>
    </div>
  );
}

export default App;
