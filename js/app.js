const fetchPromise = fetch("http://172.24.41.200:8080/eventos");

const main = document.getElementById("main");
// Loading Placeholder
main.innerHTML = "<p>Loading...";
fetchPromise.then(response => {
  return response.json();
}).then(eventos => {
  main.innerHTML = listOfEventos(eventos);
});
function listOfEventos(eventos) {
  const _eventos = eventos.map(evento => `<li> <a href="http://172.24.41.200:8080/eventos/${evento.id}">${evento.nombre}</a></li>`).join("\n");
  return `<ul>${_eventos}</ul>`
}

function llamarPost(e)
{
    e.preventDefault();
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const nombre = document.getElementById("nombre").value;
    const categoria = document.getElementById("categoria").value;
    const lugar = document.getElementById("lugar").value;
    const direccion = document.getElementById("direccion").value;
    const fechaInicio = document.getElementById("fechaInicio").value;
    const fechaFin = document.getElementById("fechaFin").value;
  
var raw = JSON.stringify({
  "nombre": nombre,
  "categoria": categoria,
  "lugar": lugar,
  "direccion": direccion,
  "fechaInicio": fechaInicio,
  "fechaFin": fechaFin
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://172.24.41.200:8080/eventos", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
}