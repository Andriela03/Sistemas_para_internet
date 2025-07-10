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


////


let idade = 18;

if (idade < 18) {
    console.log('Você pode ter acesso.');
}
else if (idade >= 18 && idade < 25) {
    console.log('Você pode entrar com ressalvas...');
}
else {
    console.log("Você pode ter acesso");
}



////


let array = [10, "Andriela", true, "Gleice"]

const objetos = {nome: "Andriela", idade:29, sexo:"F" }

console.log(objetos['nome'])


const usuarios = [{
    nome:"Andriela",
    idade: 19,
    sexo: "F", 
    endereco: {
        rua: "rua",
        cidade: "Cidade",
        numero: "Número"
    }
}, {
    nome:"Gleice",
    idade: 20,
    sexo: "F", 
    endereco: {
        rua: "rua lelele",
        cidade: "lalala",
        numero: "9"
    }
}
]

console.log(usuarios[0].endereco.rua)
console.log(usuarios[1].nome)

//Se o usuario não tiver coocado nome, 
// o nome padrão dele será user111
//se ele colocar o nome, apresenta o nome 

const nomeUsuario = ""
const nomePadrao = nomeUsuario || 'user111'

console.log(nomePadrao)


function soma(valor1, valor2) {
    return valor1 + valor2
}

console.log(soma(10, 15))


function somaTodosValores(valores) {
    let soma = 0
    for(let i=0; i<valores.length; i++) {
        soma = soma + valores[1]
        if (typeof(valores[i]) !== 'number') 
        {return 'Valor inválido'}
    }
    return soma
}

console.log(somaTodosValores(10, 29, 30, 40))