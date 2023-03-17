var scroll=0;
$(document).ready(function(){
	$(this).on({
	"scroll":function(e){
			if((scrollY)<scroll||(scrollY)<60){
				if($('#header').css('opacity')=='0'){
				$('#header').css('opacity','1');
				$(document).scrollTop(scrollY);
				}
			}else{
				if($('#header').css('opacity')!='0'){
				$('#header').css('opacity','0');
				$(document).scrollTop(scrollY);
			}
			}
			window.scroll=scrollY;
	}
	});
});

		
