---
video_id: Fj7e3WGUKO8
title: EEVblog #504 - UPS Tutorial & Teardown
url: https://www.youtube.com/watch?v=Fj7e3WGUKO8
source: youtube-asr
timestamps: {"0": 1, "1": 24, "2": 44, "3": 57, "4": 65, "5": 83, "6": 92, "7": 112, "8": 134, "9": 148, "10": 160, "11": 167, "12": 177, "13": 189, "14": 202, "15": 216, "16": 231, "17": 240, "18": 253, "19": 271, "20": 282, "21": 294, "22": 302, "23": 323, "24": 341, "25": 354, "26": 376, "27": 391, "28": 405, "29": 415, "30": 434, "31": 449, "32": 464, "33": 477, "34": 493, "35": 510, "36": 534, "37": 557, "38": 583, "39": 598, "40": 619, "41": 630, "42": 643, "43": 665, "44": 676, "45": 689, "46": 698, "47": 718, "48": 736, "49": 746, "50": 763, "51": 772, "52": 782, "53": 797, "54": 812, "55": 824, "56": 839, "57": 852, "58": 869, "59": 885, "60": 903, "61": 916, "62": 924, "63": 936, "64": 953, "65": 967, "66": 983, "67": 1007, "68": 1021, "69": 1047, "70": 1065, "71": 1085, "72": 1103, "73": 1119, "74": 1127, "75": 1143, "76": 1156, "77": 1171, "78": 1181, "79": 1194, "80": 1206, "81": 1223, "82": 1245, "83": 1253, "84": 1265, "85": 1285, "86": 1298, "87": 1310, "88": 1324, "89": 1341, "90": 1351, "91": 1360, "92": 1374, "93": 1389, "94": 1403, "95": 1415, "96": 1433, "97": 1447, "98": 1461, "99": 1474, "100": 1487, "101": 1507, "102": 1519, "103": 1535, "104": 1547, "105": 1561, "106": 1573, "107": 1588, "108": 1610, "109": 1622, "110": 1636, "111": 1651, "112": 1669, "113": 1681, "114": 1697, "115": 1710, "116": 1722, "117": 1739, "118": 1750, "119": 1766, "120": 1776, "121": 1791, "122": 1817, "123": 1833, "124": 1855, "125": 1881, "126": 1891, "127": 1913, "128": 1924, "129": 1942, "130": 1958, "131": 1974, "132": 1994, "133": 2002, "134": 2019, "135": 2028, "136": 2050, "137": 2061, "138": 2079, "139": 2092, "140": 2104, "141": 2122, "142": 2136, "143": 2146, "144": 2169, "145": 2183, "146": 2196, "147": 2205, "148": 2214, "149": 2226, "150": 2238, "151": 2246, "152": 2264, "153": 2275, "154": 2290, "155": 2302, "156": 2311, "157": 2326, "158": 2350, "159": 2357, "160": 2378, "161": 2390, "162": 2408, "163": 2418, "164": 2429, "165": 2440, "166": 2453, "167": 2468, "168": 2482, "169": 2497, "170": 2510, "171": 2525, "172": 2535, "173": 2545, "174": 2562, "175": 2574, "176": 2595, "177": 2609, "178": 2623, "179": 2635, "180": 2651, "181": 2665, "182": 2675, "183": 2688, "184": 2697, "185": 2710, "186": 2719, "187": 2730}
---

**Dave Jones:** Hi, welcome to teardown Tuesday. Yes, I'm at the whiteboard. We're not going to jump in to the teardown. Thought I'd just do a little bit of white and board fundamental theory today and then we jump in to the teardown and see if we can see a similar arrangement to what we get in the basic topology of in this case uninterruptible power supplies or UPS.

**Dave Jones:** You've no doubt heard of them. You're probably using one at home to backup power your PC for example when the mains power fails then the battery inside the UPS takes over and supplies power for 5 or 10 minutes or maybe even longer so that you can continue to use your machine or at least it gracefully can gracefully shut down and save your work for example.

**Dave Jones:** So if the power just fails boom, it doesn't just shut off and you lose everything. So very common device the UPS. And there's actually three types so basically three different topologies.

**Dave Jones:** There's a few more but these are the three basic types which will have a look at. There's the offline standby type probably the most popular you'll find in the really cheap ones.

**Dave Jones:** There's line interactive which is the one we'll take a look at today in the teardown and there's the full online / double conversion type which is the more expensive and reliable types for the more robust applications.

**Dave Jones:** So if we take a look at the basic offline standby one you're probably familiar with how they work. We've got AC mains coming in here. AC mains going out.

**Dave Jones:** That's it. And inside we've got ourselves a AC to DC rectifier here. Yes, it's just a traditional bridge rectifier or whatever and that goes into a charger which then charges the battery and then the battery goes into a switcher or which is usually a H bridge arrangement but it doesn't have to be.

**Dave Jones:** But it basically a switcher driving the uh of a transformer and the secondary of the transformer produces your sine or your square wave out. And then they've got a basic switch in here which can uh usually this thing by meaning offline, it means that the uh the charger and battery part of it is usually offline.

**Dave Jones:** So, it's switched out and your AC is switched directly through to your output like that. So, only when it detects that main input mains power has failed, does it rapidly switch over.

**Dave Jones:** So, I haven't shown any switch in here, but it rapidly uh starts up the uh inverter in here, your step-up uh conversion here, and generates your sinusoidal or square wave output voltage.

**Dave Jones:** And it you can usually, you know, it can take it from, you know, tens of milliseconds or 100 milliseconds or something to sort of switch over and start up.

**Dave Jones:** So, the device that you're actually powering has to be able to handle that little uh sort of, you know, drop out or brownout as it uh switches over to the battery backup.

**Dave Jones:** Now, that is uh the cheapest and most uh common one. Now, I'll skip this line interactive one for a second, and we'll jump straight down here to the online {slash} double conversion type.

**Dave Jones:** You'll see why it's called double conversion in a second. Now, the difference between these two basic types is that this is the offline type, as I said, the usually the output is powered directly from the input, it's switched straight through.

**Dave Jones:** So, it's the uh battery backup part of it is offline, but you guessed it, the online type is where the uh battery is continuously powering the output here regardless of what the input is doing.

**Dave Jones:** And that's why there's no switch going through the AC input through to the AC output, cuz it's all that power is always coming, well, not necessarily coming from the battery, but actually coming from the DC rectifier down here.

**Dave Jones:** And you'll notice that all of the, you know, all the common components are still there. They're virtually identical. We've got our AC rectifier down here. We've got our battery charger.

**Dave Jones:** We've got our battery. We've got our switcher with our step-up transformer to generate uh either your sine sinusoidal or your square wave output. But, you'll notice that there is no switch connecting it can't bypass any of this stuff.

**Dave Jones:** It's always working. And what we're switching here, instead of switching from input directly to output, we're switching basically whether or not we want to power the output from the battery or from the rectifier circuit down here.

**Dave Jones:** And that's one of the big differences. Uh one of the main reasons you want to do it is for isolation. For example, you'll notice that there's no directly direct electrical connection from the output to the in- input.

**Dave Jones:** I.e., it's galvanically isolated. So, if you if your uh the device you're powering needs to be electrically isolated from the input, then an online or double conversion switcher is the way to go.

**Dave Jones:** But, as you can see here, there's no isolation. Even though we've got a transformer in there, you'll notice that it's all common like that from the input to the output.

**Dave Jones:** And the other main reason why you want to use the online one compared to the offline is that uh if you've got a real noisy mains and it's always dropping, there's always brownouts and dropouts, and all sorts of stuff, you don't want this thing to be continually switching back and forth between the uh input and the input and the battery, for example.

**Dave Jones:** You're much better off on those noisy in those noisy and troublesome environments to go for an online conversion, where it's just always running from the DC here. And that's why it's called double conversion, because we're converting AC into DC, and then it's permanently the output here is permanently running from that DC connection.

**Dave Jones:** It's not switching through the AC and then switching between AC and DC sources effectively. It's always powered from that DC source. That's why they call it the double conversion cuz you're converting once and then you convert it again.

**Dave Jones:** Yes, this one does it up here, too, but there is the option to switch through with no conversion at all. Hence the name double conversion. But one of the disadvantages of this double conversion type is that Well, you notice that this switch down here is switching the low relatively low voltage battery for example, 48 V battery might be typical.

**Dave Jones:** They might be using 12 V for example. Then lower voltage Ohm's law still must apply, right? That means for the same amount of output power delivered to the load, you've got much higher switching currents in here.

**Dave Jones:** So, I've shown this as a, you know, a mechanical switch or relay, and the topology doesn't exactly need to be like that. But it it basically means you've got very high switching currents in here that you have to switch from the battery.

**Dave Jones:** Uh up here, if you're got, say for example, a typical 10 amp mains outlet, well, you only need a 10 amp relay in there. That's it. Not a problem.

**Dave Jones:** But down here, you need much, much higher current. So, the switching can be an issue down here. And also, this rectifier down here has to deliver the full load all the time because you notice when it's not powered from the battery, it's got to deliver all that power from that poor little rectifier down in here.

**Dave Jones:** Whereas here, the rectifier is only only needs to be um sized enough, designed well enough to deliver enough power to charge the battery, which might be much, much less than the output load is capable of.

**Dave Jones:** So, that's why these things are more expensive and more difficult to design. They're going to run hotter, things like that cuz the circuitry inside is got to deliver that full load, and then you've got losses in there, and the switch is always got to be operated and delivering the output load.

**Dave Jones:** Whereas up here, your switcher or output load might only need to be sized and designed for operation for 10 minutes, 30 minutes, for example. But this thing, it's got to work all day, every day, 24/7.

**Dave Jones:** So, this thing needs a lot more cooling and much better design system. So, that's why it's typically more expensive to design an online UPS. So, that brings us to the third type, which we're actually going to look at in the teardown today, is what's called a line interactive UPS.

**Dave Jones:** And it's essentially exactly the same as the offline standby type, but it's a bit of a compromise between these two in that, let's say you've got, you know, a and mains input here, which sort of, you know, brown and browns out or drops out, you know, a couple of times a day.

**Dave Jones:** You don't want the thing always switching over to battery. So, instead of it switching over to battery, what they include in here, you'll notice it's virtually identical, except for the fact that in this path here, where it's the AC is switched through, there's actually what's called an auto transformer in there with various little taps with some other switching relays in here that can then, or you know,

**Dave Jones:** doesn't have to be a relay, it can be an electronic switch as well, then it switches between the different taps on the transformer. So, let's say your mains input, normally 240 volts, it drops down to 220 or 210, then bingo, what they might do is then switch to this tap here, which then the output voltage is going to be boosted up a bit.

**Dave Jones:** So, you're still going to get your 240 volts out. It can compensate for small variations, you know, 10 or 20% variations in your mains input. If your the device you're powering cannot handle that, and then likewise, if the mains input here goes up, goes above what your load, you know, I really wouldn't like to have, then it can switch in this tap here can switch over to here and then

**Dave Jones:** you'll notice that the output is going to be somewhere below, because it's a different tap, somewhere below that mains input voltage. So, it can accommodate both higher and lower input voltages without having to switch over to the battery backup system.

**Dave Jones:** So, that's what a line interactive UPS does. Sort of a compromise between those and that's what we're going to take a look at now. Oops, I forgot to include that little line in there powering our AC rectifier there, but when we take a look at our teardown now, which we're going to do in a second, we expect to see all these basic components in here.

**Dave Jones:** We expect to see a big ass auto transformer. It's going to be big ass because it's delivering all of the full output power load, the full, you know, 2400 watts or whatever, through to the output.

**Dave Jones:** So, that's got to be a big beast. Then we're going to have our rectifier, we're going to have our charging circuitry, we're going to have our battery bank. In the case of this one, I know it's 48 volts.

**Dave Jones:** Then we're going to have our switcher, most likely a H-bridge configuration. We won't know until we turn it until we actually take it apart. The H-bridge configuration is going to have four large MOSFETs in there driving the primary side of the step-up transformer, which could possibly be integrated into the main auto transformer here with another tap.

**Dave Jones:** We'll see when we open the thing and and that's pretty much it. We expect to see some big ass relays to switch the taps or some electronic components to actually switch those.

**Dave Jones:** Instead, most likely we're going to see relays in this thing and that's what we expect to find. Will we? Only one way to find out. Take it apart. And here's what we're tearing down today.

**Dave Jones:** Please excuse the fact that I've got this thing on the floor. It is a massively heavy base. It weighs more than a brick, Donnie, and I'm sure it's built like one as well.

**Dave Jones:** What it is is an APC. They're a top brand in the UPS business, so we expect top quality. It's a smart UPS model 2200 XL. As you can see, a rack mount unit designed for server backups and things like that, three unit high rack.

**Dave Jones:** And yes, I scored this one from the Australian Defense Force auction that I scored a whole bunch of other stuff, as you've seen in a previous video. And this is just a front fascia panel here that just pops off to reveal the control panel here and the internal battery pack.

**Dave Jones:** I do have a second rack mount unit which just contains an extra two sets of batteries as well. And you'll see the other connector on the other side. So, this one can have three sets of batteries hooked up to it.

**Dave Jones:** And it's model number is SUA 2200 RMUXL to be precise. And you can see on the control panel here why it's a line interactive UPS. It's got two LEDs here.

**Dave Jones:** One to show that look, what happens when like to show you indicate that the mains voltage has gone over voltage and then it needs to correct and pull it back down.

**Dave Jones:** So, it needs to switch in that extra tap there. And then likewise down here, if the mains voltage is sagging, it needs to pull it up and correct it like that.

**Dave Jones:** So, obviously it's switching in the taps on the auto transformer there. And there's charge level and various other stuff, bad battery and whether or not I think that LED is for comes on when it's powered from the battery.

**Dave Jones:** And there's some test functionality as well. It's got a Anderson connector on here by the looks of it for the battery bank. And that just uh, swings around and we can pull I've undone the screws on this.

**Dave Jones:** We can pull this sucker out. Needs a bit of percussive maintenance, I think. Hang on. There we go. There we go. We got it. Bit of percussive maintenance and uh, the battery weighs an absolute ton.

**Dave Jones:** More than a brick dunny, as I said. And that will pop out. But the thing is even with that it's still very heavy. So obviously there's a huge monster uh, auto transformer in here.

**Dave Jones:** So uh, we expect to find that. You can see it comes in two models. We got the lower one here, the 2200 W one. Does come in a 3000 W one which uh, maximum input current of 15 amps.

**Dave Jones:** And that's what will and output rating 2700 W. This is 1980 W. So almost 2000 W output power. You see it does have a 15 amp uh, mains input jack there.

**Dave Jones:** Uh, what have got a USB interface. We've got a serial port uh, EPO that's emergency power off. And there's the there's the other Anderson connector the second one that goes off to the battery pack the external one which I've got two.

**Dave Jones:** This I believe is an option slot. There's nothing underneath that so I'm not sure what's actually installed in this thing. I haven't you know, I actually been able to power up and communicate to it or I haven't even tried but there's all the output connectors big whopping 15 amp one plus eight 10 amp outputs as well.

**Dave Jones:** All wired in parallel of course so of course you can't draw 10 amps from each one. You're limited to that 2700 W total. So that's all those outputs are more for convenience sake.

**Dave Jones:** All right, got my cordless drill this time to help out. There's a few screws on this thing. So let's crack it open. And as I said, what do we expect to find?

**Dave Jones:** Well, uh pretty much exactly what we saw on the uh whiteboard there. We expect to find a big ass auto transformer, of course, that'll be the bulk of the weight in this thing.

**Dave Jones:** It'll be absolutely massive. And uh we expect to find a uh rectifier. That'll be uh pretty beefy to handle all the uh charge current for these batteries. I'm not sure what it actually uh charges at, but I'd expect that pretty darn beefy as well.

**Dave Jones:** Has to be, especially when it's uh charging external battery packs. We'll most likely find a huge uh H bridge uh in inverter in there. We'll uh find some massive wiring for the batteries and all that sort of stuff.

**Dave Jones:** And uh the H bridge, because there's so much power involved, um I expect the uh not to use a single MOSFET for each um branch there. There's probably multiple ones in uh parallel.

**Dave Jones:** That'd be my guess, anyway. So, we'll give it a go. All right, let's lift the lid on this thing and see what we get. No, there's nothing else holding it down.

**Dave Jones:** Ta-da! Oh, look at that. We have two transformers. We'll uh get a better look at this beast. I'll set the camera up uh vertical above it, but uh yeah, that looks very nice at first glance.

**Dave Jones:** Wow, beauty. Now, first of all, that was a bit of a surprise. We've got two separate transformers here. I expected one huge uh transformer, but I guess uh I don't know for uh technical or manufacturing or uh performance reasons, they decide to go with two separate ones, but if you'll notice that there's a huge cable over here.

**Dave Jones:** I love the fact that they've actually clamped that down there with a a crimp lug and they've screwed it down. You'll notice that there's no connection from basically this is the this is the primary of the transform well, depends on which way you're talking about your terminology.

**Dave Jones:** If it's powered from the batteries, then this is the primary and then this becomes the secondary. So, we'll just call it the battery side of the transformer. You'll notice that there's a huge bridge joining those two, but there's no tap coming off that into the main circuitry.

**Dave Jones:** So, really it's effectively just one winding there. So, they're using this as one big transformer. So, it's not a center tapped winding on that. So, they're definitely a H bridge to do it and if you have a look down in here, ta-da, you'll be able to see that.

**Dave Jones:** Here's where the wiring comes off and once again, huge big crimp terminals screwed into what looks like the heat sink. Well, it is the heat sink for the power MOSFETs, the switching MOSFETs down in there, which we'll have a closer look.

**Dave Jones:** I'll get the macro lens out, see if we can get some part numbers in there, but they're also using that to carry the current down there as well. And you'll notice that there's one, two, three, four.

**Dave Jones:** So, I that looks to be correct. It looks to be a H bridge because that's the most typical configuration. So, it looks like we're going to have four sets of power MOSFETs here, each on their own thing.

**Dave Jones:** Each on their own little heat sink slash current conductor there. And you'll notice that So, these two, there's one over here. So, this top one is the uh black wire which goes over the transformer or one side of the transformer.

**Dave Jones:** The other side of the transformer goes to this um part of the bridge. And then the battery will be connected to these two inner ones. And that H bridge arrangement switches the battery and then alternates the uh supply onto the transformer.

**Dave Jones:** And we can see that uh H bridge configuration on this DaveCad drawing here. Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it.

**Dave Jones:** What we've got is uh four MOSFETs here. And you can see why it's called a H bridge cuz it looks like a H. If you take out that line there and take out that line there, it looks like a H with the uh transformer in the uh center taps there.

**Dave Jones:** And we've got our 48-V uh battery across here. And we've got uh two P-channel MOSFETs up the top. Or as we'll see uh in this case down here, we're going to have multiple ones in that parallel.

**Dave Jones:** But it's exactly the same thing. They just uh getting higher power dissipation, better power dissipation there. So, um basically, I won't go into H bridge in detail, but basically, you can switch pairs like that, which then you can alternate the polarity on your transformer there.

**Dave Jones:** So, that's how you can switch it. But then if you just switch them off and on and had just a simple square wave uh output, which the cheaper UPSs do because when you turn on a MOSFET, you know, they've got very low on resistance so that when you um uh yeah, if you just do a square wave output, then uh these things turn on hard and there's not a huge amount of

**Dave Jones:** power dissipation in these MOSFETs. Although they try to, you know, there's things with gate capacitance and everything else. But and driving conditions, we won't go into any of that detail.

**Dave Jones:** But because we're getting a sine wave out of this thing, we're going to have to dissipate more power in the MOSFETs, which is probably why they've gone for um the arrangement with, you know, this huge uh huge big heat sink.

**Dave Jones:** And it looks like they got four parallel MOSFETs on there as well. As you can clearly see, that's the configuration we've got. We've got our uh transformer uh hooked on to uh two of the taps effectively on that H bridge, the uh center taps there, and then we've got our battery hooked onto these other two down here.

**Dave Jones:** If we follow the wires, we'll find that they actually these two plates here uh go down to the battery pack. I find it rather interesting that they've got a quite a hefty amount of uh capacitance there across the uh battery uh terminals.

**Dave Jones:** Not sure why they're doing that. They're uh 1,500 microfarads at uh 75 volts. I can't get in there to see the uh brand at the moment, but looks like there's three of those in uh parallel.

**Dave Jones:** And uh of course, not an ideal location being stuck between these two heat sinks, which are likely going to get quite hot. But, as I said, only because this is not a full online UPS, this thing is not used or running 24 hours a day.

**Dave Jones:** So, this is going to be dissipating uh uh you know, nothing uh basically until you switch uh until the mains power fails, and then it switches on, and then drives the transformer to uh power your load.

**Dave Jones:** And it does appear that uh the uh battery the internal uh battery pack is just wired in parallel with these cables which go off to the Anderson connector on the output.

**Dave Jones:** So, it looks like all the battery packs when you use the external ones uh just all wired in uh parallel, basically. And of course, we've just got our positive and negative there.

**Dave Jones:** There's no um smart, you know, there's no like a sense wire or anything like that. But of course, um maybe if they wanted to, maybe they could be passing uh some sort of uh sense data over the uh power as well.

**Dave Jones:** I'm not sure. I haven't gone into the uh details of how that works. I find this rather interesting. Check it out. They've got two fans here. They've got a big ass one here, which is obviously blowing air directly over these large heat sinks here.

**Dave Jones:** So, I presume that that sucker only turns on when you're when it's actually powering the load. Then they've got a small little, you know, wimpy piss ant one down here, which might be running all the time or something like that just to get some air flow through the system.

**Dave Jones:** And they've got an additional fan here, which looks like it just Yeah, I can just put my finger through there and spin it. So, it looks like it's just sucking some air over the battery compartment.

**Dave Jones:** Now, as for the main board down here, there's just one board. It looks like it's all combination of surface mount and through hole just single sided. So, I'm not going to take this whole thing apart because I don't expect there to be anything on the bottom of this board of any note whatsoever.

**Dave Jones:** Looks like it's big enough, sparse enough for all the SMD stuff to be on top. And anything of interest is going to be on the top anyway. So, we've got our mains input over here securely clamped down to the chassis down there with earth.

**Dave Jones:** And remember as I said, because this is a line interactive UPS, it is not isolated. So, the transformer is an auto transformer. So, the output the mains output is not isolated from the mains input.

**Dave Jones:** Anyway, if we have a look down here, I should probably get a shot of that. You can see the flow through here. We've got our input filter here. We've got some these five five relays.

**Dave Jones:** One two yeah, five relays. There's our relays used for we're going to be switching some taps down here. So, here's the Anyway, it it flows through. We've got some protect We've got some common mode choke, line filtering.

**Dave Jones:** We've got some more filtering. Looks like we've got a current transformer down there. And here's our output line. So, it comes straight through the input from the input straight through some filtering and some surge protection and stuff like that and then straight off to your output connectors over there and then we've got the switching of our auto transformer here.

**Dave Jones:** So it looks like these couple of relays around here or these two are probably your high side and your low side auto transformer switch. I can't see any electronic switching.

**Dave Jones:** These things are uh What are they? 20 amps I think. 20 amp relays mains are rated of course. So they're definitely going to be able to do the job and they switch the taps on the auto transformer over here.

**Dave Jones:** So it looks like we've only got one on the high side, one on the low side. So not particularly they're not catering for various steps. It's basically is it higher than a threshold?

**Dave Jones:** Yes, switch on a transformer and then pull the output voltage lower and same thing on the low side as well. Got our fan outputs there. Oops, looks like we've got a second current transformer down in there and uh that's all she wrote.

**Dave Jones:** Let's get some close-ups. Have a look at our input circuitry down in here. We can see a MOV directly on the input there and then we've got a classic common mode filter here, common mode choke with some filtering.

**Dave Jones:** Moving along we've got a couple of extra inductors here and then we've got some more filtering. Large, huge filter caps down here and then there's our current transformer. There it is.

**Dave Jones:** See here? It's even labeled CT. CT1. You can see that they've got a single wire going through a little transformer coil there so they can just get an isolated tap off that and they can measure the current coming from the mains input and they've got our and then we've got a bleeder resistor there by the looks of it.

**Dave Jones:** Then we've got ourselves another current transformer down in there. That would be measuring the output current. And of course I'd be tapping the output voltage as well as the input voltage and reading those so they can get the output power and the output voltage.

**Dave Jones:** So, yeah, pretty obvious. Um mains input here and then we've got our the other one over here is measuring the output and these cables here then bugger off to our output over here.

**Dave Jones:** And as you can see, yep, they're all wired in uh parallel there. So, uh there's not they're obviously got So, they've got a separate wire there going off to the 15 amp jack and then all the 10 amp jacks are wired in parallel.

**Dave Jones:** And we've got ourselves a little Well, not a little, a big ferrite. And I'd probably say that this third relay here is the one that actually switches the input directly through to the output basically until Look, they've got these huge beefy Well, that's actually coming from this one here.

**Dave Jones:** I mean, huge beefy tracks in there. I mean, check that out. Joined in and then the output, of course, big beefy ones going over to here. So, I don't know what the exact topology they're actually using for the auto transformer and the power bypass.

**Dave Jones:** But, yeah, these ones are also got beefy power tracks going through them as well. So, make up your own mind. Trace it out if you want to. And we've got more protection here, another MOV there, and another MOV over there.

**Dave Jones:** So, there's no shortage of protection in this thing as you'd expect cuz they actually claim it's part of the functionality of this UPS is to basically clean up your input mains waveform.

**Dave Jones:** You know, it it filters it and it clamps it with some MOVs and then with the auto transformer configuration actually can slightly adjust and correct for the input voltage.

**Dave Jones:** Now, there's one thing that I'm is starting to puzzle me, I'm not quite sure about, is where is the rectifier and the charging circuitry in this thing. Obviously, look, we've got two isolation transformers down in here.

**Dave Jones:** If we take a look at these, there they are there, but they're you know, really small fry. I mean, you know, not a huge amount of power at all, especially for the battery pack.

**Dave Jones:** So, these are clearly not charging the battery packs. But, if you saw our topology on the whiteboard, then that's what you'd expect. I expected a really big another big transformer in here just and and some big rectification and filtering and everything else.

**Dave Jones:** We've got We've got some filtering happening over here, but it's directly across the batteries rather than at the output of any rectifier. So, I don't see any power rectifier in here.

**Dave Jones:** These are obviously just little low-power isolation transformers to power all the circuitry underneath here. So, I mean, I can take out the fan there, but I don't think there's going to be anything doing there at all.

**Dave Jones:** So, I'm rather rather puzzled by that. They're obviously doing it some other some other way. No. No, they've just got some control stuff under there. No, there's nothing. So, it's This thing is clearly not uh working like our classic uh topology we had on the whiteboard up there.

**Dave Jones:** There it is. Ooh, there's a new perspective. Now, I've had a little head scratch over this rectifier thing, and some people are probably screaming at me right now saying, "Oh, yeah, it's obvious, Sandor." It is obvious when you think about what they're actually doing here, and it's rather clever, I think.

**Dave Jones:** Um this is my uh first thought of what they're doing, and it uh tips off why they've got a huge amount of capacitance in parallel with the battery here and no other I mean clearly there's no other uh you know a charger you know a power charger circuitry or uh rectifier.

**Dave Jones:** So, how are they doing it? Well, they must be doing it by tapping off the output of the transformer. So, the transformer is not actually uh switched here. They're actually they're always feeding power back through the transformer uh back in the other direction back into and using the H-bridge itself to actually uh charge the batteries.

**Dave Jones:** It's rather clever. This is the only way that they can be getting away with it cuz we need a huge amount of power to charge these huge battery packs.

**Dave Jones:** And the only power devices in here uh the H-bridge um devices themselves. Actually, I probably should have a look down here. I might be jumping the gun, but what I haven't shown here on my Dave CAD drawing, what I omitted because I thought it didn't matter, is the substrate diode across each one of these.

**Dave Jones:** And there's going to be one of those uh substrate reverse bias diodes across each of these MOSFETs. I won't go into details of why, but all MOSFETs are going to have these substrate diodes in there.

**Dave Jones:** And when you have diodes like that in reverse bias, you can feed power back in from this transformer, and then you can actually have um huge amount, you know, large capacitance across here like this or across there and there.

**Dave Jones:** You got large amount of capacitance, and that's what we've got. We've got these huge three huge caps here, and I think they're feeding power back in from the transformer through the reverse bias substrate diodes, filtering that out and using that to charge the batteries.

**Dave Jones:** That is incredibly clever. I really like that. Now, you may or may not be able to see that, but what we've got is four international rectifier IRFB4710 power MOSFETs in there.

**Dave Jones:** They're 100 V 75 amp rated, 14 mΩ on resistance, and they're clearly paralleling four of those up, and there's room for another four in there. So, obviously the 3,300 W model would have fully populated power MOSFETs in there.

**Dave Jones:** So, they're getting away with four, and they're tapped into holes directly on the heat sink. Or, well, it's not really a heat sink. It's actually used as the main current carrier as well.

**Dave Jones:** Quite neat. And if you try and have a look down the heat sinks at the other ones, you can see that they're exactly the same. They'll be two with P-channel MOSFETs and two with matching N-channel MOSFETs, of course, and I don't see anything else down in there.

**Dave Jones:** There's no huge power diodes or anything like that sharing the heat sink. So, they're obviously there's just some caps down in there. You can see those things down there.

**Dave Jones:** And really, there's nothing left for me to conclude except for the fact that they must be doing exactly what I said there and using the substrate diodes on here reverse biased to then charge up Well, to then and then they rectify that.

**Dave Jones:** So, it's effectively rectifying the AC coming from the output. When you're plugging in the mains, it's coming back from the transformer, and they're just rectifying that and filtering that, and then charging the battery from that.

**Dave Jones:** There's probably some, you know, more smarts in there, of course, actually taking care of things, but that's the basic topology that they're using. And it's very clever. And if we get rid of that option slot, which literally is an option slot and that and that just plugs in that ribbon cable just plugs in there.

**Dave Jones:** It's non-populated in my unit, but you can get like I believe you can get like ethernet interfaces and various other management modules and things to plug into. And as you can see, it looks like we've got a socketed micro there.

**Dave Jones:** I'll maybe try and get a close-up of that. Looks like we've got a USB micro cable micro here. It's a dead giveaway. It's right next to the USB. We've got an RS-232 you know, probably a Maxim serial driver in there.

**Dave Jones:** And that's about all she wrote. Not a huge amount of control, you know, we're obviously going to have some analog to digital converter stuff around here to measure your voltage coming from your the current transformer and also measuring the mains input and output voltages as well to try and track that power.

**Dave Jones:** And of course, the battery management charging capability as well. And for those who absolutely must know what the main processor is, I peeled off the sticker there. It's a Philips 87C51 classic.

**Dave Jones:** Now, I was curious about how that charging system worked. So, what do you do when you want to find out info on how something works? Well, look at what we have here on the back.

**Dave Jones:** US patent number 5,302,858. Let's look it up. And bingo, look what we have here. Sometimes you just get lucky. Now, at best I expected maybe to find a snippet of information on how the charger system worked in the patent application and but we haven't.

**Dave Jones:** Look what we found here. Method and apparatus for providing battery charging in a backup power system. It is exactly what and it turns out it's exactly what I thought was happening or pretty you know, pretty darn close to it.

**Dave Jones:** So, this is where I love Google patents. It pops up. You just type in Google and the patent number. Here's the patent number and it's got all the images and the full text of the patent and it's fantastic.

**Dave Jones:** I'll link this in, by the way, so that you can have a look to your heart's content. And here we go. We have some images popped up here and they've got some prior art here.

**Dave Jones:** What they're showing is that this is how a traditional UPS works with the what they call a static switch here, the exactly the switch we showed on the whiteboard there.

**Dave Jones:** Then we've got a a transformer rectifier configuration converts AC to DC. Then we've got a battery charger circuitry, a battery, an inverter, a H bridge, and then our output transformer powering the output.

**Dave Jones:** And that's the prior art, but what they've got this patent for, by the looks of it, I haven't read all the details of the patent and what everything does, but I've got the general overview of it.

**Dave Jones:** And look what we have here. It's the same as before. You got your AC input here. You've got your switch which goes through the output, but there's no charger that we had before.

**Dave Jones:** There's Look, there's no rectifier here and there's no charging circuitry. And that's exactly what we found when we opened this thing. It looked like there was no charging circuitry, effectively, and there was no rectified power rectifier in there and power charger.

**Dave Jones:** So, what they've got is the original inverter, the battery for driving the output, and what they're clearly doing is permanently connecting the output transformer instead of switching it between the input and this.

**Dave Jones:** It's permanently connected to the output and that back feeds power into the inverter here through those body diodes of that MOSFET and then are charging the battery here. And they've got a controller circuitry to power all that.

**Dave Jones:** They're obviously monitoring input and output currents and voltages and everything else, but that's basically working exactly like I said. And if we take a look at this figure here, they're actually showing some of the details.

**Dave Jones:** They're showing an ideal transformer here, but they're obviously showing uh you know, the winding inductance and uh stuff in there cuz that obviously has something to do with it.

**Dave Jones:** They're storing the energy in the winding inductances in there to actually back power the uh charging circuitry the battery. And look, they've drawn in the body diodes there, substrate diodes on the MOSFETs there.

**Dave Jones:** And that's exactly what they're doing. Now, they're showing the AC input here. And if you flick it over and we rotate it, oops. There we go. Then they What they're showing is that they are powering the uh well, they're taking the line uh output voltage um and then using the winding inductance to then supply power back through those diodes.

**Dave Jones:** They don't show any filter caps in here, of course. They're grossly uh simplifying this in the uh patent uh diagram. They're not going to show anything they don't need to.

**Dave Jones:** And but that back charges the battery. And it is very clever, as I figured. And look, they've got uh they're showing you know, various configurations here. And you'd have to look up the text and all the individual points are numbered, so you'd have to read the text in depth if you wanted to uh figure out how this works cuz this is how patent applications work.

**Dave Jones:** They obfuscate everything. They just, you know, rewrite it. They take a clear technical description from the engineer who designed this thing and uh they just That's what patent attorneys do.

**Dave Jones:** They just change it into gobbledygook. But it's all eventually there in the uh text. So, they're showing both uh positive and negative configurations of which MOSFETs turn on. And look, this is showing clearly this diode here is then back charging through there, etc., etc.

**Dave Jones:** So, looks like they've got a charging waveform here. Perhaps you'd have to read the associated text. And they've got some clearly some uh control circuitry here. Here's the battery.

**Dave Jones:** They've got some other Yeah, they've got a error amplifier here with a voltage reference control ADC all that sort of jazz. So, that's clearly the control if looks like they got some There we go.

**Dave Jones:** Energy build-up state. That would be in the winding inductance and they got the discharge state and energy build-up state again. And you can associate that with the text description of the system operation.

**Dave Jones:** And there's a full resistive discharge curves and all sorts of goodness in there. So, they're showing you exactly how it works. But, the detail is all down here in this descriptive text.

**Dave Jones:** And here it is in the summary of the invention here. The present invention eliminates the need for separate charger transformer and battery charger conveniently used in backup power systems by utilizing the main inverter to do the battery charging.

**Dave Jones:** Bingo. Eliminating the separate charger lowers cost, reduces complexity and weight of the system, and improves system reliability. Cuz as I said, I expected there to be a fairly hefty charging transformer in there plus associated power circuitry as well.

**Dave Jones:** But, this does away with it. Fantastic. The invention provides inherent power factor correction because without the need for any additional control circuitry, the inverter charger draws a sinusoidal non-distorted current from the power lines.

**Dave Jones:** Brilliant. Another side benefit of this. And here's a bit more detail. The present invention utilizes the primary and secondary leakage reactances of the main power transformer in cooperation with the switching devices for the H-bridge inverter.

**Dave Jones:** The Consequently, the battery pack will back bias diodes intrinsic anti-parallel diodes conduct connected across each of the switching devices in the inverter bridge. Brilliant. Does exactly what I thought.

**Dave Jones:** But, in the end, like when I you know, thought about it for 5 minutes, it was obvious due to the lack of various components that um you know this was exactly what they were doing.

**Dave Jones:** There was no other way to do it. And it also tells you the inverter may be operating in constant frequency inverter charge mode or a variable frequency mode as well, yielding a higher charge current.

**Dave Jones:** So, there's they can probably chop and choose under software control what method they want to use. Fantastic. And this patent isn't new either. It's dates back to 1991. It was granted in 1994 and it was done by a guy named Douglas C.

**Dave Jones:** Faults. Good on you, Doug. And he worked for a company called Best Power Technology. I have no idea who they are or how they're associated with APC. I haven't checked.

**Dave Jones:** But maybe they got acquired or maybe it's Doug's company. Who knows? Anyway, one smart cookie invented this and presumably nobody in the UPS business has been able to implement this I don't know what what you would call it you know reverse inverter battery charger technology or something like that.

**Dave Jones:** Nobody else has been able to implement it because they would presumably violate the APC patent on this thing. Or I'm sure there's people out there are using it and they don't care and you know they're in another country and well, it's you know, it's real difficult and expensive to sue them.

**Dave Jones:** But anyway, it's has the patent expired? I don't know. What is it? 20 or 25 years on a patent or something. But presumably APC have been the only ones that have been able to incorporate this novel this novel technology.

**Dave Jones:** I mean there could be you know prior art. Just because they grant the thing doesn't mean that it's you know enforceable and stuff like that. If you can find prior art to beat it, then you can easily well, not easily.

**Dave Jones:** Still cost you a buttload of money to win any patent infringement lawsuit. That's for sure. And that's the disadvantage of these patents. You think you're protecting your design and well, you not cuz here's all the details in depth of how it all works.

**Dave Jones:** So, it doesn't stop anyone copying it. It puts all the info out there so that anyone uh in the world can copy it. But, what it does do, the patent, is gives you a right to sue them very expensively if they do.

**Dave Jones:** So, there you go. I hope you enjoyed that look at a to well, a combined tutorial teardown Tuesday, I guess you could call it. Uh where I started with some uh theory.

**Dave Jones:** I thought, oh, you know, some basic theory on how these things operate. See how well a product when you take it apart matches the basic uh theory that you'd find in any uh textbook basic block diagram approach.

**Dave Jones:** And usually, you know, it does. But, in this case, it actually surprised us, and it's a good example of how and why I like taking things apart because you often find surprises like this.

**Dave Jones:** I hadn't heard of this technique before, but it seems obvious with the hindsight. Maybe this widely uh used in the industry, I'm not sure, but anyway, that was a rather interesting.

**Dave Jones:** I found something I didn't know. I'm going to have to read further about how this works, but it seems to be a very clever little technique, and I'm bet there's a lot of people out there that didn't know about this either.

**Dave Jones:** So, there you go. Some uh benefits to tearing stuff down and investigating things. I love it. And uh if you like the video, please give it a big thumbs up on YouTube.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
