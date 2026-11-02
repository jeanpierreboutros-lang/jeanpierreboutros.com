"""Published studio credits. Preserve the distinction between person and studio.

Sources were checked on 2 November 2026. Artist-channel descriptions are preferred;
storefront personnel metadata, institutional catalogues and contemporary reporting
are identified by name. A studio/location credit does not establish every engineer
or production stage. Do not infer additional roles from a shared artist credit.
"""
from html import escape as e

QOBUZ_BI_SARAHA = "https://www.qobuz.com/gb-en/album/bi-saraha-abeer-nehme/xxqwrx69r9zmc"
SING_A_LITTLE = "https://mediatheque.philharmoniedeparis.fr/mediatheque/doc/ALOES/1114862/abeer-nehme-marcel-khalife-sing-a-little-marcel-khalife-composition"

CREDIT_GROUPS = [
    {"id": "nancy-ajram", "name": "Nancy Ajram", "artists": ["Nancy Ajram"], "works": [
        {"title": "Men Nazra", "year": "2024", "role": "Mixing & mastering", "source": "Nancy Ajram · Official release credits", "url": "https://www.youtube.com/watch?v=UFn1-pTQ85s", "note": "Words and music: Ziad Jamal."},
        {"title": "Aamon Jadidon", "year": "2024", "role": "Mixing & mastering", "source": "Nancy Ajram · Official release credits", "url": "https://www.youtube.com/watch?v=Zc6nH0sK7rU"},
        {"title": "Ya Eid", "year": "2022", "role": "Mixing & mastering", "source": "Nancy Ajram · Official release credits", "url": "https://www.youtube.com/watch?v=Mh4_BMRP43M", "note": "Words and music: Salim Assaf."},
        {"title": "Warana Eh", "year": "2025", "role": "Recording", "source": "Nancy Ajram · Official music video credits", "url": "https://www.youtube.com/watch?v=Lb21_-odDjs"},
        {"title": "Akher Esdar", "year": "2023", "role": "Mixing & mastering", "source": "Nancy Ajram · Official lyric video credits", "url": "https://www.youtube.com/watch?v=xJIH9jJr9SA"},
    ]},
    {"id": "georges-wassouf", "name": "Georges Wassouf", "artists": ["Georges Wassouf"], "works": [
        {"title": "Noss Omry", "year": "2023", "role": "Mixing & mastering", "source": "Georges Wassouf · Official release credits", "url": "https://www.youtube.com/watch?v=Tn39YMcJUxg"},
        {"title": "Raksa Espani", "year": "2024", "role": "Mixing & mastering", "source": "Georges Wassouf · Official release credits", "url": "https://www.youtube.com/watch?v=I1ilzrqdZ10"},
    ]},
    {"id": "carole-samaha", "name": "Carole Samaha", "artists": ["Carole Samaha"], "works": [
        {"title": "Golden Album", "year": "2023", "role": "Mixing & mastering", "source": "Carole Samaha · Official album credits", "url": "https://www.youtube.com/watch?v=M--KeGtmvgM", "project": "carole-samaha-golden-album", "note": "Twelve tracks, released 3 March 2023.", "tracks": ["Satantahi Al Harbu", "Elahy", "Beirut", "Fakker Bi Ghayrika", "Ehtizar", "Ayoha Al Marroun", "Sa Assiru Yawman", "Toyour Al Nil", "Sa Ahlomu", "Kitar Al Sa’a Al Wahida", "La Anamu Li Ahloma", "Wa Nahnu Nohebb Al Hayat"], "track_source": "https://music.apple.com/us/album/golden-album/1675126762"},
    ]},
    {"id": "cyrine-abdel-nour", "name": "Cyrine Abdel Nour", "artists": ["Cyrine Abdel Nour"], "works": [
        {"title": "Aamellon Aeqdi", "year": "2025", "role": "Mixing & mastering", "source": "Cyrine Abdel Nour · Official music video credits", "url": "https://www.youtube.com/watch?v=CpqTVr-fMFY"},
    ]},
    {"id": "abeer-nehme", "name": "Abeer Nehme", "artists": ["Abeer Nehme"], "works": [
        {"title": "Ossotna", "year": "2022", "role": "Recording, mixing & mastering", "source": "Abeer Nehme · Release credits", "url": "https://www.youtube.com/watch?v=mUo8CVKMAEs", "credit_source": "https://rw.popnable.com/libani/indirimbo/746931-abeer-nehme-ossotna/amagambo-n%27ubusobanuro"},
        {"title": "Bala Ma Nhess", "year": "2022", "role": "Mastering · StudioJPB", "source": "Universal Music MENA personnel metadata · Qobuz", "url": "https://www.qobuz.com/us-en/album/bala-ma-nhess-abeer-nehme/tpoeewi2tys9a", "note": "The mastering credit is published under Jean Pierre Boutros Studio."},
        {"title": "Shou Baamel", "year": "2022 album version", "role": "Mastering & studio credit · StudioJPB", "source": "Universal Music MENA personnel metadata · Qobuz", "url": QOBUZ_BI_SARAHA},
        {"title": "Sawt", "year": "2022", "role": "Mastering & studio credit · StudioJPB", "source": "Universal Music MENA personnel metadata · Qobuz", "url": QOBUZ_BI_SARAHA},
        {"title": "Ossotna (Unplugged Version)", "year": "2022", "role": "Mastering & studio credit · StudioJPB", "source": "Universal Music MENA personnel metadata · Qobuz", "url": QOBUZ_BI_SARAHA},
        {"title": "Aamel Nasini", "year": "2022", "role": "Studio credit · StudioJPB", "source": "Universal Music MENA personnel metadata · Qobuz", "url": "https://www.qobuz.com/se-en/album/aamel-nasini-abeer-nehme/ko747w2te5eqc", "note": "The release lists Jean Pierre Boutros Studio; mixing and mastering are credited to Sleiman Damien."},
        {"title": "Bi Saraha", "year": "2022", "role": "Studio recording · StudioJPB", "source": "Universal Music MENA metadata / contemporary release coverage", "url": QOBUZ_BI_SARAHA, "credit_source": "https://ahwal.media/archives/94293", "note": "Recording is credited to StudioJPB; mixing and mastering are credited to Sleiman Damien."},
        {"title": "El Meelad El Jayi", "year": "2021", "role": "Vocal recording studio · StudioJPB", "source": "Abeer Nehme · Official release credits", "url": "https://www.youtube.com/watch?v=cUPS5sXwxm4", "note": "StudioJPB is credited for the vocal recording location. Ralph Sleiman is credited for recording, mixing and mastering."},
        {"title": "Fallou", "role": "Mixing & mastering", "source": "Abeer Nehme · Official release; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=hqyW-9LJLoM", "confirmed_by_owner": True},
        {"title": "Hikayi", "role": "Mixing & mastering", "source": "Abeer Nehme · Official release; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=XMFdqEu8Jx4", "confirmed_by_owner": True},
        {"title": "Fi Asfour", "role": "Mixing & mastering", "source": "Abeer Nehme · Official album audio; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=09L7zX-SVRc", "confirmed_by_owner": True},
        {"title": "Kil Ma T'illi", "role": "Mixing & mastering", "source": "Abeer Nehme · Official album audio; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=cn4K-fZ-x70", "confirmed_by_owner": True},
        {"title": "Addaysh Bhebak", "year": "2022 music video", "role": "Recorded at StudioJPB", "source": "Abeer Nehme · Official release / MTV Lebanon coverage", "url": "https://www.youtube.com/watch?v=-NSBIfNe7pA", "credit_source": "https://www.mtv.com.lb/news/1250854", "note": "Recording is credited to Studio Jean-Pierre Boutros. No personal recording engineer or mixing/mastering credit is inferred."},
    ]},
    {"id": "sing-a-little", "name": "Marcel Khalifé & Abeer Nehme", "artists": ["Marcel Khalifé", "Abeer Nehme"], "works": [
        {"title": "Sing A Little", "year": "2019 CD edition", "role": "Recorded at StudioJPB", "source": "Philharmonie de Paris · CD catalogue", "url": SING_A_LITTLE, "note": "Composed and produced by Marcel Khalifé, sung by Abeer Nehme; Faraj Hanna is credited on buzuq. The catalogue identifies Studio Jean-Pierre Boutros as the recording studio.", "tracks": ["Al Musiqa", "Mizmar", "Raja’a", "Hayda Init", "Ma Ajmal Al Hob", "Ba’atilak Sawti", "Ektibni Qasideh", "Toufola", "Allilini", "Ya Mariam", "Ya Henna", "Ya Mahla Nourha", "Fakr Bi Ghayrak", "Ghanni Kalilan"]},
    ]},
    {"id": "ramy-ayyach", "name": "Ramy Ayyach", "artists": ["Ramy Ayyach"], "works": [
        {"title": "Sway بالعربي", "year": "2024", "role": "Mixing & mastering", "source": "Ramy Ayach · Official release credits", "url": "https://www.youtube.com/watch?v=Yl691WC3dFk"},
        {"title": "Ahlan Bil Jamal", "year": "2024", "role": "Mastering", "source": "Ramy Ayach · Official release credits", "url": "https://www.youtube.com/watch?v=A3x-IdvDIro", "note": "Arrangement and mixing: The AB Brothers."},
        {"title": "Ismallah", "year": "2025", "role": "Mastering", "source": "Contemporary release coverage · Assawsana", "url": "https://www.assawsana.com/article/680079"},
        {"title": "Ma Bensak", "role": "Mixing & mastering", "source": "Ramy Ayach · Official release; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=6bNch07UIaA", "confirmed_by_owner": True},
    ]},
    {"id": "al-walid-hallani", "name": "Al Walid Hallani", "artists": ["Al Walid Hallani"], "works": [
        {"title": "Zeffo El Amar", "year": "2023", "role": "Mixing & mastering", "source": "Al Walid Hallani · Official music video credits", "url": "https://www.youtube.com/watch?v=6mOQ_iczvhk", "confirmed_by_owner": True},
    ]},
    {"id": "marwan-chami", "name": "Marwan Chami", "artists": ["Marwan Chami"], "works": [
        {"title": "Tayer", "year": "2022", "role": "Mixing & mastering", "source": "Marwan Chami · Official music video credits", "url": "https://www.youtube.com/watch?v=Y44I1oeyfQE"},
    ]},
    {"id": "nader-khoury", "name": "Nader Khoury", "artists": ["Nader Khoury"], "works": [
        {"title": "Idi bi Idik", "year": "2018", "role": "Recorded at StudioJPB", "source": "United Nations Information Centre Beirut · Official release announcement", "url": "https://unicbeirut.org/index.php/Press%20Release/create-press-releases-32", "note": "The UN announcement credits Jean Pierre Boutros Studio for recording; it does not identify an individual engineer or mixing/mastering role."},
    ]},
    {"id": "georges-nehme", "name": "Georges Nehme", "artists": ["Georges Nehme"], "works": [
        {"title": "Hayda Hali", "year": "2022", "role": "Mixing & mastering", "source": "George Nehme · Official release / MTV Lebanon", "url": "https://www.youtube.com/watch?v=Ip8bWgOD5Fc", "credit_source": "https://www.mtv.com.lb/amp/details/1299182"},
        {"title": "Moving Mountains", "year": "2014 CD edition · OK World", "role": "Vocal recording · Selected takes", "source": "CD personnel and recording notes · Musicbase", "url": "https://www.qobuz.com/us-en/album/ok-world-bugge-wesseltoft-josemi-carmona-shrikant-shriram/w893anvdzt5pc", "credit_source": "https://musicbase.net/ok-world", "note": "Jean-Pierre is credited for recording track 1. The notes identify Georges Nehme’s vocal takes at StudioJPB; no whole-album recording or other vocalists’ recording is inferred."},
        {"title": "Betetzekkari", "year": "2017", "role": "Recorded at StudioJPB", "source": "Contemporary release coverage · Elfann", "url": "https://elfann.com/news/show/1172993/جورج-نعمة-يطلق-جديده-بتتذكري-بالصوت", "note": "The recording studio is credited to Jean-Pierre; mixing and mastering are credited to Elie Barbar."},
    ]},
    {"id": "macadi-nahhas", "name": "Macadi Nahhas", "artists": ["Macadi Nahhas"], "works": [
        {"title": "Nour", "year": "2014", "role": "Recording & mixing", "source": "CD personnel and production notes · Musicbase", "url": "https://musicbase.net/nour", "note": "Album mastering is credited to Abbey Road Studios.", "tracks": ["Taaban", "Khilis Il Haki", "Nashidon Ma", "Intal Hala", "Ta’a Nis’har", "Tiji Nsafer", "Hamam Il Dar", "Khadra"]},
    ]},
    {"id": "tania-saleh", "name": "Tania Saleh", "artists": ["Tania Saleh"], "works": [
        {"title": "Oum Sakker El Dekkene", "year": "2015", "role": "Recording & mastering", "source": "Contemporary release coverage · Veto", "url": "https://www.vetogate.com/1818528", "note": "Arrangement and mixing: Cesar Kahwagi."},
    ]},
    {"id": "rasha-rizk", "name": "Rasha Rizk", "artists": ["Rasha Rizk"], "works": [
        {"title": "اللعبة (The Play)", "year": "2014", "role": "Recording", "source": "Spotify · Album release; recording role confirmed by Jean-Pierre Boutros", "url": "https://open.spotify.com/album/5jBdrUfmowed8lJVvzFuyp", "confirmed_by_owner": True},
    ]},
    {"id": "yara", "name": "Yara", "artists": ["Yara"], "works": [
        {"title": "Mosh Bimazagak", "year": "2023", "role": "Mixing & mastering", "source": "Yara · Official release credits", "url": "https://www.youtube.com/watch?v=VycPpNdp3us"},
    ]},
    {"id": "leen-hayek", "name": "Leen Hayek", "artists": ["Leen Hayek"], "works": [
        {"title": "Nassini", "year": "2024", "role": "Mixing & mastering", "source": "Leen Hayek · Official release / published credits", "url": "https://www.youtube.com/watch?v=xT7aAVu4HlU", "credit_source": "https://www.lyrics-arabic.com/2024/02/lyrics-nassini-leen-hayek.html"},
    ]},
    {"id": "chantal-bitar", "name": "Chantal Bitar", "artists": ["Chantal Bitar"], "works": [
        {"title": "Mech Rah Khallik Tfell", "year": "2020", "role": "Recording, mixing & mastering", "source": "Chantal Bitar · Official release credits", "url": "https://www.youtube.com/watch?v=zxl5bRawqdM", "note": "Faraj Hanna is credited on buzuq."},
    ]},
    {"id": "carlos-azar", "name": "Carlos Azar", "artists": ["Carlos Azar"], "works": [
        {"title": "Kel Ma Bde’ellak", "year": "2023", "role": "Mixing & mastering", "source": "Contemporary release coverage · Lebanon24", "url": "https://www.lebanon24.com/news/arts-celebrities/1076261/فنان-لبناني-شهير-يعود-للغناء-بعد-انقطاع-9-سنوات-من-هو؟"},
    ]},
    {"id": "ziad-bourji", "name": "Ziad Bourji", "artists": ["Ziad Bourji"], "works": [
        {"title": "Shtaatella", "year": "2022", "role": "Mixing & mastering", "source": "Ziad Bourji · Official release / Ahram coverage", "url": "https://www.youtube.com/watch?v=pc-osWzFyi0", "credit_source": "https://gate.ahram.org.eg/News/3907358.aspx"},
    ]},
    {"id": "sarina-cross", "name": "Sarina Cross", "artists": ["Sarina Cross"], "works": [
        {"title": "Ragismena Matia (Ραγισμένα Μάτια)", "year": "2019", "role": "Mixing & mastering", "source": "Sarina Cross · Official release credits", "url": "https://www.youtube.com/watch?v=5awyeu88fgQ", "note": "The video credits identify JPB Studios, Beirut."},
    ]},
    {"id": "ziad-jamal", "name": "Ziad Jamal", "artists": ["Ziad Jamal"], "works": [
        {"title": "Yemken", "year": "2025", "role": "Mixing & mastering", "source": "Contemporary release coverage · Al Boraq Media", "url": "https://www.alboraqmedia.com/2025/06/Ziad-Jamal%20.html"},
    ]},
    {"id": "mouhamad-khairy", "name": "Mouhamad Khairy", "artists": ["Mouhamad Khairy"], "works": [
        {"title": "Ya Samra", "year": "2023", "role": "Mixing & mastering", "source": "Contemporary release coverage · Al Rabia FM", "url": "https://www.alrabiafm.com/mohamed-khairy-presents-the-song-ya-samra/", "note": "Words and music: Ziad Jamal."},
    ]},
    {"id": "mohammed-islam", "name": "Mohammed Islam", "artists": ["Mohammed Islam"], "works": [
        {"title": "Nheb El Dini", "year": "2023", "role": "Mixing & mastering", "source": "Platinum Records · Official release; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=z--xdkXvyEg", "confirmed_by_owner": True},
    ]},
    {"id": "salim-assaf", "name": "Salim Assaf", "artists": ["Salim Assaf"], "works": [
        {"title": "Shu Hal Hob", "role": "Recording, mixing & mastering", "source": "Salim Assaf · Official lyric video; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=RWWslews8mI", "confirmed_by_owner": True},
        {"title": "Eza Fik", "role": "Recording, mixing & mastering", "source": "Salim Assaf · Official music video; role confirmed by Jean-Pierre Boutros", "url": "https://www.youtube.com/watch?v=P-sxaVWswg4", "confirmed_by_owner": True},
    ]},
    {"id": "salah-el-kurdi", "name": "Salah El Kurdi", "artists": ["Salah El Kurdi"], "works": [
        {"title": "Taii Nkhoun", "role": "Mixing & mastering", "source": "Salah El Kurdi · Official release credits", "url": "https://www.youtube.com/watch?v=3IX_hsiP_lU", "confirmed_by_owner": True},
    ]},
    {"id": "ria-ellinidou", "name": "Ria Ellinidou", "artists": ["Ria Ellinidou"], "works": [
        {"title": "Στα Κόκκινα", "role": "Mixing & mastering", "source": "Ria Ellinidou · Official lyric video credits", "url": "https://www.youtube.com/watch?v=CosSCMqn4WA", "confirmed_by_owner": True},
        {"title": "Όταν Αγαπάς", "role": "Mixing & mastering", "source": "Ria Ellinidou · Official lyric video credits", "url": "https://www.youtube.com/watch?v=sRL16GeOES8", "confirmed_by_owner": True},
    ]},
    {"id": "mike-massy", "name": "Mike Massy · Naseej", "artists": ["Mike Massy"], "works": [
        {"title": "Naseej", "year": "2014", "role": "Vocal recording · Selected takes", "source": "CD personnel and recording notes · Musicbase", "url": "https://musicbase.net/naseej", "note": "Jean-Pierre is named among the recording engineers. The album notes locate Fadia Tomb El Hage’s vocal takes at StudioJPB; Mike Massy’s vocals were recorded in France."},
    ]},
]


def studio_groups_html(*, compact=False):
    """Show titles and Jean-Pierre's credits; retain research notes in the source data."""
    groups = []
    for group in CREDIT_GROUPS:
        works = []
        for work in group["works"]:
            title = e(work["title"])
            if work.get("project"):
                title = f'<a href="/projects/{e(work["project"])}/">{title}</a>'
            elif work.get("url"):
                title = f'<a href="{e(work["url"])}" target="_blank" rel="noopener noreferrer">{title}<span class="sr-only"> (opens in a new tab)</span></a>'
            role = work["role"]
            if role == "Recorded at StudioJPB":
                credit = "Studio Jean-Pierre Boutros · Recording studio"
            elif role.endswith(" · StudioJPB"):
                credit = "Studio Jean-Pierre Boutros · " + role.removesuffix(" · StudioJPB")
            else:
                credit = "Jean-Pierre Boutros · " + role
            works.append(f'<li><div class="studio-credit-title">{title}</div><p class="studio-credit-role">{e(credit)}</p></li>')
        content = '<ul class="studio-credit-works">' + ''.join(works) + '</ul>'
        if compact:
            groups.append(f'<details class="studio-credit-group"><summary>{e(group["name"])}</summary>{content}</details>')
        else:
            groups.append(f'<section class="studio-credit-group" id="{e(group["id"])}"><h2>{e(group["name"])}</h2>{content}</section>')
    return '<div class="studio-credits-list">' + ''.join(groups) + '</div>'
