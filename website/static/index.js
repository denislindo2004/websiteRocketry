function adicionarIngrediente(){
    var ing = document.getElementById("ingredientes").value;
    var lista = document.getElementById("lista").innerHTML;

    lista = lista +"<br><li class=\"list-group-item\">" + ing + "</li><br>";

    document.getElementById("lista").innerHTML = lista;
}

function soma(){
    var campo1 = parseInt(document.getElementById("campo1").value);
    var campo2 = parseInt(document.getElementById("campo2").value);

    soma = campo1 + campo2;
    alert(soma);
}
