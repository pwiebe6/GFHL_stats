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

    just_the_text_from_the_button = html_button.childNodes[0].textContent;
    stripped_text_from_button = just_the_text_from_the_button.replace("\u21e7", "").replace("\u21e9", "");

    const button_elements = html_th.children;

    // Check if the current button has an up or down arrow at the end of the text
    // If not an up arrow (ie, down arrow or no arrow) then clear all arrows, change this one to up arrow, reverse sort (ie, do largest -> smallest).
    if (just_the_text_from_the_button.slice(-1) != "\u21e7"){
        console.log("Noticed no up arrow. Could be a down arrow or no arrow.");

        for (let i = 0; i < button_elements.length; i++) {
            const button_element = button_elements[i];
            temp = button_element.childNodes[0].textContent.replace("\u21e7", "").replace("\u21e9", "");
            button_element.childNodes[0].textContent = temp;
        }
        html_button.childNodes[0].textContent = stripped_text_from_button + "\u21e7";
        while (switching) {
            switching = false;
    
            for (var i = 1; i < rows.length - 1; i++) {
                var shouldSwitch = false;
                var x = rows[i].getElementsByTagName("TD")[columnIndex];
                var y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
    
                if (!isNaN(x.innerHTML)){
                    if (Number(x.innerHTML) < Number(y.innerHTML)) {
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
    // if up arrow, clear all arrows, change this to down arrow, regular sort (ie, do smallest -> largest).
    else {
        console.log("Noticed an up arrow.");
        
        for (let i = 0; i < button_elements.length; i++) {
            const button_element = button_elements[i];
            temp = button_element.childNodes[0].textContent.replace("\u21e7", "").replace("\u21e9", "");
            button_element.childNodes[0].textContent = temp;
        }
        html_button.childNodes[0].textContent = stripped_text_from_button + "\u21e9";
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
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
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

    
}