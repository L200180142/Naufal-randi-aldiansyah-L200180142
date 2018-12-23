def persegi():
    sisi=10
    hitung=sisi*sisi
    return hitung;

print "<!DOCTYPE html>"
print
print """<html>
<head>
	<title>persegi</title>
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

<div class="foto"><img src="persegi.jpg" width="100%" height="230px"></div>
<div class="text">
	<h2>bangun geometri</h2>
	<p>Nama bangun : Persegi</p>
	<p>Dimensi : 2 Dimensi</p>
	<p>Rumus luas : Sisi x Sisi</p>
	<p>Parameter : 10</p>
	<p>Luas  """
print ": ", persegi()
print """</p>
</div>

</body>
</html>"""
