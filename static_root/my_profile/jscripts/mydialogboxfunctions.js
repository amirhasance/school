jQuery.fn.center2 = function (top,left,bottom,right) {
	var centerX, centerY;
	if(self.innerHeight){
		centerX = self.innerWidth;
		centerY = self.innerHeight;
	}else if(document.documentElement && document.documentElement.clientHeight){
		centerX = document.documentElement.clientWidth;
		centerY = document.documentElement.clientHeight;
	}else if(document.body){
		centerX = document.body.clientWidth;
		centerY = document.body.clientHeight;
	}
	if(!top && !bottom)
		this.css('top', Math.max(20, (centerY - jQuery(this).outerHeight()) / 2 + jQuery(window).scrollTop())+"px");
	else if(top)
		this.css("top", top);
	else
		this.css("bottom", bottom);
	if(!left && !right)
		this.css('left', Math.max(0, (centerX - jQuery(this).outerWidth()) / 2 + jQuery(window).scrollLeft()) + "px");
	else if(left)
		this.css("left", left);
	else
		this.css("right", right);
	return this;
}

jQuery.fn.center = function () {
    this.css("position","absolute");
    this.css("top", Math.max(0, (($(window).height() - $(this).outerHeight()) / 2) + 
                                                $(window).scrollTop()) + "px");
    this.css("left", Math.max(0, (($(window).width() - $(this).outerWidth()) / 2) + 
                                                $(window).scrollLeft()) + "px");
    return this;
}

jQuery.fn.movable = function () {//MAKE DIALOGBOX MOVABLE ...
	var MDBYdifference,MDBXdifference,MDBmove = false;
	function startMove() {
		jQuery('.movable').mousemove(function(event) {
			if(MDBmove){
				var thisX = event.pageX - MDBXdifference,
				thisY = event.pageY - MDBYdifference;
				jQuery('.movable').offset({
					left: thisX,
					top: thisY
				});
			}
		});
	}
	
	jQuery(document).ready(function() {
		//jQuery('#mydialogbox div#header').live('mouseout',function(){
			//MDBmove = false
		//});
		jQuery("#mydialogbox #title").on('mousedown',function(e) {
			jQuery('#mydialogbox').addClass('movable');
			var parentOffset = jQuery('#mydialogbox').offset();
			MDBYdifference = e.pageY - parentOffset.top;
			MDBXdifference = e.pageX - parentOffset.left;
			MDBmove = true;
			startMove();
		}).on('mouseup',function() {
			jQuery('#mydialogbox').removeClass('movable');
		});
	});
}

function myDialogBoxOpen(title, content, speed, locationid, options){
	jQuery('#mydialogbox,#overaly-back').remove();
	if(speed == ''){speed = 400;}
	var defaults = {//DEFAULT OPTIONS ...
		width: false,height: false,padding: false,top: false,bottom: false,left: false,right: false,autoclose: true,positionType: 'absolute',movable:true,usealererter:true,reloadOnClose:false
	}
	options = jQuery.extend(defaults, options);
	if(options.usealererter){alererter(4,'لطفا  منتظر بمانید ...  <img src="appssch/lms/images/loading.gif" />');}
	var dialogFrame = '<div id="mydialogbox"><div title="بستن پنجره(Close: Esc)" id="closemydialogbox">×</div><span id="title"></span><div id="mydialogcontent">شکیبا باشید. صفحه در حال بارگذاری ...</div></div><div id="overaly-back"></div>';
	if(!locationid){
		jQuery('body').prepend(dialogFrame);
	}else{
		jQuery('#'+locationid).html(dialogFrame);
	}
	if(options.width){jQuery('#mydialogbox #mydialogcontent').width(options.width);}
	if(options.height){jQuery('#mydialogbox #mydialogcontent').height(options.height);}
	if(options.padding){jQuery('#mydialogbox #mydialogcontent').css('padding',options.padding);}
	jQuery('#mydialogbox #mydialogcontent').html(content);
	if(title){jQuery('#mydialogbox #title').html(title);}
	jQuery('#overaly-back').fadeIn('fast', function(){
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
		jQuery('#mydialogbox').fadeIn(speed,function(){
			jQuery('#mydialogbox #mydialogcontent').slideDown(speed,function(){
				if(options.usealererter){jQuery('#messagealerter').hide();}
			});
//			if(options.movable){jQuery('#mydialogbox').movable();}
		});
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
//		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
	});
	if(options.positionType != 'absolute'){jQuery('#mydialogbox').css('position', options.positionType);}
	var cbco = '';
	if(options.autoclose){
		jQuery(document).keypress(function(e){
			if(e.keyCode==27 && jQuery('#mydialogbox').is(':visible')){ 
				myDialogBoxClose(300);
				if(options.reloadOnClose){location.reload();}
			}
		});
		cbco = ',#overaly-back';
	}
	jQuery('div#closemydialogbox'+cbco).on('click',function(){myDialogBoxClose(300);if(options.reloadOnClose){location.reload();}});
	jQuery(window).resize(function(){
		jQuery('#mydialogbox').center(options.top,options.left,options.bottom,options.right);
	});
}

function myDialogBoxClose(speed){
	if(speed == ''){speed = 400;}
	jQuery('#mydialogbox div#mydialogcontent').slideUp(speed, function(){
		jQuery('#mydialogbox #mydialogcontent').html('شکیبا باشید. صفحه در حال بارگذاری ...');
		jQuery('#mydialogbox').hide(speed, function(){
			jQuery('#overaly-back').fadeOut(speed);
		});
	});
	jQuery('#mydialogbox,#overaly-back').remove();
}