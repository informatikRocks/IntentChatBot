import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    // Zentriert alles auf dem Bildschirm mit einem grauen Hintergrund
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      
      {/* Die Card-Komponente */}
      <div className="bg-white p-8 rounded-2xl shadow-xl max-w-sm w-full text-center border border-gray-200">
        
        <h1 className="text-3xl font-extrabold text-gray-800 mb-2">
          React + Tailwind
        </h1>
        
        <p className="text-gray-500 mb-6">
          Vite v4 macht das Styling extrem schnell.
        </p>

        {/* Der Counter-Bereich */}
        <div className="bg-blue-50 rounded-lg py-4 mb-6">
          <span className="text-5xl font-mono font-bold text-blue-600">
            {count}
          </span>
        </div>

        {/* Button mit Hover-Effekten */}
        <button
          onClick={() => setCount((count) => count + 1)}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors duration-200 shadow-lg active:transform active:scale-95"
        >
          Zähler erhöhen
        </button>

        <p className="mt-4 text-xs text-gray-400 uppercase tracking-widest">
          Vite v7 Server läuft
        </p>
      </div>
    </div>
  )
}

export default App