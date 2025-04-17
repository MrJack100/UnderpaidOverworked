# UnderpaidOverworked

UnderpaidOverworked is the name of a project given to me by an anonymous client.
It is called that because the client does not want to pay for the project. I am continuing to work on it for them because it sounds interesting.

## Table of Contents

* [Table of Contents](#table-of-contents)
* [Task List](#task-list)
* [Specifications by Client](#specifications-by-client)
  * [Battle Features](#battle-features)
  * [Figure 1](#figure-1)
  * [Figure 2](#figure-2)
  * [Figure 3](#figure-3)
  * [World Map](#world-map)
  * [Addendum](#addendum)

## Task List

1. Create map with grid locations, user will be able to select a location on a map, and are able to change data about the location, including naming the location itself. Each location will store any amount of groups, each group is a JSON object that will contain **what items there are, what amount of them there are, and what side the group is on**. The user should also be able to move groups from locations to other locations. The user should be able to merge groups with each and create groups as per the aforementioned format.
2. The user should be able to select groups on the map and list them as engaged in a battle.
3. The user should be able to initiate a battle state with the selected groups, with the requirement of **at least two opposing sides must be selected**.
4. A Battle GUI should display all involved groups, and will request prompts of what is to happen to different groups on each side. A statistics tab should be visible with the statistics able to be edited. The battle should be able to be terminated, with a winner(s) and loser(s) decided by the user. The battle should be saved with a name in a log book of all past battles.
5. All data saved by the server should be accessible to the user and editable.

> This might be in future but I'm not entirely sure, so as to ensure the user does not make a massive mistake and delete everything, should there be a versioning history?

## Specifications by Client

### Battle Features

* Part of screen should say numbers for each side (*See Figure 1*)
* ⁠Knight Side has specific items (*See Figure 2*)
* ⁠Gnome Side has specific items (*See Figure 3*)
* ⁠Hidden menu that asks user to pick which sides are involved, and how many soldiers are involved on each side in a battle.
* ⁠User can then create groups of items for each side, example in instruction sheet.
* ⁠Each group of items may have one than one type of item, the user chooses how much of each item goes into each group.
* ⁠Groups should be able to be merged with a simple process.
* ⁠Groups can be summoned in from different areas of the world map.
* ⁠Groups are able to be created during the battle.
* ⁠It should be easy for the user to add new items to different sides.
* ⁠All items selected will appear next to each other on a battle screen.
* ⁠A statistics tab should be visible.
* ⁠Statistics should be editable by user.
* ⁠User should be able to terminate battle.
* ⁠User should be able to save result of battle and information about it with a name.

### Figure 1

* Knights
* Gnomes
* Animorts

### Figure 2

* Trebuchets
* ⁠Knights

### Figure 3

* Gnomes
* ⁠Dwarves
* ⁠Elves
* ⁠Gonks
* ⁠Fairies
* ⁠Wizards
* ⁠Halflings

### World Map

* Show statistics of how items are distributed across a map.
* ⁠Items locations are editable by the user.
* ⁠Item locations information such as names are editable by the user.

### Addendum

* Must be able to recruit soldiers.
* ⁠Must be able to overwrite all information if necessary.
