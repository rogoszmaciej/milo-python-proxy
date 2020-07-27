"use strict";

function modifyHeaders(details) {
    for (var i = 0; i < details.requestHeaders.length; ++i) {
        if (details.requestHeaders[i].name === 'User-Agent') {
            details.requestHeaders.splice(i, 1);
        }
    }
    const permissionDesc = {
        active: true,
        currentWindow: true
    }
    let tabId = 0;
    chrome.tabs.query(permissionDesc, function(tabArray){tabId=tabArray[0].id;}
    );
    const new_header = {"name": "Test", "value": `${tabId}`}
    details.requestHeaders.push(new_header);
    return {requestHeaders: details.requestHeaders};
}

chrome.webRequest.onBeforeSendHeaders.addListener(
    modifyHeaders,
    {urls: ["<all_urls>"]},
    ["blocking", "requestHeaders", "extraHeaders"]);
