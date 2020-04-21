# SDN-Multi-Tenants

### Framework:
The framework has been evaluated by the SDN emulator "Mininet", http://mininet.org/ , with POX as a network operating system
(controller), https://github.com/noxrepo/pox/.
<div class="container">
  <div class="subcontainer">
    <figure>
      <p align="center">
      <img  src="https://user-images.githubusercontent.com/12594727/74975632-45ccf200-541f-11ea-8af2-43984c4fbeae.png" width="200" height="300"/>
      <figcaption><p align="center">Fig.1: Architecture of the proposed framework and its components: the
primary contribution of this paper is on the SLA blocks. Openflow is used on
the southbound interface and POX APIs are used on the northbound interface.</figcaption>
    </figure>
  </div>
</div>

### Network topology: 
The network is modelled as an undirected graph G(V,E), hence, we utilised the NetworkX tool, https://networkx.github.io/, (version 1.11). European Reference network (ERnet) has been used to represent the data plane topology.
 <div class="container">
  <div class="subcontainer">
    <figure>
      <p align="center">
<img  src= "https://user-images.githubusercontent.com/12594727/74964248-0ac0c380-540b-11ea-9190-3b1eef2d3716.png"
     width="500" height="400"/>
        <figcaption><p align="center">Fig.2: The European reference network topology (ERnet) with 12 hosts.
The added hosts are classified into two SLA categories: Gold and Bronze. The gold hosts have the IPs from 10.0.0.1 to 10.0.0.6, while, the IP of bronze hosts start from 10.0.0.7 to 10.0.0.12.</figcaption>
    </figure>
  </div>
</div>

### Network traffic:
The DistributedInternet Traffic Generator (D-ITG), http://www.grid.unina.it/software/ITG/manual/, is used to generate the network traffic. D-ITG is a platform capable to produce IPv4 and IPv6 traffic by accurately replicating the workload of current Internet applications. At the same time D-ITG is also a network measurement tool able to measure the most common performance metrics (e.g. throughput, delay, jitter, packet loss) at packet level. 

<div class="container">
  <div class="subcontainer">
    <figure>
      <p align="center">
<img  src= "https://user-images.githubusercontent.com/12594727/75080948-7f782880-5505-11ea-8c75-8fc9aaa7ed57.png"
     width="300" height="250"/>
        <figcaption><p align="center">Fig.3: Architecture of  <a href="http://traffic.comics.unina.it/software/ITG/manual/">D-ITG</a> </figcaption>
    </figure>
  </div>
</div>

### Wireshark obtained results:
<div class="container">
  <div class="subcontainer">
    <figure>
      <p align="center">
<img  src= "https://user-images.githubusercontent.com/12594727/75635721-3f552c00-5c10-11ea-9f21-f40a4cdb7255.jpg"
     width="300" height="200"/>
<img  src= "https://user-images.githubusercontent.com/12594727/75635775-a5da4a00-5c10-11ea-8aa6-cc3671cd2bcb.jpg"
     width="300" height="200"/>
<img  src= "https://user-images.githubusercontent.com/12594727/75635816-01a4d300-5c11-11ea-84a3-7a844d5fdff0.jpg"
     width="300" height="200"/>
<img  src= "https://user-images.githubusercontent.com/12594727/75635928-37968700-5c12-11ea-8561-e4fbd4e2c937.jpg"
     width="300" height="200"/>
<img  src= "https://user-images.githubusercontent.com/12594727/75635929-38c7b400-5c12-11ea-9e6a-a0fdf7f637be.jpg"
     width="300" height="200"/>
<img  src= "https://user-images.githubusercontent.com/12594727/75635930-39f8e100-5c12-11ea-9b9d-6574e5ae18c5.jpg"
     width="300" height="200"/>
     <img  src= "https://user-images.githubusercontent.com/12594727/75635933-3bc2a480-5c12-11ea-90fc-b0933ec74e96.jpg"
     width="300" height="200"/>
     <img  src= "https://user-images.githubusercontent.com/12594727/75635936-3d8c6800-5c12-11ea-8817-ce44240f9084.jpg"
     width="300" height="200"/>
     <img  src= "https://user-images.githubusercontent.com/12594727/75635938-3ebd9500-5c12-11ea-88a0-3cfead384f80.jpg"
     width="300" height="200"/>
     <img  src= "https://user-images.githubusercontent.com/12594727/75635940-411fef00-5c12-11ea-9fd4-78c69151aa31.jpg"
     width="300" height="200"/>
     <img  src= "https://user-images.githubusercontent.com/12594727/75635941-42e9b280-5c12-11ea-834d-9a984bd30e01.jpg"
     width="300" height="200"/>
     <img  src= "https://user-images.githubusercontent.com/12594727/75635942-441adf80-5c12-11ea-96b0-09c0ff0a7b44.jpg"
     width="300" height="200"/>
        <figcaption><p align="center">Fig.4: Wireshark view showing the flow of packets recorded via hosts from
0-5000 seconds (x-axis). Hosts H1 to H6 to represent the gold tenants and
the hosts H7 to H12 represent the bronze tenants. In addition, blue indicates
sender hosts and red indicates receiver. Hosts H1 to H6 (rows 1 and 2) exhibit
lower packet loss as there a fewer dips in this throughput (y-axis) during the
experiment run. </figcaption>
    </figure>
  </div>
</div>





![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `If you use this framework or any of its code in your work then, please cite the following publication: "SLA-Aware Routing Strategy for Multi-Tenant
Software-Defined Networks".IEEE ISCC 2020 (to appear)`
