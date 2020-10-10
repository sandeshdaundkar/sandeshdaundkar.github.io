Title: Learning ES6 For React - Part One
Category: frontend
Tags: frontend, javascript
Date: 2020-10-10
Summary: In this post, I will introduce you to variables and arrow functions in ES6.


> _ECMAScript is Eurpoean standard for JavaScript, AppleScript & JScript._
> _ECMAScript 2015 also known as ES6, is one such JavaScript standard, which adds significant new features for developing complex applications._

I recently, started learning React, and came across the javascript standard used widely for developing React applications. I assume you already have
little experience with JS. Most of the latest browsers support the ES6 Syntax, so if you wish to try the snippets, you can start the developer console and try 'em.
In this section, we will see how we can declare variables and write compact functions using ES6 syntax.

# Variables

In ES6 you can declare variables using either of the three keywords `var`, `let` and `const`, depending on the scope of the variable.
Scope of the variable is nothing but the visibility of the variable within the program.

```javascript
// Declaring variables
var language = "javascript";
let standard = "ecmascript";
const version = 6;
```

`var` is used in case you want to declare variable in global/local scope.

`let` allows you to declare variables, within the scope of the block, statement or expression in which they are declared. <br/>


```javascript
// Understanding Scope
function localScope(){
    var language = "JS";
    if (true){
        var language = "JavaScript"; // considered as same variable inside/outside the if-statement block
        console.log(language);
    }
    console.log(language);

}

function restrictedScope(){
    let standard = "ES6";
    if (true){
        let standard = "ECMAScript 2015"; // considered as new variable inside the if-statement block
        console.log(standard);
    }
    console.log(standard);
}

globalScope();
restrictedScope();
```
The scope of the variables declared using `const` is similar to that of `let`, except that such variables cannot be re-assigned(immutable).
You should use `const` if the value of that variable is not going to vary later in the program. <br/>

```javascript
// Constants cannot be re-assigned
const version = 6;
version = 2015; // raises TypeError: Assignment to constant variable.
```
---

# Arrow Functions

Functions are basically resuable block of code. ES6 introduced a compact way to declare javascript functions.

The syntax for writing arrow functions is as below

`functionName = (parameters) => {return statement};`

Let's see an example of defining functions using JS and ES6

```javascript
// functions in javascript
function addNumbers(a, b) {
    console.log(a+b);
}
addNumbers(4, 5);

// The same function can be written in compact form using arrow functions

addNumbers = (a, b) => { console.log(a+b);}
addNumbers(4,5);

```

You can also write arrow functions alternatively, depending on the number of parameters in the function and the statement.

- You can omit parentheses **if and only if** you have only one parameter. <br>`square = number => {return number * number}`
- You can omit the return statement and curly braces, **if and only if** all you do is return something. <br> `square = number => number * number;`
- If a function takes no parameters, **empty parentheses** is mandatory. <br> `greet = () => {console.log("Welcome to my blog")}`
- If a function takes **more than one parameter**, parentheses is mandatory. <br> `sum = (a,b) => {return a+b}`

Hope you enjoyed the post.

In the next post, we will see how you can create classes in javascript using ES6.

I will be integrating [disqus](https://disqus.com/) later for comments on the posts, meanwhile feel free to write me on my [email](mailto:me@sandeshdaundkar.com).
