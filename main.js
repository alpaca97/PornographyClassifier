var main = function(classifier) { # 

};



$(document).ready(function(){
	Promise.all(['ClassifierJSONfile', ].map($.get)).then(main); 
})