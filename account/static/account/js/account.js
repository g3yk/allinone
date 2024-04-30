
function reveal_password()
{
    if(document.getElementById('show').checked){
        document.getElementById("id_password1").type='text'
    }
    else{
        document.getElementById("id_password1").type='password';
    }
}
function reveal_confirm()
{
    if(document.getElementById('show2').checked){
        document.getElementById("id_password2").type='text'
    }
    else{
        document.getElementById("id_password2").type='password';
    }
}