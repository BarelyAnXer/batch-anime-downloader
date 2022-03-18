var validUrls = ["4anime.to"]


// TODO check if url is valid ok na yung isa valid pero example what if meron
// lang 4anime.to dun sa url edi valid parin yung kahit na pwede pasyang magkamali

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

eel.expose(getDirectory)
function getDirectory(){
    return document.getElementById("input_dir").value
}

function isValidUrl(url){
    for(i = 0; i < validUrls.length; i++){
        if(url.includes(validUrls[i])){
            return true
        }
        else{
            return false
        }
    }
}

//async function parseEpisodes(){
//
//    return
//}

async function browse(){
    document.getElementById("input_dir").value = await eel.getDirectory()()
}

async function loadEpisodes(){
    var isLoadingEps = false
    var url = document.getElementById("input_url").value

    eel.resetDownloadInfo()

//    to reset download info data if loading new anime

    if(url == ""){
        alert("Anime Url cant be Blank")
        return
    }

    if(isValidUrl(url)){
        console.log("valid")
        if(!isLoadingEps){
            document.getElementById("loadEpisodesBtn").disabled = true
            document.getElementById("downloadBtn").disabled = true
            document.getElementById("browseBtn").disabled = true
        }

        eel.loadAnimeInfo(url)
//      need to wait to load the animeinfo kaya dito sya naka define? experiment pa
        var animeInfo = await eel.getAnimeInfo()()
        loadTableData(animeInfo)

        isLoadingEps = await eel.getIsLoadingEps()()
        console.log(isLoadingEps)
        if(isLoadingEps){
            document.getElementById("loadEpisodesBtn").disabled = false
            document.getElementById("downloadBtn").disabled = false
            document.getElementById("browseBtn").disabled = false
        }
    }
    else{
        alert("Invalid Url")
    }
}

async function downloadProgress() {
    var dir = document.getElementById("input_dir").value
    var url = document.getElementById("input_url").value
    var isPathValid = await eel.isPathValid(dir)()
    var isDownloading = false

    if(dir == "" && url == ""){
        alert("Path and Anime Url cant be Blank")
        return
    }

    if(dir == ""){
        alert("Path cant be Blank")
        return
    }
    else if(!isPathValid){
        alert("Invalid Path")
        return
    }

    if(url == ""){
        alert("Anime Url cant be Blank")
        return
    }
//  else if(){
//        check if valid ba yung url yung valid na valid yung nabubuksan ba
//       if nabubukasan supported ba
// TODO checking if valid dir and yung mismong url yung sa url use deeper check tingnan if
// pwede ba tlga example what if meron lng domain name(not sure if iyun tawag) tapos sa susunod eh mali yung iba diba syempre magkakaerror yun
//                                               ex 4anime ... check urlss for more domain name?
//    }

    isDownloading = true
    if(isDownloading){
        document.getElementById("loadEpisodesBtn").disabled = true
        document.getElementById("downloadBtn").disabled = true
        document.getElementById("browseBtn").disabled = true
    }


    var animeInfo = await eel.getAnimeInfo()()
    for (i = 1; i < animeInfo.length+1; i++){
        eel.download()
        let currentProgress = 0
        while (currentProgress != 100){
            currentProgress = await eel.getDownloadProgress()()
            document.getElementById(`file${i}`).value = currentProgress
            if (currentProgress == 100){
                break
            }
        }
    }

    document.getElementById("loadEpisodesBtn").disabled = false
    document.getElementById("downloadBtn").disabled = false
    document.getElementById("browseBtn").disabled = false

    alert("Done")
}


function loadTableData(animeInfo){
    var tableBody = document.getElementById("tableData")
    var dataHtml = ""
    var ctr = 1

    while(tableBody.hasChildNodes()){
        tableBody.removeChild(tableBody.firstChild)
    }

    for(let anime of animeInfo){
        dataHtml += `<tr><td>${anime.title} ${anime.episode}</td>
                         <td><progress id="file${ctr}" value="0" max="100" style="width:100%"></progress></td>
                         <td>${anime.size} MB</td></tr>`
        ctr = ctr + 1
    }
    tableBody.innerHTML = dataHtml
}
