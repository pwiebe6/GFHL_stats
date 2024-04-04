function sortTable(columnIndex) {
    const html_button = event.target.parentNode;
    const html_th = html_button.parentNode;
    const html_head = html_th.parentNode;
    const html_table = html_head.parentNode;
    const parentId = html_table.id;
    var table = document.getElementById(parentId);
    var rows = table.rows;
    var switching = true;

    while (switching) {
        switching = false;

        for (var i = 1; i < rows.length - 1; i++) {
            var shouldSwitch = false;
            var x = rows[i].getElementsByTagName("TD")[columnIndex];
            var y = rows[i + 1].getElementsByTagName("TD")[columnIndex];

            if (!isNaN(x.innerHTML)){
                if (Number(x.innerHTML) > Number(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
            else{
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function smartSort(columnIndex) {
    const html_button = event.target.parentNode;
    const html_th = html_button.parentNode;
    const html_head = html_th.parentNode;
    const html_table = html_head.parentNode;
    const parentId = html_table.id;
    var table = document.getElementById(parentId);
    var rows = table.rows;
    var switching = true;


//    html_th_innerHTML = html_th.innerHTML;
    
    console.log("I don't know");
    console.log(html_th);
    console.log(html_th.innerText);

    button_text = html_th.innerText;
    console.log("button_text");
    console.log(button_text);

    if (button_text.slice(-1 != "\u21e7")) {
        console.log("Noticed no up arrow. Could be a down arrow or no arrow.");
        html_th.innerText = button_text.replace("\u21e7", "").replace("\u21e9", "") + "\u21e7";
    }
    else {
        console.log("Noticed up arrow.");
        html_th.innerText = button_text.replace("\u21e7", "").replace("\u21e9", "") + "\u21e9";
    }



    // Check if the current button has an up or down arrow at the end of the text
    // If not an up arrow (ie, down arrow or no arrow) then clear all arrows, change this one to up arrow, reverse sort (ie, do largest -> smallest).
//    if (html_th_innerHTML.slice(-10,-9) != "\u21e7"){
//        console.log("Noticed no up arrow. Could be a down arrow or no arrow.");
//        
//        // clear ALL arrows - this works, it's just commented out because it seems to kill what comes later...
//    //    temp = html_head.innerHTML;
//    //    temp2 = temp.replace("\u21e7", "").replace("\u21e9", "");
//    //    console.log("header html");
//    //    console.log(temp);
//    //    console.log("header html after clearing arrows");
//    //    console.log(temp2);
//    //    html_head.innerHTML = temp2;
//    //    t3 = html_head.innerHTML;
//    //    console.log("re-check");
//    //    console.log(html_head.innerHTML);
//
//        html_th_innerHTML = html_th_innerHTML.replace("\u21e7", "").replace("\u21e9", "");
//        console.log("button text before arrow re-added");
//        console.log(html_th_innerHTML);
//        html_th_innerHTML = html_th_innerHTML.slice(0,-9) + "\u21e7</button>"
//        console.log("button text after arrow re-added");
//        console.log(html_th_innerHTML);
//        html_th.innerHTML = html_th_innerHTML;
//        b2 = html_th.innerHTML;
//        console.log("re-check");
//        console.log(b2);
//    }
//    // if up arrow, clear all arrows, change this to down arrow, regular sort (ie, do smallest -> largest).
//    else {
//        console.log("Noticed an up arrow.");
//        // clear ALL arrows
//        html_th_innerHTML.replace("\u21e7", "").replace("\u21e9", "");
//        html_th_innerHTML = html_th_innerHTML.slice(0,-10) + "\u21e9</button>"
//        console.log(html_th.innerHTML);
//        console.log(html_th_innerHTML);
//        html_th.innerHTML = html_th_innerHTML;
//    }

    while (switching) {
        switching = false;

        for (var i = 1; i < rows.length - 1; i++) {
            var shouldSwitch = false;
            var x = rows[i].getElementsByTagName("TD")[columnIndex];
            var y = rows[i + 1].getElementsByTagName("TD")[columnIndex];

            if (!isNaN(x.innerHTML)){
                if (Number(x.innerHTML) > Number(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
            else{
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}