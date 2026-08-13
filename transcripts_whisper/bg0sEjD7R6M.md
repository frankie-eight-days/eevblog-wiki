---
video_id: bg0sEjD7R6M
title: EEVblog #254 - KiCAD PCB First Impressions
url: https://www.youtube.com/watch?v=bg0sEjD7R6M
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 30, "2": 49, "3": 70, "4": 93, "5": 108, "6": 138, "7": 158, "8": 176, "9": 194, "10": 226, "11": 248, "12": 274, "13": 294, "14": 311, "15": 333, "16": 355, "17": 370, "18": 390, "19": 419, "20": 444, "21": 469, "22": 485, "23": 508, "24": 524, "25": 545, "26": 567, "27": 592, "28": 611, "29": 632, "30": 651, "31": 672, "32": 687, "33": 716, "34": 735, "35": 751, "36": 769, "37": 788, "38": 806, "39": 830, "40": 847, "41": 869, "42": 884, "43": 906, "44": 923, "45": 945, "46": 964, "47": 981, "48": 997, "49": 1018, "50": 1043, "51": 1058, "52": 1074, "53": 1096, "54": 1113, "55": 1135, "56": 1158, "57": 1183, "58": 1203, "59": 1222, "60": 1241, "61": 1264, "62": 1289, "63": 1303, "64": 1318, "65": 1337, "66": 1357, "67": 1379, "68": 1396, "69": 1417, "70": 1433, "71": 1458, "72": 1484, "73": 1505, "74": 1526, "75": 1557, "76": 1579, "77": 1600, "78": 1626, "79": 1643, "80": 1659, "81": 1675, "82": 1694, "83": 1711, "84": 1733, "85": 1752, "86": 1768, "87": 1784, "88": 1800, "89": 1818, "90": 1845, "91": 1865, "92": 1885, "93": 1908, "94": 1926, "95": 1940, "96": 1958, "97": 1979, "98": 2001, "99": 2019, "100": 2043, "101": 2061, "102": 2077, "103": 2097, "104": 2118, "105": 2140, "106": 2161, "107": 2182, "108": 2199, "109": 2213, "110": 2232, "111": 2249, "112": 2262, "113": 2281, "114": 2305, "115": 2325, "116": 2341, "117": 2361, "118": 2377, "119": 2401, "120": 2426, "121": 2442, "122": 2458, "123": 2475, "124": 2494, "125": 2505, "126": 2522, "127": 2538, "128": 2556, "129": 2572, "130": 2592, "131": 2614, "132": 2633, "133": 2650, "134": 2668, "135": 2693, "136": 2713, "137": 2729, "138": 2743, "139": 2762, "140": 2779, "141": 2799, "142": 2821, "143": 2842, "144": 2860, "145": 2878, "146": 2897, "147": 2920, "148": 2935, "149": 2956, "150": 2973, "151": 2992, "152": 3012, "153": 3026, "154": 3038, "155": 3057, "156": 3078, "157": 3095, "158": 3116, "159": 3131, "160": 3149, "161": 3167, "162": 3183, "163": 3203, "164": 3221, "165": 3238, "166": 3253, "167": 3278, "168": 3297, "169": 3312, "170": 3334, "171": 3352, "172": 3370, "173": 3387, "174": 3406, "175": 3425, "176": 3444, "177": 3463, "178": 3479, "179": 3498, "180": 3526, "181": 3547, "182": 3570, "183": 3587, "184": 3602, "185": 3619, "186": 3633, "187": 3650, "188": 3667, "189": 3687, "190": 3700, "191": 3713, "192": 3734, "193": 3749, "194": 3767}
---

**Dave Jones:** OK, we're going to continue where we left off last time of just doing an off-the-cuff first impression review of KiCad here. Now, I, unfortunately, I guess you could say, had a couple of tip-offs from people last time about various things. So, unfortunately, I do know a little bit more than, a slight bit more than just being completely green with this program.

**Dave Jones:** Like if you do question mark in the schematic editor here, it pops up with a hotkey list. And there you go, they're the, all of the hotkey items for the schematic editor. And I know a couple of other things like this module here, which I thought might have been the library editor or something.

**Dave Jones:** This is actually to link component, it's actually to link footprints through to schematic items for your particular project, which is a little bit convoluted. You shouldn't have to do that. You should be able to do that with inside the schematic editor, I think.

**Dave Jones:** That just seems a little bit silly to me. So, what I'm going to do is I'm going to, I'm not quite sure how any of this works, because it is literally the first time. So let's open up Open Recent. We've already got that PIC programmer which we had last time, so that's a good place to start, I guess.

**Dave Jones:** So, I don't know whether or not you have to have the schematic loaded, I don't think so. So let's try and go into this component editor here, and, not sorry, not component editor, this, what's it called? It's called a Components to Modules, CVPCB.

**Dave Jones:** Jeez, I don't know, it's a bit convoluted, I think they have to fix that up, I guess. What do we do? Do we have to open it? No, that's right, somebody said that we have to do a netlist. That's right, so we have to go into, apparently, go into our schematic, generate netlist, and default format, ORCAD,

**Dave Jones:** oh, here's the different netlist formats, ORCAD PCB, CADSTAR, SPICE, there you go, or add a plug-in. Wow, you can get plug-ins for different, exporting to different netlists, that's excellent. Right, see, this button should just not say netlist, it should say generate, or go, or something like that, start.

**Dave Jones:** There's been a few buttons like that, so I'm not sure what the thinking has been for this, so we'll keep it in the PicProgrammer subdirectory here, picprogrammer.net, and, as I said, this is the absolute first time I've done this, so this is not a tutorial,

**Dave Jones:** this is very much a first impressions type thing, so absolute first time I've used any of this tool, so if you're watching this for the first time, you should check out my previous video, otherwise you won't know where I left off from last time.

**Dave Jones:** So, apparently, we've got to open, I think in this thing, we've got to open, where is it, doc, no, wasn't in tutorials, no, where was it, no, hang on, it's share, that's right, demos, and PicProgrammer, there we go. So we can load in our net, so that's what we're doing, we're loading in our netlist,

**Dave Jones:** and bingo, okay, so it looks like that is correct, this is what this module does, it actually loads in a netlist from your schematic, and then we assign footprints, so here's our footprints over here, or filtered footprints, I guess, I'm not sure where it actually got those from, but here's all of our caps,

**Dave Jones:** and do we really have to, oh, okay, no, alright, it's filtered, right, so as you choose a different component, it knows that that's a DB9 connector, for example, and it's given you various options down here, ooh, that's a bit, actually, that's kind of neat, I guess, but it's a bit convoluted,

**Dave Jones:** I would have liked to have had seen this functionality in the schematic editor, I don't see the need for having this separate program at all. Within the schematic editor, in each part, I would have expected a field, actually, let's go in there, and let's go into the schematic editor here,

**Dave Jones:** and have a look, do we actually have, if we, how do we edit, I forget, is it E? There we go, E, you hold your cursor over the particular item, and you press E for edit, and no, there it is, it's got a footprint,

**Dave Jones:** so you can presumably just enter that field value, if you know the name, I guess, so you would have to actually type it in, because if you're just typing something, you can't, it's not like it pops up or there's a button to go to a PCB library to choose your footprint,

**Dave Jones:** you see, that's what I would have expected, that's how Altium works, and some other packages, so really, you know, that's really a bit convoluted, I think it should be in the schematic editor, it's already got the field here for the footprint, so I can't see any reason why you need that separate program,

**Dave Jones:** should just be a button here that says, you know, choose footprint, a big button down here, there it is down there, there's a tip for you, off the cuff, of course, haven't really thought about it too much, but that makes sense to me, if there was a pick footprint button there,

**Dave Jones:** and you could just choose the footprint, and it puts it in the schematic, and then when you push the schematic through to the PCB, that would be much better, so yeah, I'm not too happy with that, so apparently this is how you have to do your footprints,

**Dave Jones:** it's a bit crazy, I know, but, well, these are already chosen by default, because we already have a project, so I'm not going to do one from scratch, yeah, no, 8-pin DIP, so it's already, so if we choose this IC down here, this E2P 24CXX, it looks like it's come up, I mean, it's come up with 450-odd footprints,

**Dave Jones:** which is, which is okay, I guess, at least you can choose from the whole lot, but it's, you know, it's mixed in with resistors and all sorts of stuff, so yeah, I, yeah, not too keen on that at all, so that's what apparently this module here does, display footprints list documentation,

**Dave Jones:** ooh, let's have a look at the footprints list documentation, and, right, oh, it's kind of neat, I guess, but that could be massively outdated in, well, I guess it's never outdated, because all the base footprints are there, but, gee, I don't know, so they've opened this, they've given you this PDF with,

**Dave Jones:** presumably you can auto-generate something like this, the program's capable of doing that, so that's kind of neat, I guess, if you're a beginner and you want to choose a basic footprint, but when you've, you know, in a professional package, you don't really want to,

**Dave Jones:** you know, you don't really want some sort of capability like that, here we go, what's this button up here, display the filtered footprint list for the current component, okay, yep, that's what we've got, and display the full footprint list without filtering, okay, so at any time you can just, so this one here, so if we go up, oh no, there we go,

**Dave Jones:** so filtered, yep, and you can swap between the full list and filtered, okay, fair enough, I'm not sure how it determines the filter, maybe based on that it's a cap, it knows it's a cap, maybe the designator or something, C5, maybe it filters like that, here we go,

**Dave Jones:** create export file, component footprint list used by eeschema, still don't like that name, to fill the footprint field of components, okay, so once you've matched them, that fills them up, but I think it's already been done, because this is an example project, so what is it, perform automatic footprint association,

**Dave Jones:** I don't know, I don't trust any automated tools in a CAD program, that sounds a bit dodgy, but maybe it's a decent first pass, maybe it knows caps are assigned to capacitor footprints, or something like that, view selected footprint, oh yeah, here we go, now we're talking,

**Dave Jones:** there we go, view selected footprint, so we're in, this is a footprint viewer, I'm assuming, and not a footprint editor, it doesn't look like, change cursor shape, millimeters metric, show text, show outlines, oh yeah, okay, that's pretty neat, it shows the outline, it shows just the single line like that,

**Dave Jones:** or it shows the full actual width of the silkscreen, or it shows the outline silkscreen, outline silkscreen, that's neat, text can be the same thing, there once again, panning is a bit of a pain in the ass in this thing, not too happy with the panning, but change cursor shape,

**Dave Jones:** so this is not an editor, this is just a viewer, I can't see any capability to edit, let's view 3D, oh, here we go, there's our capacitor, ah, neat, looks like red is the top layer there, green is the bottom layer, so I haven't even opened the PCB editor yet, yet I know,

**Dave Jones:** hopefully it's consistent, by default red's going to be the top layer, and green is the bottom, kind of makes sense, because green is usually ground, and that's usually on the bottom layer, and positive one's on the top, which indicates by red, so that's not bad, kind of like that,

**Dave Jones:** alright, that's pretty neat, so that's a component footprint viewer, that allows you to actually check exactly what footprint you've chosen, which is vital actually, because you can't just rely on the name over here, you know, SM0805, you know, who knows, right, someone who created that footprint might have had a different intention

**Dave Jones:** to what you think it is, or to what it's labelled, so it's good to be able to go in there and check that footprint, so here we go, save netlist and footprint files, view selected, well, actually, I think we're going to have to do that,

**Dave Jones:** because, no, it hasn't come up with anything, no, oh, okay, it's just saving the changes, right, okay, okay, view selected footprint, perform automatic, okay, create export file, okay, better do that actually, stf, alright, pickprogrammer.stf in the pickprogrammer subdirectory, save, I guess that's what we load into the PCB editor,

**Dave Jones:** alright, so we're done with that, I rather like the modular approach, I mean, the modular thing that, you know, the schematics its own window automatically, and, you know, Outium have followed, for example, have followed the unified library where everything's in the one program,

**Dave Jones:** and that can be nice in some respects, but this is, you know, it's just nice just to have these things as separate windows, because most of the time when I'm doing PCBs in Outium, I will have two separate monitors, in fact, I used to have three separate monitors,

**Dave Jones:** and I invariably end up separating the monitors into PCB and schematic anyway, so I would actually have to create a second window instance of Outium, but this does it automatically, this is because it's modular, it is the traditional way to do these programs,

**Dave Jones:** you have a separate schematic editor, separate PCB editor, separate library editor or something like that, so really, that's, you know, I don't think there's anything inherently wrong with that at all, and it could be advantageous. Now, somebody told me that within here, within the schematic editor that we're in,

**Dave Jones:** there is a way to, the library editor is in here somewhere, run PCB new to layout new printed circuit board, run CV PCB, okay, so you can load up that module we just had, associate components with footprints, pretty convoluted process as I said,

**Dave Jones:** but somebody mentioned that there is the editor in here, tools, library browser, library editor, there we go, all right, let's try the library browser, this is the schematic component library browser, and what have we got here? Well, where's the list? Create a new component, load component to edit from current library,

**Dave Jones:** ah, okay, I would have preferred if it, like, down the right-hand side here, it just had a list of all your current components, but it looks like you've got to go up here and actually load one, and choose your library, that's okay, I just would have preferred that it actually had a,

**Dave Jones:** actually had a direct, like a tabbed window or something on the side, or something like that, anyway, I do like, as I mentioned before, I do like the fact that it has generated, presumably automatically, a library for the current project. That's rather neat, when you're loading someone's existing design,

**Dave Jones:** then you can just load up their particular, you know, steal all their footprints and stuff like that, it sounds bad, but it's not, you know, that's a good idea, if you're loading someone else's project, you go, oh, look, they've got all these nice footprints I want,

**Dave Jones:** and you can actually steal them out and put them in your own libraries, or just save it as their library and then just load it up. So let's say, place, pin, that's pretty easy. Oh, where's the picture of the pin? I'm trying to place a pin, I would have expected a picture of the pin to show up,

**Dave Jones:** and I presume that, is that this end, or is that that end of the line? We'll find out, let me click there. Okay, you can do the length of it, 0.3 inches, 300 thou, to start, width is the length, does that change in real time?

**Dave Jones:** Let's try it, 2, yes it does. Alright, so it'll be shorter than the others, pin name, test, pin number, 10, and orientation, right, blah, blah, graphic styles, okay, so you can do, it's got all the standard stuff, you can do clocks, inverted clocks, and inputs and outputs,

**Dave Jones:** No, it's missing open collector. Where's an open collector output? It's not there. Anyway, let's just say it's a full image, nah, let's go with an inverted clock. There we go. Ah, now it's popped up, okay. It would have been, is that a bug?

**Dave Jones:** I don't know, it probably should pop up by default as that. So, there you go, we just added a pin. Nice, easy, that works well. What else can you place? You can place text, rectangles, circles, arcs, lines, or polygons. That's probably all you want.

**Dave Jones:** I assume that this text up here is your, do the keys work the same? So if I move the cursor over and press E, does that edit? Yes, it does, it edits that field. So it is consistent with the schematic editor, it should be,

**Dave Jones:** because the library editor is also part of the schematic editor. So, for the reference field, but how do we know that's the designator? It doesn't really, it just says it's a field, it doesn't actually say it's a reference designator, so you can't actually place,

**Dave Jones:** so all you're doing is really placing text, you're not actually placing a reference designator as such. So, there you go, okay, right. It's interesting. Now, what else have we got here? Test for duplicate and off-grid pins. That's handy, because there's nothing worse than you having,

**Dave Jones:** than you've used a different grid for your library editor and you've got some pins that are slightly off-grid, they're not in, they're not joined up to one of these dots. You probably can't see those little background dots there, it's hard to see, but that grid in there,

**Dave Jones:** if that pin is slightly off and then you go and place this library component inside your schematic, then if it doesn't match and it's slightly off, it's really annoying, unless you've got like a snap, a smart snap system that'll snap your cursor to the pin.

**Dave Jones:** That can really be annoying and really ruin your day. So, not too keen with that. Is there an option to push it straight through to place it directly, you can save it to the library, export it, import it. Oh, let's have a look at import.

**Dave Jones:** Keycad component libraries. No, it's not like you can import an Eagle footprint or something like that. Maybe there's a tool out there that allows you to convert libraries, but you can't do it directly inside the library editor. Update component, create new component, load component.

**Dave Jones:** Oh boy, okay. And presumably you'd be able to make subcomponents. I'm assuming that's what this field here is for, is for doing subcomponents. Like if you've got a NAND gate, like a 7400, it would have four individual components within the one library. So it would have, you know, U1A, U1B, U1C, U1D, etc.

**Dave Jones:** So I'm assuming that's what that field there is for. And create a new component, load component, and save current library to disk. Select working library. There's no place option. Where's a place? Export current drawing. I want just a place command. Move part anchor.

**Dave Jones:** Well, the anchor is in the center, I'm assuming. Let's try that. Yep, there we go. So... Yeah, there's no option, no button there, to just go and place it. Bummer. So it only allows you to edit... Oh well, could be worse. Discard changes.

**Dave Jones:** Yes. Alright, so that's our library editor. It's not bad. I mean, it does the job. So where were we up to? We were up to the PCB. So trying to push this through to a PCB. Now, so that's our library browser, our library editor.

**Dave Jones:** Annotate. Ooh, let's have a look at annotate. You can annotate the entire schematic. Use the entire schematic, use current page only. Okay, so you can limit the scope to the current page, which is good. You can keep any existing annotation. So presumably anything with a question mark left.

**Dave Jones:** So I assume if you put like U something, that it will actually... Like if you put U question mark, then it will actually add and give you the next available number. So if you've got C1 through 5 on your sheet, and you've got C question mark,

**Dave Jones:** it'll give you C6 for the next one. Or you can reset and just re-annotate the entire schematic. Good. That's an essential item. So we've generated our netlist. Assign component footprints. That's that CV editor thing that we had before. He's already running. Yeah, there it is.

**Dave Jones:** Continue. No. Okay. And you can save your preferences. All right. Layout printed circuit board, I guess. There's no way to... Is there a way to push it? Run PCB new to layout. So there's not like a push command to put something like that or something equivalent

**Dave Jones:** to automatically load in the PCB program and load in the netlist from this. It'd be nice if it was automated. If it was just like a push, a button up here that just said push to PCB and it would automatically generate the netlist.

**Dave Jones:** If it has to work that way, then fine. Generates the netlist, opens the PCB editor and loads in the netlist. But you've got to do it manually. It's not a big deal, but just would have been nice to automate that process. Then again, I'm getting ahead of myself.

**Dave Jones:** It might actually do that, and it might make a fool of me. So run PCB new to layout circuit board. Here we go. Ooh. Okay. No, it's smart. There you go. It's automatically loaded up the PCB. It automatically knows because this is an existing project.

**Dave Jones:** So I guess we would have had to start a new project to actually see if it had that capability of pushing those parts through. So we're in the PCB editor now, and it works, looks like panning is exactly the same. It zooms in and out wherever your current cursor is.

**Dave Jones:** How do you switch layers? Let's try the plus minus key. That's what you do in Altium. Oh, yeah, I can see it move over here. Component. No, it's just switching between. Oh, yeah, it is. It's switching between. It says the layer over here.

**Dave Jones:** It says front copper layer. The back copper layer is called cuver. I can't even pronounce that. I'm sure I'm pronouncing that wrong. But why is it called cuver by default? I have no idea. Is that some sort of, that obviously means something in a different language perhaps,

**Dave Jones:** but at least the tooltip there tells you it's the back copper layer. But okay, I'm selecting that layer, but it's not redrawing the screen. So it's not putting that on top. See, it's shadowed and it's underneath. So it's how do I make like a single layer mode,

**Dave Jones:** which is the equivalent in Altium, which allows, because this can get very complicated. Like if I'm doing this board and it's an eight layer board, for example, and you've got eight different layers of all things that are slightly all shaded in different colors,

**Dave Jones:** it's going to be very confusing. So I want to focus that color, show active layer selections. Yeah, there we go. Composent, cuver. So really these are not in English. I don't know what language that is. Somebody will tell. Ah, French, because I think the main program is French, I believe,

**Dave Jones:** if I'm not mistaken. So, and that kind of sounds French to me. So select layer pairs, top layer, bottom layer. I'm not sure what this layer pair business is. Ah, the same, yeah. Oh, okay, right. To be displayed, I guess. I don't, yeah, I don't understand that.

**Dave Jones:** Anyway, all I want to do is design rule check, read netlist. Let me look at the buttons here. Open module editor. Module editor, I assume. Once again, I believe that's the footprint editor, if I'm not mistaken. Let's click on that. And it is, it's the footprint editor,

**Dave Jones:** but they've called it the module editor. Wow, really? I think they need to work on these names. I mean, you know, nobody calls a PCB footprint a module. That's just, yeah, that just doesn't work. New module, load module from library. Yeah, load module from current board.

**Dave Jones:** No. No, nothing worked there. So anyway, their names are a bit convoluted. Coming from a English-speaking Altium user, of course. Completely biased. So, oh boy. What else have we got here? We've got mode footprint. Manual and automatic move and place modules. Mode tracking.

**Dave Jones:** Auto-routing. Why anyone bothers with auto-routing in a low-end product like this? You're just wasting your effort. If this thing does have an auto-router, then I don't know why you would bother. Yeah, I've turned that on, and I'm not sure what I'm doing there.

**Dave Jones:** Manual and automatic move and place. Hmm. Show active layer selections. And really, I'm at a loss as to, bottom layer, top layer is, I don't understand that. Okay. How do you, like a double-click on this, and I expect maybe show all copper layers.

**Dave Jones:** Yeah, okay. No, hide all copper layers. All right. I've hid all my copper layers, and I've just got, one thing I don't like, is the template on there. I don't traditionally like a template on my PCB file. Sometimes I will do that. Some jobs I've worked at have, you know,

**Dave Jones:** forced me to do that, and we'll have like a big info panel up here, which has all the build information and stuff like that. But typically, because that's red, I'm going to assume that's on the copper, that's on the top copper layer, and I really don't like that at all.

**Dave Jones:** If I move my cursor over that and hit edit, no, it is a template, I think. It looks like that hasn't been placed manually. This is all, this outer border here is a template thing, and I'm not too keen on that at all.

**Dave Jones:** If it does that by default, if you go new, I'm assuming it does that. If you go file, new, it will come up with that template. That's in my guess anyway. But I still haven't figured out how to get to my layer. I know I should read the manual,

**Dave Jones:** but I don't want to. I want to see how, that's the whole idea of this video, is to see how intuitive, high contrast display mode, oh, I like that, that allows you to, okay, that allows you to see things. Can you switch between layers with that?

**Dave Jones:** Ah, yeah, now we're talking. Okay, so maybe you've got, ah, that's the equivalent, there you go, I think I found it. That's the equivalent of the single layer mode, i.e. it makes all the other layers grayed out, and then the current layer you're on

**Dave Jones:** highlighted red above everything else, and that's, I'd have to load in a multi-layer board to actually confirm that effect. And you can see this track here, why have they gone roop, roop, roop, roop, and around like that? Why not just straight down like that?

**Dave Jones:** Anyway, that's the things you pick up when you look at boards in isolation, and look at layers in isolation like this, you can really see things. Oh, okay, there's the solid to outline trace mode. I'm not, some people are a big fan of the outline trace mode.

**Dave Jones:** I am not. When I'm laying out my boards, I like to see the real thing exactly like I'm going to get it. But some people like that, so that's a good feature, show vias in outline mode. Okay, excellent. I don't think there's any vias on this board,

**Dave Jones:** is there? Ah, yeah, there's a couple down here. Okay, there we go. And a good thing is, there you go, it shows the net name on the, it shows the net name on all, you know, parts of the trace, the traces that it can,

**Dave Jones:** which is excellent. And that really works, the threshold level there actually, where that switches on and off, that is, they've chosen that well. I'm quite happy with that because you can read that almost down to that last level there, and then it switches off.

**Dave Jones:** You see that text, that data RB7 there, it gets down to there, and I can still just read that, and then bang, threshold level, perfect, excellent work, they've done that well. So let's take a look at the, ah, still used to dragging, left dragging, hang on.

**Dave Jones:** Goof the window here. So let's, the outline via mode, show pads in outline mode, oh, okay, right, excellent. Vias in, oh, that's show outline of field areas, that's our polygon pour, excellent, okay. And now, how do I turn that off? Oh, we've disabled,

**Dave Jones:** completely disabled, do not show field areas in zones, okay. Right, and then that show field areas, okay, so we've got show field areas. If we turn the outline mode off, where was it? Show tracks in outline mode, no, we've lost that other icon,

**Dave Jones:** where'd it go? Ah, there we go, look, yeah, this window is not big enough, we've lost a couple of items down the bottom here. We've got a couple, show hide the toolbar for microwave tools, ooh, ooh, it's got microwave tools, does it? Create gap specified length for microwave applications,

**Dave Jones:** create line of specified length, there you go, there you go, excellent. It's got some high speed, high speed design capability, you can create a matched length, it doesn't, I don't know if that does a matched length pair or not, but certainly, wow, length, okay, yeah,

**Dave Jones:** I don't know how that works, that would require an hour of playing around with just on its own, but that's good that that capability is there at least, show hide the layers manager toolbar, okay, excellent, and normal contrast display mode, there it is,

**Dave Jones:** so it was off the screen, so once again, you've got to have bigger than a 1280 by 720 screen to, maybe not to use it, but to see all the icons and stuff, you've got to have a screen that's bigger than that, so there you go,

**Dave Jones:** that's our, so we'll be able to see our polygons there, our polygons are gone, you can just make them vanish, that's nice, polygon outline mode, some people like that, but me, I either want full polygons or no polygons if I'm routing the board,

**Dave Jones:** and then full polygon, can we just redraw? I wonder if we can re-flood that polygon, if we just go edit, no, maybe I've got to go to the top layer, press escape, I'm on the top layer, the QV, pronouncing that wrong, I'm sure the French people are laughing at me,

**Dave Jones:** and E for edit, see, I can't edit that polygon, so there's probably some redraw polygon command somewhere, free route, DRC, oh boy, that PCB editors are, you know, to look at these things, I've been going for 33 minutes already, and I really, it would take me many, many hours

**Dave Jones:** to come to grips with this PCB editor, so please forgive me if I don't cover, I'm definitely not going to be able to cover everything here, and once again, this is the first time I've used it, now they call it a zone, yeah, they call it a zone,

**Dave Jones:** a flood fill, or a polygon pour is a zone, but they're in zones, show field areas in zones, okay, sorry, polygon pour is a zone in KiCad Speak, I guess, so, every program has its own, you know, different thing like that, now what?

**Dave Jones:** Maybe I'm probably done enough I want to do in a preloaded PCB, actually, well, no, I haven't, I mean, let's go in and edit a pin, for example, module properties, see, it's a module, it's a, it's a PCB module, I don't like that,

**Dave Jones:** it's a, it's a part, you know, it's, oh, they call it a module, I don't like it, so you can, looks like you can change the footprint directly here, you can choose another one, change module, well, you know, it should be called footprint,

**Dave Jones:** crazy, um, heck, can I edit that pad, I just want to edit that pad, please, uh, edit, no, it just, footprint, see, they've called it footprint there, but when you go into it, it's module, right, that's, there it is, they've got footprint here,

**Dave Jones:** um, and then delete module, it's delete footprint, is it not, I don't understand all the mixed, there's a lot of mixed terminology in this program, which, could do with some clarification, um, global move in place, like, how do I, can I edit, surely,

**Dave Jones:** I can edit, the pad, must be a way I can edit the pad, this is, not good, anyway, uh, metric imperial mode, of course, um, I'm sure you can change out grid, hide, hide grid, okay, dots, at the moment, can probably change those to lines,

**Dave Jones:** for those who prefer the line, grid, uh, origin point for the grid, okay, place origin point for the drill and place files, I'm not sure why you'd want, a different one, uh, usually they're tied together, set the origin point for the grid, oh,

**Dave Jones:** okay, right, so you can offset a grid, from the, oh, um, add layer, align target, oh, okay, that's neat, so, you can add a fiducial, there we go, layer alignment, that's not a fiducial, that's just a, it's just a, yeah, they've just done a target thing,

**Dave Jones:** I don't know, don't get it, add field zones, add module, there it is, add module, not add footprint, um, display local rats nest, okay, that's what I wanted to look at, when I did a, a board, I wanted to display the rats nest,

**Dave Jones:** but you won't get that on the finished board, because presumably, the rats nest will vanish, um, if you don't know what a rats nest is, it just shows all the connections, between, you know, if this, this resistor here, is connected to this pin down here,

**Dave Jones:** there'll be a faint line, between those, um, when you first, put all the footprints down, it'll tell you that you have to, you know, you haven't routed that connection yet, and that's what a rats nest is, so, uh, highlight net, oh, there we go,

**Dave Jones:** that highlights a net, neat, that works, pretty essential feature, in a, uh, PCB program, does it, okay, it just swaps it, maybe if you hold down control, does it highlight multiple, shift, nah, it doesn't, it doesn't allow you to highlight multiple, I really like,

**Dave Jones:** it'd be nice, if that could highlight multiple, traces, maybe there is a way to do it, but, it doesn't look like it, but it highlights it in top and bottom, and does it come through, that's what I want to check, does it come through the,

**Dave Jones:** high contrast display mode, yes it does, there we go, we're in high contrast display mode, and, although it doesn't, it shows you, it does show you the highlighted on the bottom, so they've got that working, pretty happy with that, um, and what else have we got here,

**Dave Jones:** oh boy, fast access to the web based free route, advanced router, no thanks, auto routers, jeez, um, perform design rule checks, by net class minimum trace width, excellent, um, is it only in millimetres, or can you choose metric, for that, if we're in millimetre mode at the moment,

**Dave Jones:** so I'm assuming, if we go to, imperial mode, inches, and we go back up to that, where was it, design rules, no, hang on, where was it, ERC, perform design rule check, there it is, in inches, yes, it's put the, right, it's put the,

**Dave Jones:** um, quote marks there for inches, there you go, but it does, okay, it does switch, that works, they've done that, um, be nice if you could, do it from within here, just, you know, a little button up here, imperial metric, or something like that,

**Dave Jones:** but that's only a small thing, not a big deal, um, polar coordinates as well, you can display the, there you go, down in, down here, you can display polar coordinates, excellent, that's handy for laying out, uh, circular boards, and things like that, so,

**Dave Jones:** um, you know, if you've got a circular board, and you want to put things around the outside connector, at certain, you know, 10 degree intervals, um, that's pretty handy, so I like that, that's neat, disable design rule checking, presumably as you're routing, uh,

**Dave Jones:** what else have we got, page settings, paper size and text, oh yeah, by default, yeah, A4, none of this, uh, none of this, fools, none of this, you know, US rubbish, that's great, A4, excellent, um, 3D display, oh, let's have a look at it,

**Dave Jones:** there we go, let's check it out, I don't have my 3D space navigator, but presumably, hey, there we go, neat, but, you know, it's pretty primitive, but, uh, it's certainly not, nothing compared to, uh, the Altium 3D viewer, which is pretty much the best in the business,

**Dave Jones:** um, but, hey, for the price, you can't complain, so, there you go, that's, the thing I use, uh, 3D mode for, though, is not necessarily for the components, I use it because it gives you the very high contrast of what the board's going to look like,

**Dave Jones:** now, this 3D mode doesn't appear to give me the, uh, solder mask, and stuff like that, which is what I use the 3D editor in Altium, mostly for, is to actually, you can, it actually looks like your finished board, you can change the colour of the solder mask,

**Dave Jones:** it shows the solder mask expansion, and stuff like that, that's one thing we haven't looked at yet, is, uh, solder mask, expansion in here, 3D axis, 3D, zone fill in, you can turn the zones off and on, okay, well, that's wonderful, but, where's the,

**Dave Jones:** where's the, uh, solder mask? I mean, that's a huge, I think they've missed, the boat there, oh, yeah, there you go, you can export to a PNG or JPEG, that's nice, but, I think they've entirely, missed half of the point of having a 3D mode,

**Dave Jones:** is that you can actually view, the board as a finished product, and I'd have to load up Altium to actually, um, show you, but I've done it in previous videos, and it shows the solder mask expansion, and the silkscreen, and stuff like that,

**Dave Jones:** so, here we go, if we go mask, here we go, here's our mask, there we go, see, that's the solder mask expansion, right, assuming, like, this is all a through-hole board, but if this was a, if this was a, um, uh, SMD board,

**Dave Jones:** right, that distance between, those two pink, or purple solder masks, um, that solder mask there, that wouldn't be enough, and you'd get a breakout, between those two, you know, there would be a minimum, um, say, four thou, or five thou, or something like that,

**Dave Jones:** that you'd want, between, the, uh, solder mask, points there, so, um, you'd have to go through, and, ah, there's so much, to do in a PCB editor, it's crazy, so in the design rule checker, um, you would have to check, I would have to make sure,

**Dave Jones:** that it can actually do, uh, solder mask, uh, solder mask, um, uh, rule, that the actual rules, apply to the solder mask as well, and possibly, it looks like it might only be a copper, DRC checker, I don't, I don't, quote me on this,

**Dave Jones:** but I can't see, like, any option there, minimum track width, minimum via size, minimum micro via size, but where's, like, the options, for the, solder mask, expansion, I don't, ah, for, for the solder mask, you know, like a, a minimum solder mask, uh,

**Dave Jones:** slither, like, they might call it, so, I don't see anything there at all, crazy, unconnected, track clearances, nah, looks like it's only a copper, DRC, oh, that's pretty disappointing, um, any, good, uh, PCB tool, should be able to, um, tell you that you haven't met some minimum requirement,

**Dave Jones:** between your solder mask, there, so, oh, geez, I wish it had that feature, it's not a show stopper, but, gee, that would have been nice, um, and also in the 3D viewer, of course, because, but, we can view our, we're in high contrast mode here,

**Dave Jones:** okay, so if we, yeah, you've got to go into that high contrast mode, to actually see, the solder mask expansion, and that's not bad, you know, you can, that's a substitute for the good 3D, mode that would have that, but, yeah, well, there you go,

**Dave Jones:** I mean, once you're in, okay, once you're in that high contrast mode, you can just single click, between the layers, and that's, that's, that's really quite good, I do, I do like that, that works, as expected, excellent, and the silkscreen layers, and, uh,

**Dave Jones:** PCB edges, so it looks, render, okay, ah, okay, what's that, okay, so you can, yeah, tell it to render, certain, layers only, effectively, okay, so that's like an, a, um, turn on off, feature for that layer, I guess, get, no, but that's, no,

**Dave Jones:** that's, turn off and on, eh, okay, it seems to do the same thing, if you go on there, and you, okay, I don't get that, but, anyway, let's, oh, now, what else, we haven't, rat's nest, we haven't looked at rat's nest, not being on for 45 minutes already,

**Dave Jones:** geez, sorry, this sort of stuff, takes, you know, it takes a long time, this is me, playing with it for the first time, as I've said, so, maybe, if we go into, if we go back into, our schematic editor, and we go, run new PCB,

**Dave Jones:** run PCB new, to layout printed circuit board, well, that's what I did last time, but I want to, actually, get, do a completely new one, layout printed circuit board, and it's just going to load, PCB new was already running, continue, yes, it just loads up the existing board,

**Dave Jones:** maybe, I've got to rename it, let's try and, save, whole schematic project, save current sheet as, oh, now you get into where, oh, I can, oh, I can, I can, I can't, yeah, so, maybe, where I can go in, and layout printed circuit board,

**Dave Jones:** and it's just going to load, PCB new is already running, continue, maybe, oh, now you get into where, you've, no, I'd have to go into, explorer, and, you know, the file system, and actually change, copy a project, and then delete, or manually delete the PCB,

**Dave Jones:** and, oh, boy, yeah, I could do it, I could do it, yeah, if we're really, really keen, I think I am, I think I really want to, see this, so let's, I'm, I'm off screen here, I'm just, program files, x86, key cad, where are we,

**Dave Jones:** yeah, key cad, and, bin, share, documents, demos, demos, yep, pick programmer, okay, I'm, what I'm going to do, is I'm going to re-label, that pick programmer board, so, I'm going to, I'm going to, I'm going to, I'm going to, I'm going to, I'm going to,

**Dave Jones:** I'm going to, continue, okay, I've re-labeled it, alright, so let's go back into, this file doesn't exist anymore, so I'm going to shut down that, nope, and, right, so I've re-labeled that board, so it, hopefully shouldn't be able to find, that pick programmer PCB anymore,

**Dave Jones:** so if we push through, to our PCB, there we go, excellent, hang on, let's come up with this error message, this is normal for a new project, yeah, whatever, does not exist yet, right, okay, so it's actually created, so it knows that file's not there,

**Dave Jones:** and it's created, the board, let me drag this, into view here, so it's created our PCB there, and once again, it did exactly what I thought, it's created that template, there you go, it's create, I'm not, a fan of that, maybe there's a way to disable it,

**Dave Jones:** but I don't, like having a template, on my, board, unless I, choose to do it, but anyway, so now, we've, it hasn't, see this is where it should have, automatically, pushed through those components, this is where you need to, integrate the programs, just a little bit,

**Dave Jones:** you need, to automatically, push through that netlist, and load it, onto this PCB, and it hasn't done that, so we've got to do that manually, obviously, so open existing board, save board, place, blah, blah, blah, import, net, find component, net, read netlist, here we go,

**Dave Jones:** so I've got to read the netlist, read current netlist, browse netlist files, ah, there you go, it knows, at least it knows, the current netlist, is pickprogrammer.net, or did it get that before, we, did, it just knows that, from before, when we had it loaded up,

**Dave Jones:** I don't know, whether or not it's smart, or just coincidence, but let's read it, so, rebuild board, connectivity, some footprints are not found in libraries, ah, great, okay, it hasn't found, dip, it hasn't found the dip packages, terrific, hasn't, hasn't found quite a few things,

**Dave Jones:** that's disappointing, for an example demo, program, not too happy with that, extra footprints, keep, exchange module, exchange module, I have no idea what that means, but we do know that means, but we do know that module means, footprint, module selection, reference, time stamp,

**Dave Jones:** what, select how footprints are recognized, by their reference designator, or their time stamp, why would you, want them recognized by their, ah, if it's newer, special setting, after a full schematic re-annotation, okay, right, fair enough, keep or change an existing footprint, when the netlist gives a different footprint,

**Dave Jones:** all right, ah, keyboard track deletion, oh, that's nice, if it does, keyboard delete bad tracks, after netlist change, if that does what I think it does, that's quite a neat feature, um, if you're laying out a board, and you've done it, you've half done it,

**Dave Jones:** or you've fully done it, and you make some changes in the schematic, and you push them forward, and you import the netlist here, then any non-matching tracks, that don't go anywhere anymore, are automatically deleted, that can be a nice, clean up step, so you don't have to go through,

**Dave Jones:** and manually clean up those traces, I'm going to assume, that that's what that does, it really sounds like it, so that's a neat feature, I like that, that could come in, that could save you a lot of time, so, somebody was thinking there,

**Dave Jones:** extra footprints, and if we've got any left over footprints, um, and you can lock footprints, good, okay, I didn't check that capability, you can actually lock them, um, footprints test, read the current netlist file, and list missing, and extra footprints, well, duplicates, there's no duplicates,

**Dave Jones:** but we're missing, a few, so, missing, a couple of P's, and a couple of U's, rebuild board connectivity, rebuild the full rat's nest, useful after a manual pad change, right, no, okay, so, we've read it in, I guess, we're done, we close, right,

**Dave Jones:** where are our footprints, oh, there they are, there they are, they've, uh, created a new automatic way, to spread them, that's the first thing, would have been nice, if it automatically just, spread them out, but, so is there an auto place, capability, so this is the only thing,

**Dave Jones:** that auto placement, auto component placement, is good for is just, getting them out of this jumbled, mess, and, uh, ah, I don't think, I don't remember seeing, any, there was auto routing, but there's no auto placement, tools, no, free route, no, design, no,

**Dave Jones:** all we had, is the auto router, thing over here, web based free route, advanced router, no, okay, maybe there is some, selection clarification, but yeah, this is going to get nasty, so what we're going to do, what we might have to do, there's probably,

**Dave Jones:** a better way to do this, surely they've thought about it, but M for move, so, you know, you just go M, and you've got to, just, manually, get them out of there, oops, see, I accidentally moved a, foot, a designator, instead of a footprint,

**Dave Jones:** you know, so, wow, and this can be, this can, you know, really be, an annoying step, if you've got a lot of components, then, but maybe there's a better way to do it, so don't quote me, because I don't, know anything about this package at all,

**Dave Jones:** so there you go, but anyway, that shows the net lists, and, especially when you drag components around, that's what I was looking for, unfortunately all the chips aren't in there, but, when you move something around, you can see, that the net lists, net lists,

**Dave Jones:** the, the, rat's nest, sorry, the rat's nest, lines there, automatically, move around, with it, to show you, and that's, absolutely essential, with any PCB editor, program, to be able to, do that, because once again, there's a bit of, ghosting, left over on the display,

**Dave Jones:** bit of garbage, left there, that's just a driver issue, or something like that, but anyway, that's quite, that's quite neat, so, the, rat's nest, works, and you can turn that off and on, where was it, highlight net, display local rat's nest, oh, it doesn't,

**Dave Jones:** allow you to switch it off, hmm, okay, no, don't know what's going on there, yeah, highlight and display local rat's nest, doesn't let you turn it off, which can be annoying, because sometimes, you just want to get rid of those, bloody rat's nest lines,

**Dave Jones:** because they're annoying, um, but other times, they're absolutely essential, so you want to be able to turn those, off and on, fairly easily, there probably is a way, I'm going to give it the benefit of the doubt, um, what else have we got in a PCB editor,

**Dave Jones:** tons of stuff, haven't even covered, uh, haven't even tried to route anything yet, for goodness sake, um, and, uh, grids, where's our grid, where's our, uh, component and, uh, electrical grids, hide grid, preferences, display, there's no, grid references, let's try display, I guess,

**Dave Jones:** or let's try general, uh, display polar grid, oh, there we go, that's neat, okay, and once again, got a full screen cursor, for the fan of the full screen cursor, it's there, very 1970s, the old, uh, full screen cursor, if you don't know what that is,

**Dave Jones:** it's, uh, it, it's a full screen cursor like that, and you go all the way across, it's very old school, but some people love it, some people really get off on that, um, and it, and it can be useful, so, uh, that's neat,

**Dave Jones:** and, uh, DSC on, uh, I assume there, no, you say, right, DSC, I assume when you're routing, it'll automatically tell you if you're, uh, it'll do online, DS, what's called online, DSC, or, uh, real time DSC, magnetic tracks, when creating tracks, control the capture of the PCB,

**Dave Jones:** cursor, when the mouse cursor enters a track, excellent, that looks like automatic, uh, snap centering, which I think I mentioned before, um, magnetic pads, excellent, so you, snap to the center of the pad, that's absolutely essential, so, if your component's off grid, this is really useful in mixed,

**Dave Jones:** um, uh, imperial metric, uh, boards, if you're, um, say you're laying out a, a board, an all SMD board, but you've got one through hole part on there, which is off grid, because it's an imperial pin pitch of .1 inch, then you don't have to change your grids,

**Dave Jones:** this will, you can just place your component, and even though it's, the pad is off the grid, this should automatically snap, your track, into that particular, um, pad, and we can try that, but, jeez, I've been going for almost an hour, and, wow,

**Dave Jones:** it'd take me, another hour, just to try out all the, routing, things on here, so, really it's, you know, eh, oh, outline mode, does it automatically do that, or are we, okay, but it, it has limited due to 45 degrees, and, ah, ah,

**Dave Jones:** that's, yeah, that, that works, works as expected, routing works, routing works a treat, what if we go over something, that, is, not, the design, not in the design rule, no, hang on, that doesn't seem to snap into place, hey, what happened to my,

**Dave Jones:** what happened to my, route there, I put it in place, doesn't let me, doesn't let me, ah, right, now, how do you back, can you go back, backspace, will that take you back, yes, backspace takes you back one, point at a time, that works exactly like Altium,

**Dave Jones:** that's brilliant, excellent, so you can, so if you just play some really complicated route, you don't have to ditch it all, and go back, you can just press backspace, and go back, that's excellent, excellent, excellent, now, it looks like, it's not telling me that that's going to be a DRC error,

**Dave Jones:** if I go over that, pad, if I go over this pad here, or try and connect to this pad, you watch, it won't, see, it didn't let me do it, it didn't let me create, that, route, because it knows that it's a DRC violation I'm assuming,

**Dave Jones:** so, if we go like this, but it will let me do, that, there we go, and, and presumably I can finish that, by going escape, can I? No, escape gets through the whole lot, I'm not happy with that, why can't, why can't that just end,

**Dave Jones:** like that, how do I end, routing, here's my hotkey list, for, the PCB editor, zoom in, zoom out, zoom auto, switch units, oh, switch units is control U, that's handy, reset local coordinates, space, undo, ah, okay, well, I'm not, may, don't tell me that it's only going to let you finish,

**Dave Jones:** the route, if you go to a valid, DRC, maybe you've got to turn, DRC off, so if we switch, um, where was that, tools, preferences, general, wow, now I'm really getting into it, um, DRC on, let's turn DRC off, okay, so we've, track only 45 degrees,

**Dave Jones:** yeah, excellent, track auto delete, enabled, so automatic track deletion when, recreating a track, okay, show, mod, rat nest, okay, let's try that, I switched off my DRC, okay, so, if I try, if I place, my trace like this, it's got a question mark there,

**Dave Jones:** don't know why it's got a question mark, now, okay, yeah, see, it let me go, it let me, place that trace over, the pad, before, whereas online DRC, it wouldn't let me do that, but it didn't tell me, that's the thing, it just wouldn't tell me,

**Dave Jones:** unless I missed something down the bottom of the display, or some, status indicator somewhere, but it didn't tell me that I was violating, that particular track, it just wouldn't let me place it, and I find that rather annoying, so, um, if I go into there,

**Dave Jones:** how do I end, the, I guess it's left, end track, oh, you've got to press the end key, there it is, alright, duh, okay, well, okay, so don't press escape, people, if you're routing, a trace like that, you've got to press the end key,

**Dave Jones:** too bad if your end key's not conveniently, uh, located, then you'll have to right click, and uh, select this menu, so, end track, and there we go, we can place it, and it goes like that, so, I don't know how long DSE works,

**Dave Jones:** but it, it didn't seem to give a status indicator, rather annoying, um, anyway, I've got to look into that stuff, but I've been going for an hour, folks, that's, uh, far too long for this, uh, episode, so I'm probably going to have to call it quits,

**Dave Jones:** and um, I will, very likely, uh, do more of this stuff, so that's my, first impression of the PCB editor, I'm not, that keen on the way it, uh, you manually have to, uh, export the netlist first, and then load the netlist into the PCB,

**Dave Jones:** and uh, it should just automatically, do that sort of stuff, um, and uh, I, I don't know how to say, edit the pad, haven't figured out, how to do something simple, like, edit, that particular pad, on that, particular component, maybe I've, you know,

**Dave Jones:** I'm not selecting, maybe I've got to select a certain layer, or something, before I do that, but, yeah, not too pleased, if you can't, I'm sure you can do it, surely, there's got to be a way to, got to be a way to do it,

**Dave Jones:** because how, I'm assuming also, that that hole size, is actual hole size, um, I'd be very disappointed, if that isn't actual size, but the only way to do that, is to go in there, and change it, and see if that hole size, changes,

**Dave Jones:** but, it doesn't let me, I'm only in the module, here, I'm uh, solder paste layers, I don't actually have like a pad, layer, or something silly like that, and uh, I don't know, edit, is there a way to edit pads, please, it must be,

**Dave Jones:** oh, anyway, could take me half an hour to find that, so, anyway, yeah, first impression, it um, it's a bit quirky, uh, but it's got some, it's got some nice features, it seems to be doing some things right, it really needs to work on it's naming,

**Dave Jones:** to get things consistent, with sort of what people call it in the industry, I think, um, I don't know, maybe it's different in France, or something like that, but, anyway, considering it's uh, free, and open source, it seems, reasonably uh, powerful, it's just a matter of,

**Dave Jones:** driving the thing, that's all, so, I'll catch you next time. . .
