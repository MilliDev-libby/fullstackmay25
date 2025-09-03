// const express = require("express")
// const bodyParser = require('body-parser')
// const app = express();
// const port = 8000

// app.use( bodyParser.json() )

// let books = [
//     {
//         "title":"The Cat in the Hat",
//         "author":"Dr. Suess"
//     },
//     {
//         "title":"The Lorax",
//         "author":"Dr. Suess"
//     },
//     { "id":3,
//         "title":"Green Eggs and Ham",
//         "author": "Dr.Seuss"
//     }
// ]

// app.get("/books", (request ,response) => {
//     response.send( books )  // request to get all book in the book list
// })
 
// app.get("/books/:id", (request ,response) => {
//     let book = books.find ((books) => book.id == request.params.id)    //request to get book by id
// })
 
 
 
// app.post('/books', (request,response)=>{
//     let book = request.body
//     books.push(book)
//     response.send(books)   // request to add a new book
 
// })
 
 
 
// app.listen(port, ()=>{
//    console.log("Server is running on port 8080 ")
// }) 
// app.get("/books/:id", (request, response) => {
//     let book = books.find((book) => book.id == request.params.id);
//     if (book) {
//         response.send(book);
//     } else {
//         response.status(404).send({ error: "Book not found" });
//     }
// });
const express = require("express")
const bodyParser = require('body-parser')
const app = express()
const port = 8080
 
app.use( bodyParser.json() )
 
app.get('/', (request,response)=>{
    response.send("Hello Postman!")
})
 
app.post('/post', (request,response)=>{
    let data = request.body
 
    response.send( data )
})
 
app.listen(port, ()=>{
   console.log("Server is running on port 8080 ")
})