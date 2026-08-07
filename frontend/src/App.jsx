import { useState } from "react"

function App() {
  const [file, setFile] = useState(null)
  const [logs, setLogs] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const uploadLog = async () => {
    if (!file) {
      setError("Please select a log file.")
      return
    }

    setLoading(true)
    setError("")

    const formData = new FormData()
    formData.append("file", file)

    try {
      const response = await fetch("http://127.0.0.1:8000/api/upload/", {
        method: "POST",
        body: formData,
      })

      if (!response.ok) {
        throw new Error("Failed to upload log")
      }

      const data = await response.json()
      setLogs(data)

    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1>Tiranalyx</h1>
      <p>AI Log Intelligence</p>

      <input
        type="file"
        accept=".log"
        onChange={(event) => {
          setFile(event.target.files[0])
          setLogs([])
          setError("")
        }}
      />

      {file && (
        <p>
          Selected file: {file.name}
        </p>
      )}

      <button onClick={uploadLog} disabled={loading}>
        {loading ? "Uploading..." : "Analyze Log"}
      </button>

      {error && (
        <p>{error}</p>
      )}

      {logs.length > 0 && (
        <div>
          <h2>Parsed Logs</h2>

          {logs.map((log, index) => (
            <div key={index}>
              <p>
                <strong>{log.level}</strong>{" "}
                {log.timestamp} — {log.message}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App