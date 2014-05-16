$.fn.serializeObject = function()
{
    
    var fromData = {};
    var toData = {};
    var letterData={};
    var dataTarget='toData';
    
    var a = this.serializeArray();
    var o={};
    o['fromData']=fromData;
    o['toData']=toData;
    o['letterData']=letterData;
    
    $.each(a, function() {
    	var value = this.name.split(".");
        var target=value[0];
        var key=value[1];
        
        
        if (o[target][key] !== undefined) {
            
            if (!o[target][key].push) {
                o[target][this.name] = [o[target][key]];
            }
            
            o[target][key].push(this.value || '');
        } else {
            o[target][key] = this.value || '';
        }
    });
    

    return o;
};



function fillForm(data) {
	var element = $('#Brief')[0];
	var key="";

	$.each(element, function() {
		var name=this.name.split('.');
		
		var type=name[0];
		var key=name[1];
		
		
		if ((this.type!=='submit')&&(type!== undefined) && (key in data[type])){
			this.value = data[type][key];
		}
		else{
		}

	});
}


function getVCards() {
	var element = $('#Brief')[0];
	var key="";

	$.each(element, function() {
		var name=this.name.split('.');
		
		var type=name[0];
		var key=name[1];
		
		
		if ((this.type!=='submit')&&(type!== undefined) && (key in data[type])){
			this.value = data[type][key];
		}
		else{
		}

	});
}



function sendTestData_old(data) {
    
        $.ajax({
   			 type: "POST",
    		 url: "/createLetter",
    		// The key needs to match your method's input parameter (case-sensitive).
		    data: JSON.stringify(data),
		    contentType: "application/json; charset=utf-8",
		    dataType: "json",
		    success: function(data){
		    	//$('#result').text(JSON.stringify($('form').serializeObject()));
		    	window.location="/download/"+data.filename;
		    	console.log('ok');
		    	//console.log(data);
		    	//return data;
		    	},
		    failure: function(errMsg) {
		        alert(errMsg);
		    }
		});
        //$('#result').text(JSON.stringify($('form').serializeObject()));
        return false;
    };

function sendTestData(data) {
	url="https://freya/createLetter";
	if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }else{// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("POST",url,false);
    xmlhttp.setRequestHeader("Content-type", "application/json; charset=utf-8");
    xmlhttp.setRequestHeader("Content-length", data.length);
    xmlhttp.setRequestHeader("Connection", "close");
	xmlhttp.send(JSON.stringify(data));
	console.log(xmlhttp.responseText);
    return xmlhttp.responseText;    
}


$(function() {
    $('form').submit(function() {
        $.ajax({
   			 type: "POST",
    		 url: "/createLetter",
    		// The key needs to match your method's input parameter (case-sensitive).
		    data: JSON.stringify($('form').serializeObject()),
		    contentType: "application/json; charset=utf-8",
		    dataType: "json",
		    success: function(data){
		    	//$('#result').text(JSON.stringify($('form').serializeObject()));
		    	window.location="/download/"+data.filename;
		    	console.log('ok');
		    	alert(data.filename);
		    	//console.log(data);
		    	//return data;
		    	},
		    failure: function(errMsg) {
		        alert(errMsg);
		    }
		});
        //$('#result').text(JSON.stringify($('form').serializeObject()));
        return false;
    });
});

