export default function Message({ msg }) {
    return (
        <div style={{ margin: "10px" }}>
            <b>{msg.role}</b>: {msg.text}
        </div>
    )
}