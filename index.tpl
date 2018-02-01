<!DOCTYPE html>

<html>
<head>
    <title>Fréttir</title>
    <link rel="sylesheet" href="/static/styles.css">
    <meta charset="utf-8">
</head>
<body>
    % include('header.tpl')
    <h1>{{frettir[0]['fyrirsogn']}}</h1>
    <img src="/static/{{frettir[0]['mynd']}}" alt="frett 1">

    <ul>
        <li><a href="/frett/0">{{frettir[0]['fyrirsogn']}}</a></li>
        <li><a href="/frett/1">{{frettir[1]['fyrirsogn']}}</a></li>
        <li><a href="/frett/2">{{frettir[2]['fyrirsogn']}}</a></li>
        <li><a href="/frett/3">{{frettir[3]['fyrirsogn']}}</a></li>
    </ul>

    % include('footer.tpl')
</body>
</html>