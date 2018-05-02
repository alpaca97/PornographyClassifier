var main = function(classifier) { 



title = document.getElementById("title").value;
// https://developer.mozilla.org/en-US/docs/Web/API/FormData/get
};



$(document).ready(function(){
	Promise.all(['model.json','model.h5','porn_classifier.py'].map($.get)).then(main); 
})