var page = new WebPage();
var args = require('system').args;

var url = args[1];

// var url = 'http://jsfiddle.net/qv8Pd/'; // 1 sec


function getElementByXpath(path) {
	var template = document.createElement("template");
	template.innerHTML = page.frameContent;
	return document.evaluate(path, template, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}


page.open(url, function (status) {
		if ('success' !== status) {
		console.log("Error");
		} else {
		page.switchToFrame("result");
		setTimeout(function() {
				// console.log(page.frameContent);
				// console.log(page.frameContent);
				var result = getElementByXpath("//*[@id='target']");
				console.log("Fondo: " + result.style.backgroundColor);

				phantom.exit();
				},1000);
		}
		});
