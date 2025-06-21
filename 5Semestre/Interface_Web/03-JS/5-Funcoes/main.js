(function (win, doc) {
    let isvalid = false
    console.log("main", isvalid)    
    win.alert("ALERTA")
    function init(params) {
        console.log("init da main")
    }
    init()
})(window, document)