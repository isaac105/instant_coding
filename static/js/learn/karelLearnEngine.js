function KarelLearnEngine(type, idx, cnt, time) {

   var that = {};

   var windowWidth = $(window).width();
   var windowHeight = $(window).height();
   var topicIndex = 0;
   var slideIndex = 0;
   var content = Content();

   var lessonsModel = LessonsModel();
   var progressModel = ProgressModel(lessonsModel);
   
   progressModel.setUserIdx(idx)
   progressModel.setHintCnt(cnt)
   progressModel.setClearTime(time)

   that.header = Header();
   that.centerArea = CenterArea();
   that.progressBar = ProgressBar(that);

   if(type !== 'pass'){
      that.onWindowResize = function() {
         resize();
      }
   }

   that.progressModelStatus = progressModel
   
   that.onHashChange = function () {
      that.progressModelStatus = ProgressModel(lessonsModel)
      //progressModel.setClearTime(startTime);

      var previousUnit = progressModel.getUnitIndex();
      var previousLesson = progressModel.getLessonIndex();
      progressModel.loadHash();
      var newUnit = progressModel.getUnitIndex();
      var newLesson = progressModel.getLessonIndex();
      if (newUnit != previousUnit || newLesson != previousLesson) {
         render(newUnit != previousUnit);
      }
   }
   
   that.changeLesson = function(lesson) {
      progressModel.changeLesson(lesson);
      that.centerArea.fadeOutElements(finishedChangeAnimation);
   }

   function render(newUnit) {
      if (!progressModel.isAtHomescreen()) {
         if (newUnit) {
            that.progressBar.createLessonIcons(progressModel);
         } else {
            that.progressBar.updateLessonIcons(progressModel);
         }
         that.header.updateHeader(progressModel);
      }
      that.centerArea.createLesson(progressModel, lessonsModel, lessonFinished);
      progressModel.setHash();
   }

   function init() {
      render(true);
      resize();
   }

   function lessonFinished() {
      progressModel.finishedLesson();
      that.centerArea.fadeOutElements(finishedChangeAnimation);
   }

   function finishedChangeAnimation() {
      render(progressModel.isStartingNewUnit());  
   }

   function resize() {
      windowWidth = $(window).width(); 
      windowHeight = $(window).height() - ($(window).height() * 0.1);

      content.resize(progressModel);
      that.progressBar.resize(!progressModel.isAtHomescreen());
      that.header.resize(!progressModel.isAtHomescreen());
      var headerHeight = that.header.getHeight();

      var bodyHeight = content.getHeight() - (content.getHeight() * 0.1);

      bodyHeight -= that.progressBar.getHeight();
      bodyHeight -= headerHeight;

      that.centerArea.setTop (headerHeight + (headerHeight * 0.7));
      that.centerArea.setHeight(bodyHeight);
      that.centerArea.resize();
   }

   
   if(type !== 'pass'){
      init();
   }

   return that;
}
