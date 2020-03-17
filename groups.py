# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List, Tuple

from locations import Location


@dataclass
class Group(object):

    name: str
    link: str
    center: Location

    def distance(self, location: Location) -> float:
        return location.distance(self.center)

    def __str__(self):
        return f'{self.name}: {self.link}'


@dataclass
class GroupProposal(object):

    group: Group
    distance: float

    def __str__(self):
        return f'- {self.group}'


GROUP_LIST = [
    Group(name='Barcelona - Sants',
          link='badalsuperior',
          center=Location(latitude=41.378146, longitude=2.136023)),
    Group(name='Barcelona - Badal superior',
          link='https://t.me/badalsuperior',
          center=Location(latitude=41.377685, longitude=2.129068)),
    Group(name='Barcelona - Sant Frederic - Pl. Olivareta',
          link='https://t.me/joinchat/InZOV0tIsFwTXGm0m0wpog',
          center=Location(latitude=41.373148, longitude=2.127712)),
    Group(name='Barcelona - Rambla Brasil - Av. Madrid',
          link='https://t.me/rabbmdr',
          center=Location(latitude=41.379481, longitude=2.129450)),
    Group(name='Barcelona - Plaça del Centre',
          link='https://t.me/plcentre',
          center=Location(latitude=41.3821, longitude=2.1358)),
    Group(name='Barcelona - Sant Baltasar - Pomar',
          link='https://t.me/santbaltasar',
          center=Location(latitude=41.3722, longitude=2.1347)),
    Group(name='Barcelona - Plaça Joan Corrades',
          link='https://t.me/joancorrades',
          center=Location(latitude=41.373188, longitude=2.144534)),
    Group(name='Barcelona - Plaça La Farga',
          link='https://t.me/joinchat/A3b6vhyg36MryoMpzh8HgA',
          center=Location(latitude=41.372435, longitude=2.138757)),
    Group(name='Barcelona - Sagunt - Constitució',
          link='https://t.me/joinchat/EluNFBpo3AiWs6Z8Bub5Fw',
          center=Location(latitude=41.3695, longitude=2.1341)),
    Group(name='Barcelona - Plaça Sants',
          link='https://t.me/joinchat/EluNFBovelYds5NqPnwbMg',
          center=Location(latitude=41.375763, longitude=2.135366)),
    Group(name='Barcelona - Plaça Osca',
          link='https://t.me/AF7PDRwG7PTTAcZyToxl3Q',
          center=Location(latitude=41.3761, longitude=2.1387)),
    Group(name='Barcelona - Carrer Andalusia',
          link='https://t.me/joinchat/ANdMghuzjWnYWZwK565aEA',
          center=Location(latitude=41.371136, longitude=2.133323)),
    Group(name='Barcelona - Carrer Masnou',
          link='https://t.me/cMasnouSants',
          center=Location(latitude=41.3761, longitude=2.1398)),
    Group(name='Barcelona - Carrer Begur',
          link='https://t.me/CarrerBegur',
          center=Location(latitude=41.3734, longitude=2.1305)),
    Group(name='Barcelona - Sant Andreu',
          link='https://t.me/suportsantandreu',
          center=Location(latitude=41.436372, longitude=2.191330)),
    Group(name='Barcelona - Raval',
          link='https://t.me/RavalSuport',
          center=Location(latitude=41.378782, longitude=2.169290)),
    Group(name='Barcelona - Poblenou',
          link='https://t.me/SuportMutuP9',
          center=Location(latitude=41.403531, longitude=2.203162)),
    Group(name='Barcelona - Poble-Sec',
          link='https://t.me/covidpoblesec',
          center=Location(latitude=41.3732, longitude=2.1638)),
    Group(name='Barcelona - Vallcarca',
          link='https://t.me/VallcarcaVKK',
          center=Location(latitude=41.412576, longitude=2.143283)),
    Group(name='Barcelona - Gràcia',
          link='https://t.me/suportgracia',
          center=Location(latitude=41.4029, longitude=2.1569)),
    Group(name='Barcelona - Clot/Camp de l\'Arpa',
          link='https://t.me/XarxaSuportCA',
          center=Location(latitude=41.4132, longitude=2.1821)),
    Group(name='Barcelona - Sant Antoni',
          link='https://t.me/santantonicovid19',
          center=Location(latitude=41.3785, longitude=2.1588)),
    Group(name='Barcelona - Mercat de Sants',
          link='https://t.me/joinchat/AS5arRzobwCq3VvUSX8bqQ',
          center=Location(latitude=41.3751, longitude=2.1337)),
    Group(name='Barcelona - Creu Coberta',
          link='https://t.me/creucuesquerra',
          center=Location(latitude=41.3751, longitude=2.1462)),
    Group(name='Barcelona - Olzinelles',
          link='https://t.me/olzinelles',
          center=Location(latitude=41.3733, longitude=2.1366)),
    Group(name='Barcelona - Barceloneta',
          link='https://t.me/joinchat/QjDQuxq-jgGVbNwVOFSGGw',
          center=Location(latitude=41.3825, longitude=2.1859)),
    Group(name='Barcelona - El Carmel',
          link='623144345',
          center=Location(latitude=41.422, longitude=2.1554)),
    Group(name='Barcelona - La Tregua',
          link='https://twitter.com/espailatregua',
          center=Location(latitude=41.4066, longitude=2.1584)),
    Group(name='Barcelona - Carrer Bonveí',
          link='https://t.me/bonveisuportmutu',
          center=Location(latitude=41.3751, longitude=2.1248)),
    Group(name='Barcelona - Jocs Florals',
          link='https://t.me/JocsFloralsSolidari',
          center=Location(latitude=41.3716, longitude=2.135)),
    Group(name='Sant Boi de Llobregat',
          link='https://twitter.com/xarxasantboi',
          center=Location(latitude=41.346, longitude=2.0357)),
    Group(name='Barcelona - Grup de suport popular del barris de Cassoles',
          link='https://chat.whatsapp.com/Lfv2nt2TscjKh7T2NG7PQr',
          center=Location(latitude=41.4096, longitude=2.1304)),
    Group(name='Barcelona - Xarxa de Suport Mutu Dreta de l\'Eixample',
          link='https://chat.whatsapp.com/J36A3MsqxgB1NHqgQ61I19',
          center=Location(latitude=41.3938, longitude=2.168)),
    Group(name='Barcelona - Xarxa de Suport Mutu Eixample Esquerra',
          link='https://t.me/eenscuidem',
          center=Location(latitude=41.3866, longitude=2.1545)),
    Group(name='Barcelona - Espai de Suport Fort Pienc',
          link='casagroga.fortpienc@gmail.com',
          center=Location(latitude=41.3965, longitude=2.1823)),
    Group(name='Barcelona - Xarxa de Suport Mutu d\'Horta Guinardó',
          link='https://t.me/suporthg',
          center=Location(latitude=41.4157, longitude=2.1646)),
    Group(name='Barcelona - Pl. Eivissa',
          link='https://chat.whatsapp.com/LtO0KcqWKBA4xkUD01op78',
          center=Location(latitude=41.4307, longitude=2.161)),
    Group(name='Barcelona - Xarxa de Suport 3VR (Nou Barris)',
          link='https://t.me/xarxasuport3vr',
          center=Location(latitude=41.4307, longitude=2.161)),
    Group(name='Barcelona - Grup de Suport del Barri de Porta',
          link='https://chat.whatsapp.com/G5vIGv1m50L7Z8AMw7P8jQ',
          center=Location(latitude=41.4348, longitude=2.1783)),
    Group(name='Barcelona - Grup de Suport Mutu de Sant Gervasi',
          link='https://chat.whatsapp.com/FiG2aVw0E4H9oLP1iA6bAu',
          center=Location(latitude=41.4035, longitude=2.1315)),
    Group(name='Barcelona - Grup de Suport de Sarrià',
          link='https://chat.whatsapp.com/Hua9aQF8NEZ6TKEd91r5pm',
          center=Location(latitude=41.4001, longitude=2.1226)),
    Group(name='Barcelona - Xarxa de Suport de Vallvidrera',
          link='https://chat.whatsapp.com/EyIupietCZA1hqYLZUKUV1',
          center=Location(latitude=41.418, longitude=2.1002)),
    Group(name='Castellar del Vallès',
          link='https://chat.whatsapp.com/JMxS81Vef8bBoyUwFCCGIU',
          center=Location(latitude=41.6177, longitude=2.0882)),
    Group(name='Xara Conca d\'Òdena de solidaritat',
          link='https://chat.whatsapp.com/FetNunJzbIm6dupUi3GSx6',
          center=Location(latitude=41.5822, longitude=1.6177)),
    Group(name='Cornellà de Llobregat',
          link='https://t.me/Covid19enKorney',
          center=Location(latitude=41.3574, longitude=2.0716)),
    Group(name='Lleida (Bordeta/Magraners)',
          link='https://chat.whatsapp.com/D8lExXwTOfKITSFcrBslKr',
          center=Location(latitude=41.609230, longitude=0.654732)),
    Group(name='Lleida (Camp Esport/Ciutat Jardí)',
          link='https://chat.whatsapp.com/CKJQ2u6sjx53BTTCnHoeq8',
          center=Location(latitude=41.624310, longitude=0.611117)),
    Group(name='Lleida (Cappont)',
          link='https://chat.whatsapp.com/KiMweuSRmdP0ARCKz72H7g',
          center=Location(latitude=41.613046, longitude=0.630181)),
    Group(name='Lleida (Centre Històric)',
          link='https://chat.whatsapp.com/IZhZ9pO3n8Q1aNTZ1tr58W',
          center=Location(latitude=41.617085, longitude=0.623306)),
    Group(name='Lleida (Horta/Llívia)',
          link='https://chat.whatsapp.com/LadTIDhMUoDA2IAc1NhDp1',
          center=Location(latitude=41.647039, longitude=0.639429)),
    Group(name='Lleida (Mariola/Escorxador)',
          link='https://chat.whatsapp.com/I71DLyRDx27DBx1pcYTabw',
          center=Location(latitude=41.611964, longitude=0.614738)),
    Group(name='Lleida (Secà/Balàfia/Pardinyes)',
          link='https://chat.whatsapp.com/KbOr6hRv51r20rpTUoRbkG',
          center=Location(latitude=41.630375, longitude=0.629216)),
    Group(name='Lleida (Zona Alta/Clot)',
          link='https://chat.whatsapp.com/Bh2DXQvImXaFwPxs7Q5KIv',
          center=Location(latitude=41.623687, longitude=0.623000)),
    Group(name='Xarxa de suport de Sabadell',
          link='https://twitter.com/SuportSabadell',
          center=Location(latitude=41.546459, longitude=2.103025)),
    Group(name='Xarxa de solidaritat de Sant Feliu de Llobregat',
          link='https://t.me/XarxaSanfeliuenca',
          center=Location(latitude=41.384121, longitude=2.050138)),
    Group(name='Xarxa Solidària Gramenet',
          link='https://t.me/XarxaSolidariaGramenet',
          center=Location(latitude=41.444716, longitude=2.210846)),
    Group(name='Xarxa local de Santa Coloma de Gramenet',
          link='https://t.me/joinchat/AQhrFUmZi84eD6jX2Ff4lQ',
          center=Location(latitude=41.444845, longitude=2.213764)),
    Group(name='Tarragona - Part Alta',
          link='https://chat.whatsapp.com/Hpml5azPSBDFDshVll4OEV',
          center=Location(latitude=41.118170, longitude=1.257414)),
    Group(name='Tarragona - Sant Pere i Sant Pau',
          link='https://chat.whatsapp.com/FIMZCC5B1OiA8aln2H5Xan',
          center=Location(latitude=41.138373, longitude=1.253599)),
    Group(name='Tarragona - Sant Salvador',
          link='https://chat.whatsapp.com/B6v3yfrQmRsAoH2ysnPf2e',
          center=Location(latitude=41.157861, longitude=1.241360)),
    Group(name='Tarragona - Serrallo',
          link='https://chat.whatsapp.com/D7HUoF6os78Czdik3MDPhc',
          center=Location(latitude=41.109931, longitude=1.240871)),
    Group(name='Tarragona - Centre',
          link='https://chat.whatsapp.com/FC2u6rYMzTBHbiQFGxDZiS',
          center=Location(latitude=41.118368, longitude=0.245300)),
    Group(name='Tarragona - Llevant',
          link='https://chat.whatsapp.com/GUskamqtY8fJ5340FgAFi9',
          center=Location(latitude=41.120163, longitude=1.268211)),
    Group(name='Tarragona - Torreforta',
          link='https://chat.whatsapp.com/Keg1OQ9iRwWFxWn2L0twnB',
          center=Location(latitude=41.118433, longitude=1.217407)),
    Group(name='Tarragona - La Sageta',
          link='https://twitter.com/la_Sageta',
          center=Location(latitude=41.116839, longitude=1.257222)),
    Group(name='Terrassa',
          link='https://chat.whatsapp.com/EGWyOGH9K8X4tXVsAeTcqk',
          center=Location(latitude=41.561782, longitude=2.008551)),
    Group(name='Barcelona - Nova Esquerra de l\'Eixample',
          link='https://t.me/joinchat/AJPe1xhxkBwooC_wcDT0uQ',
          center=Location(latitude=41.383, longitude=2.1491)),
    Group(name='Sant Cugat del Vallès',
          link='https://t.me/XarxaSuportSantCugat',
          center=Location(latitude=41.4684, longitude=2.0804)),
    Group(name='Badalona',
          link='https://t.me/XarxaSolidariaBDN',
          center=Location(latitude=41.4484, longitude=2.244)),
    Group(name='Barcelona - Casca Antic',
          link='https://chat.whatsapp.com/JJyuiGFC5ZAL7Gy45UZFqg',
          center=Location(latitude=41.378607, longitude=2.170172)),
    Group(name='Barcelona - La Marina',
          link='https://t.me/covid19Lamarina',
          center=Location(latitude=41.345322, longitude=2.133411)),
    Group(name='Barcelona - Carrer Burgos',
          link='https://t.me/joinchat/AKm2tRpy_xMhfypIYxVL3w',
          center=Location(latitude=41.372327, longitude=2.134401)),
    Group(name='Barcelona - Xarxa de Suport de Verdum',
          link='https://t.me/XarxadeSuportVerdum',
          center=Location(latitude=41.442887, longitude=2.175689)),
    Group(name='Girona',
          link='https://t.me/joinchat/AAAAAExwU5olb62cdiXxxA',
          center=Location(latitude=41.979290, longitude=2.817422)),
    Group(name='Hospitalet del Llobregat - Bellvitge i Gornal',
          link='https://chat.whatsapp.com/I7HaQ36H1YZB7EEJhA5BQs',
          center=Location(latitude=41.353510, longitude=2.114561)),
    Group(name='Hospitalet del Llobregat - Florida',
          link='https://chat.whatsapp.com/LMfTHzNP6zgAQaMM7VZnTI',
          center=Location(latitude=41.368309, longitude=2.110016)),
    Group(name='Hospitalet del Llobregat - Pubilla Cases - Cam Serra',
          link='https://chat.whatsapp.com/H6FsAwlr2my4XVPZAsargu',
          center=Location(latitude=41.370291, longitude=2.103871)),
    Group(name='Hospitalet del Llobregat - Carrer Rodes',
          link='mercehermar@gmail.com',
          center=Location(latitude=41.361, longitude=2.1086)),
    Group(name='Hospitalet del Llobregat - Sant Josep Centre',
          link='https://chat.whatsapp.com/LEcPBrwbAX6Ca59bdj3Nfd',
          center=Location(latitude=41.361281, longitude=2.109546)),
    Group(name='Hospitalet del Llobregat - Suport Barri de Santa Eulàlia',
          link='https://t.me/SuportStaEulali',
          center=Location(latitude=41.3655, longitude=2.1242)),
    Group(name='Hospitalet del Llobregat - Torrassa / Collblanc',
          link='https://chat.whatsapp.com/L4fvhQhwZJT5eOIKLDRKjb',
          center=Location(latitude=41.370928, longitude=2.117303)),
    Group(name='Girona',
          link='https://t.me/joinchat/AAAAAExwU5olb62cdiXxxA',
          center=Location(latitude=41.979290, longitude=2.817422)),
    Group(name='Mataró',
          link='https://t.me/joinchat/AAAAAFSNw0GqqFo4op6YVQ',
          center=Location(latitude=41.539142, longitude=2.444395)),
    Group(name='Montmeló',
          link='https://chat.whatsapp.com/IkGzHloom2n62PGt2DE5vb',
          center=Location(latitude=41.554162, longitude=2.247238)),
    Group(name='Vic',
          link='https://twitter.com/covic2020',
          center=Location(latitude=41.9308, longitude=2.2545)),
    Group(name='Barcelona - Besós/Maresme',
          link='https://chat.whatsapp.com/CEYJgc7SsncIuRUzEp5nGP',
          center=Location(latitude=41.1412, longitude=2.2165)),
    Group(name='Barcelona - Can Baró',
          link='https://chat.whatsapp.com/CTtgpqyAzMV6E7v87kxZoO',
          center=Location(latitude=41.4166, longitude=2.1629)),
    Group(name='Barcelona - Gòtic/Sta Caterina/Ribera/Born',
          link='https://t.me/BarriGoticEnXarxa',
          center=Location(latitude=41.384995, longitude=2.180424)),
    Group(name='Barcelona - El Poblet',
          link='https://chat.whatsapp.com/CakCRZl2Boc6fdJE5yZBwp',
          center=Location(latitude=41.402524, longitude=2.170314)),
    Group(name='Barcelona - Verneda/La Pau',
          link='https://t.me/xarxavernedalapau',
          center=Location(latitude=41.422853, longitude=2.205490)),
    Group(name='Barcelona - Font de la Guatlla',
          link='https://t.me/RedApoyoFontGuatlla',
          center=Location(latitude=41.370613, longitude=2.144228)),
    Group(name='Barcelona - Carrer Lanzarore',
          link='https://chat.whatsapp.com/JanKsReKVQhCCGvNv6zwrU',
          center=Location(latitude=41.439727, longitude=2.189930)),
    Group(name='Cerdanyola del Vallès/Montflorit',
          link='https://chat.whatsapp.com/IuFolPVAFrtGGNBZ2dr3Qd',
          center=Location(latitude=41.489984, longitude=2.131965)),
    Group(name='El Masnou',
          link='https://t.me/xarxasuportelmasnou',
          center=Location(latitude=41.482801, longitude=2.311675)),
    Group(name='Navàs',
          link='https://t.me/suportnavas',
          center=Location(latitude=41.9002, longitude=1.8784)),
    Group(name='Rubí',
          link='ceeixam@gmail.com',
          center=Location(latitude=41.496801, longitude=2.035134)),
]


def groups_by_distance(location: Location) -> List[GroupProposal]:
    proposals = map(
        lambda group: GroupProposal(group, group.distance(location)),
        GROUP_LIST
    )
    return sorted(proposals, key=lambda proposal: proposal.distance)
