function removetinymce() {
	//jQuery('.ckeditor').each(function() {
	//	var id = jQuery(this).attr('id');
	//	tinyMCE.execCommand('mceRemoveControl', false, id);
	//})
}

function removetinymcebyid(id) {
	//tinyMCE.execCommand('mceRemoveControl', false, id);
}

function returnpage(id, url) {
	removetinymce();
	url += '&header=no';
	send(id, url);
	return false;
}

function divvote(id, data, idloading) {
	var vote = "";
	var result = "";
	var countvote = "";
	var lastvote = "";
	var insert = "";
	var idvote = "";
	var taid = "";
	jQuery("resultvote", data).each(function () {
		vote = jQuery("vote", this).text();
		result = jQuery("result", this).text();
		countvote = jQuery("countvote", this).text();
		insert = jQuery("insert", this).text();
		lastvote = jQuery("lastvote", this).text();
		idvote = jQuery("idvote", this).text();
		taid = jQuery("taid", this).text();
	});
	if (insert) {
		if (taid == '0') {
			var intvotet = lastvote - 0;
			intvotet++;
			var str = '<DIV class="votename"><a href="?app=lms&view=stud/comments&type=dore&id=' + idvote + '" >' + vote + '</a></DIV>';
			if (intvotet == 1)
				jQuery('<div class="nazarat" id="vote' + intvotet + '">').appendTo('#votes');
			else
				jQuery('<div class="nazarat" id="vote' + intvotet + '">').insertBefore('#vote' + lastvote);
			jQuery("#vote" + intvotet).html(str);
			jQuery("#tn").html(countvote);
			jQuery("#lastvote").val(intvotet);
		}
	}
	alererter(insert, result);
	jQuery("#vote").val('');
	document.getElementById('privatevote').checked = false;
	jQuery("#" + id).html(result);
}

function divcomment(id, data, idloading) {
	var idcomment = "";
	var result = "";
	var insert = "";
	var show = "";
	jQuery("resultvote", data).each(function () {
		idcomment = jQuery("idcomment", this).text();
		insert = jQuery("insert", this).text();
		show = jQuery("show", this).text();
	});
	if (insert) {
		showPage(idcomment, show, 1, 0);
		jQuery("#content").val('');
	}
	jQuery("#" + id).html(result);

}

function insertquote(id, data, idloading) {
	var idcomment = "";
	var result = "";
	var insert = "";
	var show = "";
	jQuery("resultvote", data).each(function () {
		idcomment = jQuery("idcomment", this).text();
		insert = jQuery("insert", this).text();
		show = jQuery("show", this).text();
	});
	if (insert) {
		showPage(idcomment, show, 1, 0);
		jQuery("#quetcontent").val('');
		jQuery("#divquet").hide();
	}
	jQuery("#" + id).html(result);
}

function replaycomment(id, data, idloading) {
	var idcomment = "";
	var vote = "";
	var result = "";
	var message = "";
	var idpasokh = "";
	jQuery("resultdata", data).each(function () {
		idcomment = jQuery("idcomment", this).text();
		idpasokh = jQuery("idpasokh", this).text();
		vote = jQuery("vote", this).text();
		result = jQuery("result", this).text();
		message = jQuery("message", this).text();
	});
	if (result) {
		jQuery('<div id="pt' + idpasokh + '">').appendTo("#pasokh" + idcomment);
		jQuery("#pt" + idpasokh).html(vote);
		alererter(1, message);
	} else {
		alererter(0, message);
	}
}

function delcom(id, data, idloading) {
	// jQuery("#pe"+data).html('ff');
	var iddiv = "pe" + data;
	document.getElementById(iddiv).innerHTML = '';
}

function jcback(id, data, idloading) {
	if (id != '') {
		alererter(5, '');
		jQuery("#" + id).html(data);
	} else {
		alererter(1, data);
	}
}

function jcbacknoloading(id, data, idloading) {
	jQuery("#" + id).html(data);
}

function doajaxjquery(url, query, callback, reqtype, dataType, pageElement, idloading, htmlloading) {
	jQuery.ajax({
		type: reqtype,
		url: url,
		data: query,
		dataType: dataType,
		error: function (data, status, e) {
			//eval(callback + '(pageElement,data,idloading)');
			//$('body').html('<textarea>' + status + "\n" + data + "\n" + e + '</textarea>');
			alert('اطلاعات دریافت نشد. از اتصال به اینترنت اطمینان حاصل کنید');
		},
		success: function (data) {
			//alert(data);
			eval(callback + '(pageElement,data,idloading)');
		}
	});
}

////////////////////////////////////////////////////////////////////
function ajaxjquery(pageElement, url, query, type, cback) {
	alererter(4, 'لطفا منتظر بمانید ... <img src="appssch/lms/images/loading.gif" />');
	doajaxjquery(url, query, cback, 'post', type, pageElement, '', '');
}

function ajaxjquery2(pageElement, url, query, type, cback) {
	doajaxjquery(url, query, cback, 'post', type, pageElement, '', '');
}

function send(id, url, query) {
	alererter(4, 'لطفا منتظر بمانید ... <img src="appssch/lms/images/loading.gif" />');
	ajaxjquery2(id, url, query, 'html', 'jcback');
	return false;
}

function sendnoalert(id, url, query) {
	document.getElementById('').innerHTML = "<img src=\"appssch/lms/images/loading.gif\" />";
	ajaxjquery2(id, url, query, 'html', 'jcback');
	return false;
}

function sendnoloding(id, url, query) {
	ajaxjquery(id, url, query, 'html', 'jcbacknoloading');
	return false;
}

function sendxml(id, url, query) {
	ajaxjquery(id, url, query, 'xml', 'jcxmlback');
	return false;
}

function jcbackajax(id, data, idloading) {
	var message = "";
	var result = "";
	var content = "";
	var masir = "";
	var shtable = 0;
	jQuery("resultdata", data).each(function () {
		message = jQuery("message", this).text();
		result = jQuery("result", this).text();
		content = jQuery("content", this).text();
		if (jQuery("shtable", this))
			shtable = jQuery("shtable", this).text();
		if (jQuery("masir", this))
			masir = jQuery("masir", this).text();
	});
	if (result == 1 || result == 2)
		jQuery("#" + id).html(content);

	if (shtable == 1)
		jQuery("#masir").html(masir);

	alererter(result, message);
}

function jcbacknocontent(id, data, idloading) {
	var message = "";
	var result = "";
	jQuery("resultdata", data).each(function () {
		message = jQuery("message", this).text();
		result = jQuery("result", this).text();
	});
	alererter(result, message);
}

function sendajax(id, url, query) {
	ajaxjquery(id, url, query, 'xml', 'jcbackajax');
	return false;
}

function sendajaxnocontent(id, url, query) {
	ajaxjquery(id, url, query, 'xml', 'jcbacknocontent');
	return false;
}

function jcbackpage(id, data, idloading) {
	if (id != '')
	{
		alererter(5, '');
		jQuery("#" + id).html(data);

		var height = jQuery('.popup_container').height();
		if (height > 420)
		{
			jQuery("#" + id).css("overflow", "scroll");
			jQuery("#" + id).css('height', '420px');
		}


	} else {
		alererter(1, data);
	}
}

function sendpage(id, url, query) {
	alererter(4, 'لطفا منتظر بمانید ... <img src="appssch/lms/images/loading.gif" />');
	ajaxjquery2(id, url, query, 'html', 'jcbackpage');
	return false;
}

function showpage(id, address, query) {
	sendpage(id, address, query);
}

function closepage() {
	jQuery('#pageloader').css("display", "none");
	jQuery('.ui-dialog').remove();
}
///////////////////////////////////////////////////////////////