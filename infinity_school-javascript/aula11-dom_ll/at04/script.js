// Pega os elementos do HTML
const area = document.getElementById("areaMouse");
const coordenadas = document.getElementById("coordenadas");

// Evento que captura o movimento do mouse
area.addEventListener("mousemove", (event) => {
  const x = event.offsetX; // Posição X dentro da área
  const y = event.offsetY; // Posição Y dentro da área
  coordenadas.textContent = `Coordenadas: X=${x}, Y=${y}`; // Mostra na tela
});