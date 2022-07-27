import React, { useState } from 'react';
import axios from 'axios';

axios.defaults.withCredentials = true;


function App() {

  const [data, setDate] = useState('')
  const [auth, setauth] = useState(false)
  const [url, setURL] = useState('')

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
    })
      .then(res => {
        setauth(false)
      })
  }

  const getProject = () => {
    console.log('go localhost:3001')
    axios.post('http://localhost:8000/user/Dashboard', {
      url: url
    }
    )
      .then(res => {
        setauth(true)
      })
  }

  const URLChange = ({ target: { value } }) => {
    setURL(value)
  }

  const TestAPI = () => {
    axios.post('http://localhost:8000/user/Dashboard',{
      'make':"data"
    })
  }
 
  return (
    <div>{
      auth ?
        <div>
          <button onClick={getProject} >
            P1으로 가는길~~
          </button>
          <input onChange={URLChange}></input>
        </div>
        :
        <div>

          <div>
            <form onSubmit={(event) => sendData(event)}>
              값을 입력하시오
              <input onChange={handleChange}></input>
              <button type='submit'>입력</button>
            </form>
          </div>
          <br/>
          <button onClick={TestAPI}>헤더에 토큰이 있을까요??</button>
        </div>
    }
    </div>
  );


}

export default App;
