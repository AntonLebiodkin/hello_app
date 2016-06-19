$('.name-submit').click(function(){
    var name = $('#usr').val();
    $.get('set_name', {'name': name}, function(res){
        $('.result').text(res);
    })
});
