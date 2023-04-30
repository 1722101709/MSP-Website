window.addEventListener('DOMContentLoaded', count, false);
function count(){
    var eles = document.querySelectorAll('.question span');
    for(let i = 0; i < eles.length; i++){
        eles[i].innerHTML = (i+1) + '. ' + eles[i].innerHTML;
    }
}
