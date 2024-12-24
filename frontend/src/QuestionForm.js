import { useState } from "react"
import axios from 'axios'

const api=axios.create(
    {baseURL:'http://localhost:8000'}
)
function QuestionForm(){
    const [question,setQuestion] =useState('')
    const [answer,setAnswer] =useState('')

    const handleSubmit=async (e)=>{
        e.preventDefault();
        console.log("your question",question)
        const response= await api.post('/chat',{'message':question})
        setAnswer(response.data.answer)
    }
    return(
        <div>
            <form>
            <input type="text" value={question} onChange={(e)=>setQuestion(e.target.value)}></input>
            <button type="Submit" onClick={handleSubmit}>Submit</button>
        </form>
        <p>Answer:{answer}</p>
        </div>

    )
}

export default QuestionForm