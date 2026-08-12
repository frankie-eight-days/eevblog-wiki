---
video_id: nTpE1Nw3Yy4
title: EEVblog #1241 - Power Up Display Counter Project - Part 1
url: https://www.youtube.com/watch?v=nTpE1Nw3Yy4
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 26, "2": 54, "3": 73, "4": 92, "5": 110, "6": 125, "7": 142, "8": 155, "9": 173, "10": 187, "11": 210, "12": 229, "13": 249, "14": 264, "15": 281, "16": 300, "17": 324, "18": 345, "19": 360, "20": 377, "21": 394, "22": 414, "23": 432, "24": 455, "25": 471, "26": 491, "27": 511, "28": 534, "29": 559, "30": 575, "31": 594, "32": 615, "33": 635, "34": 654, "35": 672, "36": 689, "37": 704, "38": 728, "39": 749, "40": 768, "41": 786, "42": 803, "43": 819, "44": 838, "45": 856, "46": 874, "47": 888, "48": 903, "49": 920, "50": 933, "51": 953, "52": 975, "53": 998, "54": 1019, "55": 1043, "56": 1059, "57": 1079, "58": 1095, "59": 1111, "60": 1127, "61": 1142, "62": 1163, "63": 1178, "64": 1202, "65": 1216, "66": 1242, "67": 1270, "68": 1288, "69": 1305, "70": 1326, "71": 1347, "72": 1365, "73": 1385, "74": 1403, "75": 1425, "76": 1440, "77": 1455, "78": 1478, "79": 1501, "80": 1515, "81": 1535, "82": 1556, "83": 1575, "84": 1594, "85": 1616, "86": 1635, "87": 1653, "88": 1676, "89": 1695, "90": 1719, "91": 1740, "92": 1758, "93": 1778, "94": 1795, "95": 1813, "96": 1828, "97": 1843, "98": 1860, "99": 1877, "100": 1893, "101": 1910, "102": 1936, "103": 1958, "104": 1980, "105": 2000, "106": 2023, "107": 2044, "108": 2061, "109": 2078, "110": 2099, "111": 2123, "112": 2142, "113": 2159, "114": 2196}
---

**Dave Jones:** Hi, it's mini project series time and I probably could have done this little project as just like one video, like here it is, and Bob's your uncle, but I thought it's more interesting just to show like the process as I've done in some previous videos and it's only a very simple one, but you might get to know that a lot of, there's a lot of tedious business that goes into even like the simplest project.

**Dave Jones:** So this project has actually got a very niche application, but you might see why in future videos, but what it is, is basically I want a board about, I don't know, yay big, something like that, haven't decided yet. It'll, once again, you know, like open-ended kind of specs, which could be good and bad, but I want like a little board like this that has a little e-ink display on it, and e-ink's important for a specific reason,

**Dave Jones:** that has basically just a counterweight. So I want a board that has a counter on it, and every time that you power up this board, I want the counter to increment by one. Why? Well, it can be useful as a product, as an integrated product power-up counter, like how many power cycles has this particular product gone through?

**Dave Jones:** And there can be various applications for like something like this can be like buried inside the product for like, you know, servicing reasons or something like that, or it can be actually displayed to the user. for whatever reason you want and I might go into that in future videos and the reason for e-ink is

**Dave Jones:** because I want the display to always be there so even if you remove the power of this board you can instantly see the uh the count there and it doesn't require any power at all to actually retain that count so anyway I won't go into too many more reasons but basically I want a little

**Dave Jones:** e-ink display it's going to need a little microcontroller and that's it and possibly the board will like have uh castellations on the outside so it can be a module that you actually like can solder onto uh your product board like a little like surface mount module so to speak so

**Dave Jones:** anyway um this video will be about looking at e-ink displays I thought well let's go let's try and find an e-ink or e-paper display I think e-ink's a trademark of e-incorporation or whatever a lot of people call them e-paper displays generically these days so let's have a look

**Dave Jones:** to see what we can find shall we now of course I could do this with a dot matrix a little dot matrix one I think I've even got like an an e-ink dot matrix display here of probably about the right size like this but

**Dave Jones:** um anyway it's somewhere I could probably dig it up but don't necessarily want a dot matrix like it'd be easier and simpler for the project if I just use like a seven segment display and you can get e-ink seven segment display so let's go um or just do not seven segment but segment display so

**Dave Jones:** let's just go with that and I'll see you in the next video just google it shall we here we go graphic no we don't want any of that rubbish uh waves you know no it's all graphic it's all graphic ink display bingo we're in like Flynn straight away let's go

**Dave Jones:** have a look at that that that's what I want uh digits six digits is plenty for a power up display what's this one report image yeah I'll report it it's pornographic um alibaba um yeah e-ink high resolution uh display kits so here you go maybe something like that that looks like a really annoying ribbon interface

**Dave Jones:** though I'd prefer something that I could just maybe solder down onto the board perhaps oh that's interesting look at that I know you're probably screaming oh I know you know oh look there's a starburst display I like that one two four see eight digit starburst display that'd be nice for

**Dave Jones:** that that looks time 1.24 inch yeah that'd be nice for like a calculator um as in a calculator watch on this desktop calculator rubbish oh look at oh here we go flexible oh there we go too but that's another eight digit job and that one oh I like I like the

**Dave Jones:** can cart what's cancart.com I like the look of that anyway I'm just like Google like randomly Googling at the moment this is how you might start or of course you might jump immediately to one of your catalog supplies like digikey or something like that

**Dave Jones:** so that's a flexible 1.2 inch so yeah 1.2 inches that's about the length I need that'd be that looks like it'll do the business and you can make like you could glue that down to the board for example and you can even put your chips under there if you're really you know if you're um if it if it's

**Dave Jones:** flexible you can like solder it down one end like this and then like reflow it down one end and then you can even snake it up and over your chips if you wanted a really small module something like that like this is don't take this video as the best way to do it I'm just randomly doing stuff so we

**Dave Jones:** could go like we could go to digikey have a squares or e-paper what is the uh what have they got display modules character and numeric only six items opto electronics let's go into display modules have they got one specifically for I don't think they have one specifically for e-ink LCD character and

**Dave Jones:** metric 1450 do that yeah e-incorporation so yeah that includes so e-inks are included in LCD ones uh there we go e-ink segmented display uh super right so it's only got that one category there's no more filters there that's just like size and stuff like that so we only got six only got six

**Dave Jones:** in there and there you go that one we saw before that was a digi key job but that is a discontinued discontinued a digi key and that's from that's actually um from e-incorporation so that's a genuine one like a dot bar graph thing isn't that

**Dave Jones:** cute so like for battery gauge or something like that but look at that's a better battery gauge I like that one geez and there's no um interface chip rubbish for that you can just drive that directly that's nice so what do you do just uh you know apply that uh I'm not even sure of the

**Dave Jones:** logic levels for ink I I just haven't played with it outside of a driver sort of thing I've never used actually directly like that can you just drive it of course set it once the good idea thing about e-ink is that you set it in one polarity on or off and it stays like that which is fantastic

**Dave Jones:** um so can you just like pulse that with a regular pin I don't know data sheet sunlight read all wide viewing low power consumption it's going to have no power consumption 650 microns wow thick thickness that is doesn't give you any other uh drive voltage 15 volts or five volts

**Dave Jones:** I don't know 3.3 looks like it's not going to do it though and sure enough if you go into e-inks uh one here they've got ones for watches and and stuff like that but we can go into shop look at these they got like watch displays and things like that but it looks like um they don't have

**Dave Jones:** if we go into e-ink display modules looks like yeah they've they've discontinued this by the looks of it yeah it looks like they've discontinued that uh seven segment looks like e-ink don't make seven segment display modules anymore there you go that's why did you key discontinued it I'm assuming so anyway like I don't want something that's

**Dave Jones:** discontinued even if like they had stock left like you know if you if you know you only need like you know a 10 or 100 or something that's you know fine you can do like a one-off buy something like that if you can find some new old stock somewhere but uh anyway so it looks like did

**Dave Jones:** you key don't have what we want I'm assuming mouser aren't going to be any better oh look at this parallax micro artifruit wow mouser are really carrying a lot of the make crowd supply really carrying a lot of the maker stuff display development tool adapter board wow they're really getting into that aren't they don't

**Dave Jones:** really want to develop why is it in display development tools what like engineering tools embedded Solutions engineering tools for a flexible e-ink display I I I don't get it like I know it's like a mod it's kind of a module but it's really just the

**Dave Jones:** display isn't it I mean I I just don't understand that at all that's just that's silly crazy characterization don't like that at all anyway I think mouser are a waste of space so as is uh genuine e-ink and looks like digi keys out so what we're going to do is uh okay it's Ali Express time

**Dave Jones:** spandex what I didn't search for that it's just a fault give me a break anyway um ink ink segment let's put the dash in there no let's try e-paper no doesn't like that seven segment e-paper display display e-ink segmented display look at this um alibaba.com okay well so we can go to Alibaba

**Dave Jones:** couldn't find anything on Ali Express Aliexpress is just the if you don't know just like the in-stock version of alibaba.com the alibaba.com is the Marketplace where you find you might get prices if you're lucky or you get ballpark prices usually you got to contact them

**Dave Jones:** it's just a place to advertise stuff that you have available whereas Ali Express you can actually specifically add it to your shopping cart buy it boom it's yours that's the difference so Ali Express really didn't have anything there so let's have a look at this so that one's yeah it's not big

**Dave Jones:** in that there we go that looks like an LCD display e-ink circular wow that's interesting mini e-ink for e-watch there you go but it's just got a watch display I think we need more than uh four digits so I think you know we need like six something like there we go now that that looks photoshopped

**Dave Jones:** that does not look oh wow look at that that looks photoshopped as well that looked pretty genuine this one though is interesting check this out this is like is that a that that's with the backlight wow I like that I don't care like it's obviously designed for a

**Dave Jones:** like a scale or something like that but it doesn't matter that uh it has those extra characters you don't have to use them oh they'll look okay they're showing their different things so yeah like quantity one to ten thousand you don't know estimated time ten days negotiable like

**Dave Jones:** can you design your own don't don't want to design my own I just want something off the shelf that looks so photoshopped doesn't it that's the real back of it though how they that's that that's photoshopped as well photoshopped it nice work but yeah obviously like like you you tell them

**Dave Jones:** you want this and they'll go oh oh five thousand pieces minimum order but you know if they're well they wouldn't be like cents each or tens of cents they're going to be like a dollar or something each but yeah so it looks like you know that's neat but that's sort of like a custom kind of thing smart

**Dave Jones:** electronics what's a smart electronics no one I like this starburst it's only got two decimal places that's really interesting anyway there's a driver on that oh there you go you can get model number of the drive I see and stuff like that so you can start you know once you go in there

**Dave Jones:** and find stuff that like that you can go okay how do I drive these um sorry search for PDF and good display repository daily good display ultra wide there you go so that's no that was the no that was the product that's the that's the data sheet that's not just the drive I see yeah no that's the model

**Dave Jones:** number I thought that was like the part number of the uh of the driving interface gooddisplay.com check this out dot like defect line defect is that a thing in e-ink displays is it how they can like manufacturing defects in your uh your lines and your dots that's interesting um yeah that's not a that's not the driving

**Dave Jones:** chip that doesn't even have a pin out and therein lies one of the dangers I'm gonna do a search for character e-ink display and see if we get oh I like hello hello I like like the look of that that looks like a PCB mountable module that's what I'm after is another one the character

**Dave Jones:** e-ink there's a pin based one dollar to ten one piece minimum order well e-ink yeah they they look like LCDs all right that did the business it's often it's just a matter of getting the right keywords don't just rely on one keyword and then just give up or one string of

**Dave Jones:** keywords and give up and go oh I can't find what I want you know experiment with stuff seven segment if you don't like seven segment hey just take away the seven it might be segmented display it might be starburst display it might be character display like this one for example so I think character was

**Dave Jones:** the uh keyword it was like yeah eight eight character or eight digit you might search for digit uh e-ink display or e-paper I haven't searched for e-paper display yet look look at that I really like that that one hasn't got pins attached or if they photoshopped two four like six

**Dave Jones:** that that'll be fine that gives you a million power-ups you have one message look we can talk to whoever it is over here with the fake photo so there you go model number and of course we don't need anything like that don't need anything fancy drive voltage three volts so this would have a

**Dave Jones:** glass and this would have a chip on glass uh driver I would assume you know it's got to be under there I assume it's under there or is it just like a multiplexed thing anyway I really like that is that the same there's the same that's the same one okay so it does actually

**Dave Jones:** have the pins so I think they photoshopped same as beauty KP beauty English Alibaba.com it's the same as this one but they've yet they've just photoshopped out the pin so it's a through hole one and uh I'm sure you could order them without the pins if you wanted

**Dave Jones:** uh two or you know shorter pin different lead length or something like that you don't really want a through hole one because if you're the problem with through hole is that is if you've got a board like that and the pins penetrate the bottom then you've got these conductive pins like

**Dave Jones:** you've got to cut them flush otherwise the thing doesn't flush on the board and then you crack your joints it's not great like you can um but you know it's it's not terrific so it's got to like sit off the board like that and then once it's if it's got pins on the bottom sitting off the board then

**Dave Jones:** those side castellations on the little half moon uh pads on the side of the board it doesn't surface Mount nearly as well you've got to put a lot more big solder blob on there in order to surface Mount it so yeah it's it's not terrific of course you could bend the pins out something or you can cut

**Dave Jones:** them off before and then like surface Mount that once again you could have your chip because we're going to have to have a microcontroller in here I should just block it shouldn't I um you should just you could have your chip could easily fit

**Dave Jones:** under this thing so all your circuitry required on the board could fit under this so your board is exactly the same envelope as or shape size as the LCD and that well apart from the castellations at the side for example so that'd be really cool I know we've transitioned into LCDs now so you can

**Dave Jones:** go to ebay and uh looks like epaperdisplay.com there you go I I just found a an online supplier I didn't know about e-paper display oh this is good display didn't we see them before yeah okay there you go they look serious okay so once you've found a manufacturer like this you would um trawl through

**Dave Jones:** their website and uh and see what you can come up with but yeah that looks really terrific that comes I I assume they look like a manufacturer I guess what do they got there that's a little that's nice isn't that little three I like that wow a little three digit jobby in a dip package with a battery

**Dave Jones:** indicator and a little audio display I that's cute so there's our data sheet there you go so you've got all the pins dimensions come standard as I said you know if you want to yeah no that's it a segmented display there's no driver I guess we have to Google how to drive e-paper displays now

**Dave Jones:** don't we drive in e-ink displays essential scrap no renaissance there you go the devcon devcon from 2012. which one did I go to I was I at devcon in 2012. no it was 20 2009 2011 probably anyway so this is from e-ink I I'm going to assume that there's not you know huge differences

**Dave Jones:** between them then it could be let's get technical display cell structure wow must have its own dedicated driveline the top electrode must be in opposite States when charging pick it moves up or down in the capsule and that's how it that's how it does its business that's how it stays there

**Dave Jones:** permanently display driver MCU yeah don't want that oh yeah here's the five or 15 that we saw before operating between 0 5 or 0 to 15 volts all segments and field of black so there you go so we can just um alternate the thing and you can do that if you like assume you've got a five volt micro

**Dave Jones:** controller you can put it on two IO pins um each segment between two IO pins multiplexing is a different beast but you can put it in between there and then just flip you know one zero one zero like that and you could uh turn your and then of course set it to tri-state when when you don't

**Dave Jones:** want to drive it because you don't have to leave the drive voltage there and uh that's that's cool it looks like we can just flip it back and forth there you go and once again like I have not looked into e-ink drive voltages before so yeah I I just

**Dave Jones:** don't know but it looks like yeah they come in a couple of different types I I only want this as kind of like a one-off or it was a do-it-yourself project and other people can build like the one else and stuff like that so a dip would be fine and what I do is actually cut the leads off

**Dave Jones:** right at the base there and then I'd I'd have like small holes so it could like self-align it just in and then you solder it on the top so then you don't get any penetration of the pins through to the bottom and then that would leave enough you could actually measure that you could you know

**Dave Jones:** that's that's the scale you could actually uh print that out and figure out what the distance between there and there is so the so the gap in there that would be the height you have to put all your circuitry underneath there and that that looks like plenty uh what is it seven and a half

**Dave Jones:** and I estimate that's you know two millimeters something like that you know that's that's plenty of height to put your chips under you know little SO packages or whatever so uh you might you know you might have to get some thinner ones if you're doing that but and your passives won't be a problem

**Dave Jones:** so that's anyway I I think we've found like yeah these ribbon cables are just you know for certain products they're great but in this case I don't I just want like a little board like this I just solder the uh LCD LCD the e-paper e-ink display on it and Bob's your uncle a few of those and we

**Dave Jones:** can just experiment a good thing about the dip one just whack it in a breadboard and we can just have a play around with this thing experiment using a dip microcontroller we can do all this on a breadboard this is great like you know we don't have to get any sort of board manufactured or

**Dave Jones:** anything we will get one at like 2008 that's really quite uh that's really quite old isn't it no hang up like LCD driving voltage this is LCD oh oh I've come a gutser completely come a gutser this is an LCD uh yep they do LCDs as well and monochrome LCD I think if we go in there I yeah I think we've come

**Dave Jones:** a gutser damn it's not an e-paper display ah segmented e-paper display that's what I want maybe you can't get them with just like a direct drive can you oh man got all excited there look at this 0.9 inch flexible I I don't want flags I want a little bar graph no no I I don't I just got crapping on about all the

**Dave Jones:** advantages of the pin based one and I completely come a gut so I'm just going to leave that in the video I'm not going to edit it out this is me like you know doing my thing like learning about uh what's available in the e-paper display marker just bumming around and once again this is all

**Dave Jones:** the work you've got to do uh like it's not like I instantly know oh yeah I could just get that particular partner but e-ink display I don't know that I'm just bumming around looking to see what's available yeah no look this is not e-ink right this is this is LCD it looks like

**Dave Jones:** an LCD smells like an LCD right and I think they've just put e-ink in there to get you in so yeah you've got to watch out for that 12 o'clock yeah viewing angle yeah like we're a bias ratio a third we're talking about an LCD here completely come and go see I got all

**Dave Jones:** excited thinking that we can get these pin based e-ink modules and nope nope once again static drive one yeah one bias yep no that that's all that type TN twisted pneumatic you don't see twisted pneumatic associated with e-ink displays because it's an LCD thing ah give me a well there you go

**Dave Jones:** learn something I hope you've learned something too I don't want that why can't I have that and here's where you start like second guessing yourself and going oh maybe we could have an LCD display and they're so low power we could have one of those super slim super caps on

**Dave Jones:** there that would just keep it all be always on it'd keep there and every time you power it up it'll recharge the super cap and yeah yeah you know you could it could it may come it it may come down to that oh now I'm thinking that you know that's a good idea because you can get

**Dave Jones:** these really thin super caps now and yeah the amount of power required to drive a little LCD um leave it in the comments down below if you think that's a more sensible idea uh to have the LCD with like a super cap is that

**Dave Jones:** is that a more exciting project I like e-ink like no it's LCD they're lying once again that's a good display one e-paper display and uh I've seen these at the checkouts look uh the promotion I've seen these at some supermarkets um have these they have these little e-ink

**Dave Jones:** uh tag displays now and of course they don't need power to run fantastic that they can just go up with a little uh programming machine and just reprogram the thing or they might have more net no I don't think they're networked they might have to go up and just manually change or whatever like

**Dave Jones:** they did with the paper uh prices and stuff like that so you know they've got a whole bunch of employees going around putting on you know 50 off special stickers and stuff like that well they can just stick on their little uh programmer and change the display

**Dave Jones:** so that looks so photoshopped it's terrible Muriel anyway I'm not having much luck it looks like the segmented e-paper displays are in a form that I don't physically like I don't know it's just like I can make it work but it's just annoying that that's it that's all they got

**Dave Jones:** like it's suitable do the business two four six and well one with a little but you know that's fine no no I need more chocolate it's not actually chocolate it's carob milk carob highly recommended beauty I do actually have these uh sharp memory display LCDs in the right form

**Dave Jones:** factor of course with a bit of annoying ribbon cable you'd have to put a connector and all that they aren't um actually e-ink or e-paper display you do actually still need power to make these available you don't have to continuously uh drive them

**Dave Jones:** and they're incredibly low power though like ridiculous like a couple of microamps or something like smell of an oily rag stuff so yeah like if you're going for a potentially some sort of like super cap uh solution or something like that you know and one of these um memory LCD displays is

**Dave Jones:** a possibility but eh segmented e-paper display um it displays as graphic ones so you know we might have to go for a graphic e-ink solution I guess it's not what I want like I you know because I don't want to have to implement like fonts and everything in my microcontroller and all that just want to be

**Dave Jones:** able to like have some real simple code that just like drives segments and and has a counter like and we don't want color e-paper display and stuff like that anyway let's go back e-paper display generically yeah there's there's an example of those uh tags the uh supermarket shelf label display

**Dave Jones:** you know that was a full like full color jobby that's nice seven bucks though see yeah it looks look yeah it looks like you can get these these tags let's just like out of curiosity let's just have a look at these because these they actually sell them like in a framed module like as it like

**Dave Jones:** a tag that actually just goes straight on that's that that's really quite cool I like that what's what's the interface yeah yeah look look they they sell the uh the label machine they sell the label machine and everything and what's what's that one what is what is number one there it looks like it's some sort of

**Dave Jones:** oh is that it no is that a charging because they wouldn't need these are e-paper display they shouldn't need any sort of charging anyway that's another whole fascinating like electronic like it's a whole segment now it's a whole industry segment and there's just tons of those if you're

**Dave Jones:** really wanted to get into it I want one in like a long thin form factor like this one I showed and maybe I'm mixing up I thought I had an e-ink version of one of the like a similar shape to this but maybe it's not maybe I'm actually thinking of the sharp memory LCD once again

**Dave Jones:** they claim that this one is an e-paper display oh no LCD display screen now once again it's got LCD this is not e-paper I squared C serial interface refresh time reflectivity angle of contrast and that could genuinely be eating yeah once again you can request data sheets and stuff like that

**Dave Jones:** I obviously can't do that right now so I don't want Square I want like that's really not pulling up that's really getting out of uh ink e-paper to Slay's uh pervasive oh Crystal fonts yeah I thought you know I didn't think to go to one of my regular LCD

**Dave Jones:** uh suppliers and check those out looks like pervasive displays they're really targeting that that that shopping thing you'll see that everywhere eventually like even in the uh mom-and-pop stores you'll find those there so you know these are still like too thick I just want even if I went for a it's not looking great is it this is nice

**Dave Jones:** they you know you can get a nice little SPI adapter board that's that's really great for uh development so that's that's their e-paper displays hmm open source demonstration code works on the c-duino nice yeah I just don't want a dot Matrix so maybe this one over here I might try and get some data on

**Dave Jones:** that but I really don't like the interface I'm not liking this at all it's it's driving man another one of these projects that you know you think is uh quick and simple I'll just find a little e-ink uh display module just you know shaped like this and and maybe with like a nice flat uh you know

**Dave Jones:** pin well maybe not a pin interface but you know it's something easy to easy to do onto a little module board and well no no it's not looking great I mean you know what have I only I've only been at this for like an hour or something uh but it's it's not looking terrific so it's always pushing

**Dave Jones:** towards that silly uh idea of well may not be so silly of a like a super cap and a and an LCD or a sharp memory LCD but I really like that uh display that I saw I really like that pin one with the six

**Dave Jones:** digit or whatever that that it's near perfect anyway maybe that'll be a more interesting project to get it like a little super cap and a micro or something and it just like yeah but unfortunately the problem with that to keep it update if you don't use the good thing about these sharp memory LCDs is that basically

**Dave Jones:** you just need power on it like you don't need to keep updating and refreshing and stuff like that whereas if you had an LCD equivalent and you were driving it with an LCD microcontroller of course that microcontroller is already it's got to be constantly keep running of course you're running

**Dave Jones:** it you know 32 32 kilohertz like low power mode or something but still you know it's gonna it's gonna suck some juice but it might be adequate because I don't necessarily want what is the battery life I want for this thing I don't know it's a shoulder

**Dave Jones:** shrug um like you know it's got to be like 12 months or something like that it's got to like be 12 months or a couple of years something like that from each charge so maybe we can uh go through in another video perhaps give me a thumbs up if you want to see that uh where we could like look at

**Dave Jones:** thin but potentially even if we don't go that way we can look at thin uh super caps and how they can potentially or you know in any sort of format super cap um you can even get surface mount super caps now maybe one of those little surface mountable like you can get them in like

**Dave Jones:** 1206 type surface mount packages now which is really amazing maybe we could get one of those on do the calculations for the current drawer of a typical microcontroller typical LCD just to keep a number displayed on there and is that possible um to like get a year's worth out of a

**Dave Jones:** single charge from a super cap probably doubting it like just off the top of my head like I wouldn't expect it to last that long like a year or two but hey you know you never know until you do the calculation so uh have I come a gut so it's probably this video is probably long

**Dave Jones:** enough so anyway I know there's not a happy ending here I haven't found a like you know is that like is that really like this photoshopped one though like what what the like that that could be good if this is real like is that a real thing like once again I'd have to get a data sheet the model number

**Dave Jones:** wow um and that one it seems like it could be an actual e-ink e-paper yeah e-pay DKE DKE group part covers an area 25 000 square meters construct looks like they got there that's a serious DKE okay and this is actually DKE yeah DKE limited

**Dave Jones:** okay so this is an actual e-ink display manufacturer so it turns out uh DKE is uh China epaper.com and yep they have a whole segmented uh display type here so these are the real deal and uh unfortunately there is no like uh kind of for more information yeah product specs

**Dave Jones:** so you've got to contact them to get your uh spec which I'll do it's 54 millimeters by 14. bit bigger than I want but you know I I can work with that in mill it's not 0.1 millimeters no I think it's 0.5 there you go so not sure what the deal is there but anyway uh yeah we can contact them

**Dave Jones:** online chat send them an email I get the data sheet for that but anyway they do this is they have a segmented code type here we go oh wow wow hello hello McFly custom e-paper right that's just um the active area can make 600 segments with six chips cascade connection modular flexible

**Dave Jones:** e-paper display blah blah blah so yeah if you want a custom e-paper display maybe I could do a custom e-paper display for some use I wouldn't do it for this um but like like I did for the LCD my um the custom LCD video series that was uh that was popular anyway um five there's a five-digit jobby

**Dave Jones:** look at that so you know we we have a few options this one here could be smaller than that one 33 oh by 70. okay oh but that's that includes the ribbon and stuff like that but once again damn ribbon you gotta yeah

**Dave Jones:** anyway that that looks really funky doesn't it it's really remarkable like they don't show any gap between the segments in there so I'm not sure what the deal is anyway 28 and a half by 14. that looks like the go and that one's got like a hot bar attachment

**Dave Jones:** you could uh well you could reflow that down you could just get your hot air gun on there and or even a soldering iron across there if you once you had your uh tinned or your uh whatever or your solder paste pads on there pin pitch looks like a mongrel though um don't like that but anyway um yeah I'm

**Dave Jones:** gonna get data sheets on uh these but uh China e-paper display so it looks like we've got some solutions here so you know reasonably happy ending there but uh if you know of any others please leave them in the comments down below I'll talk to my good mate uh Sophia do a thousand quantity minimum it's not really what I

**Dave Jones:** want but I don't know maybe the ad revenue from this video series can pay for even though I only want a couple you can pay for my thousand minimum pieces so if you've got a link to a suitable um e infuser that LCD rubbish leave it in the comments down below please and let me know what you think

**Dave Jones:** about uh if you've got any other ideas for this uh little project that just simply that's all it does is it it's just designed to you know solder into your product and it just counts it increments once that's it when you power it up it increments once and Bob's your uncle that's all I want it for

**Dave Jones:** it's all I want to do not just no feature creep that's all it's going to be so anyway there you go let us know what you think down below and as always I hope you found that interesting if you did please give it a big thumbs up comments down below Ev blog forum all that sort of stuff anyway catch you next time

**Dave Jones:** you
