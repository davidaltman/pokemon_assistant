import React from 'react';

/**
 * Component that displays detailed information about a Pokemon
 * @param {Object} props
 * @param {Object} props.pokemon - Pokemon data object
 * @param {string} [props.pokemon.name] - Name of the Pokemon
 * @param {string} [props.pokemon.sprite] - URL of the Pokemon's sprite image
 * @param {string[]} [props.pokemon.types] - Array of Pokemon types
 * @param {number} [props.pokemon.height] - Height of the Pokemon in decimeters
 * @param {number} [props.pokemon.weight] - Weight of the Pokemon in hectograms
 * @param {string[]} [props.pokemon.abilities] - Array of Pokemon abilities
 * @param {string} [props.pokemon.error] - Error message if Pokemon data fetch failed
 * @returns {JSX.Element|null} A Pokemon information display or null if no Pokemon data
 */
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