// 🎮 Seleciona os elementos do jogo
const mario = document.querySelector('.mario');
const pipe = document.querySelector('.pipe');
const audio = document.getElementById('bg-music');
const scoreDisplay = document.getElementById('score');
const gameOverDisplay = document.getElementById('game-over');
const finalScoreDisplay = document.getElementById('final-score');

// 🎵 Variáveis de controle
let musicaIniciada = false; // controla início da música
let score = 0;              // pontuação atual
let gameEnded = false;      // indica se o jogo acabou
let canScore = true;        // permite pontuar uma vez por tubo

// 🕹️ Função que faz o Mario pular
const jump = () => {
  mario.classList.add('jump');

  setTimeout(() => {
    mario.classList.remove('jump');
  }, 500); // duração do pulo
};

// 🔁 Loop principal do jogo (executa a cada 10ms)
const loop = setInterval(() => {
  const pipePosition = pipe.offsetLeft;
  const marioPosition = +window.getComputedStyle(mario).bottom.replace('px', '');

  // 💥 Verifica colisão entre Mario e tubo
  if (pipePosition <= 120 && pipePosition > 0 && marioPosition < 80) {
    // Para as animações
    pipe.style.animation = 'none';
    pipe.style.left = `${pipePosition}px`;

    mario.style.animation = 'none';
    mario.style.left = `${pipePosition}px`;

    // Troca imagem do Mario para "game over"
    mario.src = '../images/game-over.png';
    mario.style.width = '75px';
    mario.style.marginLeft = '-50px';

    // Exibe mensagem de fim de jogo
    gameOverDisplay.classList.remove('hidden');
    finalScoreDisplay.textContent = `Score final: ${score}`;

    gameEnded = true;
    clearInterval(loop); // para o jogo
  }

  // ✅ Pontuação: quando o tubo passa com segurança
  if (pipePosition < 0 && canScore && !gameEnded) {
    score++;
    scoreDisplay.textContent = `Score: ${score}`;
    canScore = false; // impede pontuação duplicada
  }

  // 🔄 Reabilita pontuação para o próximo tubo
  if (pipePosition > 120 && !gameEnded) {
    canScore = true;
  }
}, 10);

// 🎹 Controle de teclas
document.addEventListener('keydown', (e) => {
  const tecla = e.key;

  // 🔁 Reinicia o jogo com a tecla R após o game over
  if (gameEnded && tecla.toLowerCase() === 'r') {
    location.reload();
  }

  // 🕹️ Faz o Mario pular com a tecla espaço
  if (!gameEnded && tecla === ' ') {
    // Inicia a música na primeira vez que espaço é pressionado
    if (!musicaIniciada) {
      audio.currentTime = 0;
      audio.play();
      musicaIniciada = true;
    }
    jump();
  }
});
