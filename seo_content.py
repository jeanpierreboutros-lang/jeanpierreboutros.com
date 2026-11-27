"""Search copy based on the existing, confirmed portfolio; no new credits."""

PRODUCTS = [
    ("zynforge-live", "zynforge-live.png", "Zynforge Live", "Live performance",
     "A plugin host for taking audio processing onto the stage."),
    ("zynforge-recording", "zynforge-recording.png", "Zynforge Recording", "Recording & playback",
     "Multitrack recording and playback for live performance."),
    ("zynforge-stage", "zynforge-stage.png", "Zynforge Stage", "Production planning",
     "Stage plots and technical riders for planning a production."),
]

# Short, individually written search snippets. Full production names remain in
# the visible headings and records; character counts are editorial guardrails.
PROJECT_METADATA = {
    "nancy-ajram-qatar-fashion-2022": ("Nancy Ajram Qatar Fashion United | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at Qatar Fashion United, Doha, on 16 December 2022."),
    "nancy-ajram-ayla-aqaba-2022": ("Nancy Ajram Ayla Music Festival | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at Ayla Music Festival in Aqaba, Jordan, on 18 June 2022."),
    "nancy-ajram-red-sea-2022": ("Nancy Ajram Red Sea Film Festival 2022 | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at Red Sea Film Festival in Jeddah, Saudi Arabia on 8 December 2022."),
    "nancy-ajram-kuwait-february-2023": ("Nancy Ajram February Kuwait Festival 2023 | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at February Kuwait Festival in Kuwait on 10 February 2023."),
    "nancy-ajram-riyadh-february-2024": ("Nancy Ajram Riyadh Season 2024 | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at Riyadh Season in Riyadh, Saudi Arabia on 2 February 2024."),
    "nancy-ajram-riyadh-august-2024": ("Nancy Ajram Kingdom Tour 2024 | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at Kingdom Tour in Riyadh, Saudi Arabia on 16 August 2024."),

    "nancy-ajram-soundstorm-2021": ("Nancy Ajram at Soundstorm Riyadh | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at MDLBEAST Soundstorm in Riyadh on 19 December 2021."),
    "nancy-ajram-alamein-2023": ("Nancy Ajram New Alamein Festival | FOH and Monitor", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at New Alamein Festival in New Alamein, Egypt on 28 July 2023."),
    "nancy-ajram-casino-liban-2023": ("Nancy Ajram Casino du Liban | FOH and Monitor", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at Casino du Liban in Jounieh, Lebanon on 3 August 2023."),
    "nancy-ajram-alula-2024": ("Nancy Ajram AlUla Moments | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at AlUla Moments in AlUla, Saudi Arabia on 11 January 2024."),
    "nancy-ajram-byblos-2024": ("Nancy Ajram Byblos International Festival | Monitor Engineer", "Jean-Pierre Boutros was monitor engineer for Nancy Ajram at Byblos International Festival in Byblos, Lebanon on 26 July 2024."),

    "nancy-ajram-houston-2023": ("Nancy Ajram Houston | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at 713 Music Hall in Houston on 10 March 2023."),
    "nancy-ajram-montreal-2023": ("Nancy Ajram Montréal | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at Salle Wilfrid-Pelletier, Place des Arts in Montréal on 12 March 2023."),
    "nancy-ajram-las-vegas-2023": ("Nancy Ajram Las Vegas | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at Encore Theater at Wynn Las Vegas in Las Vegas on 18 March 2023."),
    "nancy-ajram-temecula-2023": ("Nancy Ajram Temecula | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at Pechanga Theater in Temecula on 19 March 2023."),
    "nancy-ajram-mississauga-2024": ("Nancy Ajram Mississauga | FOH and Monitor Engineer", "Jean-Pierre Boutros was FOH and monitor engineer for Nancy Ajram at Paramount Fine Foods Centre in Mississauga on 2 March 2024."),
    "cartoon-orchestra-doha-2025": ("Cartoon Orchestra Doha | FOH Engineer Jean-Pierre Boutros", "Jean-Pierre Boutros was FOH engineer for Cartoon Orchestra at Al Mayassa Theatre, QNCC, Doha, on 17 October 2025."),
    "charbel-rouhana-aub-2026": (
        "Charbel Rouhana: Echo – Sadā | FOH Engineer Jean-Pierre Boutros",
        "Jean-Pierre Boutros was FOH engineer for Charbel Rouhana’s Echo – Sadā at AUB Assembly Hall, Beirut, on 28 January 2026.",
    ),
    "ry-x-qatar-philharmonic-doha": (
        "RY X & Qatar Philharmonic | Jean-Pierre Boutros, FOH",
        "Jean-Pierre Boutros: FOH engineer for RY X with the Qatar Philharmonic Orchestra at QNCC, Doha, for Doha Film Festival on 23 November 2026."),
    "tarteeb-shareet-doha": (
        "Shareet · Tarteeb at QNCC | Jean-Pierre Boutros, FOH",
        "Jean-Pierre Boutros was the FOH engineer for Tarteeb’s Shareet concert at Al Mayassa Theatre, QNCC, Doha, on 14 November 2026. View the project."),
    "the-eighties": (
        "The Eighties, Kuwait · FOH | Jean-Pierre Boutros",
        "FOH engineering by Jean-Pierre Boutros for The Eighties… The Knockout at JACC in Kuwait, October 2026. Explore the role, production and photographs."),
    "marina-viotti": (
        "Marina Viotti Opera Gala · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Marina Viotti’s opera gala at Zouk Mikael, Lebanon, on 8 September 2026. View the project and production context."),
    "cartoon-orchestra": (
        "Cartoon Orchestra, Kuwait · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Cartoon Orchestra at JACC National Theatre in Kuwait on 4 October 2025. Explore the concert role and production."),
    "al-sharq-symphony": (
        "Al Sharq Symphony · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Marcel Khalifé and the Istanbul Philharmonic in Al Sharq Symphony, Istanbul, 2017. View the concert record."),
    "abeer-nehme-qatar": (
        "Abeer Nehme & Qatar Philharmonic | Jean-Pierre Boutros",
        "FOH engineering by Jean-Pierre Boutros for Abeer Nehme with the Qatar Philharmonic Orchestra at U VENUE, Doha, 23 January 2026. Explore the project."),
    "baligh-hamdi-night": (
        "Nancy Ajram · Baligh Hamdi Night | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: monitor engineer for Nancy Ajram at Baligh Hamdi Night, Riyadh, 9 November 2023. View his artist-specific role and event context."),
    "warda-night": (
        "Nancy Ajram · Warda Night | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: monitor engineer for Nancy Ajram at Warda Night, Abadi Al Johar Arena, Jeddah, 4 July 2024. Explore the role and concert context."),
    "night-of-arab-stars": (
        "Nancy Ajram · Night of Arab Stars | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: monitor engineer for Nancy Ajram at Night of Arab Stars, Riyadh Season, 31 December 2023. View his role and the concert record."),
    "lebanese-philharmonic-diman": (
        "Lebanese Philharmonic, Diman · FOH | Jean-Pierre Boutros",
        "FOH engineering by Jean-Pierre Boutros for the Lebanese National Philharmonic’s Eternal Covenant concert in Diman, Lebanon, on 26 July 2026."),
    "nancy-ajram-olympia": (
        "Nancy Ajram at L’Olympia · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Nancy Ajram at L’Olympia in Paris, France, on 10 June 2022. View the concert case study, role and photographs."),
    "marcel-khalife-muscat": (
        "Marcel Khalifé, Muscat · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Marcel Khalifé at the House of Musical Arts, Royal Opera House Muscat, Oman, 26–27 September 2019. View the record."),
    "ehdeniyat-abeer-nehme": (
        "Abeer Nehme at Ehdeniyat · FOH | Jean-Pierre Boutros",
        "FOH engineering by Jean-Pierre Boutros for Abeer Nehme at Ehdeniyat International Festival, Lebanon, on 25 July 2025. View the concert and role."),
    "ehdeniyat-al-shami": (
        "Al Shami at Ehdeniyat · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Al Shami at Ehdeniyat International Festival, Lebanon, on 3 August 2025. Explore the concert role and photographs."),
    "ehdeniyat-adam": (
        "Adam at Ehdeniyat · Monitors | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: monitor engineer for Adam at Ehdeniyat International Festival, Lebanon, on 31 July 2025. Explore his role and event context."),
    "nancy-ajram-expo-dubai": (
        "Nancy Ajram at Expo Dubai · Monitors | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: monitor engineer for Nancy Ajram at Infinite Nights, Expo 2020 Dubai, UAE, on 12 November 2021. View his artist-specific role."),
    "papal-broadcast": (
        "Papal Mass Broadcast, Beirut | Jean-Pierre Boutros",
        "Jean-Pierre Boutros’s broadcast sound engineering credit for the 2025 Papal Mass at Beirut Waterfront, Lebanon. Explore the role and production context."),
    "studio-jpb": (
        "StudioJPB · Recording & Mixing | Jean-Pierre Boutros",
        "StudioJPB in Jounieh, Lebanon, founded by Jean-Pierre Boutros in 2008. Explore his recording, mixing and mastering practice and named release credits."),
    "studio-integration": (
        "Studio Audio System Integration | Jean-Pierre Boutros",
        "Explore Jean-Pierre Boutros’s audio system integration work at Merwas Studios in Riyadh and Playsound Studios in Lebanon, with related engineering services."),
    "marcel-khalife-amman": (
        "Marcel Khalifé, Amman · Recording | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: monitor and recording engineer for Marcel Khalifé at Amman Citadel, Jordan, on 13 September 2016. Explore the concert case study."),
    "abeer-nehme-baalbeck": (
        "Abeer Nehme at Baalbeck · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Abeer Nehme at the Temple of Bacchus, Baalbeck International Festival, Lebanon, 19 August 2016. View the project."),
    "beiteddine-marco-polo": (
        "Marco Polo at Beiteddine · Audio | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: audio technical supervision for On the Steps of Marco Polo at Beiteddine Palace, Lebanon, 21–22 June 2013. View the project."),
    "carole-samaha-golden-album": (
        "Carole Samaha · Golden Album Mix | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: mixing and mastering engineer for Carole Samaha’s Golden Album, released 3 March 2023. Explore the album credit and studio work."),
    "zade-dirani-dbayeh": (
        "Zade Dirani, Dbayeh · FOH | Jean-Pierre Boutros",
        "FOH engineering by Jean-Pierre Boutros for Zade Dirani at Palais des Congrès, Dbayeh, Lebanon, on 11 October 2018. Explore the role and event record."),
    "zade-dirani-amman": (
        "Zade Dirani, Amman · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Zade Dirani’s Hope Concert at Royal Cultural Palace, Amman, Jordan, 22 February 2019. Explore the concert record."),
    "marcel-khalife-baalbeck": (
        "Marcel Khalifé at Baalbeck · FOH | Jean-Pierre Boutros",
        "FOH engineering by Jean-Pierre Boutros for Marcel Khalifé’s Ode to a Homeland at Baalbeck, Lebanon, on 5 July 2019. Explore the concert role and sources."),
    "nancy-ajram-jounieh": (
        "Nancy Ajram · Bnoss Jounieh FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Nancy Ajram’s Bnoss Jounieh concert at Fouad Chehab Stadium, Lebanon, 18 August 2022. View the role and event record."),
    "mazeej-ndu": (
        "Mazeej at NDU · FOH | Jean-Pierre Boutros",
        "Jean-Pierre Boutros: FOH engineer for Mazeej by Lucas Sakr at NDU’s Bechara El Rahi Theater, Zouk Mosbeh, Lebanon, on 11 March 2019. View the project."),
    "beirut-the-sea-lover": (
        "Beirut the Sea Lover · 3D Mix | Jean-Pierre Boutros",
        "Jean-Pierre Boutros’s published 3D sound mixing credit for Beirut the Sea Lover at the Roman Baths, Lebanon, on 14 June 2019. Explore the production."),
}

# Production facts and roles already present in build.py and its research files.
# The planning paragraphs explain a future brief, not undocumented past methods.
CASE_STUDIES = {
    "ry-x-qatar-philharmonic-doha": (
        "Case study: songwriting with a symphony orchestra",
        "RY X’s contemporary songwriting and the Qatar Philharmonic Orchestra shared the programme at QNCC’s Auditorium 3 for Doha Film Festival’s DFF Music on 23 November 2026. Jean-Pierre’s confirmed assignment was front-of-house engineering: the audience mix for this performance in Doha.",
        "For a similar vocalist-with-orchestra engagement, the starting brief should identify the ensemble, soloist, programme, stage plan, rehearsal schedule and venue audio system. Recording, broadcast and monitor responsibilities should be specified separately. Explore the orchestra sound service for the information to include in an inquiry."),
    "nancy-ajram-olympia": (
        "Case study: an international concert in Paris",
        "Nancy Ajram’s 10 June 2022 concert at L’Olympia brought her repertoire and live band to the Paris stage following Nancy 10. Jean-Pierre’s confirmed FOH assignment is a documented example of his live sound work in Europe, with the official concert recap and event listing linked in this record.",
        "Front-of-house engineering concerns what the audience hears. Nancy Ajram’s later Baligh Hamdi Night and Warda Night entries document separate artist-monitor assignments. A comparable concert inquiry should identify the engineering position, artist rider, rehearsal and show dates, venue system and local crew."),
    "marcel-khalife-amman": (
        "Case study: concert monitors and recording",
        "For Marcel Khalifé’s Jordan Festival concert at Amman Citadel on 13 September 2016, Jean-Pierre’s confirmed responsibilities were monitor engineering and recording. This combines the performer’s stage-listening requirement with capturing the performance, two distinct parts of the concert brief.",
        "For a comparable engagement, specify who handles FOH, the artist’s monitor requirements, what should be recorded and the intended handover. Channel count, equipment, routing and delivery formats are agreed for each new production. Related Marcel Khalifé records in Muscat and Baalbeck identify Jean-Pierre’s separate FOH work."),
}
