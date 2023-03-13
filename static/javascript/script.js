/*

let playerName = document.getElementById("playerName")

let totalScore = document.getElementById("totalScore")
let score = 0

let roundTotal = document.getElementById("roundTotal")
let roundScore = 0
document.querySelector(".new-game h2").textContent = roundScore

document.getElementById("startGame").addEventListener("submit", function(event){
    event.preventDefault(); // stop the form from refreshing the page
    document.querySelector(".info span:nth-child(1)").textContent = playerName.value //this is the span element where the player name will show

    letterGeneration()
    countdown()
    totalScore.textContent = score + roundScore
    roundTotal.textContent = roundScore

});
*/

function startGame() {
    console.log("start")
}

/*


function letterGeneration() {
    let letter = document.getElementById("letter")
    let alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = Math.floor(Math.random()*alphabet.length)
    letter.textContent = alphabet[index].toUpperCase()
}

function countdown() {
    let count = 30
    let timer = document.getElementById("timer")
    const interval = setInterval(() => {
      timer.textContent = count;
      count--;
      if (count < 0 ) {
        clearInterval(interval);
        document.querySelector(".main-game").style.display = "none";
        document.querySelector(".new-game").style.display = "flex";

        checkAnswers()
      }
    }, 1000);
  }



*/