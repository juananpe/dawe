var page = new WebPage();
//var url = 'http://jsfiddle.net/ancalotoru/tuya1dL9/';
// var url = 'http://jsfiddle.net/gw2tzt8t/1/'; // 1 sec

var url = "https://lab.pentestit.ru/pentestlabs/5"

//      xpath --> //*[@id="qunit-testresult"]/*/text()
//     [ passed, total, failed ]

function getElementByXpath(path) {
	var template = document.createElement("template");
	template.innerHTML = page.frameContent;
	// return document.evaluate(path, template, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

	var message = [];
	var xPathRes = document.evaluate ( path, template, null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null);

	var element = xPathRes.iterateNext ();
	while (element) {
		if (element.innerHTML != '')
                        message.push(element.innerHTML);
		element = xPathRes.iterateNext ()
	}

	return message;

}


page.open(url, function (status) {
		if ('success' !== status) {
		console.log("Error");
		} else {
		page.switchToFrame("result");
		setTimeout(function() {
				// console.log(page.frameContent);
				// console.log(page.frameContent);
				var result = getElementByXpath("//*[@class='jspPane']");
				console.log("Passed, total, failed: " + result);

				phantom.exit();
				},1000);
		}
		});
