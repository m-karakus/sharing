// https://github.com/googleworkspace/apps-script-oauth2  --> 1B7FSrk5Zi6L1rSxxTDgDEUsPzlukDsi4KGuTMorsTQHhGBzBkMun4iDF
var gaid = 'YOUR-GA-PROFILEID'
var json = {
    "private_key": "YOUR-PRIVATE-KEY",
    "client_email": "YOUR-CLIENT-EMAIL",
}
var query = {
    'ids': 'ga:' + gaid,
    'metrics': 'rt:pageviews',
    'dimensions': 'rt:pagePath',
    'filters': 'rt:pagePath!@second;rt:source=@google;rt:pagePath=@question,rt:pagePath=@article',
    'sort': '-rt:pageviews',
    'max-results': 10
}

function getOAuthService(user) {
    var service = OAuth2.createService('Service Account')
        .setTokenUrl('https://accounts.google.com/o/oauth2/token')
        .setPrivateKey(json.private_key)
        .setIssuer(json.client_email)
        .setSubject(json.client_email)
        .setPropertyStore(PropertiesService.getScriptProperties())
        .setParam('access_type', 'offline')
        .setScope(['https://www.googleapis.com/auth/analytics.readonly']);
    return service
};

function reset() {
    var service = getOAuthService();
    service.reset();
};

function myFunction(service_token) {

    var service = getOAuthService();
    var access_token = 'Bearer ' + service.getAccessToken()
    var url = "https://analytics.googleapis.com/analytics/v3/data/realtime";
    var params = {
        'method': 'GET',
        'muteHttpExceptions': true,
        'headers': { 'Authorization': access_token, 'Content-Type': 'application/json' },
    };
    var response = UrlFetchApp.fetch(url + '?' + generateQueryString(query), params);
    var json = response.getContentText();
    var data = JSON.parse(json);
    var rows = data.rows;
    console.log(rows)
    console.log("response")
    service.reset();

}

function generateQueryString(data) {
    const params = [];
    for (var d in data)
        params.push(encodeURIComponent(d) + '=' + encodeURIComponent(data[d]));
    return params.join('&');
}