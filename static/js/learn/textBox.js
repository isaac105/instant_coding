function TextBox(dim, text) {
   var that = TextElement(dim, text, 'centerAreaDiv');
   that.div.className = 'rounded';
   that.div.style.background = '#c4e3ec';
   
   return that;
}
