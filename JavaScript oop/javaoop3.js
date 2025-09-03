Class Person{
    constructor(name,id)
    this.name = name
    this.id = id
}
print Person Info(){
    console.log('Person: name = ${this.name} id=$ {this.id}')
}

Class Employee extends Person {
    constructor(name, id, number, salary, post)
    super(name,id)
    this.name = name
    this.id = id
    this.salary = salary
    this.post = post
}
