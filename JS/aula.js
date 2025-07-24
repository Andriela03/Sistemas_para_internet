function soma(valor1, valor2){
    const soma = valor1 + valor2
    
    if(typeof(valor1) === 'number' && typeof(valor2) === 'number'){
        if(valor1 < 0 || valor2 < 0){
            return "Não é válido"
         }
         else{
             return soma
         }
    }
    else{
        return "Não é válido somar um número com uma string"
    }

    
} 

const receberResultado = soma(100, "Andri")
console.log(receberResultado)

//Return = utilizar a informação em outro local
//console.log = visualizar somente