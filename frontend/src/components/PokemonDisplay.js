import React from 'react';

function PokemonDisplay({ pokemon }) {
  if (!pokemon) return null;

  if (pokemon.error) {
    return (
      <div className="pokemon-display error">
        <p>{pokemon.error}</p>
      </div>
    );
  }

  const name = pokemon.name ? pokemon.name.charAt(0).toUpperCase() + pokemon.name.slice(1) : 'Unknown';

  return (
    <div className="pokemon-display">
      <h2>{name}</h2>
      {pokemon.sprite && (
        <img src={pokemon.sprite} alt={name} />
      )}
      <div className="pokemon-info">
        {pokemon.types && (
          <p>Types: {pokemon.types.join(', ')}</p>
        )}
        {pokemon.height && (
          <p>Height: {pokemon.height / 10}m</p>
        )}
        {pokemon.weight && (
          <p>Weight: {pokemon.weight / 10}kg</p>
        )}
        {pokemon.abilities && (
          <p>Abilities: {pokemon.abilities.join(', ')}</p>
        )}
      </div>
    </div>
  );
}

export default PokemonDisplay;