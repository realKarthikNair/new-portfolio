const url = "https://dev.to/feed/ishubhamsingh2e";
const Http = new XMLHttpRequest();

Http.open("GET", url, false);
Http.send(null);

if (Http.status == 200) {
  xmlDoc = Http.responseXML;

  var title = xmlDoc.getElementsByTagName("title");
  var pubDate = xmlDoc.getElementsByTagName("pubDate");
  var link = xmlDoc.getElementsByTagName("link");

  for (let i = 2; i < title.length; i++) {
    var _title = title[i].childNodes[0].data;
    var _pubDate = pubDate[i].childNodes[0].data;
    var _link = link[i].childNodes[0].data;
    if (_title.length > 77) {
      _title = _title.replace(/(.{77})/g, "$1\n-");
    }
    var div = document.getElementById("article");
    div.innerHTML +=
      "<pre>\n# " +
      _title +
      "\n" +
      "Publish Date: " +
      _pubDate.slice(0, _pubDate.length - 6) +
      "\n"
      +
      `-> <a href=${_link}>https://dev.to/ishubhamsingh2e</a>` +
      "</pre>";
  }
} else if (xmlhttp.status == 404) {
  alert("XML could not be found");
}