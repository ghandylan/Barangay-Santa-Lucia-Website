function updateClock() {
    var now = new Date();
    var dy = now.getDay(),
        mth = now.getMonth(),
        dt = now.getDate(),
        yr = now.getFullYear(),
        hr = now.getHours(),
        min = now.getMinutes(),
        sec = now.getSeconds(),
        pd = "AM";
        
        if(hr == 0) {
            hr = 12;
        }
        if(hr > 12) {
            hr -= 12;
            pd = "PM";
        }

        Number.prototype.pad = function(digits) {
            for(var n = this.toString(); n.length < digits; n = 0 + n);
            return n;
        }

        var month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        var day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        // var ids = ["month", "year", "date", "day", "hour", "minute", "second", "period"];
        // var values = [month[mth], yr, dt.pad(2), day[dy], hr.pad(2), min.pad(2), sec.pad(2), pd];
        var ids = ["month", "year", "date1", "date2", "date3", "date4", "date5", "date6", "date7"];
        if(day[dy] == "Monday") {
            var values = [month[mth], yr, (dt).pad(2), (dt+1).pad(2), (dt+2).pad(2), (dt+3).pad(2), (dt+4).pad(2), (dt+5).pad(2), (dt+6).pad(2)];
        }
        else if(day[dy] == "Tuesday") {
            var values = [month[mth], yr, (dt-1).pad(2), (dt).pad(2), (dt+1).pad(2), (dt+2).pad(2), (dt+3).pad(2), (dt+4).pad(2), (dt+5).pad(2)];
        }
        else if(day[dy] == "Wednesday") {
            var values = [month[mth], yr, (dt-2).pad(2), (dt-1).pad(2), (dt).pad(2), (dt+1).pad(2), (dt+2).pad(2), (dt+3).pad(2), (dt+4).pad(2)];
        }
        else if(day[dy] == "Thursday") {
            var values = [month[mth], yr, (dt-3).pad(2), (dt-2).pad(2), (dt-1).pad(2), (dt).pad(2), (dt+1).pad(2), (dt+2).pad(2), (dt+3).pad(2)];
        }
        else if(day[dy] == "Friday") {
            var values = [month[mth], yr, (dt-4).pad(2), (dt-3).pad(2), (dt-2).pad(2), (dt-1).pad(2), (dt).pad(2), (dt+1).pad(2), (dt+2).pad(2)];
        }
        else if(day[dy] == "Saturday") {
            var values = [month[mth], yr, (dt-5).pad(2), (dt-4).pad(2), (dt-3).pad(2), (dt-2).pad(2), (dt-1).pad(2), (dt).pad(2), (dt+1).pad(2)];
        }
        else if(day[dy] == "Sunday") {
            var values = [month[mth], yr, (dt-6).pad(2), (dt-5).pad(2), (dt-4).pad(2), (dt-3).pad(2), (dt-2).pad(2), (dt-1).pad(2), (dt).pad(2)];
        }
        
        for(var i = 0; i < ids.length; i++)
        document.getElementById(ids[i]).firstChild.nodeValue = values[i]
}

function initClock() {
    updateClock();
    window.setInterval("updateClock()", 1);
}