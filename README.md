<h1> Prometheus node_exporter för PhotonOS </h1>

<h2> Introduktion </h2>
"Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors".<br>
Dessvärre så verkar den inte finns paketerad för Photon OS. Här kommer jag därför att dokumenter vad som behövs för kunna paketera i rpm form och sen installera det på Photon OS.<br>

Mera information finns på github projektet för [Prometheus](https://github.com/prometheus/node_exporter)

<h2> Installation </h2>
- Ladda ner detta repo till lämplig katalog i din Photon OS nod och kör:<br>
<code> rpmbuild -ba node_exporter.spec </code><br>
- Lokalisera ditt bygg packet och installera som exempeln visar:<br>
<code> tdnf install $path/node-exporter-1.2.2-1.x86_64.rpm </code>

<h2> Resultat </h2>
Resultatet, dvs de värde data som läses ut finns att se under http://${HOSTNAME}:9100/metrics

