![ezOSINT](https://github.com/user-attachments/assets/d15bb1b5-5bc9-4251-900f-55e3f113ed68)



# ꧁꧂  ezOSINT
ezOSINT is a cross platform Username lookup tool used in OSINT. What sets this version apart is how easy it is for anyone to add sites and/or commit updates to the repo. Designed to be easy. 

# ꧁꧂ Adding sites

Open config.ini and follow the template. You can only provide a valid keycheck, everything else will be considered invalid. This means you must look at the source of both pages and then use a site or tool like [Diffchecker](https://www.diffchecker.com/) and find something that is on the valid version that can not be found when searching the invalid version. 

The config template for each site is only 2 lines. The URL - replace the actual username with {USER} & the valid string to look for.

Example: 

`[Link 138]`

`url = https://facebook.com/{USER}`

`valid_string = ProfileCometTilesFeed.react`


# ꧁꧂ Valid Results

Results are saved in the app directory or root directory of this script. 

# ꧁꧂ Updating

Once you download the Exe or .py script you will only need to download the new config.ini file to update. I will try to fix/update/add to this list regularly.  If you want to commit changes you find to config it will be appreciated. 


# ꧁꧂  Buy me a coffee ☕

![qrCode](https://raw.githubusercontent.com/noarche/cd-ripper/main/unrelated-ignore/CryptoQRcodes.png)

**Bitcoin** address `bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j`


**Ethereum** address `0x94FcBab18E4c0b2FAf5050c0c11E056893134266`


**Litecoin** address `ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx`



-------------------------------------------------------------------

![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)

# ꧁꧂  Docker Image

`docker pull torquetraction/ezosint`

`docker run -it torquetraction/ezosint`

[Download Docker Image](https://hub.docker.com/repository/docker/torquetraction/ezosint/general)
