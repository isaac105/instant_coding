

function KarelImages() {
   var that = {};

	var images = new Array();
	var imageNames = new Array();
	imageNames[0] = "/static/images/karelNorth.png";
	imageNames[1] = "/static/images/karelSouth.png";
	imageNames[2] = "/static/images/karelEast.png";
	imageNames[3] = "/static/images/karelWest.png";
	imageNames[4] = "/static/images/cross.png";
	imageNames[5] = "/static/images/beeper.jpg";
	imageNames[6] = "/static/images/karelNorthSmall.png";
	imageNames[7] = "/static/images/karelSouthSmall.png";
	imageNames[8] = "/static/images/karelEastSmall.png";
	imageNames[9] = "/static/images/karelWestSmall.png";
	imageNames[10] = "/static/images/karelNorthTiny.png";
	imageNames[11] = "/static/images/karelSouthTiny.png";
	imageNames[12] = "/static/images/karelEastTiny.png";
	imageNames[13] = "/static/images/karelWestTiny.png";

	var callback = null;
	var imagesLoaded = 0;
	var allLoaded = false;
	var calledLoadImages = false;
	var listeners = [];

	that.checkLoaded = function() {
		for ( var i = 0; i < images.length; i++ ) {
			if (!images[i].complete) {
				return;
			}
		}
		interval=self.clearInterval(interval);
		karelImages.createVariables();
		allAreLoaded();
	}

	that.haveCalledLoadImages = function() {
	   return calledLoadImages;
   }

   that.haveLoadedAllImages = function() {
      return allLoaded;
   }

   that.addListener = function(listener) {
      listeners.push(listener);
   }

	that.loadImages = function(callbackFn) {
		if (calledLoadImages) alert("called loadImages twice");
		callback = callbackFn;
		calledLoadImages = true;
		imagesLoaded = 0;
	

		for (var i = 0; i < imageNames.length; i++) {
			var imageName = imageNames[i];
			images[i] = new Image();
			images[i].src = imageName;
		}
		interval = setInterval("karelImages.checkLoaded()",500);
	}
	
	that.imageProcessed = function() {
		imagesLoaded += 1;
 
		if (imagesLoaded == imageNames.length) {
			karelImages.createVariables();
			allAreLoaded();
		}
	}

	that.createVariables = function() {
		that.karelNorth = images[0];
		that.karelSouth = images[1];
		that.karelEast = images[2];
		that.karelWest = images[3];
		that.cross = images[4];
		that.beeper = images[5];
		that.karelNorthSmall = images[6];
		that.karelSouthSmall = images[7];
		that.karelEastSmall = images[8];
		that.karelWestSmall = images[9];
		that.karelNorthTiny = images[10];
		that.karelSouthTiny = images[11];
		that.karelEastTiny = images[12];
		that.karelWestTiny = images[13];
	}

	function allAreLoaded() {
	   allLoaded = true;
	   if(callback) {
	      callback();
      }
	   for (var i = 0; i < listeners.length; i++) {
	      listeners[i]();
      }
	}
	
	return that;
}
