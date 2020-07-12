function TWSHprocess(inc)
{
	notajax = false;
	window.location.hash = inc.toString().replace('index2.php?', '', 'gi');
	checkAnchor();
	return false;
}
notajax = false;
var currentAnchor = null;
function checkAnchor() {
	if (currentAnchor == null && document.location.search.replace('?', '', 'gi') == document.location.hash.replace('#', '', 'gi')) {
		currentAnchor = document.location.hash;
	}
	if (!notajax && currentAnchor != document.location.hash && currentAnchor != '#top' && currentAnchor != '#TOP' && (document.location.hash.toString() != '' || currentAnchor != null)) {
		jQuery("#ajaxloader").show();
		currentAnchor = document.location.hash;
		if (document.location.hash.toString() == '') {
			query = document.location.search.replace('?', '', 'gi');
		} else {
			var splits = currentAnchor.substring(1).split('&');
			var params = splits.join('&');
			var query = params;
		}
		//Send the petition
		jQuery.get("index2.php", query, function (data) {
			data = data.toString().replace('parseek', '');
			data = data.toString().replace('document.write', '');
			data = data.toString().replace('document.navigate', '');
			jQuery("#ajaxcontent").html(data);
			jQuery('html, body').animate({scrollTop: 0}, 800);
			jQuery('#ajaxloader').fadeOut(400);
			//document.title = 'ای ژاکسیزیشن';
		});
	}
}
(function ($) {
	jQuery(document).ready(function () {
		setInterval("checkAnchor()", 1000);
	});

///////////////////////// jquery ajax /////////////////////////

	function jcback(id, data, idloading)
	{
		jQuery("#" + id).html(data);
		jQuery('#ajaxloader').fadeOut(400);
	}
	function doajaxjquery(url, query, callback, reqtype, dataType, pageElement, idloading, htmlloading)
	{
		//jQuery("#"+idloading).html(htmlloading);
		jQuery.ajax({
			type: reqtype,
			url: url,
			data: query,
			dataType: dataType,
			error: function () {
				alert('Error loading document');
			},
			success: function (data) {
				eval(callback + '(pageElement,data,idloading)');
				// alert(data);
			}
		});
	}


	function ajaxjquery(pageElement, url, query)
	{
		doajaxjquery(url, query, 'jcback', 'post', 'html', pageElement, '', '');
	}

/////////////////////// page load- AHAHLIB
	function evalScript(scripts)
	{
		try

		{
			if (scripts != '')

			{
				var script = "";
				scripts = scripts.replace(/<script[^>]*>([\s\S]*?)<\/script>/gi, function () {
					if (scripts !== null)
						script += arguments[1] + '\n';
					return '';
				});
				if (script)
					(window.execScript) ? window.execScript(script) : window.setTimeout(script, 0);
			}
			return false;
		} catch (e)
		{
			alert(e)
		}
	}

	function cback(id, text) {
		jQuery('#ajaxloader').fadeOut(400);
		document.getElementById(id).innerHTML = text;
		evalScript(text);
	}
	function send(id, url, query)
	{
		jQuery("#ajaxloader").show();
		ajaxjquery(id, url, query);
// doAjax(url,query,'cback','post','0',id);
	}

})(jQuery);