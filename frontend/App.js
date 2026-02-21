import { useState } from "react";
import axios from "axios";

function App() {

  const [url, setUrl] = useState("");
  const [q, setQ] = useState("");
  const [ans, setAns] = useState("");

  const ingest = async () => {
    await axios.post("http://localhost:8000/ingest", { url });
    alert("Ingested");
  }

  const ask = async () => {
    const res = await axios.post("http://localhost:8000/ask", { question: q });
    setAns(res.data.answer);
  }

  return (
    <div style={{ padding: 40 }}>
      <h2>Website RAG Bot</h2>

      <input placeholder="URL" value={url} onChange={e => setUrl(e.target.value)} />
      <button onClick={ingest}>Ingest</button>

      <br /><br />

      <input placeholder="Question" value={q} onChange={e => setQ(e.target.value)} />
      <button onClick={ask}>Ask</button>

      <p>{ans}</p>
    </div>
  )
}

export default App;
