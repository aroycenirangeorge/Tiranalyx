import { useState } from "react"

function App() {
  const [file, setFile] = useState(null)
  const [logs, setLogs] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [analysis, setAnalysis] = useState(null)
  const [aiAnalysis, setAiAnalysis] = useState("")

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

      setLogs(data.logs)
      setAnalysis(data.analysis)
      setAiAnalysis(data.ai_analysis)

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
          setAnalysis(null)
          setAiAnalysis("")
          setError("")
        }}
      />

      {file && (
        <p>
          Selected file: {file.name}
        </p>
      )}

      <button onClick={uploadLog} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Log"}
      </button>

      {error && (
        <p>{error}</p>
      )}

      {analysis && (
        <div>
          <h2>Analysis</h2>

          <p>Total Logs: {analysis.total_logs}</p>
          <p>Errors: {analysis.statistics.error_count}</p>
          <p>Warnings: {analysis.statistics.warning_count}</p>
          <p>Info: {analysis.statistics.info_count}</p>
        </div>
      )}

      {analysis && analysis.issues && analysis.issues.length > 0 && (
        <div>
          <h2>Detected Issues</h2>

          {analysis.issues.map((issue, index) => (
            <div key={index}>
              <h3>
                {issue.issue_type} — {issue.severity}
              </h3>

              <p>
                <strong>Message:</strong> {issue.message}
              </p>

              <p>
                <strong>Timestamp:</strong> {issue.timestamp}
              </p>

              <p>
                <strong>Impact:</strong> {issue.impact}
              </p>
            </div>
          ))}
        </div>
      )}

      {aiAnalysis && (
        <div>
          <h2>AI Analysis</h2>

          <pre>
            {aiAnalysis}
          </pre>
        </div>
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