$(document).ready(function(){
var time=setTimeout("$('#slider-tab>button:first').click();",10);
$('#slider-tab>button').click(function(){
	window.clearTimeout(time);
	$('.slider-image').removeClass('active');
	$(this).addClass('active');
	$('#slider>h1').text($(this).attr('heading'));
	$('#slider').css({'background-image':'url("'+$(this).attr('imag')+'")'});
	time=setTimeout("$('#next').click();",2000);
});
	$('#next').click(function(){
	tag=$('.active').next();
		if($('.active').attr('class') == $('#slider-tab>button:last').attr('class')){
			tag=$('#slider-tab>button:first');
		}
		$(tag).click();
	});
	$('#prev').click(function(){
	tag=$('.active').prev();
		if($('.active').attr('class') == $('#slider-tab>button:first').attr('class')){
			tag=$('#slider-tab>button:last');
		}
		$(tag).click();
	});
});