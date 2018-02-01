<!DOCTYPE html>

<html>
<head>
    <title>{{frettir[int (n)]['fyrirsogn']}}</title>
    <link rel="sylesheet" href="/static/styles.css">
    <meta charset="utf-8">
</head>
<body>
    % include('header.tpl')
    <h1>{{frettir[int (n)]['fyrirsogn']}}</h1>
    <img src="/static/{{frettir[int(n)]['mynd']}}" alt="frett 2">
    <p>{{frettir[int (n)]['texti']}}</p>
    <h5>{{frettir[int(n)]['email']}}</h5>
    <a href="/b">Til baka</a>
    % include('footer.tpl')
</body>
</html>