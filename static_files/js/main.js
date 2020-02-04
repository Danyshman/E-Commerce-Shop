setTimeout(function() {
    $('#message').fadeOut(0, 'slow');
}, 3000);

$(function (){
    $('#btn-change-avatar').click(() => {
        $('#btn-change-avatar').slideUp(1000);
        $('#upload-avatar').slideDown(1000);
    });

    $(window).on('load', () => {
        const url = window.location.pathname;
        if(url === "/accounts/login/")
         $('#login-button').click();
    })
});