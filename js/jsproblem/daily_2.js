// 데일리 실습 1
    // 1
    // const name = 'Tom'
    // console.log(`Hi, my name is ${name}`)

    // 2
    // const add = (x, y) => x + y 
    // console.log(add(1, 2))
    

    // // 3
    // const tom = {
    //   name: 'Tom',
    //   introduce() {
    //     console.log('Hi, my name is ' + this.name)
    //   }
    // }

    // tom.introduce()

    // // // 4
    // const url = 'https://test.com'
    // const data = { message: 'Hello World!' }

    // const request = { url, data }

    // console.log(request)

// 데일리 실습 2

    /* 
      1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
      2. filter 메서드를 활용해 결혼한 사람들만 모아 married 상수에 할당하시오.
      3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오.
      4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
      5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
    */

    //   const users = [
    //     { name: 'John', age: 31, isMarried: true, balance: 100, },
    //     { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
    //     { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
    //     { name: 'Robert', age: 27, isMarried: false, balance: 400, },
    //     { name: 'Tom', age: 35, isMarried: true, balance: 500, },
    //   ]

    // //   1
    // users.forEach((user) => {
    //     return console.log(user.name)
    // })
    
    // // 2
    // const married = users.filter((user) => {
    //     return user.isMarried === true
    // }) 

    // console.log(married)

    // // 3
    // const tom = users.find((user) => {
    //     return user.name === 'Tom'
    // })
    
    // console.log(tom)

    // // 4
    // const newUsers = users.map((user) => {
    //     user.isAlive = true
    //     return user
    // })
    
    // console.log(newUsers)


    // // 5
    // const totalBalance = users.reduce((total, user) => {
    //     return total + user.balance
    // }, 0)

    // console.log(totalBalance)

// 데일리 실습 3
        /* 
      1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
      2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
      3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
    */

    // 1-1
    const savedFile = {
        name: 'profile',
        extension: 'jpg',
        size: 29930
      }
      function fileSummary(file) {
        const {name} = savedFile
        const {extension} = savedFile
        const {size} = savedFile
        console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
      }
      fileSummary(savedFile);
  
      // 1-2
      const data = {
        username: 'myName',
        password: 'myPassword',
        email: 'my@mail.com',
      }
  
      const {username, password, email} = data
      
      

      // 2
      function addNumbers(...numbers) {
        return numbers.reduce((sum, number) => { 
          return sum + number
        }, 0)
      }

      console.log(addNumbers(1, 2, 3, 4, 5))
      

    //   // 3-1
      const defaultColors = ['red', 'green', 'blue'];
      const favoriteColors = ['navy', 'black', 'gold', 'white']
      const palette = [...defaultColors, ...favoriteColors]
      console.log(palette)

    //   // 3-2
      const info1 = { name: 'Tom', age: 30 }
      const info2 = { isMarried: true, balance: 3000 }
      const fullInfo = { ...info1, ...info2}
      console.log(fullInfo)