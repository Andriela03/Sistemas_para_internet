console.log("Olá mundo!") //Print

let nome = "Andriela"; //Variável string
nome = "Gleice";
const numero = 10; //Variável número

let lista = [1, 2, 3, 4]; //Lista
console.log(lista[1]) // Mostrar o número de uma lista 


if (nome === "Andriela") {
    console.log("Você acertou seu nome.")
}
else if (nome === "Gleice") {
    console.log("Esse é o seu sobrenome")
}
else {
    console.log("Seu nome está incorreto.")
}

for (let i = 0; i < 4; i ++) {
    console.log("Contando:" + i)
}

let x = 1;
while (x < 4) {
    console.log("Contando:" + x);
    x++;
}

oi("Andriela", 19);

function oi(nome, idade) {
    console.log(`Olá ${nome} vc tem ${idade} anos`);
}

let pessoa = {
    nome: "Andriela",
    idade: 21
}

console.log (pessoa.nome)