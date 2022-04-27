#TEST 3 - Horisontalpodautoskalering - HPA
Ble lagt til fire linjer i components.yaml for å få den til å fungere under arg:
command:
- /metrics-server
- --kubelet-insecure-tls
- --kubelet-preferred-address-types=InternalIP