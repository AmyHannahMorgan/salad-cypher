# salad-cypher

A cypher idea I had while not paying attention during a lecture

## How It works
Firstly the code takes any cypher key given to it and appends the remainder of the alphabet to it to create the full key, referred to in the code as the "cypherbet". 

The code will then iterate through the input text and find each characters corresponding index within the cypher key. this cypher index then has the current Fibonacci number, defined by the index within the input, added to or subtracted from it depending on whether the input index is even or odd. The result of this is then used to determine what character from the cypher key is written to the output

For example, with the cypher key:

`STABCDEFGHIJKLMNOPQRUVWXYZ`

and the input:

`Hello World`

The `o` in `Hello` would be encoded as `J` as the `o` is the 5th character in the string meaning that we encode the `o` as what ever is F5 spaces back along the cypher key from `O`. The 5th Fibonacci number is 5, meaning we go back 5 spaces from `O` to `J`

## Why?

Honestly I had nothing better to do and this sounded like a fun way to waste an hour or so of my time