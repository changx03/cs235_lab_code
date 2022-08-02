/*!
 * Coffee Bean Colour Picker
 *
 * Date: 2020-07-23
 */
var cnvHeight;
var cnvWidth;
var mousePos;
var cnvActiveImage;
var ctx;
var cPix;
var ctxPix;
var img;
var imgHeight;
var imgWidth;
var sDefaultImage = './img/beans/00 nousnou-iwasaki-myPzH34VYK4-unsplash.jpg';

var numLastRgbVal;

var arrRoastColour = [];
arrRoastColour[0]  = ["Green Beans","#8f8c64",143, 140, 100];
arrRoastColour[1]  = ["Green Beans","#a49865",164, 152, 101];
arrRoastColour[2]  = ["Green Beans","#d9c893",217, 200, 147];
arrRoastColour[3]  = ["Drying Phase","#d9b65c",217, 182, 92];
arrRoastColour[4]  = ["Drying Phase","#d4b066",212, 176, 102];
arrRoastColour[5]  = ["Drying Phase","#cfb357",207, 179, 87];
arrRoastColour[6]  = ["Cinnamon Roast","#df7217",223, 114, 23];
arrRoastColour[7]  = ["Cinnamon Roast","#fb9536",251, 149, 54];
arrRoastColour[8]  = ["American Roast", "#8c7165", 140, 113, 101];
arrRoastColour[9]  = ["American Roast","#c76917",199, 105, 23];
arrRoastColour[10] = ["City Roast","#9a5431",154, 84, 49];
arrRoastColour[11] = ["Full City Roast","#763717",118, 55, 23];
arrRoastColour[12] = ["French Roast","#432911",67, 31, 17];
arrRoastColour[13] = ["Italian Roast","#090a07",9, 10, 7];


oFReader = new FileReader(), rFilter = /^(?:image\/bmp|image\/cis\-cod|image\/gif|image\/ief|image\/jpeg|image\/jpeg|image\/jpeg|image\/pipeg|image\/png|image\/svg\+xml|image\/tiff|image\/x\-cmu\-raster|image\/x\-cmx|image\/x\-icon|image\/x\-portable\-anymap|image\/x\-portable\-bitmap|image\/x\-portable\-graymap|image\/x\-portable\-pixmap|image\/x\-rgb|image\/x\-xbitmap|image\/x\-xpixmap|image\/x\-xwindowdump)$/i;

oFReader.onload = function (oFREvent) {
    document.getElementById("imgPreview").crossorigin = "anonymous";   
    document.getElementById("imgPreview").src = oFREvent.target.result;
//Use the following line of code to get encoded information about the loaded image
//    document.getElementById("userComments").value = document.getElementById("imgPreview").src;
};

function loadImageFile() {
    //This function loads the selected image into the (hidden) image element
    if (document.getElementById("uploadImage").files.length === 0) { return; }
    var oFile = document.getElementById("uploadImage").files[0];
    if (!rFilter.test(oFile.type)) { alert("You must select a valid image file!"); return; }
    oFReader.readAsDataURL(oFile);
}

function loadDefaultImage(){
    //This function assigns a default image when the page loads
    document.getElementById("imgPreview").crossorigin = "anonymous";   
    document.getElementById("imgPreview").src = sDefaultImage;            
    //If on PC, default the mouse move mode for cnvActiveImage as "Rolling"
    var dvPointerStatus = document.getElementById("pointerMode");
    dvPointerStatus.innerHTML = "Rolling";
}

function clearUserComments() {
    document.getElementById("userComments").value = '';
}

var onclickListener = function(evt) {
    //Do colour search and return results on clicking image (based on centre of cnvZoomPixels)
    imageData = ctxPix.getImageData(0,0,150,150);
    var decRGBRed   = imageData.data[45300+0];
    var decRGBGreen = imageData.data[45300+1];
    var decRGBBlue  = imageData.data[45300+2];
    var strRGBActive='#'+dec2hex(decRGBRed)+dec2hex(decRGBGreen)+dec2hex(decRGBBlue);
    if (strRGBActive != numLastRgbVal) {
        numLastRgbVal = strRGBActive;
        document.getElementById("dvActiveColour").style.backgroundColor=strRGBActive;
        document.getElementById("dvActiveColour").dataset.colour=strRGBActive+','+decRGBRed+','+decRGBGreen+','+decRGBBlue;
        getColourNames(decRGBRed, decRGBGreen, decRGBBlue);
    }
    // In the case of PC, allow toggling between roving selection and fixed seleciton when moving mouse 
    // over the loaded image (cnvActiveImage)
    istat=!istat;
    var dvPointerStatus = document.getElementById("pointerMode");
    if (istat) {
        dvPointerStatus.innerHTML = "Rolling";
    } else {
        dvPointerStatus.innerHTML = "Sampled";
    }
};

function getColourNames(decRGBRed, decRGBGreen, decRGBBlue){
	// Find the Roast Bean Colour names that are closest to the selected RGB value.
    var getClosestColour  = getClosestMatch(arrRoastColour, decRGBRed, decRGBGreen, decRGBBlue);
    var intCloseColourPos = getClosestColour.arrList[0];
	document.getElementById("userComments").value = arrRoastColour[intCloseColourPos][0];
}

function getClosestMatch(arrColourResults, intDecRed, intDecGreen, intDecBlue) {
    //Find the colour result(s) that have the lowest difference in rgb values from the search colour
    var intMaxDeviation = 255;
    var intMidDeviation = 255;
    var intMinDeviation = 255;
    var intCurrMaxDeviation = 0;
    var intCurrMidDeviation = 0;
    var intCurrMinDeviation = 0;
    var arrLowPosList = new Array();
    for (var i = 0; i < arrColourResults.length; i++) {
        var arrAbsDiffVals = [Math.abs(intDecRed-arrColourResults[i][2]), Math.abs(intDecGreen-arrColourResults[i][3]), Math.abs(intDecBlue-arrColourResults[i][4])];
        arrAbsDiffVals.sort(function(a, b){return a-b});
        intCurrMinDeviation = arrAbsDiffVals[0];
        intCurrMidDeviation = arrAbsDiffVals[1];
        intCurrMaxDeviation = arrAbsDiffVals[2];
        if (intCurrMaxDeviation < intMaxDeviation){
            arrLowPosList = [i];
            intMaxDeviation = intCurrMaxDeviation;
            intMidDeviation = intCurrMidDeviation;
            intMinDeviation = intCurrMinDeviation;
        } else {
            if ((intCurrMaxDeviation == intMaxDeviation) && (intCurrMidDeviation < intMidDeviation)){
                arrLowPosList = [i];
                intMidDeviation = intCurrMidDeviation;
                intMinDeviation = intCurrMinDeviation;
            } else {
                if ((intCurrMaxDeviation == intMaxDeviation) && (intCurrMidDeviation == intMidDeviation) && (intCurrMinDeviation < intMinDeviation)) {
                        arrLowPosList = [i];
                        intMinDeviation = intCurrMinDeviation;
                } else {
                    if ((intCurrMaxDeviation == intMaxDeviation) && (intCurrMidDeviation == intMidDeviation) && (intCurrMinDeviation == intMinDeviation)) {
                        arrLowPosList.push(i);
                    }
                }
            }
        }
    }        
    return { arrList: arrLowPosList };
}

function loadCanvas(){
    //This function renders the content of the hidden imgPreview element into the cnvActiveImage element
    istat=true;

    cnvActiveImage=document.getElementById("cnvActiveImage");
    ctx=cnvActiveImage.getContext("2d");

    cPix=document.getElementById("cnvZoomPixels");
    ctxPix=cPix.getContext("2d");

    ctxPix.ImageSmoothingEnabled = false;
    ctxPix.webkitImageSmoothingEnabled = false;

    img=document.getElementById("imgPreview");
	img.crossorigin = "anonymous";   
    imgHeight = img.height;
    imgWidth = img.width;
	
    if (imgHeight<cnvHeight && imgWidth<cnvWidth){
        ctx.ImageSmoothingEnabled = false;
        ctx.webkitImageSmoothingEnabled = false;
    }

    //the following is to do with scaling the image on the canvas
    //for landscape (470/300 = 1.56667)
    cnvWidth  = 470;
    cnvHeight = 300;
    if ((imgWidth/imgHeight)<1.56667){
        //if image is comparatively taller in ratio, reduce canvas width
        cnvWidth=imgWidth/imgHeight*cnvHeight;
    }else{
        //if image is comparatively wider in ratio, reduce canvas height
        cnvHeight=cnvWidth/(imgWidth/imgHeight);
    }
    ctxPix.setTransform(1, 0, 0, 1, 0, 0);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, cnvActiveImage.width, cnvActiveImage.height);
    ctx.drawImage(img,(470-cnvWidth),0,cnvWidth,cnvHeight);
    	
    var onmoveListener = function(evt) {
        // Allow toggling between roving selection and fixed seleciton when moving mouse 
        // over the loaded image (cnvActiveImage)
        if (istat==false){
            //Do nothing
        } else {
            //Get the position of the mouse relative to the cnvActiveImage canvas
            mousePos = getMousePos(cnvActiveImage, evt);
            //Refresh the display in cnvZoomPixels
            drawPix(cPix, ctxPix, img, Math.round((mousePos.x + cnvWidth - 470)*(imgWidth/cnvWidth)), Math.round(mousePos.y*(imgHeight/cnvHeight)));
        }
    };
    cnvActiveImage.addEventListener('mousemove', onmoveListener, false);
    cnvActiveImage.addEventListener('mousedown', onclickListener, false);
	
    var onMiniclickListener = function(evt) {
        //Select colour sample when click on cnvZoomPixels
        mousePos = getMousePos(cPix, evt);
        imageData = ctxPix.getImageData(0,0,150,150);
        var loc= Math.round(mousePos.y)*600+Math.round(mousePos.x)*4;
        var decZoomRGBRed   = imageData.data[loc+0];
        var decZoomRGBGreen = imageData.data[loc+1];
        var decZoomRGBBlue  = imageData.data[loc+2];
        var strRGBActive='#'+dec2hex(decZoomRGBRed)+dec2hex(decZoomRGBGreen)+dec2hex(decZoomRGBBlue);
        if (strRGBActive != numLastRgbVal){
            numLastRgbVal = strRGBActive;
            document.getElementById("dvActiveColour").style.backgroundColor=strRGBActive;
            document.getElementById("dvActiveColour").dataset.colour=strRGBActive+','+decZoomRGBRed+','+decZoomRGBGreen+','+decZoomRGBBlue;
            getColourNames(decZoomRGBRed, decZoomRGBGreen, decZoomRGBBlue);
        }
    };
    cPix.addEventListener('mousedown', onMiniclickListener, false); 
}

function drawPix(cPix, ctxPix, img, x, y) {
    //refresh the image in cnvZoomPixels
    ctxPix.clearRect(0, 0, cPix.width, cPix.height);
    //ensure that the x and y coordinates are within the image range
    if (x<5) x=5;
    if (y<5) y=5;
    if (x>imgWidth-4) x=imgWidth-4;
    if (y>imgHeight-4) y=imgHeight-4;
    //
    ctxPix.drawImage(img,x-5,y-5,9,9,0,0,cPix.width,cPix.height);
}

function getMousePos(canvas, evt) {
    //return mouse x and y coordinates relative to the selected canvas
    var rect = canvas.getBoundingClientRect();
    return { x: evt.clientX - rect.left, y: evt.clientY - rect.top};
}

function dec2hex(d){
    //decimal to hex conversion
    return ("0"+d.toString(16)).slice(-2).toUpperCase();
}

function copyComments() {
   //copy user comments to clipboard
   document.getElementById("userComments").select();
   try {
      document.execCommand('copy');
      document.getElementById("userComments").blur();
   }
   catch (err) {
      alert('please press Ctrl/Cmd+C to copy');
   }
}