import React, { useState } from 'react';
import axios from 'axios';

function App() {

  const [data , setDate ] = useState('')

  const sendData = (event) =>{
    event.preventDefault()
    // console.log(data)
    sendaxios(data)
  }

  const handleChange = ({target:{value}}) =>{
    setDate(value)
  }

  const sendaxios = (sendData) => {
    axios.post('http://127.0.0.1:8000/user/',{
      data: sendData
    })
    .then(res => {
      console.log(res.data.message.data)
    })
  }

  return (
  <div>
    <form onSubmit={(event) => sendData(event)}>
    값을 입력하시오 
    <input onChange={handleChange}></input>
    <button type='submit'>입력</button>
    </form>
  </div>
  );


}

export default App;
