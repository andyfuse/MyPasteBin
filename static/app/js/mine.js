$(function() {
	$("#Del").click(function(){
		$("#onDelete").submit();
	});
	$(".LangIco").click(function(){
		$(this).parent().submit();
	});
    $("#Change").click(function(){
        $("#onChange").submit();
    });
	timer();
});
function redirect(){
    window.location.href = "/"; 
}
function timer() {
    var interval = setInterval(function() {
        var sec_str = $('#seconds').text(),
            sec_int = parseInt(sec_str, 10);              
        sec_int--;
        $('#seconds').text(sec_int);
        if (sec_int == 0) {
            redirect();
            clearInterval(interval);
        }
    }, 1000);
}