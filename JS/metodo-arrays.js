let nome = ["Andriela", "Gleice", "Silva"]

//Método em lista 
// Tamanho da lista

console.log(nome.length)

// Acessar elementor por índice 

console.log(nome[0])


// Inserir elementos na lista (fim)

nome.push("Pereira")
console.log(nome)

// Inserir no início

nome.unshift("Maria Clara")
console.log(nome)

// Remove no final

const nomeRemovido = nome.pop()
console.log(nomeRemovido)

// Remover do início 

nome.shift()
console.log(nome)

// Função SPLICE

nome.splice(nome.length, 0, "Nome qualquer", "Outro Nome")
console.log(nome)

// Atividade: 
//Inserir Ana Clara (1°)
//Inserir Marcos (3°)
//remova elementos (2°)
nome = ['Pedro Leo', 'Pedro Lucas', 'Joao Vitor']
nome.splice(0, 0, "Ana Clara")
nome.splice(2, 0, "Marcos")
nome.splice(1,1)


console.log(nome)

// SLICE
nome = ['Pedro Leo', 'Pedro Lucas', 'Joao Vitor']
let pedros = nome.slice(0,2)
console.log(pedros)

//Modais
/* const nomeDoUsuario = prompt("Qual é o seu nome?")
alert("Você não pode acessar") */

// Funções callback

function f1(){
    setTimeout(function(){
        console.log('f1')
    }, 500)
    
}

function f2(){
    setTimeout(function(){
        console.log('f2')
    }, 100)
}

function f3() {
    setTimeout(function(){
        console.log('f3')
    }, 3000)
}

f1()
f2()
f3()


