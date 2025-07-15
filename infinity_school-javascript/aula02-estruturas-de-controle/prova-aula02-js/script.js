let idade = Number(prompt("Digite sua idade:"));

let status = prompt("Digite seu status (registrado ou não registrado):").toLowerCase();

let maioridade = idade >= 18 ? "maior de idade" : "menor de idade";
console.log(`Você é ${maioridade}.`);

switch (status) {
    case "registrado":
        console.log("Bem-vindo! Seu acesso está sendo processado.");
        break;
    case "não registrado":
    case "nao registrado":
        console.log("Por favor, complete seu registro para continuar.");
        break;
    default:
        console.log("Status desconhecido.");
        break;
}

if (idade >= 18 && status === "registrado") {
    console.log("✅ Acesso completo liberado.");
} else {
    console.log("⚠️ Acesso limitado.");
}