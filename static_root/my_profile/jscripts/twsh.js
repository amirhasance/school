(function ($) {
	$(document).ready(function () {
		$('body').on('change', '.branches', function () {
			$(this).next('select').find('option').show();
			if ($(this).val() > 0) {
				$(this).next('select').find('option[data-branch!=' + $(this).val() + ']').hide();
			}
			$(this).next('select').find('option[data-branch=' + $(this).val() + ']:eq(0)').attr('selected', 'selected');
		});
		$('body').on('focus', 'input[type="text"],input[type="number"]', function () {
			$(this).select();
		});
		$('body').on('keyup', '[type="number"]', function () {
			var max = parseFloat($(this).attr('max'));
			if ($(this).val() > max) {
				$(this).val(max);
			}
		});
		$('body').on('click', '.close', function () {
			$(this).parent('div').slideUp();
		});
		$('body').on('keyup', 'span.dateinputs [name$="[d]"],span.dateinputs [name$="[m]"],span.dateinputs [name$="[y]"]', function (e) {
			var value = $(this).val().replace(/[^0-9]/g, '');
			var type = $(this).attr('name').substr($(this).attr('name').length - 3, 3);
			switch (type) {
				case '[d]':
					if (value.length > 1) {
						if (value > 31) {
							showTooltip($(this), 'روز باید عددی بین 1 تا 31 باشد', 2000);
							value = value.substr(0, 1);
						} else {
							if (value < 1) {
								value = '01';
							}
							//if(e.keyCode != 9){
							//	$(this).next('input:text').focus();
							//}
						}
					}
					value = value.substr(0, 2);
					break;
				case '[m]':
					if (value.length > 1) {
						if (value > 12) {
							showTooltip($(this), 'ماه باید عددی بین 1 تا 12 باشد', 2000);
							value = value.substr(0, 1);
						} else {
							if (value < 1) {
								value = '01';
							}
							//if(e.keyCode != 9){
							//	$(this).next('input:text').focus();
							//}
						}
					}
					value = value.substr(0, 2);
					break;
				case '[y]':
					value = value.substr(0, 4);
					break;
			}
			$(this).val(value);
		});
		$('body').on('blur', 'span.dateinputs [name$="[d]"],span.dateinputs [name$="[m]"],span.dateinputs [name$="[y]"]', function () {
			var value = $(this).val().replace(/[^0-9]/g, '');
			var type = $(this).attr('name').substr($(this).attr('name').length - 3, 3);
			switch (type) {
				case '[d]':
					if (value < 10 && value > 0 && value.length == 1) {
						value = '0' + value;
					}
					break;
				case '[m]':
					if (value < 10 && value > 0 && value.length == 1) {
						value = '0' + value;
					}
					break;
				case '[y]':
					var lngth = value.length;
					switch (lngth) {
						case 1:
							value = '139' + value;
							break;
						case 2:
							value = '13' + value;
							break;
						case 3:
							value = '1' + value;
							break;
					}
					break;
			}
			$(this).val(value);
		});
		$('body').on('click', '#poiallselect', function () {
			if ($(this).hasClass('selected')) {
				$(this).parent().find('option').removeAttr('selected');
				$(this).removeClass('selected');
			} else {
				$(this).addClass('selected');
				$(this).parent().find('option').attr('selected', 'selected');
				$(this).parent().scrollTop(0);
			}

		});
		$("#headselect").toggle(
			function () {
				$('input[type="checkbox"]').attr("checked", "checked");
			},
			function () {
				$('input[type="checkbox"]').removeAttr("checked");
			}
		);
		$('img[title]').each(function () {
			$this = $(this);
			$.data(this, 'title', $this.attr('title'))
		});
		$("img").mouseover(function () {
			var titletext = this.title.toString();
			if (titletext.length > 0) {
				showTooltip(this, titletext, 0);
				$(this).attr("title", "");
			}
		}).mouseout(function () {
			$("#tooltip").hide();
			$(this).attr("title", $.data(this, 'title'));
		});
		////////////////// tab ////////////////////////////
		//$('select[multiple]:not(.multi,.single)').prepend('<option id="poiallselect" value="">همه</option>');


		//CHANGE TICKS ...
		window.onload = function () {
			// Listen to the double click event.
			if (window.addEventListener)
				document.body.addEventListener('dblclick', onDoubleClick, false);
			else if (window.attachEvent)
				document.body.attachEvent('ondblclick', onDoubleClick);

		};

		function onDoubleClick(ev) {
			// Get the element which fired the event. This is not necessarily the
			// element to which the event has been attached.
			var element = ev.target || ev.srcElement;

			// Find out the div that holds this element.
			var name;

			do {
				element = element.parentNode;
			} while (element && (name = element.nodeName.toLowerCase()) &&
				(name != 'div' || element.className.indexOf('editable') == -1) && name != 'body');

			if (name == 'div' && element.className.indexOf('editable') != -1)
				replaceDiv(element);
		}

		var editor;

		function replaceDiv(div) {
			if (editor)
				editor.destroy();

			editor = CKEDITOR.replace(div);
		}
		poiuisetup();
		$('body').on('click', ".poiloadpdfviewer", function () {
			var html = '<iframe style="float:right; width: 100%; height: 100%; min-height: 500px;" src="' + poisiteurl + 'jscripts/pdf/#' + $(this).attr('src') + '" allowfullscreen webkitallowfullscreen></iframe><br/>';
			$(this).replaceWith(html);
		});
	});
	$(document).ajaxComplete(function () {
		poiuisetup();
	});
	$('form').on('focus', 'input[type=tel]', function (e) {
		$(this).on('wheel.disableScroll', function (e) {
			e.preventDefault();
		});
	});
	$('form').on('blur', 'input[type=tel]', function (e) {
		$(this).off('wheel.disableScroll');
	});
	$('.poiaccordion').accordion();
	$('.poitabs').tabs();
})(jQuery);

function poiuisetup() {
	if (jQuery('.timepicker').length > 0) {
		jQuery('.timepicker').mdtimepicker();
	}
	jQuery('.tooltip,#tooltip').hide();
	addpdfviewer();
	jQuery('<div class="ioswitch"><div class="inner"></div></div>').insertBefore("input[type=checkbox][name!='select[]'][class!='simple'][data-poiswitch!=done]:not([onclick]):not(:checked)");
	jQuery('<div class="ioswitch checked"><div class="inner"></div></div>').insertBefore("input[type=checkbox][name!='select[]'][class!='simple'][data-poiswitch!=done]:not([onclick]):checked");
	jQuery("input[type=checkbox][name!='select[]']").attr('data-poiswitch', 'done');
	jQuery('input[type=checkbox]').change(function () {
		jQuery('input[type=checkbox]').each(function () {
			if (jQuery(this).is(':checked') && !jQuery(this).prev('.ioswitch').hasClass('checked')) {
				jQuery(this).prev('.ioswitch').addClass('checked');
			} else if (!jQuery(this).is(':checked')) {
				jQuery(this).prev('.ioswitch').removeClass('checked');
			}
		});
	});
	jQuery.tabs = function (selector, start) {
		jQuery(selector).each(function (i, element) {
			if (jQuery(this).attr('tab') != undefined) {
				jQuery(element).click(function () {
					if (jQuery(this).attr('class') != 'selected') {
						jQuery(selector).each(function (i, element) {
							jQuery(jQuery(element).attr('tab')).slideUp();
							jQuery(element).removeClass('selected');
						});
						jQuery(jQuery(this).attr('tab')).slideDown();
						jQuery(this).addClass('selected');
					}
				});
			}
		});
		jQuery(selector + '[tab=\'' + start + '\']').trigger('click');
	};
	jQuery.tabs('.tabs a[tab]');
}

function addpdfviewer() {
	if (poigetget('app') != '') {
		jQuery('a[href$=".pdf"]').each(function () {
			if (!jQuery(this).hasClass('poiviewerloaded') && jQuery(this).attr('href').indexOf(poisiteurl) === 0) {
				jQuery(this).addClass('poiviewerloaded');
				var html = '<button class="poiloadpdfviewer" src="' + jQuery(this).attr('href') + '" >نمایش PDF</button><br/>';
				jQuery(html).insertBefore(this);
			}
		});
	}
}

function alererter(result, message, notfade) {
	if (notfade === false || notfade === null || notfade === undefined || notfade === 'undefined') {
		notfade = '';
	}
	if (result != 5) {
		if (result == 1 || result == 'success')
			var messageshow = '<div class="alert_success"> ' + message + '</div>';
		else if (result == 0 || result == 'error')
			var messageshow = '<div class="alert_error"></span> ' + message + '</div>';
		else if (result == 2 || result == 'info')
			var messageshow = '<div class="alert_info">' + message + '</div>';
		else if (result == 4 || result == 'loading')
			var messageshow = '<div class="alert_loading">' + message + '</div>';
		jQuery("#messagealerter").html(messageshow);
		jQuery('#messagealerter').css("display", "block");
		if (notfade == '') {
			jQuery('#messagealerter').fadeTo(100, 0);
			jQuery('#messagealerter').fadeTo(100, 1);
			jQuery('#messagealerter').fadeTo(100, 0);
			jQuery('#messagealerter').fadeTo(100, 1);
			jQuery('#messagealerter').fadeOut(20000);
		}
	} else {
		jQuery('#messagealerter').css("display", "none");
	}
}

function poidump(obj) {
	var out = '';
	for (var i in obj) {
		out += i + ": " + obj[i] + "\n";
		for (var i2 in obj[i]) {
			out += "|_ " + i2 + ": " + obj[i][i2] + "\n";

		}
	}

	alert(out);
	var pre = document.createElement('pre');
	pre.innerHTML = out;
	document.body.appendChild(pre)
}

function Move(seccio) {
	jQuery(seccio).each(function () {
		var posY = jQuery(window).scrollTop() - jQuery(this).attr('yPos');
		//if(posY < 81 && posY > -180){
		jQuery(this).css('background-position', 'center ' + ((posY / 1.7)) + 'px');
		//}
	});
}
function showTooltip(object, content, displaytime) {
	jQuery("#tooltip").text(content).css({'width': 'auto', 'height': 'auto'});
	var pos = jQuery(object).offset();
	var tooltipwidth = jQuery("#tooltip").outerWidth();
	var thiswidth = jQuery(object).outerWidth();
	if (pos.left < tooltipwidth + thiswidth / 2) {
		pos.left = tooltipwidth + thiswidth;
	}
	jQuery("#tooltip").css({
		"top": (pos.top - jQuery("#tooltip").outerHeight()),
		"left": (pos.left - tooltipwidth + thiswidth / 4)
	});
	jQuery("#tooltip").fadeTo("fast", 0.9).show();
	if (displaytime > 0) {
		setTimeout(function () {
			jQuery("#tooltip").hide()
		}, displaytime);
	}
}

function imginputpreview(input, selector) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();
		reader.onload = function (e) {
			jQuery(selector).attr('src', e.target.result);
		}
		reader.readAsDataURL(input.files[0]);
	}
}

function poigetget(name) {
	name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
	var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
		results = regex.exec(location.search);
	return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function trim(str) {
	return str.replace(/^\s+|\s+$/g, "");
}

function eteraz(stdid, classid, divid)
{
	var comment = jQuery('#comment').val();
	var lessen = jQuery('#stdlessen').val();
	var url = "";
	var query = "stdid=" + stdid + "&classid=" + classid + "&lessen=" + lessen + "&comment=" + comment;
	url = "appssch/workbook/eteraz.php";
	send(divid, url, query)
}

function numberCheck(e) {
	return !(e.which != 8 && e.which != 0 && e.which != 46 && e.which != 45 && (e.which < 48 || e.which > 57) && (e.keyCode != 65 && e.ctrlKey !== true));
}

function correct_number_format(n, decPlaces, thouSeparator, decSeparator) {
	if (n == '-') {
		return n;
	} else {
		var decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 0 : decPlaces,
			decSeparator = decSeparator == undefined ? "." : decSeparator,
			thouSeparator = thouSeparator == undefined ? "," : thouSeparator,
			sign = n < 0 ? "-" : "",
			i = parseInt(n = Math.abs(+n || 0).toFixed(decPlaces)) + "",
			j = (j = i.length) > 3 ? j % 3 : 0;
		return sign + (j ? i.substr(0, j) + thouSeparator : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thouSeparator) + (decPlaces ? decSeparator + Math.abs(n - i).toFixed(decPlaces).slice(2) : "");
	}
}

function number_format(elem) {
	var number = jQuery(elem).val(), minus = '', afterPoint = '';
	if (number.indexOf('-') !== -1) {
		minus = '-';
		number = number.replace(/\-/g, '');
	}
	var dotPos = number.indexOf('.');
	if (dotPos > 0) {
		afterPoint = '.' + number.substring(dotPos).replace(/[^0-9]/g, '');
		number = number.substring(0, dotPos);
	}
	jQuery(elem).css('direction', 'ltr').val(minus + number.replace(/[^0-9]/g, '').replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + afterPoint);
}

function isemail(emailAddress) {
	var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
	return pattern.test(emailAddress);
}

function isurl(textval) {
	var urlregex = new RegExp("^(http:\/\/www.|https:\/\/www.|ftp:\/\/www.|www.){1}([0-9A-Za-z]+\.)");
	return urlregex.test(textval);
}

function isnumeric(str) {
	var RE = /^-{0,1}\d*\.{0,1}\d+$/;
	return (RE.test(str));
}

function changestate(state) {
	var url = "appscms/forms/selectcity.php";
	var options = '<option value="0">در حال بارگذاری...</option>';
	jQuery("#city" + jQuery(state).attr('id')).html(options);
	options = '';
	jQuery.get(url, {
		state: jQuery(state).val(),
		ajax: 'true'
	}, function (data) {
		var j = data.split("\n");
		for (var i = 0; i < (j.length - 1); i++) {
			options += '<option value="' + j[i] + '">' + j[i] + '</option>';
		}
		jQuery("#city" + jQuery(state).attr('id')).html(options);
	});
}

function g2j(gy, gm, gd) {
	g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
	jy = (gy <= 1600) ? 0 : 979;
	gy -= (gy <= 1600) ? 621 : 1600;
	gy2 = (gm > 2) ? (gy + 1) : gy;
	days = (365 * gy) + (parseInt((gy2 + 3) / 4)) - (parseInt((gy2 + 99) / 100))
		+ (parseInt((gy2 + 399) / 400)) - 80 + gd + g_d_m[gm - 1];
	jy += 33 * (parseInt(days / 12053));
	days %= 12053;
	jy += 4 * (parseInt(days / 1461));
	days %= 1461;
	jy += parseInt((days - 1) / 365);
	if (days > 365)
		days = (days - 1) % 365;
	jm = (days < 186) ? 1 + parseInt(days / 31) : 7 + parseInt((days - 186) / 30);
	jd = 1 + ((days < 186) ? (days % 31) : ((days - 186) % 30));
	return [jy, jm, jd];
}

function j2g(jy, jm, jd) {
	gy = (jy <= 979) ? 621 : 1600;
	jy -= (jy <= 979) ? 0 : 979;
	days = (365 * jy) + ((parseInt(jy / 33)) * 8) + (parseInt(((jy % 33) + 3) / 4))
		+ 78 + jd + ((jm < 7) ? (jm - 1) * 31 : ((jm - 7) * 30) + 186);
	gy += 400 * (parseInt(days / 146097));
	days %= 146097;
	if (days > 36524) {
		gy += 100 * (parseInt(--days / 36524));
		days %= 36524;
		if (days >= 365)
			days++;
	}
	gy += 4 * (parseInt((days) / 1461));
	days %= 1461;
	gy += parseInt((days - 1) / 365);
	if (days > 365)
		days = (days - 1) % 365;
	gd = days + 1;
	sal_a = [0, 31, ((gy % 4 == 0 && gy % 100 != 0) || (gy % 400 == 0)) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	for (gm = 0; gm < 13; gm++) {
		v = sal_a[gm];
		if (gd <= v)
			break;
		gd -= v;
	}
	return [gy, gm, gd];
}

jQuery.fn.print = function () {
	// NOTE: We are trimming the jQuery collection down to the
	// first element in the collection.
	if (this.size() > 1) {
		this.eq(0).print();
		return;
	} else if (!this.size()) {
		return;
	}

	// ASSERT: At this point, we know that the current jQuery
	// collection (as defined by THIS), contains only one
	// printable element.

	// Create a random name for the print frame.
	var strFrameName = ("printer-" + (new Date()).getTime());

	// Create an iFrame with the new name.
	var jFrame = jQuery("<iframe name='" + strFrameName + "'>");

	// Hide the frame (sort of) and attach to the body.
	jFrame
		.css("width", "1px")
		.css("height", "1px")
		.css("position", "absolute")
		.css("left", "-9999px")
		.appendTo(jQuery("body:first"))
		;

	// Get a FRAMES reference to the new frame.
	var objFrame = window.frames[ strFrameName ];

	// Get a reference to the DOM in the new frame.
	var objDoc = objFrame.document;

	// Grab all the style tags and copy to the new
	// document so that we capture look and feel of
	// the current document.

	// Create a temp document DIV to hold the style tags.
	// This is the only way I could find to get the style
	// tags into IE.
	var jStyleDiv = jQuery("<div>").append(
		jQuery("style").clone()
		);
	// Write the HTML for the document. In this, we will
	// write out the HTML of the current element.
	objDoc.open();
	objDoc.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">");
	objDoc.write("<html dir=rtl>");
	objDoc.write("<body><link rel=\"stylesheet\" href=\"jscripts/twshprint.css\" type=\"text/css\" media=\"screen\" charset=\"utf-8\" />");
	objDoc.write("<head>");
	objDoc.write("<title>");
	objDoc.write(document.title);
	objDoc.write("</title>");
	objDoc.write(jStyleDiv.html());
	objDoc.write("</head>");
	objDoc.write(this.html());
	objDoc.write("</body>");
	objDoc.write("</html>");
	objDoc.close();

	// Print the document.
	objFrame.focus();
	objFrame.print();

	// Have the frame remove itself in about a minute so that
	// we don't build up too many of these frames.
	setTimeout(
		function () {
			jFrame.remove();
		},
		(60 * 1000)
		);
};

function mytest(col) {
	var nomre = jQuery('#n' + col).val();
	if (jQuery.trim(nomre) != '') {
		jQuery('#nomrat tr').each(function () {
			if (this.rowIndex > 1) {
				jQuery(this).find('td').eq(col).find('input').val(nomre);
			}
		});
	}
}

function displayunicode(event, cur, nrow) {
	if (event.keyCode == 38) { // up
		var pre = cur - 1;
		var mytext = document.getElementById(pre);
		mytext.focus();
		mytext.select();
		return false;
	} else if (event.keyCode == 40 || event.keyCode == 13) { //down
		var next = cur + 1;
		var mytext = document.getElementById(next);
		mytext.focus();
		mytext.select();
		return false;
	} else if (event.keyCode == 37) { //left
		var next = cur + nrow;
		var mytext = document.getElementById(next);
		mytext.focus();
		mytext.select();
		return false;
	} else if (event.keyCode == 39) { //right
		var next = cur - nrow;
		var mytext = document.getElementById(next);
		mytext.focus();
		mytext.select();
		return false;
	}
	if (event.keyCode == 13) {
		return false;
	}
}

window.alert = function (message) {
	swal(message)
};

function checkMelliCode(meli_code) {
	if (meli_code.length == 10) {
		if (meli_code == '1111111111' ||
			meli_code == '0000000000' ||
			meli_code == '2222222222' ||
			meli_code == '3333333333' ||
			meli_code == '4444444444' ||
			meli_code == '5555555555' ||
			meli_code == '6666666666' ||
			meli_code == '7777777777' ||
			meli_code == '8888888888' ||
			meli_code == '9999999999') {
			return false;
		}
		c = parseInt(meli_code.charAt(9));
		n = parseInt(meli_code.charAt(0)) * 10 +
			parseInt(meli_code.charAt(1)) * 9 +
			parseInt(meli_code.charAt(2)) * 8 +
			parseInt(meli_code.charAt(3)) * 7 +
			parseInt(meli_code.charAt(4)) * 6 +
			parseInt(meli_code.charAt(5)) * 5 +
			parseInt(meli_code.charAt(6)) * 4 +
			parseInt(meli_code.charAt(7)) * 3 +
			parseInt(meli_code.charAt(8)) * 2;
		r = n - parseInt(n / 11) * 11;
		if ((r == 0 && r == c) || (r == 1 && c == 1) || (r > 1 && c == 11 - r)) {
			return true;
		} else {
			return false;
		}
	} else {
		return false;
	}
}