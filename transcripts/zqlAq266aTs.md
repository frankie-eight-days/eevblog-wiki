---
video_id: zqlAq266aTs
title: EEVblog #1180 - Component Parametric Search Tutorial
url: https://www.youtube.com/watch?v=zqlAq266aTs
source: youtube-asr
---

**Dave Jones:** Hi, let's have a look at component parametric searching because it's a very important aspect in electronics design, product design, and I've talked about and demonstrated parametric searching lots of videos over the years, but I had a search in my videos and I could not

**Dave Jones:** find one where I did a video specifically on parametric searching. So, let's take a look at it. This was prompted by email from a viewer. I'm working on a project and I'm looking in a number of different microcontroller suppliers. I

**Dave Jones:** am now dialed down to two suppliers, Microchip and TI. I'm working on making a project that will utilize UART, plain ASCII text, all that sort of stuff, require 10 user inputs, 10 outputs represented on LEDs, so pretty simple

**Dave Jones:** requirement. As each button is pressed, corresponding LED turns on. It's a very simple project, but I hate to say they can't find a decent micro with enough memory, number of IO UART capable in a decent price. The cheapest I found was

**Dave Jones:** around $4.20 US. I remember you had posted a video regarding cheap one-time programming micros for like pennies, so I figured I'd ask you what hopefully have something in mind to help me out. Here are the requirements: 256k of memory. I

**Dave Jones:** have no clue why you'd need 256k of memory for a simple like UART thing and input output mapping. I that's even with you know, the most bloated C or other language possible. I like I just don't see it. Anyway, but let's run with that,

**Dave Jones:** shall we? Number of IO at least 25, fair enough, which rules out like 16-pin dips and things like that. You're looking at probably in that you might be able to get away with say a 28-pin dip for example. Communications ports UART and

**Dave Jones:** SPI, they pretty much come standard with most things. And we're searching for the cheapest possible price. And this is a very common requirement in electronics design is that you're searching for price? You've decided, okay, I need a microcontroller with these

**Dave Jones:** specifications or I need this part. Doesn't matter what it is. I've done one with uh selecting enclosures, for example. So, you've got a list of requirements and often what you're searching for is either the cheapest price or and or uh the best

**Dave Jones:** availability, the most stock, you know, stuff like that. And but it doesn't have to be like that. Other uh components you might be use parametric search for finding a particular value uh of a parameter, for example, like if you're

**Dave Jones:** searching MOSFETs, for example, you might want to search for the on resistance of the MOSFET. You might be looking for the lowest on resistance versus, you know, gate drive voltage and you know, all sorts of stuff like that.

**Dave Jones:** So, there's countless different examples of parametric searching on components, but we'll just stick for microcontrollers here just um to help this viewer out and as a classic example of trying to find the cheapest part possible for the job. So, what is

**Dave Jones:** parametric searching? Well, it's searching for a component based on parameters, hence the name, parametric search. This is a very common term in the industry, classic one to throw around in a job interview, by the way, trust me. So, virtually every component

**Dave Jones:** you can think of has parameters available for it, whether it's a microcontroller with all the parameters that we're going to see here, whether it's a MOSFET, whether it's a as a humble resistor, for example, can have a ton of parameters. In fact, I'll show

**Dave Jones:** you that. If we just go into surface mount resistors, for example, look at all these filters available. We can search by manufacturer. That's a parameter. We can search by the type of packaging, depending on whether or you not where you want full reels for uh

**Dave Jones:** your pick and place machine or whether you want tape or whether you want tube um or just cut tape or bulk or whatever it is or a partial uh manufacturer's reel or whatever it is. You can be searching by

**Dave Jones:** whether or not it's an active component, whether or not it's uh obsolete. For example, the series and the resistance, of course, the tolerance, the power, the composition, the type of the resistor, um uh features. Look, anti-sulfur, that meets automotive grade, things like

**Dave Jones:** that. The temperature coefficient, of course, the operating temperature range can be important. The package and case type. Oh, I love MELF, you know I love MELF. And uh the size, dimensions, the height, the number of terminals on it,

**Dave Jones:** the the failure rate. Like like the meantime between failure rate, stuff like that. All of these are parameters for a simple resistor, let alone a more complex part. So, how do you do a parametric search? Well, there's many different ways to do it. A

**Dave Jones:** one I often use is Digi-Key, for example. They're a big catalog supplier. Mouser is another one, Element 14. Any of your catalog suppliers, RS Components, they all have these parametric searches, and that some are a bit better than others, but not

**Dave Jones:** universally. It depends on what type of part you're searching from, whether or not they might have the uh the parameter you need. You might find that one supplier's parametric search doesn't have the particular parameter you need, but another one might. So, you might

**Dave Jones:** have to use various ones, depending on your needs at the time. And there's other websites like Octopart and Findchips, for example. These ones have uh parametric search in them as well. Here we go, we're in microcontrollers, and we

**Dave Jones:** can do all sorts of searches. And the advantage of both of these types of uh websites, like Octopart, which is started out by finding price, and then they added parametric uh search in. And the catalog suppliers, like your

**Dave Jones:** Digi-Keys, your Mousers, your Farnells, and your RS, they're and you're even uh your like big-time suppliers, like Arrow and things like that, they're more sort of industrial suppliers, they'll have uh parametric searches as well. So, there's dozens of different places you can go to

**Dave Jones:** for parametric search. The good thing about the catalog suppliers and the other websites, like Octopart is they search many different manufacturers. So in this case we want to search Microchip and Texas Instruments because our viewer has narrowed it down to those two for

**Dave Jones:** whatever reason and that's fine. But you may not care. But it's going to depend upon your requirements about what you're searching for. And so that's a good thing is you can search many different manufacturers. But let's say that we did

**Dave Jones:** know that we wanted to narrow it down to Microchip here. Well, we can go into products here, microcontrollers and microprocessors. Let's say we knew we wanted an 8-bit microcontroller for example. Well, we can go in here, 8-bit PIC MCUs. Here we

**Dave Jones:** go. Parametric search. It's on their website. Some manufacturers' websites are easier to find stuff than others, but it takes a little while, but bingo. We're bewildered by There's a scroll bar down here for a reason. Look at all of

**Dave Jones:** these parameters. Now, the manufacturers' websites can often be better than your Digi-Keys, Mousers, and all your other ones. They might have a more comprehensive parameters that you can search from. You can see the Microchip website here has product part number documents, 5K

**Dave Jones:** pricing. So if you wanted to search for price, you could do that. And look, even the cheapest the most expensive 5K pricing Microchip part is a $1.99 for the 16 PIC Yeah, this is the 16 Yeah, the 8-bit

**Dave Jones:** series. So I'm sure we could find a part in there that probably did the business. So I think we're already well ahead straight off the bat. But look at these ADCs, ADCs with computation. For example, if you wanted to do some

**Dave Jones:** computing stuff on that, number of DACs, resolution, internal band gap, voltage references. Yeah, it's just a hardware limit timer. Signal measurement timers, math accelerator, angular timer, you know, for rotational stuff, and class B hardware. I don't know what class B hardware is. That's

**Dave Jones:** weird. You need CRC, you know, in in hardware. You can It's all in there. You can search for all these parameters. And often, you can actually go in and select and deselect, so you have a more less cluttered view here. You can sort of

**Dave Jones:** like narrow it down. You can In fact, I think we have That's just a summary. If we go in and click show all specs, I think we might we might even have a few more. There you go. So, you can actually

**Dave Jones:** tidy those up and pick and choose sometimes. But, you can see how comprehensive parametric searching really is. It's amazing. Anyway, we're going to use Digi-Key to search for our microcontroller. So, we type in microcontroller at the top. Now, here is

**Dave Jones:** often a trap. Sometimes, you will choose the wrong category. And these parametric searches, if you're uh choosing a part and you don't Sometimes, it's not that obvious. You know, it's fairly obvious for microcontrollers, but if you're searching for a voltage regulator, for

**Dave Jones:** example, well, is it a voltage regulator or is it a voltage control regulator controller or something like that? There might be little subcategories in there, and you may be searching in the wrong category. So, you know, you really have

**Dave Jones:** to know your terminology. And uh it's Sometimes, you can spend all day, days, just, you know, finding uh the one part, doing all these parametric search. You might not find it on one's website. You got to go to another. You might end up

**Dave Jones:** at this manufacturer or that manufacturer to double-check that you didn't miss anything. Because sometimes, a part might be so critical to your design, that's worth spending days on. For example, if you can shave off, say, 10¢ per part by choosing the correct

**Dave Jones:** part, then if you're making, say, 10,000 widgets, there's a thousand bucks. That's a thousand bucks in your time that you can spend that's worth you spending that time. And if your time is valued at, say, a hundred bucks an hour,

**Dave Jones:** you can spend 10 hours searching or 5 hours say searching for that one part and you're still going to be ahead. And I'll just show you that category thing with that voltage regulators I was talking about. Look, you got linear, DC

**Dave Jones:** to DC switching regulators, but you then you've got switching controllers. So, it depends on whether or not the regulators usually, you know, has a built-in pass transistor, all that sort of stuff. But, like a a switching controller might have

**Dave Jones:** an external one and there might be just various categories, you know, linear plus switching down here. A part might be listed in there and it may not be listed in another because there are errors in these websites in terms of

**Dave Jones:** listing parts and things like that. It's very common. So, don't just rely on the one website uh to do it. Even you might even find issues in a manufacturer's uh webs own website. So, just be careful. Okay, so let's type in microcontroller.

**Dave Jones:** Let's go into embedded microcontrollers here and it's given us just some basic ones at the top. You'll notice that we've got 77,864 microcontrollers on uh Digi-Key. So, we're going to first of all sort down into Microchip and which

**Dave Jones:** will include Atmel now. You'll notice that Atmel's not there anymore and we want TI because our viewer has said that they want that. And you'll notice that our 77,000 has gone down to 7,000, just over 7,000 parts. So, we can apply the

**Dave Jones:** filter on that. You can either do them all at once or you can sort of like slowly narrow down. I like this cuz it tells you how many parts you've got left. Right? And then we can go in and

**Dave Jones:** we can choose, you know, we didn't say anything about architecture or anything like that, so we don't really care. So, you might want to search for active parts for example cuz you don't want to choose an obsolete part for a new

**Dave Jones:** design. So, look, there's 1,300. I love how it does this live. 1,390 obsolete parts. So, likely, you know, you want to be real careful if you're choosing an obsolete part. So, you might want to search just for active parts and

**Dave Jones:** it's lowered it from 7,000 to 4,800. Some of them are just discontinued at Digikey, which is no big deal. They just decided not to carry it anymore or something like that. So, I really, you know, I I wouldn't be too concerned

**Dave Jones:** about that. There's last time buy, for example, like it's about to become obsolete and you better buy them up in huge volume now, otherwise you won't be able to buy it anywhere or not for new designs. It means they'll phase it out.

**Dave Jones:** They'll make it obsolete in a couple of years time. They're just sort of like warning you. But, these uh parts statuses, you remember somebody had to enter in all this data, right? So, it can often be wrong. So, just be wary

**Dave Jones:** about uh doing something like that. So, I really wouldn't typically go with an active one. Once I've chosen found my part, I'd go to the manufacturer's website and and get it right from the horse's mouth whether or not it's a new

**Dave Jones:** part. So, that's how I generally do it. Okay, so we'll clear that and we'll go more filters. So, remember how we said we needed at least 20 25 IO. That was a high-level requirement, okay? So, we absolutely needed that. So, we need at

**Dave Jones:** least that and you can hold down shift and like um do like a whole array of them like that or you can just hold down control and just select like oddball ones like that if you really wanted. So, we're we're

**Dave Jones:** going to go for 25 because uh they didn't say didn't say an upper limit like size of the package. These requirements were like incredibly basic. Like there's no upper limit on the number of pins, there's no whether or not it's SMD or

**Dave Jones:** through-hole. We'll just assume it's SMD or whatever. And, you know, so no major or package size, you know, I I need it in an SO package cuz that's all I can solder, you know, I don't want any of

**Dave Jones:** that TSOP rubbish or BGA or any uh you know, stuff like that. There's just tons of options. Anyway, we need at least 25, okay? So, we've got with 25 IO, we've got 5 and 1/2 thousand parts remaining. So, we'll apply our filter down here.

**Dave Jones:** Sorry for having my head in that corn in this corner. Um because I probably my eyes are looking somewhere else. If I put it over there in that corner over there, I'm bound to miss something. So, it's just the way the camera works and

**Dave Jones:** my eyes work and all that. Anyway, whatever. The other was 256K of memory. There was no speed requirement. What is our program memory size? Okay, I have no idea why you need 256K for that, but hey, we'll work with

**Dave Jones:** that. Um and it didn't say whether or not that was uh bytes or whether or not that was program words. I'm going to assume it's program words. So, um so, in this particular case, like there we go. Like this one might be 256

**Dave Jones:** kilobytes program size, but because it's a 16-bit micro, it needs two of those per word. So, it's actually only 128K. So, we're just going to say 256K. We can go all the way to 4 meg. Wow. That's pretty serious business. But we've still

**Dave Jones:** got 1,700 microcontrollers from just these two manufacturers. This is insane. But it's not actually 1,700 different parts. The parts might be like slightly different package variations, temperature variations, uh like you know, military or commercial grade and stuff like that. So, yeah.

**Dave Jones:** It's you know, don't get too excited about the variants. Uh right, it didn't say anything about RAM size. No worries. So, we're sorted by IO and you'll notice that look it is now only uh was an oddball number,

**Dave Jones:** so it just wasn't there. And we'll just do flash. We probably don't want FF RAM for example. So, you know, like you don't have to do that. But we'll we'll we'll just do that for kicks, shall we? Now, as in terms of UART and SPI, this

**Dave Jones:** is where it's harder on Digikey and other uh websites, they sort of like combine them. Look, you've got a like you know, it's got to like CAN bus. Look, it's got like all all this combined one and you can easily miss

**Dave Jones:** ones. Like, oh, I need a UART. So we need a UART and SPI, but we have to go through and manually, if we wanted to search for that on Digikey, we'd have to go in and manually search for all and

**Dave Jones:** select all the ones that had the those particular peripherals. So, you know, it's and that's different to your peripherals over here. So, yeah, I I generally wouldn't search for that. Most micros are going to have a UART and an SPI

**Dave Jones:** these days. So, I wouldn't even bother searching for that, but you can. So, if you really wanted to do that, I'd probably go it back over to the manufacturer's website over here and they probably have it separately. And

**Dave Jones:** there we go. Yep, they have it separately, UART and SPI. So, there you go. We've got our parametric search data, 256 K of memory and in fact it put killer bits, but it doesn't matter. 256 K of memory, 25 IO pins minimum, UART

**Dave Jones:** and SPI. So, I almost guarantee they'll have SPI. So, anyway, we were good to go. Yep. So, you'll find that this is all updates live in the background. So, we've got 1,681 parts. So, we go down here and here's

**Dave Jones:** all our parts. Now, what's the other thing we wanted to search for? Price. We didn't we didn't get a volume. There's no volume price, but let's say that we wanted to search for thousand quantity volume. You don't have to do it up here,

**Dave Jones:** but they've they've added this in recent years, view prices at a thousand volume, okay? So, it will give us prices in this list down here, not of one of quantity. It'll give us the thousand price quantity. So, there it is, at quantity

**Dave Jones:** 1,000, okay? Whereas that was different before and you can just go back, by the way, uh which is handy. So, whereas before, so yeah, this column down here, that was just the one-off price, but if you go for the thousand up here, then it

**Dave Jones:** will give you the thousand-off quantity in all of those. Now, the other thing is, you might go, "Well, I I'm not going to design in a part if I can't get stock at least from Digi-Key." Geez, you know,

**Dave Jones:** that means if you can't get it from there, it's probably, you know, a bit obscure. So, we can select in stock here. For example, you can select ones that only have a data sheet, uh for example, but that's getting a bit, you

**Dave Jones:** know, it's getting a bit anal. Most of them have a data sheet. Normally stocking new products, I generally wouldn't uh touch those. The RoHS compliant, non-RoHS, man, that'll just come out in the wash you generally, unless you are really strictly

**Dave Jones:** searching. And maybe if you wanted one with um EDA or CAD modules models, it's all in here. You can see how ridiculously, it's almost an unlimited variety of parameters you can search for in a parametric search, and that's what it

**Dave Jones:** is. Anyway, in stock, we're now down to 331. You see how before we were get get rid of that. 1,681, we got all excited. Oh, wow, we have so many to choose from. Oh, in stock, nah, sorry. You only got 331 left. So, let's

**Dave Jones:** apply our filter. And let's go down, and we only get the thousand-off quantity now. You see? So, there it is, $3.89. So, we want to search for the minimum price. Let's go. Wow, there you go. Search for Actually, reasonably expensive, because

**Dave Jones:** it's the memory that's going to do it. Memory is expensive, and we'll search for that in a minute. But, our viewer said $4.20 US, right? So, if we remove our thousand-off quantity let's go down to a hundred price, for

**Dave Jones:** example, that's quite reasonable. There you go, $5 something like that. So, the cheapest one, yeah. Um so, actually, I was I was a bit surprised. There you go. So, the 256k of memory is really done the you know,

**Dave Jones:** that's really done us in. So, we'll search for price here. And the other annoying thing is you'll find that once we've gone to that 256k of memory, look at all these pain in the ass packages they can't like they're all really large

**Dave Jones:** packages even though we only search for ones with like 25 IO, for example. Um it's In fact, the filters are up here. It'll actually narrow down number of IO pins. Look at this. So, if you wanted one with

**Dave Jones:** only 20 There's only one two devices. Two devices with 26 pin. Let's see what they are. There you go. And it's a TI part and it's the F28 149. What on earth is that one? Oh, it's one of the C2000 Piccolo series

**Dave Jones:** there, for example. And it's 9 bucks 50 and 11 bucks. But if you you know, if you wanted the smallest pin count with that 256k of memory, like there's no choice. But once again, that's just on Digikey. You might go if

**Dave Jones:** you're a desperate and that was your only you know, you had to fit that requirement, then you would like go search wider number of manufacturers. You go search other parametric search engines. You go to the manufacturer's website, stuff

**Dave Jones:** like that. Actually, this doesn't add up. Look at the size of this package. That's a 64 lead quad flat pack and it's only supposed to have 26 IO pins. So, something have we got an oopsy in the database here? We might very well

**Dave Jones:** have. To have so few IO that you know, on a 64 pin package. It's nuts. Actually, nope, that's genuine. Look at here. This 60 64-pin PM 26 IO. Why? What's the actual pinout? Yeah, sure enough, the PM low profile quad flat

**Dave Jones:** pack. Yeah, look, there's tons of pins like VRF, LOV like PGA 2 in. So, a lot of these A5 These are like filter one, filter two, whatever it is. Like the TME like it's got Yeah, it looks like it's

**Dave Jones:** got a separate dedicated JTAG pins and stuff like that. Yeah, so and there's lots of ground and lots of IO. So, yeah, you can see why that's only 26 IO in such a large package. That's just oddball. Damn it. I

**Dave Jones:** was hoping we'd find a mistake in the parametric search. So, I'm just going to go back here and you can actually use the back button to go back and we're still at our 256K program memory. Let's say we wanted to

**Dave Jones:** say 32K of program memory. So, let's go from 32K to 256K, for example. So, let's do that again. And we'll search we're still got our number of IO and we'll find that our prices have significantly changed. So, there's our 1,000 of quantity. So, if

**Dave Jones:** you can get by without your 200 with your without your 256K of memory, search by you see that up arrow there? So, each one of these tables you can search by sort by lowest to highest, which is what the up arrow

**Dave Jones:** means, or search from highest to lowest price. So, our highest price micro in that at a 1,000 of quantity is $2,803. It's a development board. Well done, TI, for your $2,800 MSP430FR4M development board. Give me a break. Anyway, but no, look,

**Dave Jones:** they do actually have a part and SM320F. Oh, look at it's still got the the cage on it that holds the chip. Isn't that sex on a stick? Oh, that's worth every one of the $336 but you may have a requirement for that.

**Dave Jones:** So, you know Anyway, so that's the you know the 80 bucks. There's other parts like MSP430 for 82 bucks. 60 pound 28K flash, jeez. Jeez, I want that personally delivered by a graybeard. That's that's ridiculous. Anyway, we search for lowest price

**Dave Jones:** upwards and you'll see that when we search for 32K up our prices came down to a dollar 40 in a thousand volume and there's looks like TI's the winner there. I don't see Microchip matching that and there there is a plugin by the

**Dave Jones:** way. It used to be like a the Greasemonkey plugin and there was a I I haven't used it for years but it used to be a very nice Digi-Key plugin that allowed you allowed you to search for add more variety to your parametric

**Dave Jones:** searches and stuff like that but I I don't I don't know why I stopped using that and maybe like Digi-Key and Mouser and all the rest just keep getting better and better and better in the parametric searches. Ah. Did I get

**Dave Jones:** something wrong? Are we only searching for TI? I think I think I goofed. Sorry about that. Microchip, I didn't press control. Microchip and TI. Sorry about that. We'll just 32 to 256K, minimum 25 IO. Let's not go silly, you know, let's go

**Dave Jones:** up to 80 pins or something like that. Let's not go nuts. Okay, there we go. Search for price. There's our thousand off quantity. Hey, look at this. There you go. A Microchip part, AT oh, that's the that's an an Atmel one and an arm cortex

**Dave Jones:** M0, for example, that's 51 cents and that's got 64K of a flash, surely that's more than enough, but that's in a pain in the ass micro BGA package, you don't want that. So, you know, you might want this nice There we go. Nice quad flat

**Dave Jones:** pack down there. 32K of flash memory, you know, it's 82 cents. They've got them in stock, 220 too. It's not a huge number of stock. And as I said, like all of them have UARTs and SPI and stuff

**Dave Jones:** like that, so that's, you know, it's pretty much a given these days, almost guaranteed. So, you know, there's plenty of options in there. Look, I I could go through until the cows come home and search for the perfect microcontroller for this

**Dave Jones:** application, but quite frankly, we need more information on just that. That's that's way too broad and information at the cheapest possible. It's just And and I've got a question the 256K requirement in there for such a a simple

**Dave Jones:** thing. But anyway, I hope you can see how powerful these parametric searches are. And once again, and like I said, it totally depends on your requirements, but if you're, you know, really spending hours and hours or even days on

**Dave Jones:** parametric searching one part because it was critical to some aspect of your design, then, you know, you might not be searching on just the one website. I'd go over once I've narrowed down a few manufacturers that I wanted that might

**Dave Jones:** make the types of parts that I'm interested in. I'll just go and double-check their websites and then, you know, you might uh see you might search because your price is once again absolutely critical, you might go over to a Chinese sourced website and you

**Dave Jones:** might be happy with one of the obscure brands, for example, that we've looked at before. No, I'll do it. No, thank you. I don't want to do that. But if we go over here and have a look at

**Dave Jones:** at processors. We've got all these embedded processors and controllers. We can go in here, but unfortunately, it looks like LCSC doesn't have a parametric search engine available across multiple manufacturers like this. Like we might be able to go into say

**Dave Jones:** Microchip, which has a lot of parts, right? And then we get our parametric search, but you can't do it across the different uh manufacturers, which is what you can do on your Mouser, your Digi-Key, and your Arrows, and your uh Octopart, and

**Dave Jones:** your FindChips, and all those um types of websites. So, now quite often you'll use parametric searching to actually find manufacturers of parts that you didn't know about. You might have some obscure thing, oh I need I I know I need

**Dave Jones:** one of these parts, but I don't know who makes those. You go to your catalog suppliers, and bingo, you can find all of your manufacturers in the list down here, and you do your parametric search, and all these manufacturers pop up, ones

**Dave Jones:** you've never heard of. You might go, "Oh, I've never heard of Zilog, I've never heard of Wiznet, XMOS, who's that?" You know? And then you go check them out. It's actually quite a real good way. You can just spend all your idle hours

**Dave Jones:** parametric searching, and you'll find all these manufacturers and other obscure uh requirements and and parameters of parts that you never knew about. You might find some obscure parameter in here, and you go, "I have no idea what that mean what that aspect

**Dave Jones:** of a MOSFET means." I I'll show you. Go into MOSFETs. Go to singles down here. These are all the MOSFET manufacturers, not necessarily all of them. Wouldn't have like the, you know, your more obscure Chinese uh suppliers and stuff like that. 49,000

**Dave Jones:** odd MOSFETs. Ah, look at that stupid little four-bump BGA rubbish flip thing. Bugger off. Again, what's a GAN FET? What's a gallium nitride, right? You might not know what that is. So, you might go, "Ah, I'll go and check out that

**Dave Jones:** technology. I've never heard of that. That's absolutely fantastic." And these these parameters down here, yeah, you know, you might know what VGS is, you might know what you know, you might want an on resistance. I I talked about it

**Dave Jones:** before, you might want the absolute lowest on resistance, but you might go, "Oh, what's this gate charge? I don't know what that is." Go Google it. Find out. Input capacitance. Um you know, there's a whole bunch of stuff. Then you

**Dave Jones:** might go, "Oh, what's a super junction? What's depletion mode? I don't know anything about the current sensing? What? I you know, like you just go and search. "A supplied only in passivated die form with solder bumps. Ah, bugger

**Dave Jones:** off." Great for your mobile phone, but you know. So, you might search for current sensing, for example. There's 38 parts down there that do current sensing. And oh, look at that. Stud package. Isn't that Well, it's very studly. Oh, yeah,

**Dave Jones:** from IXYS. You might never have heard of IXYS. Uh for example, Nexperia. So, you know, look, you can just go in and have a look at this data sheet because you didn't know what current sensing is, for example. And N-channel uh trench fit

**Dave Jones:** standard level fit. Boom. Let electrostatically robust. And bingo, you might go down and you might see, "Why does it have all these pins? It's only a MOSFET." No, look, it's got a Kelvin sense pin, for example. Perfect for current sense applications. You got

**Dave Jones:** your current sense resistor down in your uh source down here. I've done videos on that, and it's got an I sense pin as well. Absolutely brilliant. You might not have known these things even existed. These obscure parts that

**Dave Jones:** actually tap it off right on the die, which is absolutely fantastic. And then that might That might give you an idea for your uh product. It might go, "Oh, but wow, I can add extra capability to my product cuz I found a part that did,

**Dave Jones:** you know, this obscure thing I didn't even know existed." And that's the power of searching through parametric searches. So, you know, you wonder why um myself and other, you know, experienced designers know about all these parts and all these things. It's

**Dave Jones:** because we've spent, you know, like countless years doing parametric searches. And you just find all sorts of obscure stuff. It's a great way to learn. But, I know everyone wants to know what is the cheapest microcontroller, well, at least on

**Dave Jones:** Digikey here, that's in stock that has 256K of program memory. Here you go. I'm searching all the manufacturers and bingo, we're sorted by a thousand off quantity price. We're talking 81 cents. Winner winner chicken dinner to Microchip. Um their SAM 3 um Cortex M3

**Dave Jones:** chip. There you go. And yes, it does have the UI UART and SPI. It's only 81 cents. It's in stock. Absolutely fantastic. So, Microchip win there. Who's the next winner? And STMicro, the 32F uh 030. That's a It's almost twice the price

**Dave Jones:** there. So, you know, I mean, if you you really desperately needed, if that was your only requirement, I need 256K of uh program memory and uh just some IO and a UART and a thing at the 81 cents.

**Dave Jones:** And yes, it's got 34 IO. So, I'm actually not sure why this one didn't show up before. That's interesting. There's something There's a glitch in the matrix. There's a glitch in the product parametric search here. Like, you could go in and

**Dave Jones:** try and figure out the reason why it's not showing up and everything. But, yeah, I mean, we were searching Microchip before and that wasn't showing in 256K and the minimum number of IO and stuff like that and it wasn't like Oh, I can get a

**Dave Jones:** 14-pin IO. no, IO. That's not the number of pins, but you can get you can sort by package, of course. There you go, look. Oh, you can get a 16, a 16-pin one in with 256K or at least yeah, at

**Dave Jones:** least 256K of flash. Nice. Who's that? That's a maximum. There you go. If you want 256K of flash in a little bumpy BGA, knock yourself out. So, anyway, that's just right there is an interesting example. I just like fell into this one.

**Dave Jones:** I decided to do the extra search. If I didn't do that, I might have thought that Microchip didn't have anything available, you know, under with 256K of flash memory that with the IO that we wanted. Like in that the original search, maybe

**Dave Jones:** there's an error in the parameters or whatever it was that it prevented that coming up. That we might have found that if we went over to the Microchip website and did the parametric search on on there, but yeah,

**Dave Jones:** it just popped out of the woodwork where it didn't before. So, it's a good example of where you can come a cropper, run off with your tail between your legs thinking that oh, I've got to use a, you

**Dave Jones:** know, a three or four dollar micro and nope, look, found a winner winner chicken dinner. And that's why it pays to sometimes, you know, spend an extra few minutes, few extra hours, maybe an extra day searching for the right part.

**Dave Jones:** And of course, we're not even done yet. I mean, you know, we haven't even searched. I could I could spend hours just searching for that basic parameter, 256K micro to find the absolute cheapest damn thing on the market.

**Dave Jones:** Go down the rabbit hole. So, there you go. I hope you found that useful and I hope I answered Simon's question. Well, I didn't really answer it, but you know, parametric searching. I just thought it'd be a nice way to do a dedicated

**Dave Jones:** video on it. It's a very useful thing. Highly recommend it and there's tons of nuances and variations of this. It's practically infinite. But, you know, there some rules are don't just trust one website and ultimately go back to the

**Dave Jones:** manufacturers parametric search or don't believe things like, you know, it's it's discontinued or something like that. Only trust the manufacturers, you know, if something is really critical, if if a parameter is really critical, go back to the horse's mouth. Go back to

**Dave Jones:** the manufacturer's website and their latest data sheet to get exactly right. Because, you know, it's very common to find errors in parametric searches. And, you know, if you're having a bad day, Murphy will get you every time. So, hope

**Dave Jones:** you enjoyed that. You did, please give it a big thumbs up and as always, you can discuss down below and over on the EVblog forum. Thanks to all my patron and new subscribe star supporters. Catch you next time.
