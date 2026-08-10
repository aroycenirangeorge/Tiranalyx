import "./App.css"
import { useState } from "react"

function App() {
  const [file, setFile] = useState(null)
  const [logs, setLogs] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [analysis, setAnalysis] = useState(null)
  const [aiAnalysis, setAiAnalysis] = useState(null)

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
  <div className="app">
    <div className="container">

      <header className="header">
        <h1>Tiranalyx</h1>
        <p>AI Log Intelligence</p>
      </header>

      <div className="upload-box">

        <input
          className="file-input"
          type="file"
          accept=".log"
          onChange={(event) => {
            setFile(event.target.files[0])
            setLogs([])
            setAnalysis(null)
            setAiAnalysis(null)
            setError("")
          }}
        />

        {file && (
          <p className="selected-file">
            Selected file: {file.name}
          </p>
        )}

        <button
          className="analyze-button"
          onClick={uploadLog}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze Log"}
        </button>

        {error && (
          <p className="error">{error}</p>
        )}

      </div>

      {analysis && (
        <section className="section">

          <h2 className="section-title">
            Analysis
          </h2>

          <div className="stats">

            <div className="stat-card">
              <div className="stat-number">
                {analysis.total_logs}
              </div>
              <div className="stat-label">
                Total Logs
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-number">
                {analysis.statistics.error_count}
              </div>
              <div className="stat-label">
                Errors
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-number">
                {analysis.statistics.warning_count}
              </div>
              <div className="stat-label">
                Warnings
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-number">
                {analysis.statistics.info_count}
              </div>
              <div className="stat-label">
                Info
              </div>
            </div>

          </div>

        </section>
      )}

      {analysis?.issues?.length > 0 && (
        <section className="section">

          <h2 className="section-title">
            Detected Issues
          </h2>

          <div className="issue-list">

            {analysis.issues.map((issue, index) => (

              <div className="issue-card" key={index}>

                <div className="issue-header">

                  <span className="issue-type">
                    {issue.issue_type}
                  </span>

                  <span className="severity">
                    {issue.severity}
                  </span>

                </div>

                <div className="issue-message">
                  {issue.message}
                </div>

                <div className="issue-meta">
                  {issue.timestamp}
                </div>

                <div className="issue-impact">
                  <strong>Impact:</strong>{" "}
                  {issue.impact}
                </div>

              </div>

            ))}

          </div>

        </section>
      )}

      {aiAnalysis && (
        <div>
          <h2>AI Analysis</h2>

          <div>
            <h3>Problem</h3>
            <p>{aiAnalysis.problem}</p>
          </div>

          <div>
            <h3>Likely Cause</h3>
            <p>{aiAnalysis.likely_cause}</p>
          </div>

          <div>
            <h3>Recommended Actions</h3>

            <ol>
              {aiAnalysis.recommended_actions.map((action, index) => (
                <li key={index}>
                  {action}
                </li>
              ))}
            </ol>
          </div>
        </div>
      )}

      {logs.length > 0 && (
        <section className="section">

          <h2 className="section-title">
            Parsed Logs
          </h2>

          <div className="logs">

            {logs.map((log, index) => (

              <div className="log-entry" key={index}>

                <span className={`log-level ${log.level}`}>
                  {log.level}
                </span>

                <span className="log-message">
                  {log.timestamp} — {log.message}
                </span>

              </div>

            ))}

          </div>

        </section>
      )}

    </div>
  </div>
  )
}
export default App