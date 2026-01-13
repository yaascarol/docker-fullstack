import './App.css';
import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const path =
      window.location.pathname === "/" ? "/api01" : window.location.pathname;

    axios.get(path).then(res => setData(res.data));
  }, []);

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}

export default App;
