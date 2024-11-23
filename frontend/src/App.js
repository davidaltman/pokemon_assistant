import React, { useState } from 'react';
import ChatBox from './components/ChatBox';
import PokemonDisplay from './components/PokemonDisplay';

function App() {
  const [messages, setMessages] = useState([]);
  const [pokemonData, setPokemonData] = useState(null);

  const handleSendMessage = async (message) => {
    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();

      setMessages(prev => [...prev,
        { type: 'user', content: message },
        { type: 'assistant', content: data.response }
      ]);

      // Try to extract Pokemon name from message and fetch data
      const pokemonName = message.toLowerCase().match(/(?:about|is|pokemon)\s+(\w+)/)?.[1];
      if (pokemonName) {
        const pokemonResponse = await fetch(`http://localhost:8000/api/pokemon/${pokemonName}`);
        const pokemonData = await pokemonResponse.json();
        setPokemonData(pokemonData);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokémon Assistant</h1>
      </header>
      <main className="App-main">
        <div className="chat-container">
          <ChatBox messages={messages} onSendMessage={handleSendMessage} />
        </div>
        {pokemonData && (
          <div className="pokemon-container">
            <PokemonDisplay pokemon={pokemonData} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;