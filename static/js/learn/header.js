function Header() {
   var HEIGHT_FRACTION = 0.05;
   var LESSON_TITLE_X_FRACTION = 0.26;

   var that = {};

   var div = document.getElementById('headerDiv');

   var lessonTitle = TitleElement(LESSON_TITLE_X_FRACTION, '');

   var homeButtonDim = {
      left:0, 
      top:0, 
      width:0.246, 
      height:1
   };

   var referenceDim = {
      left:0.93,
      top:1,
      width:0.14,
      height:1.0,
   }
   
   
   var homeButton = {};
   homeButton.div = document.createElement('div');
   homeButton.div.id = 'homeButton';
   homeButton = MakeAbsoluteDiv(homeButton, 'headerDiv', homeButtonDim);

   var linkUrl = "learn.html";
   var link = document.createElement('a');
   link.setAttribute('href', linkUrl);
   
   var resize = homeButton.resize;
   homeButton.resize = function() {
      resize();
   }
   div.appendChild(homeButton.div);
   homeButton.div.appendChild(link);

   that.getHeight = function() {
      return $('#headerDiv').height();
   }

   that.resize = function(show) {
      var contentHeight = $('#content').height();
      var headerHeight = contentHeight * HEIGHT_FRACTION;
      if(!show) headerHeight = 0;
      if(!show) homeButton.div.style.display = "none"
      div.style.height = headerHeight + 'px';
      lessonTitle.resize();
      homeButton.resize();
      var centerHeight = $('#headerDiv').height();
   }

   that.updateHeader = function(progressModel) {
      var text = '챕터 ' + progressModel.getUnitIndex();
      text += ' 단계 ' + progressModel.getLessonIndex();
      lessonTitle.setText(text);
   }
   
   return that;

}
