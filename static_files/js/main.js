setTimeout(function() {
    $('#message').fadeOut(0, 'slow');
}, 3000);

$(function (){
    $('#btn-change-avatar').click(() => {
        $('#btn-change-avatar').slideUp(1000);
        $('#upload-avatar').slideDown(1000);
    });
});