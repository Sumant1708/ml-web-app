import logo from './logo.svg';
import './App.css';

function App() {
  const predict = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/predict/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ value: 5 })
    });
    const data = await res.json();
    alert(data.prediction);
  };

  return <button onClick={predict}>Predict</button>;
}

export default App;
