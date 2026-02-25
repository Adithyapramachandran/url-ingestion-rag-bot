import axios from "axios"

const API = "http://127.0.0.1:8000"

// ingest website
export const ingestURL = async (url) => {
    return axios.post(`${API}/ingest/`, { url })
}

// chat question
export const chat = async (question) => {
    return axios.post(`${API}/chat/`, { question })
}
