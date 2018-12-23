
import cgi

print "<!DOCTYPE html>"
print
print """<html>
<head>
	<title>data diri</title>
	<style type="text/css">
		.foto{
			width: 20%;
			height: 400px;
			float: left;
			margin-right: 30px;
		}
		.text{
			width: 70%;
			height: 400px;
			float: left;
		}
	</style>
</head>
<body>

<div class="foto"><img src="foto.png" width="100%" height="230px"></div>
<div class="text">
	<h2>data diri</h2>
	<p>Nama : Naufal randi aldiansyah</p>
	<p>Alamat : bogor</p>
	<p>tempat tanggal lahir : bogor </p>
	<p>tempat wisata favorit : kasur</p>
	<p>motto : jadilah diri sendiri dan lakukan yang terbaik</p>
</div>

</body>
</html>"""
