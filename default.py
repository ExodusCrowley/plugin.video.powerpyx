# -*- coding: utf-8 -*-
#------------------------------------------------------------
# PowerPyx Playlist Loader
# (c) 2018 - ExodusCrowley
# version 1.0.0
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.powerpyx'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
		("[B][COLOR yellow]SHOW ALL VIDEOS[/COLOR][/B]", "playlist/UUWBA1-H9A5IldSb3tNwQmtQ", ''),
		("[B]The Division 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFpft0gxhaUiKQLGnR58pUM", ''),
		("[B]Devil May Cry 5 Trophy Guide[/B]", "playlist/PLRr5L69yg_kGjhEBAp12HPAvgQ3ZPesAU", ''),
		("[B]Kingdom Hearts 3 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFsG4lA98HFxCj9ALXhb69_", ''),
		("[B]Anthem Collectible Guide[/B]", "playlist/PLRr5L69yg_kGbU2ED2DBIKURWwevbRX-c", ''),
		("[B]Far Cry New Dawn Trophy Guide[/B]", "playlist/PLRr5L69yg_kHCR54wfCXcCqBWd78E_hY0", ''),
		("[B]Kingdom Hearts 3 Collectible Guide[/B]", "playlist/PLRr5L69yg_kHDMnhoVSiIlMziBOFrMHDp", ''),
		("[B]Resident Evil 2 Remake Trophy Guide[/B]", "playlist/PLRr5L69yg_kFgPaCxDQanDMU5cwRfzmCw", ''),
		("[B]Just Cause 4 Trophy Guide[/B]", "playlist/PLRr5L69yg_kF9Fnfqan2wl-2ZxCwipiWC", ''),
		("[B]Red Dead Redemption 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEuUIiI4ATYjzsBNsEOqENb", ''),
		("[B]Spyro 3 Year of the Dragon (Remaster) Trophy Guide[/B]", "playlist/PLRr5L69yg_kEKhLho5cvcyFsizBeE6Q3d", ''),
		("[B]Spyro The Dragon (Remaster) Trophy Guide[/B]", "playlist/PLRr5L69yg_kE07F8VIcTsy3Ni2dmqF-Pk", ''),
		("[B]Spyro 2 Ripto's Rage (Remaster) Trophy Guide[/B]", "playlist/PLRr5L69yg_kGF-_BBtBJP4BIssWqfuGnk", ''),
		("[B]Call of Duty Black Ops 4 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEX0MAiQJsm8cs4HFWhSsnE", ''),
		("[B]Assassin's Creed Odyssey Trophy Guide[/B]", "playlist/PLRr5L69yg_kHmRUYFWfyzvP_Cs5JvbpXd", ''),
		("[B]Shadow of the Tomb Raider Trophy Guide[/B]", "playlist/PLRr5L69yg_kEQBTyx-Ea30EZ9k-lNgR6J", ''),
		("[B]Shadow of the Tomb Raider Challenge Guide[/B]", "playlist/PLRr5L69yg_kF-xDUFc4TCptqhRL7KnnhW", ''),
		("[B]Guacamelee! 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEbDZp7jjHGr5OCiEaFYhpH", ''),
		("[B]Marvel's Spider-Man All Boss Fights[/B]", "playlist/PLRr5L69yg_kEryvwePpbDNSMpmZn3HQvv", ''),
		("[B]Marvel's Spider-Man (2018) Trophy Guide[/B]", "playlist/PLRr5L69yg_kHmG-WKhDwVdOmj28NN5YiH", ''),
		("[B]The Walking Dead: The Final Season[/B]", "playlist/PLRr5L69yg_kEq8r2i-YuV-PL5gWc0Pq4l", ''),
		("[B]Far Cry 5 Trophy Guide[/B]", "playlist/PLRr5L69yg_kGZ0iCDxgCk2tRpvvwwLLok", ''),
		("[B]The Crew 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEwBI33zd8N9UBbbEGKd340", ''),
		("[B]Vampyr Trophy Guide[/B]", "playlist/PLRr5L69yg_kHrDD3vnutfcug6-vluT6JO", ''),
		("[B]Fortnite Battle Royale Weekly Challenges[/B]", "playlist/PLRr5L69yg_kFp7KpAhGbp4oN3WWMzokzv", ''),
		("[B]Detroit: Become Human Trophy Guide[/B]", "playlist/PLRr5L69yg_kEH3bXPG1l1Kl6wHXJQCD--", ''),
		("[B]God of War (2018) Trophy Guide[/B]", "playlist/PLRr5L69yg_kGofgclQfoIGeS360_IhIcu", ''),
		("[B]God of War 2018 Collectible Guide[/B]", "playlist/PLRr5L69yg_kHy9ZiXfVOG3HLffEwWvJNg", ''),
		("[B]Far Cry 5 Trophy Guide[/B]", "playlist/PLRr5L69yg_kGZ0iCDxgCk2tRpvvwwLLok", ''),
        ("[B]Ni No Kuni 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEcqeBU1wFlWK8lgCE0BaQX", ''),
        ("[B]Kingdom Come Deliverance Trophy Guide[/B]", "playlist/PLRr5L69yg_kEvHcUpBeV_Iaq9MaZ53u3W", ''),
        ("[B]Shadow of the Colossus (PS4 Remake) Trophy Guide[/B]", "playlist/PLRr5L69yg_kE9jaxnHgDfaOIZGDYN29AU", ''),
		("[B]Shadow of the Colossus (PS4) - Hard Time Attack[/B]", "playlist/PLRr5L69yg_kG66NRlVDwJJC8SLLE8eIQS", ''),
		("[B]Monster Hunter World Trophy Guide [/B]", "playlist/PLRr5L69yg_kGEeXTYgk37DHvhos5i60VK", ''),
		("[B]Dragon Ball FighterZ[/B]", "playlist/PLRr5L69yg_kH-8SYlj0diLQuib7NWYb90", ''),
		("[B]The Inpatient[/B]", "playlist/PLRr5L69yg_kG4qBBIFCWbhI1hgtx1gXBI", ''),
		("[B]Life is Strange: Before the Storm Collectible Guide[/B]", "playlist/PLRr5L69yg_kEATawuhqlzC4tKa6SaKhxp", ''),
		("[B]Destiny 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHULOMlPJ7OtAo47QuI8X_o", ''),
		("[B]Wolfenstein 2 The New Colossus Trophy Guide[/B]", "playlist/PLRr5L69yg_kFuhI_Ntseyf4Ykfr-203Fk", ''),
		("[B]Call of Duty WW2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kH6jOTvLxwmTQuGyJ_MR_2a", ''),
		("[B]Wolfenstein 2 The New Colossus Collectible Guide[/B]", "playlist/PLRr5L69yg_kFCB-irnGYt95miudZbBxhV", ''),
		("[B]Dishonored: Death of the Outsider Trophy Guide[/B]", "playlist/PLRr5L69yg_kGCEAvEYY29WLtDj9I-5YVa", ''),
		("[B]Star Wars Battlefront 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHhYNgv1qysWjYmUaUPWS6w", ''),
		("[B]Need for Speed Payback Trophy Guide[/B]", "playlist/PLRr5L69yg_kHlXKu-eu4LSfvXGUj7QlAf", ''),
		("[B]Need for Speed Payback - Derelict Car Part Locations[/B]", "playlist/PLRr5L69yg_kHuuFpIU7bOP8pNvat6fkhW", ''),
		("[B]Assassin's Creed Origins Trophy Guide[/B]", "playlist/PLRr5L69yg_kH1ziR8BrZpmzllNW-ETQNS", ''),
		("[B]Assassin's Creed Origins All Tomb Locations[/B]", "playlist/PLRr5L69yg_kGOfdkk9ziP8jvlc3yoG9pm", ''),
		("[B]Middle Earth Shadow of War Trophy Guide[/B]", "playlist/PLRr5L69yg_kHTt8U7xi9BtvO3UJmaVgCr", ''),
		("[B]South Park The Fractured But Whole Trophy Guide[/B]", "playlist/PLRr5L69yg_kGpB4FMvEIbdSDMqgoko2dG", ''),
		("[B]The Evil Within 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFchnPEWCSJdUpjiz7ldu1i", ''),
		("[B]The Evil Within 2 Collectible Guide [/B]", "playlist/PLRr5L69yg_kFeZvr3U_MIHP8cbShAU0wV", ''),
		("[B]Project Cars 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEE3jlxfjVHDc1P1AEvvLdq", ''),
		("[B]Marvel vs. Capcom Infinite[/B]", "playlist/PLRr5L69yg_kGc1v4ZKQYDR4iJGBNaFq7V", ''),
		("[B]Knack 2 Trophy Guide [/B]", "playlist/PLRr5L69yg_kFH4uWaDU_2BgqJeeelxpxx", ''),
		("[B]Uncharted The Lost Legacy Collectible Guide[/B]", "playlist/PLRr5L69yg_kGkTHAXEI6eGLHInGqNfuhe", ''),
		("[B]Uncharted The Lost Legacy Trophy Guide[/B]", "playlist/PLRr5L69yg_kEGMX-9c1z-9o7fHJKJsPdG", ''),
		("[B]Hellblade: Senua's Sacrifice Trophy Guide [/B]", "playlist/PLRr5L69yg_kH4Yk_lIZb_WPUp1C3mF4F_", ''),
		("[B]Nioh Collectible Guide[/B]", "playlist/PLRr5L69yg_kGbgqC4M9H-SN8DSl76QP_v", ''),
		("[B]Niho Trophy Guide[/B]", "playlist/PLRr5L69yg_kGn4WoNQZCTFoaHvfToJ1Vm", ''),
		("[B]Crash Bandicoot N. Sane Trilogy Trophy Guide [/B]", "playlist/PLRr5L69yg_kFNiKeAH2p85rdaYeyVCsbg", ''),
		("[B]Tekken 7 Trophy Guide[/B]", "playlist/PLRr5L69yg_kEg69GLSaPFWBnovUd5D6og", ''),
		("[B]Injustice 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHc7ed2X0oruu5_buf6XmOV", ''),
		("[B]Prey Trophy Guide[/B]", "playlist/PLRr5L69yg_kHBtitPq05aOSq7xezM9ILL", ''),
		("[B]Sniper Ghost Warrior 3 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHPDreEYrIK9n_hPFw0IF88", ''),
		("[B]Outlast 2 Collectible Guide (Documents & Recordings)[/B]", "playlist/PLRr5L69yg_kHqllR-h8u8mi8e_RXgWV0m", ''),
		("[B]Outlast 2 Trophy Guide[/B]", "playlistPLRr5L69yg_kGta90CDcXIehQkVTVzrHuA", ''),
		("[B]Mass Effect Andromeda Trophy Guide[/B]", "playlist/PLRr5L69yg_kHcJeQLXuDJ6qcniI3YPrPH", ''),
		("[B]Ghost Recon Wildlands Trophy Guide[/B]", "playlist/PLRr5L69yg_kG5FiJbHp7pCDTunt5dpao2", ''),
		("[B]Sniper Elite 4 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFE2GwGbleAbUeZaXAn6Wj6", ''),
		("[B]Horizon Zero Dawn Trophy Guide[/B]", "playlist/PLRr5L69yg_kFL7UwxM6LEiwqbhql2gYFd", ''),
		("[B]Sniper Elite 4 Collectibles Guide[/B]", "playlist/PLRr5L69yg_kFn5_y79HSGHmgp2aLvI3vD", ''),
		("[B]For Honor Collectible Guide[/B]", "playlist/PLRr5L69yg_kE5uGNGPvSC2nIa3CCMruj9", ''),
		("[B]Nioh - All Boss Fights / All Bosses[/B]", "playlist/PLRr5L69yg_kEVw4BuxPiHDXckr-yJdalK", ''),
		("[B]Resident Evil 7 Trophy Guide[/B]", "playlist/PLRr5L69yg_kGB31_w1My6PjHDgnUspFr8", ''),
		("[B]The Last Guardian Trophy Guide[/B]", "playlist/PLRr5L69yg_kGRXuY85Do4hYn94esRhAer", ''),
		("[B]Final Fantasy XV Trophy Guide[/B]", "playlist/PLRr5L69yg_kHUePpPKinhJlnfEfoSe6Qn", ''),
		("[B]Dishonored 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFw3rxaYf2HCKvO0ntsE7wd", ''),
		("[B]Watch Dogs 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kGhfRmHHyrfGBS2GXZnpnx-", ''),
		("[B]Call of Duty Infinite Warfare Trophy Guide[/B]", "playlist/PLRr5L69yg_kEOxPd8BsJmnpojoPhg-19f", ''),
		("[B]Titanfall 2 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHPA6CcAz_IHRp9iWDr9gTN", ''),
		("[B]Hitman Trophy Guide[/B]", "playlist/PLRr5L69yg_kFiOE50VgEhcvEE75K01WP1", ''),
		("[B]Dragon Ball Xenoverse 2[/B]", "playlist/PLRr5L69yg_kFI9haM5X6rZJ316ZZAq29G", ''),
		("[B]Battlefield 1 Codex Entries Guide[/B]", "playlist/PLRr5L69yg_kEQhnAggMBqW-HVlaNjZv0G", ''),
		("[B]Battlefield 1 Field Manual Locations[/B]", "playlist/PLRr5L69yg_kFZpbXItq6w0xO55A1uVJvy", ''),
		("[B]Battlefield 1 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHPfQqXVc7r0BnY_uAU2vp6", ''),
		("[B]Uncharted 4 Collectible Guide[/B]", "playlist/PLRr5L69yg_kFtYzcpWTSRxGL8SeFeNZ-7", ''),
		("[B]Rise of the Tomb Raider Trophy Guide[/B]", "playlist/PLRr5L69yg_kE59ZzBavNQj5sPminDPnAr", ''),
		("[B]Rise of the Tomb Raider Challenge Guide[/B]", "playlist/PLRr5L69yg_kEO-H2iKRF03gTlsrimwNNI", ''),
		("[B]Mafia 3 Trophy Guide[/B]", "playlist/PLRr5L69yg_kF4q3vxBlYfJBcnhAuuHZ4H", ''),
		("[B]Call of Duty 4: Modern Warfare Remastered Trophy Guide[/B]", "playlist/PLRr5L69yg_kFTWa1RYUZ3bJm0hvbvnWTR", ''),
		("[B]Call of Duty Black Ops 3 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFWCcTmM352XDUrX2NtAegs", ''),
		("[B]Deus Ex Mankind Divided Trophy Guide[/B]", "playlist/PLRr5L69yg_kErz7qs_U7tkFMy9klcAs6P", ''),
		("[B]No Man's Sky[/B]", "playlist/PLRr5L69yg_kHpuLVScTM-f9-jJz9aSkBA", ''),
		("[B]Mirror's Edge Catalyst Trophy Guide[/B]", "playlist/PLRr5L69yg_kFUFNAY5CXTbuvDCcRsR3fo", ''),
		("[B]The Witcher 3 Wild Hunt[/B]", "playlist/PLRr5L69yg_kEAq8abdqXtOMzDgE49hMdm", ''),
		("[B]The Witcher 3 Wild Hunt - Witcher Gear Sets[/B]", "playlist/PLRr5L69yg_kEUBjBAjVSZZKKD2kARYfgH", ''),
		("[B]Fallout 4 Trophy / Achievement Guide[/B]", "playlist/PLRr5L69yg_kGxOJwZKqITqqv4VqVZv-VI", ''),
		("[B]Doom 2016 Trophy Guide[/B]", "playlist/PLRr5L69yg_kHcpSB8lvDm10QZbHkCngTK", ''),
		("[B]Doom 2016 Collectible Guide[/B]", "playlist/PLRr5L69yg_kGnSJw_fwjGHHx-Bo0OOjb8", ''),
		("[B]Uncharted 4 Trophy Guide[/B]", "playlist/PLRr5L69yg_kF7Hz1J_2MoiS1SvuKt_ZTG", ''),
		("[B]One Piece Burning Blood[/B]", "playlist/PLRr5L69yg_kGdZpQl83nycTOSOeIikL6N", ''),
		("[B]Dark Souls 3 Trophy Guide[/B]", "playlist/PLRr5L69yg_kFoVHrYn8gemJvOwNQhXK-M", ''),
		("[B]Ratchet and Clank Trophy Guide[/B]", "playlist/PLRr5L69yg_kHaUjmgP-46_QNyPpXy9vro", ''),
		("[B]Dark Souls 3 - All Boss Fights[/B]", "playlist/PLRr5L69yg_kGO7ZQYK0xInqtRFnYepPf7", ''),
		("[B]Tom Clancy's The Division[/B]", "playlist/PLRr5L69yg_kG3R2-kfKt6850CfBNO5_W2", ''),
		("[B]Far Cry Primal Trophy Guide[/B]", "playlist/PLRr5L69yg_kGTc2UDWsqmJQV_JFQqdAUL", ''),
		("[B]Street Fighter V[/B]", "playlist/PLRr5L69yg_kH2bum1fehdRChSP4G_arQs", ''),
		("[B]Naruto Shippuden Ultimate Ninja Storm 4[/B]", "playlist/PLRr5L69yg_kGekuD2kqsTDLoCryECXnyD", ''),
		("[B]Assassin's Creed Chronicles: India Trophy Guide[/B]", "playlist/PLRr5L69yg_kGyOUq6AH2IAaP9yztQ90iT", ''),
		("[B]Just Cause 3 - Challenge Guide (5 Gears in All[/B]", "playlist/PLRr5L69yg_kGiebTLDUFPw_d5LJWP6HdI", ''),
		("[B]Just Cause 3 Trophy / Achievement Guid[/B]", "playlist/PLRr5L69yg_kHtYDJrCAuGD_86xNlDa9P-", ''),
		("[B]Star Wars Battlefront Trophy / Achievement Guide[/B]", "playlist/PLRr5L69yg_kGmNCifJVjQuc00z8sHRzQX", ''),
		("[B]Assassin's Creed Syndicate[/B]", "playlist/PLRr5L69yg_kF8kuEsMZHh9CqlafA_DBsO", ''),
		("[B]Uncharted 1 Treasure Guide[/B]", "playlist/PLRr5L69yg_kFcmEES9wilIqEAgjPUUCV_", ''),
		("[B]Metal Gear Solid V: The Phantom Pain Trophy Guide[/B]", "playlist/PLRr5L69yg_kHEOYiCF5kNDgDtp2a-NKNI", ''),
		("[B]Metal Gear Solid V: The Phantom Pain S-Rank[/B]", "playlist/PLRr5L69yg_kGiYcnu_StjmzsH7Mnd0fmv", ''),
		("[B]Until Dawn Collectible Guide[/B]", "playlist/PLRr5L69yg_kHeF49tYb5qTgKDFVU1SBJ0", ''),
		("[B]Batman Arkham Knight: A Matter of Family DLC[/B]", "playlist/PLRr5L69yg_kG-RVQ9sI4jz-Nfp6WwjtB8", ''),
		("[B]Batman Arkham Knight[/B]", "playlist/PLRr5L69yg_kGfuNnIzMYUXCnxaQL1dOI0", ''),
		("[B]Batman Arkham Knight - All Riddler Collectibles[/B]", "playlist/PLRr5L69yg_kGj9roh6fYVG49GbPKMYb20", ''),
		("[B]Batman Arkham Knight - Riddler Trials[/B]", "playlist/PLRr5L69yg_kFjo3sf4P4eiPV38crNoFi9", ''),
		("[B]Wolfenstein The Old Blood[/B]", "playlist/PLRr5L69yg_kFY1HRXlMFsLRJkm0cWjVNO", ''),
		("[B]Wolfenstein The Old Blood Collectible Guide[/B]", "playlist/PLRr5L69yg_kEDDeVD48SYZtliqMg3fXUo", ''),
		("[B]Mortal Kombat X[/B]", "playlist/PLRr5L69yg_kF8Q6yLrdAuAaD_v-86-kDX", ''),
		("[B]Assassin's Creed Chronicles: China[/B]", "playlist/PLRr5L69yg_kEqyb7JzcbNLkOGL9SWqzz0", ''),
		("[B]Bloodborne[/B]", "playlist/PLRr5L69yg_kFDMwd2f8lLLEwBYcWoEv_F", ''),
		("[B]Bloodborn - All Boss Fights[/B]", "playlist/PLRr5L69yg_kGtlKrCgFBTR3GFQmEVzsk", ''),
		("[B]Battlefield Hardline[/B]", "playlist/PLRr5L69yg_kGX2EaTSzGAofjnyIt8BvZs", ''),
		("[B]Battlefield Hardline Collectible Guide[/B]", "playlist/PLRr5L69yg_kEtOLI6jKkDPu-2emhHttCA", ''),
		("[B]Hotline Miami 2: Wrong Number[/B]", "playlist/PLRr5L69yg_kH-HhwMqFFKTYxq_RLKiZMQ", ''),
		("[B]Resident Evil Revelations 2[/B]", "playlist/PLRr5L69yg_kGQ-Tygleolhd_2pU1jtNX-", ''),
		("[B]The Order: 1886 Collectibles Guide[/B]", "playlist/PLRr5L69yg_kHbgw4TeO3bfFcQZMFUy1pl", ''),
		("[B]Evolve[/B]", "playlist/PLRr5L69yg_kErgK6LolVsELMf6QreeQmq", ''),
		("[B]Dying Light[/B]", "playlist/PLRr5L69yg_kEy3rPZEfcXuyNyRVMgsNgL", ''),
		("[B]Dying Light Text Collectibles[/B]", "playlist/PLRr5L69yg_kFULIdowRu20cODEnahTr39", ''),
		("[B]Assassin's Creed Unity: Dead Kings DLC[/B]", "playlist/PLRr5L69yg_kEoPY50fWOLDLu8XUy6jbwC", ''),
		("[B]Assassin's Creed Unity Sync Point Collectibles[/B]", "playlist/PLRr5L69yg_kGaijYUtKGUqiiadUGu7_Tx", ''),
		("[B]The Crew[/B]", "playlist/PLRr5L69yg_kGvPlyXXu1D05MHeEpdgX1S", ''),
		("[B]Far Cry 4[/B]", "playlist/PLRr5L69yg_kFEx6aewdK5pwENGf46vJQH", ''),
		("[B]Assassin's Creed Unity Nostradamus Enigmas[/B]", "playlist/PLRr5L69yg_kEuu8fivKehj2x1wHnKOws3", ''),
		("[B]Assassin's Creed Unity[/B]", "playlist/PLRr5L69yg_kGW9ALONS9HBiNzdhYyN-Lb", ''),
		("[B]Call of Duty Advanced Warfare[/B]", "playlist/PLRr5L69yg_kE0Ae7saM94K1dmKBJLJJBR", ''),
		("[B]The Evil Within Collectible Guide[/B]", "playlist/PLRr5L69yg_kGPUfgpnXUMBtWC0Yne9aPW", ''),
		("[B]The Evil Within[/B]", "playlist/PLRr5L69yg_kFZS9kfjeDMp3uJQpZigBOR", ''),
		("[B]Alien Isolation[/B]", "playlist/PLRr5L69yg_kGo8OuksetxRzk2uqEeBHso", ''),
		("[B]Middle Eart: Shadow of Mordor[/B]", "playlist/PLRr5L69yg_kEdVYoJIa7lSo9OScmL_8ZJ", ''),
		("[B]Destiny[/B]", "playlist/PLRr5L69yg_kGFW4B5BHifEe5EJCX8RMtD", ''),
		("[B]Velocity 2X Perfect Medal Walkthrough[/B]", "playlist/PLRr5L69yg_kGdnrltDFy7Lq9cNbVoti7t", ''),
		("[B]Velocity 2X[/B]", "playlist/PLRr5L69yg_kFAm-z2doIoVCq4ZkNAHrJJ", ''),
		("[B]Metro Last Light Redux[/B]", "playlist/PLRr5L69yg_kEe21MyfsczMKaTI4xaWZR9", ''),
		("[B]Metro 2033 Redux[/B]", "playlist/PLRr5L69yg_kHBVm0BblXTJsflAKVV4F5E", ''),
		("[B]Transformers: Rise of the Dark Spark[/B]", "playlist/PLRr5L69yg_kEBZ6UsDzd65v-QLfj6ZFnm", ''),
		("[B]Transformers: Rise of the Dark Spark Collectible Guide[/B]", "playlist/PLRr5L69yg_kGp0xVITy7LWGsy-dW5jQHa", ''),
		("[B]Metal Gear Solid  V: Ground Zeroes[/B]", "playlist/PLRr5L69yg_kFbKVhWPfXBO4W6sSBtxShY", ''),
		("[B]Sniper Elite 3[/B]", "playlist/PLRr5L69yg_kHJOycl0O7AjUQu3_kaB0iT", ''),
		("[B]Wolfenstein: The New Order Collectible Guide[/B]", "playlist/PLRr5L69yg_kGYlFq73YrFegHFoa31gjOY", ''),
		("[B]Contrast Collectible Guide[/B]", "playlist/PLRr5L69yg_kGGXL1TxvuJ9n94_hn_AVxK", ''),
		("[B]Sniper Elite 3 Collectible Guide[/B]", "playlist/PLRr5L69yg_kH1_yd8gW9IZrZL5ITyR6oB", ''),
		("[B]Thief[/B]", "playlist/PLRr5L69yg_kEMFZe3DNDto_0ckfKqutJJ", ''),
		("[B]Watch Dogs[/B]", "playlist/PLRr5L69yg_kGnaCSRsuMjYVvj-AYoZQrH", ''),
		("[B]Metal Gear Solid V: Ground Zeroes S-Rank Walkthrough[/B]", "playlist/PLRr5L69yg_kErKnE6884v8o722Abj096u", ''),
		("[B]Assasin´s Creed Liberation HD Collectible Guide[/B]", "playlist/PLRr5L69yg_kHn0nP3dCRcmap77s5H5In4", ''),
		("[B]Outlast Collectibles[/B]", "playlist/PLRr5L69yg_kHtsDyr2S-SJZKyXbh76sIT", ''),
		("[B]Thief Collectible Guide[/B]", "playlist/PLRr5L69yg_kF5k7gkvLJoJ_BzrvmQQ3Cn", ''),
		("[B]Killzone Shadow Fall Collectible Guide (Audio Logs,[/B]", "playlist/PLRr5L69yg_kG7x55CgNkmpH1V8AqYMkuZ", ''),
		("[B]Lightning Returns: Final Fantasy XIII[/B]", "playlist/PLRr5L69yg_kE1LeBGjqbzIxnlvyJa9i4p", ''),
		("[B]The Last of Us: Left Behind (DLC)[/B]", "playlist/PLRr5L69yg_kEqNJnZPp9OGNVP5XDMBXMj", ''),
		("[B]Assassin's Creed Liberation HD[/B]", "playlist/PLRr5L69yg_kGkpz9ufziwtSECYecNZiZM", ''),
		("[B]inFAMOUS Second Son[/B]", "playlist/PLRr5L69yg_kFxDbi4Uz6z7gldqv1ULZ8b", ''),
		("[B]Killzone Shadow Fall Trophy Guide[/B]", "playlist/PLRr5L69yg_kE5oZPNhYyPLv0C5WjnAKnu", ''),
		("[B]Contrast Trophy Guide[/B]", "playlist/PLRr5L69yg_kGFkYv5djdpan_MMijQ3vS3", ''),
		("[B]Knack Trophy Guide[/B]", "playlist/PLRr5L69yg_kEkrngxiY_WyCB3C4858OdO", ''),
		("[B]Outlast[/B]", "playlist/PLRr5L69yg_kHVG0UkJSVvjf6gasJVIdjG", ''),
		("[B]The Amazing Spider-Man 2[/B]", "playlist/PLRr5L69yg_kFKo3n7U1qyhkewjrM1CuUj", ''),
		("[B]Battlefield 4 Collectible Guide (Dog Tags & Weapons)[/B]", "playlist/PLRr5L69yg_kE2NGX9nnKDP4EyHgd-Cmty", ''),
		("[B]GTA V[/B]", "playlist/PLRr5L69yg_kGX8eTg3pNUNAQJO1hXzU2J", ''),
		("[B]GTA V Collectibles[/B]", "playlist/PLRr5L69yg_kGp1chdRXXJaO7WXEj6YSGd", ''),
		("[B]Metro Last Light[/B]", "playlist/PLRr5L69yg_kFajjYgWa7MHjoJOmRfSdjr", ''),
		("[B]The Last Of Us[/B]", "playlist/PLRr5L69yg_kHTZZMjjByXVc4axR-0sYJc", ''),
		("[B]The Last of Us Collectible Locations[/B]", "playlist/PLRr5L69yg_kEqs3xqlvjkjaxbPC_M3800", ''),
		("[B]Bioshock Infinite - All Collectible Locations[/B]", "playlist/PLRr5L69yg_kFJ4a4EOTQg1ueNKc3jaaAW", ''),
		("[B]Killzone Mercenary[/B]", "playlist/PLRr5L69yg_kGqRqs5U3E2PgTFJk-48EYE", ''),
		("[B]Killzone Mercenary Intel Locations[/B]", "playlist/PLRr5L69yg_kGq2uzZDW2a9EhjKYRaLpeJ", ''),
		("[B]Assasin´s Creed 4[/B]", "playlist/PLRr5L69yg_kEpj30o4EHlHwg5cIdLyNk0", ''),
		("[B]God of War Ascension[/B]", "playlist/PLRr5L69yg_kFG3o7cUfQv3Ne3vrcQQzf6", ''),
		("[B]Call of Duty Ghosts[/B]", "playlist/PLRr5L69yg_kG_AzCoXm-hKLv6wCy5qAVy", ''),
		("[B]Killzone Shadow Fall Collectible Guide (Audio Logs,[/B]", "playlist/PLRr5L69yg_kG7x55CgNkmpH1V8AqYMkuZ", ''),
		("[B]Dead Island Riptide[/B]", "playlist/PLRr5L69yg_kEPc8oGI-DcKnz6XtcLiYsi", ''),
		("[B]Far Cry 3: Blood Dragon[/B]", "playlist/PLRr5L69yg_kHnsjsK5EdK4OnuBLrQeaZ4", ''),
		("[B]Payday 2[/B]", "playlist/PLRr5L69yg_kHMet7bvcG0Gl0kcOdC3buS", ''),
		("[B]Remember Me Collectible Guide[/B]", "playlist/PLRr5L69yg_kG91a8IwSjjGJM-lHiZvWrl", ''),
		("[B]Bioshock Infinite[/B]", "playlist/PLRr5L69yg_kFRwt7t2lR__UC39aaBShHR", ''),
		
		
]



# Entry point
def run():
    plugintools.log("youtubeAddon.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("youtubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()