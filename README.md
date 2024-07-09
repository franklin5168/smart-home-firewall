# Supervising Smart Home Device Interactions: A Profile-Based Firewall Approach

**Note: This is the anonymous repository for double-blind review.
Now that this research has been accepted,
please visit the [public version](https://github.com/smart-home-network-security/smart-home-firewall).**

Profile-based Smart Home firewall, based on [nftables](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page).


## Local compilation

Compile locally with:
```bash
./translate_profiles.sh
mkdir build bin
cd build
cmake ..
cmake --build .
```
or, more easily:
```bash
./translate_profiles.sh
./build.sh
```

## Cross-compilation for OpenWrt

We provide two Docker images to cross-compile for two OpenWrt targets:
- [TP-Link TL-WDR4900](https://openwrt.org/toh/tp-link/tl-wdr4900): https://hub.docker.com/r/franklin5168/openwrt_tl-wdr4900
- [Linksys WRT1200AC](https://openwrt.org/toh/linksys/wrt1200ac): https://hub.docker.com/r/franklin5168/openwrt_linksys-wrt1200ac

To pull either of them:
```bash
docker pull franklin5168/openwrt_tl-wdr4900
docker pull franklin5168/openwrt_linksys-wrt1200ac
```

To run cross-compilation with either image:
```bash
docker run --rm --mount type=bind,source=$(pwd),target=/home/user/iot-firewall -e ROUTER=tl-wdr4900 franklin5168/openwrt_tl-wdr4900
docker run --rm --mount type=bind,source=$(pwd),target=/home/user/iot-firewall -e ROUTER=linksys-wrt1200ac franklin5168/openwrt_linksys-wrt1200ac
```
