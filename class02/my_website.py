html_header = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link href="https://fonts.googleapis.com/css?family=Odibee+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" integrity="sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <link rel="stylesheet" href="css/styles.css">
  <title>Noticias</title>
</head>
"""

html_body1 = """
<body>
  <a id="button3"></a>
  <div id="wrapper">
    <header>
      <div id="header" style="font-size:3.2em; text-align:center; padding:27px; color:#fff;">
        NOTICIAS DEL MUNDO
      </div>
    </header>
    <section>
      <div style="background-color: transparent; text-align: center;">
      </div>
    </section>
    <div id="container">
      <nav>
        <ul>
          <li><a href="mexico.html">México</a></li>
          <li><a href="usa.html">USA</a></li>
          <li><a href="canada.html">Canada</a></li>
          <li><a href="france.html">Francia</a></li>
          <li><a href="rusia.html">Rusia</a></li>
          <li><a href="japan.html">Japon</a></li>
          <li><a href="germany.html">Alemania</a></li>
        </ul>
      </nav>
      <div id="content">
"""

html_body2 = """
</div>
</div>
    <div class="footer_text1">
      Noticias del Mundo fue desarrollado por <a href="https://gustavogm.me" target="_blank"> Gustavo Gómez Macías (GOZ)</a><br>
      Este es un SITIO WEB DEMO desarrollado para el Taller de Aplicaciones con Python (AMAT)<br> 
      Toda la información presentada en el sitio es real y obtenida por medio del uso de la api newsapi<br>
      2022
 </div>
  </div>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js"
    integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous">
    </script>
  <script>
    var btn = $('#button3');
    $(window).scroll(function () {
      if ($(window).scrollTop() > 300) {
        btn.addClass('show');
      } else {
        btn.removeClass('show');
      }
    });
    btn.on('click', function (e) {
      e.preventDefault();
      $('html, body').animate({ scrollTop: 0 }, '300');
    });
  </script>
</body>
</html>
"""


