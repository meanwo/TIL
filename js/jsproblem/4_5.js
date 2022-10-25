// problem4-5/index.js
// 각 요소들을 가져온다
const scissorsButton = document.getElementById('scissors-button')
const rockButton = document.getElementById('rock-button')
const paperButton = document.getElementById('paper-button')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')
const player1Img = document.querySelector('#player1-img')
const player2Img = document.querySelector('#player2-img')


modal.addEventListener('click', () => modal.style.display = 'none')

let count1 = 0
let count2 = 0

// 가위바위 보 게임, 두 파라미터를 받아 결과를 리턴한다.
const playGame = (p1Choice, p2Choice) => {
  switch (p1Choice) {
    case 'rock':
      switch (p2Choice) {
        case 'rock': 
        return 0
        case 'paper':
          return 2
        case 'scissors':
          return 1
      }
    case 'paper':
      switch (p2Choice) {
        case 'rock': 
          return 1
        case 'paper':
          return 0
        case 'scissors':
          return 2
      }
    case 'scissors':
      switch (p2Choice) {
        case 'rock': 
          return 2
        case 'paper':
          return 1
        case 'scissors':
          return 0
      }
  }
}

const choiceButton = function (choice) {
  return () => {
    // 각 버튼에 마우스와 관련된 모든 이벤트를 제거하는 속성을 추가한다.
    scissorsButton.setAttribute('disabled', 'true')
    scissorsButton.setAttribute('style', 'pointer-events: none;')
    rockButton.setAttribute('disabled', 'true')
    rockButton.setAttribute('style', 'pointer-events: none;')
    paperButton.setAttribute('disabled', 'true')
    paperButton.setAttribute('style', 'pointer-events: none;')
    
    const cases = ['scissors', 'rock', 'paper']
    // lodash를 활용하여 무작위 값을 선정
    const randomChoice = _.sample(cases)
    
    // 가위바위보 진행
    const result = playGame(choice, randomChoice)

    // 결과에 따라 count 변수 설정
    if (result === 1) {
      count1 += 1
    } else if (result === 2) {
      count2 += 1
    }

    // 가위바위보 중 선택한 이미지로 player1 의 이미지를 설정
    player1Img.src = `img/${choice}.png`

    let i = 0
    // setInterval : 일정 시간 간격을 두고 함수를 실행함
    // 100ms 간격으로 호출
    // -> 100ms 간격으로 randomImg 가 변경됨
    const randomImg = setInterval(() => {
      i = (i + 1) % 3
      player2Img.src = `img/${cases[i]}.png`
    }, 100)

    setTimeout(() => {
      // setInterval 함수 호출 중단
      // -> player2 의 이미지가 바뀌지 않음
      clearInterval(randomImg)
      const countA = document.querySelector('.countA')
      const countB = document.querySelector('.countB')
      countA.innerText = count1
      countB.innerText = count2
      
      // 무작위로 선택된 이미지로 player2 의 이미지를 설정
      player2Img.src = `img/${randomChoice}.png`
      
      // modal 설정
      modalContent.innerText = result ? `player${result} 의 승리입니다!` : '무승부입니다!'
      modal.style.display = 'flex'
        
      // 이벤트 처음에 추가했던 속성인,
      // 각 버튼에 마우스와 관련된 모든 이벤트를 제거하는 속성을 제거한다.
      scissorsButton.removeAttribute('disabled')
      scissorsButton.removeAttribute('style')
      rockButton.removeAttribute('disabled')
      rockButton.removeAttribute('style')
      paperButton.removeAttribute('disabled')
      paperButton.removeAttribute('style')
    }, 3000)
  }
}

// 각 버튼에 이벤트를 추가한다.
scissorsButton.addEventListener('click', choiceButton('scissors'))
rockButton.addEventListener('click', choiceButton('rock'))
paperButton.addEventListener('click', choiceButton('paper'))