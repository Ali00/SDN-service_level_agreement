# SDN-Multi-Tenants

### Framework:
The framework has been evaluated by the SDN emulator "Mininet", http://mininet.org/ , with POX as a network operating system
(controller), https://github.com/noxrepo/pox/.
<div class="container">
  <div class="subcontainer">
    <figure>
      <p align="center">
      <img  src="https://user-images.githubusercontent.com/12594727/74975632-45ccf200-541f-11ea-8af2-43984c4fbeae.png" width="200" height="300"/>
      <figcaption><p align="center">Fig.1:Framework architecture</figcaption>
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
        <figcaption><p align="center">Fig.2:ERnet Topology layout with 12-attached hosts</figcaption>
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
        <figcaption><p align="center">Fig.2: Architecture of D-ITG</figcaption>
    </figure>
  </div>
</div>


![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `If you use this framework or any of its code in your work then, please cite the following publication: " ".`
