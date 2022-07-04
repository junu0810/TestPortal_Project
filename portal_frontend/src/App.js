import React, { useState } from 'react';
import axios from 'axios';

function App() {

  const [data, setDate] = useState('')
  const [auth, setauth] = useState(false)

  const sendData = (event) => {
    event.preventDefault()
    // console.log(data)
    sendaxios(data)
  }

  const handleChange = ({ target: { value } }) => {
    setDate(value)
  }

  const sendaxios = (sendData) => {
    axios.post('http://localhost:8000/user/', {
      data: sendData
    },
      { withCredentials: true }
    )
      .then(res => {
        setauth(true)
        console.log(res.data.message.data)
      })
  }

  const getProject = () =>{
    console.log('프로젝트를클릭하였다.')
    axios.post('http://localhost:8000/user/Dashboard', {
      data: sendData
    },{headers: {
      "Access-Control-Allow-Origin": "*",
    }},{ withCredentials: true})
    .then(res => {
      setauth(true)   
    })
  }

  return (
    <div>{
      auth ?
        <div>
          <button onClick={getProject} >
            P1으로 가는길~~
          </button>
        </div>
        :
        <div>
          <form onSubmit={(event) => sendData(event)}>
            값을 입력하시오
            <input onChange={handleChange}></input>
            <button type='submit'>입력</button>
          </form>
        </div>
    }
    </div>
  );


}

export default App;
