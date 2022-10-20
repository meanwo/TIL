function Person(name) {
    this.name = name
  }
  
  const david = new Person('david')
  const ingu = new Person('ingu')
  
  console.log(david.name)
  console.log(ingu.name)
  
  Person.prototype.speak = () => {
    console.log('나 말한다 !')
  }
  
  david.speak()
  ingu.speak()

  