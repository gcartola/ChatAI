function enviarParaIA(mensagem) {
  fetch('http://localhost:8000/ia-suporte', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ mensagem: mensagem })
  })
  .then(response => response.json())
  .then(data => {
    alert("Resposta da IA: " + data.resposta);
  })
  .catch(error => {
    console.error("Erro ao consultar a IA:", error);
  });
}