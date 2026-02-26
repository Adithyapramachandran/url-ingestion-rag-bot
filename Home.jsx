import { useState } from "react"
import { ingestURL, chat } from "../api"

export default function Home() {
    const [url, setUrl] = useState("")
    const [question, setQuestion] = useState("")
    const [answer, setAnswer] = useState("")
    const [loading, setLoading] = useState(false)

    const handleIngest = async () => {
        if (!url) return
        setLoading(true)
        try {
            await ingestURL(url)
            alert("Website indexed ✅ Now ask questions")
        } catch (e) {
            alert("Ingest failed")
        }
        setLoading(false)
    }

    const handleAsk = async () => {
        if (!question) return
        setLoading(true)
        try {
            const res = await chat(question)
            setAnswer(res.data.answer)
        } catch {
            setAnswer("Error getting answer")
        }
        setLoading(false)
    }

    return (
        <div style={{ maxWidth: 700, margin: "50px auto", fontFamily: "sans-serif" }}>
            <h1>RAG Website Chatbot</h1>

            {/* URL */}
            <div style={{ display: "flex", gap: 10 }}>
                <input
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter website URL"
                    style={{ flex: 1, padding: 10 }}
                />
                <button onClick={handleIngest} disabled={loading}>
                    Ingest
                </button>
            </div>

            {/* Question */}
            <div style={{ marginTop: 30, display: "flex", gap: 10 }}>
                <input
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="Ask question about website..."
                    style={{ flex: 1, padding: 10 }}
                />
                <button onClick={handleAsk} disabled={loading}>
                    Ask
                </button>
            </div>

            {/* Answer */}
            {answer && (
                <div style={{ marginTop: 30 }}>
                    <h3>Answer:</h3>
                    <p>{answer}</p>
                </div>
            )}
        </div>
    )
}