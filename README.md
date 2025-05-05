![ezosint](https://github.com/user-attachments/assets/4beed3c2-989e-4976-a998-e29a312205a6)


# ꧁꧂  ezOSINT 👁️‍🗨️
ezOSINT is a cross platform Username lookup tool used in OSINT. What sets this version apart is how easy it is for anyone to add sites and/or commit updates to the repo. Designed to be easy. 

# ꧁꧂ Adding sites 🔍

Open config.ini and follow the template. You can only provide a valid keycheck, everything else will be considered invalid. This means you must look at the source of both pages and then use a  [Diffchecker](https://www.diffchecker.com/) or [WinMerge](https://github.com/WinMerge/winmerge) and find something that is on the valid version that can not be found when searching the invalid version. 

The config template for each site is only 2 lines. The URL - replace the actual username with {USER} & the valid string to look for.

Example: 

`[Link 138]`

`url = https://facebook.com/{USER}`

`valid_string = ProfileCometTilesFeed.react`



# ꧁꧂ Valid Results 💯

Results are saved in the app directory or root directory of this script. 


# ꧁꧂  Automatic Install 🪅



1. Download, install, and add to path with: 

`go install github.com/noarche/ezosint@latest`

2. Download the config.ini

`curl -O https://raw.githubusercontent.com/noarche/ezosint/main/config.ini`

3. Run with: 

`ezosint`



### Manual Install 

1. Initialize Go module and install dependencies:

`go mod init ezosint`

`go mod tidy`

`go get gopkg.in/ini.v1`


2. Build the binary:

`go build -o ezosint main.go`

3. Run it:

`./ezosint`



# ꧁꧂ Updating 🔮

After downloading the docker or .py script you will only need to download the new config.ini file to update. I will try to fix/update/add to this list regularly.  

If you find public profiles not on list feel free to commit changes you find to config; it will be appreciated by everyone who uses. As of 5/5/2025 there are 0% false positive results.


# ꧁꧂  Buy me a coffee ☕

![qrCode](https://raw.githubusercontent.com/noarche/cd-ripper/main/unrelated-ignore/CryptoQRcodes.png)

**Bitcoin** address `bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j`


**Ethereum** address `0x94FcBab18E4c0b2FAf5050c0c11E056893134266`


**Litecoin** address `ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx`



-------------------------------------------------------------------

![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)






[Download Docker Image](https://hub.docker.com/repository/docker/torquetraction/ezosint/general)
