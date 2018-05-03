var main = function() { 
	var x = document.getElementById("text").value;
	console.log(x);
	document.getElementById("demo").innerHTML=x;
// https://developer.mozilla.org/en-US/docs/Web/API/FormData/get
};



$(document).ready(function(){
	Promise.all(['model.json','model.h5','porn_classifier.py'].map($.get)).then(main); 
})