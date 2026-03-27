---
title: "The joy of geekdom"
date: 2005-04-04 14:11:00 -0600
mood: amused
song: "Beki - Wake Up (EnergyRadio.FM - Energy Dance)"
original_url: https://restless-coder.livejournal.com/13164.html
---

I love being a geek, but sometimes it's sad when something amusing happens that no one else would understand. As a result, I'm going to pointlessly explain today's amusement in great detail, just to bore everyone.

Just now I was working on a perl program to import our TIFF format into our microscopy image database. I often Alt+Tab between shells rapidly, and sometimes lose track of which window is currently active. Having just Alt+Tabbed to what I thought was a command shell I no longer needed, I quickly typed `exit` but nothing happened. I was briefly confused until I realized that the active window was actually vim editing my perl program.

Now, by default vim is in command mode, not insert mode, meaning that the letter keys perform commands such as cursor movement and text manipulation, rather than simply being typed into the window. Typing random characters into vim in command mode is generally not a good idea, as it is liable to screw up whatever you were working on.

* The `e` key jumps to the end of the current word. So if the word is `blah` with the cursor hovering over the L, then pressing `e` will jump the cursor to hover over the H.
* The `x` key deletes the currently selected character.
* The `i` key switches to insert mode, causing subsequent characters to be inserted at the current cursor position (i.e., vim behaves like a "normal" text editor until Esc is pressed).
* The `t` key I am actually not very familiar with. But apparently when followed by another character, it jumps the cursor to just before the typed character. For example, If the word is `exposition` and the cursor is currently over the P, typing `tn` will cause the cursor to jump to the second O, since it immediately precedes the next N on the line.

A common construct in perl is the ubiquitous print statement. In perl it is very straightforward: the keyword `print` usually followed by a double quote mark, some text, often a newline (`\n`), a closing double quote mark, and a semicolon.

When I typed `exit` into the vim window accidently, I was confused even after realizing the active window was the vim window, because it did not look like typed character sequence had affected my buffer at all. _Why isn't my buffer screwed up?_ I wondered. Vim was in insert mode, so something must have gotten hosed. Just to be sure, I hit Esc to quit insert mode, then hit `u` several times to undo the last few actions. It was then I realized what had happened. And congratulations! You now also know enough about this arcane buffoonery to understand.

Today, my cursor hovered over the P in `print`. When I hit `e` the cursor jumped to the T. When I hit `x` the T was deleted. When I hit `i` vim switched to insert mode. Finally, when I hit `t` it inserted a T after the `prin` resulting in `print` once again. So for once typing some inappropriate word into vim did not result in Apocalypse. And this phenomenon amused me enough for me to bother typing up this entire explanation.

* * *

2 + 2 never equals 5, even for large values of 2.
