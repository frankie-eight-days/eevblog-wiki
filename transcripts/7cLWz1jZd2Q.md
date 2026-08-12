---
video_id: 7cLWz1jZd2Q
title: EEVblog #953 - What Is Schematic ERC?
url: https://www.youtube.com/watch?v=7cLWz1jZd2Q
source: youtube-asr
---

**Dave Jones:** Hi, this is just a little aside video from my Nixie Tube display driver videos I've been doing cuz I thought some people might find this just interesting in its own right. We're going to talk about electrical rules checking in

**Dave Jones:** schematic documents. In this case using a powerful tool like Altium Designer and just exactly what is an ERC? How does it differ from a design rule check on a PCB and what advantages it can have? So, let's get to it. Just to show you doing

**Dave Jones:** an ERC on a schematic like this. Now, a lot of people would just skip this if you're just doing it quickly and getting up and running, but hey, you know, you could get if you're doing any sort of

**Dave Jones:** serious design or even a one-off like you know, let's say we had our grid set incorrectly and we had a fine grid and we didn't connect up this trace to here or something like that and you zoomed out and you didn't notice that it wasn't

**Dave Jones:** electrically connected. For example, there could be many other connection faults on a schematic. That's why they have snap grids in here so that everything snaps. So, when you actually then do your net list for this and pass it through to your PCB, that

**Dave Jones:** information, that net list information of what pin connects to what does not get sent through to your PCB file and then you won't route the thing. You could easily miss routing that pin and your board won't work because you made a

**Dave Jones:** simple error in your schematic and you didn't do an ERC and fix it. So, let's go in and actually do an ERC of this thing. You should do it as a matter of course. Now, all programs will work differently

**Dave Jones:** and this is how Altium Designer works. Now, there are two ways to invoke an ERC and electrical rules test. One is to actually right click on here and go compile document, but as I showed in the previous video on my second channel, I

**Dave Jones:** think there's a bug with this so we're not going to use that. Anyway, Altium recommend actually compiling the PCB, the entire PCB project and that will use the uh which we'll take a look at. So, the term compile is just another

**Dave Jones:** way to actually run an electrical rules check. You can think of that, you know, it's literally like a software compiler we've written our code, we've drawn our schematic, now we're compiling and it's going to tell us if we've done something

**Dave Jones:** stupid. And the other more powerful way to actually systematically uh do this as part of your process is to uh create and use an out job. So, I'll just show you that here. Let's go in and do an out

**Dave Jones:** job, shall we? So, what we have to do here is go into uh settings, output job files. Now, I've created a new out job here. You just go in file, new out job. So, I've created an out job and what we

**Dave Jones:** have to do is this rather convoluted, but there's reasons for this. An out job is just a very systematic way of doing all sorts of things. In this case, generating net lists, uh simulators, documentation, assembly, fabrication outputs, all your Gerber stuff, doing

**Dave Jones:** all your reports like your ERC and your DRCs which we're going to do here, um and then all sorts of stuff. And it's really powerful. As a professional uh PCB designer in the past, I've made extensive use of these out jobs. You

**Dave Jones:** know, if you're professional designer, you want a rigorous process for releasing a new board. And these out jobs just force you to generate all these reports and all these different things. A very, very powerful and flexible tool for for the professional.

**Dave Jones:** Um probably a little bit annoying just for the one-off, you know, hobbyists making one-off boards or whatever. But anyway, so we can do stuff like, you know, going to fabrication outputs and we can generate our drill drawings, our

**Dave Jones:** Gerber files. Oh, there's a like update screen bug error. I think that's caused by my screen capture here. Anyway, um what we want to do is we want to create an ERC in this thing. So, we want to go

**Dave Jones:** to add new validation output. Now, we've got two different types. One's a design Oh, that's annoying, a design rules check, a DRC, but you'll notice that it's only available on our PCB document cuz DRCs, a design rule check, is done

**Dave Jones:** on PCBs. But if you want to do the same basically the same thing on a schematic, it's called an ERC, an electrical rules check. So you notice, so this is what we want, electrical rules check, and then it we've got one schematic document in

**Dave Jones:** our project, so we select that, and bingo, we've got an ERC on our um thing here. Now we enable this and we can actually send the output of this to a PDF file if you want to generate a

**Dave Jones:** report for, you know, uh a meeting or you know, or for whatever purpose, or we can generate a video, but what we'll do is we'll just generate a uh basically a HTML file here. So we'll generate a file

**Dave Jones:** and we can just go generate content. So what we're going to do is run the electrical rules check using the rules that are already set up, which I'll show you in a minute, and we can just go generate content. So it actually runs an

**Dave Jones:** ERC, and bingo, here's our report. And you'll notice that uh there's not too there's no major errors, warning Will Robinson, error error. We've only got some warnings here, hidden net added to VCC and ground, that's nothing, that's to do with the 74HC chip, which has a

**Dave Jones:** couple of hidden pins, no problem. Uh but then these, oh, what have we got here? Look, no driving source, pin U118. Huh, and basically everyone of those uh 595 chips and a couple on the uh module as well. So let's go in and take

**Dave Jones:** a look at that, shall we? Right, so it's put all these errors in our messages output here, so we can actually go in and have a look at, you know, what one of these errors is. So we can go in

**Dave Jones:** there and we can go cross probe, and bingo, it takes us it zooms us all the way in, which is rather rather annoying here, but anyway, it zooms us and then highlights the particular error. So, oops. I see the problem.

**Dave Jones:** Um D out. Um yeah, oops, that was a PEBKAC error. When I was creating this symbol, I created pin 18 there, the D out, I've actually set it as an input pin. You see that arrow going input? So,

**Dave Jones:** what's happened here is it's flagged this as a warning. It says basically there is no driving source. I've got two inputs tied together, but there's no signal driving that line. So, it knows that. It's electrical rule checking your

**Dave Jones:** schematic. So, um yeah, we need to fix that. And I've done that because it I just placed the same chip. It's populated all that error, and I think we had an error on the module as well. So, yeah, probably a couple of these inputs

**Dave Jones:** weren't, you know, the pins weren't set as inputs and outputs. So, we'll just fix that in the component, and we'll update. So, here we go. This is a real easy thing to fix. We just uh our data output pin, jeez, I'm dumb. I set it to

**Dave Jones:** a an input. Here it is, electrical type. You can set all the different pins. Now, usually by default they're like passive, and then the warning wouldn't have we wouldn't have got any warnings whatsoever. But, you know, it if you're

**Dave Jones:** doing this professionally, creating symbols professionally, you want to going to want to set the um output to a particular uh type. So, we can either set that to passive, and the warning will go away, but we'll set that to

**Dave Jones:** output cuz we're happy with And there we go. It's changed the arrow pointing outward. So, it shows us that we've got the output like that. So, D out, bingo, fixed. We can uh save that, and then we can just go update schematic sheets.

**Dave Jones:** Boom, there's 11 components in one schematic document. Yep. Okay. We're updated. We're all good. We'll notice that our symbols have now changed. There we go, data out pin, pin 18 is now output. So, if we run our out job again,

**Dave Jones:** we'll find generate content, boom, our errors are gone for those particular chips. We've still got no driving source for the module, but I don't you know, I could go in and fix that, but and get down to zero errors. And if you're a

**Dave Jones:** professional designer, and a lot of companies will enforce this to go to the next step, the PCB step, you have to show that you've got zero errors on your ERC. And of course, you can fudge that a lot of you

**Dave Jones:** know, a lot of designers will rightly in some cases just fudge that until the errors go away and ha see you know, I I know what I'm doing, you know, and so you can fudge it. But yeah, if you do it

**Dave Jones:** properly, your goal is to get all the errors and warnings to go away before you go on to the PCB layout step. But anyway, that is now fixed. I'm happy with that. Now of course, we can use this ERC to find, as I said, a whole

**Dave Jones:** slew of like I could go through maybe a hundred different examples of different variations of errors that you know, this system can find here. But like a very let's do a very serious one for example. Let's say you

**Dave Jones:** weren't thinking and you connected an output pin 18 D out here to another output. Oops, you shorted two outputs together. You could release the magic smoke. So, I've deliberately added that error in here and also another error here. Look on this chip U6 D out pin 18.

**Dave Jones:** I've actually shorted that down to ground. So, once again, yeah, you could release the magic a smoke. You really want to pick an error like this up. I've got another one D in here which is a floating and it's got

**Dave Jones:** you can do online checking as well. Like it shows it on the schematic. That's what that red squiggle is. That shows where the errors are. So, what we can do is we can just compile our project here and bingo.

**Dave Jones:** Look, ground contains output pin and well, it's power source. So, we can actually go there, have a look at that, and ta-da! It's a bit hard to find the actual thing. It doesn't point out exactly where your error is. You got to

**Dave Jones:** scroll around until aha, there it is. Our output is shorted down to ground. So, that's a real big deal that you want to get rid of. And where's the other one? We've got uh contains has no contains floating

**Dave Jones:** contains multiple output pins. Here we go. This is the one we want. We've got two outputs shorted together. And bingo, it's found that multiple output pin shorted together for us. So, it just can pick up really gross errors like that. And so, this is why

**Dave Jones:** ERCs are incredibly important, just as important, if not more so, than PCB DRC errors. If you miss things in the schematic, they can flow through to the PCB, go through to the net list, you route your board, and you get it

**Dave Jones:** manufactured, and multiple steps, could be multiple weeks or even months down the process you build up your prototype and find that error when you should have actually captured it in your schematic. So, ERC electrical rules checking very, very important thing. And

**Dave Jones:** good quality package like Altium Designer will have extensive ERC capability. And as I said, there's just a ton of stuff in here with all these reports with the ones to do with buses. So, if you got buses, code symbols, actual component

**Dave Jones:** stuff like sub parts and being used, and all sorts of, you know, you can set these to warning, no report, error, fatal error, whatever you want. You might have company rules for these sorts of things, you know, you might be forced

**Dave Jones:** to use a particular rule set when you if you're a professional PCB designer at a company or something like that. So, your real serious companies will take this extremely serious, cuz once bitten, twice shy. And ERCs can really save your

**Dave Jones:** butt. So, well worth doing, and documents and configurations, harnesses, and various nets, and you can detect all sorts of weird and wonderful things with the connection matrix, and we won't go into um sort of other stuff, but yeah, it's a

**Dave Jones:** fantastically powerful tool. Now, as you may have already gathered, the quality of your ERC is really only as good as the quality of your component libraries. In this case, actually going there and setting all of these pins to inputs,

**Dave Jones:** outputs, or setting them to, you know, open collector and bus power, you know, whatever it is. And if you've got a really generic component library that doesn't have any of these things set, then ERC is going to be of limited

**Dave Jones:** value. If every single pin in here is set to a passive, uh for example, then it's not going to do anything for you. So, it's going to miss a whole ton of stuff. So, yeah, it pays to actually put

**Dave Jones:** effort into your component libraries to ensure that all these things are set correct. And of course, nothing stops uh you, you know, no ERC is going to save you if this pin 20 here, you've accidentally labeled it pin 19 in your

**Dave Jones:** component library, but that's why uh companies put a lot of effort, and often they'll have a dedicated uh library design people or person who will just design libraries, and once the library is designed, that never gets touched again, and it's once it's verified, they

**Dave Jones:** will never touch that thing again. So, it'll just be aware of that. It's worth putting in the extra effort, but yeah, it's just be aware what your ERC is capable of and not capable of based on the information you're giving it.

**Dave Jones:** Garbage in, garbage out. A fantastically powerful tool, ERC. So, have a play with it next time you can do a schematic in your package of choice, of course. Not all packages will be this uh and powerful. But, your professional

**Dave Jones:** ones most certainly are and they are for a reason. Hope you enjoyed that. Catch you next time.
