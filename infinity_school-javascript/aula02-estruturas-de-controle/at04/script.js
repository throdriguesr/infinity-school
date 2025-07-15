// Solicita os dois números ao usuário
let numero1 = Number(prompt("Digite o primeiro número:"));
let numero2 = Number(prompt("Digite o segundo número:"));

// Solicita a operação desejada
let operacao = prompt("Digite a operação desejada (+, -, *, /):");

// Variável para armazenar o resultado
let resultado;

// Estrutura switch para escolher a operação
switch (operacao) {
    case "+":
        resultado = numero1 + numero2;
        console.log(`Resultado: ${numero1} + ${numero2} = ${resultado}`);
        break;
    case "-":
        resultado = numero1 - numero2;
        console.log(`Resultado: ${numero1} - ${numero2} = ${resultado}`);
        break;
    case "*":
        resultado = numero1 * numero2;
        console.log(`Resultado: ${numero1} * ${numero2} = ${resultado}`);
        break;
    case "/":
        if (numero2 !== 0) {
            resultado = numero1 / numero2;
            console.log(`Resultado: ${numero1} / ${numero2} = ${resultado}`);
        } else {
            console.log("Erro: divisão por zero não é permitida.");
        }
        break;
    default:
        console.log("Operação inválida. Use apenas +, -, * ou /.");
}