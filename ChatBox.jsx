import { useState } from "react"
import { askQuestion } from "../api"
import Message from "./Message"

export default function ChatBox() {

    const [messages, setMessages] = useState([])
    const [input, setInput] = useState("")

    const send = async () => {
        const user = { role: "user", text: input }
        setMessages(m => [...m, user])

        const res = await askQuestion(input)

        setMessages(m => [...m, { role: "assistant", text: res.data.answer }])
        setInput("")
    }

    return (
        <div>
            {messages.map((m, i) => <Message key={i} msg={m} />)}

            <input value={input} onChange={e => setInput(e.target.value)} />
            <button onClick={send}>Send</button>
        </div>
    )
}