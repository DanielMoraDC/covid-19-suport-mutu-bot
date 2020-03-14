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
    Group(name='Badal superior',
          link='https://t.me/badalsuperior',
          center=Location(latitude=41.377685, longitude=2.129068)),
    Group(name='Sant Frederic - Pl. Olivareta',
          link='https://t.me/suportbadal',
          center=Location(latitude=41.373148, longitude=2.127712)),
    Group(name='Rambla Brasil - Av. Madrid',
          link='https://t.me/rabbmdr',
          center=Location(latitude=41.379481, longitude=2.129450)),
    Group(name='Av. Madrid - Plaça del Centre',
          link='https://t.me/joinchat/OsrVxxf3eBl3hGsbc3yYfQ',
          center=Location(latitude=41.3821, longitude=2.1358)),
    Group(name='Sant Baltasar - Pomar',
          link='https://t.me/santbaltasar',
          center=Location(latitude=41.3722, longitude=2.1347)),
    Group(name='Plaça Joan Corrades',
          link='https://t.me/joancorrades',
          center=Location(latitude=41.373188, longitude=2.144534)),
    Group(name='Plaça La Farga',
          link='https://t.me/joinchat/A3b6vhyg36MryoMpzh8HgA',
          center=Location(latitude=41.372435, longitude=2.138757)),
    Group(name='Sagunt - Constitució',
              link='https://t.me/joinchat/EluNFBpo3AiWs6Z8Bub5Fw',
              center=Location(latitude=41.3695, longitude=2.1341)),
    Group(name='Plaça Sants',
              link='https://t.me/joinchat/EluNFBovelYds5NqPnwbMg',
              center=Location(latitude=41.375763, longitude=2.135366)),
    Group(name='Plaça Osca',
              link='https://t.me/AF7PDRwG7PTTAcZyToxl3Q',
              center=Location(latitude=41.3761, longitude=2.1387)),
    Group(name='Carrer Andalusia',
              link='https://t.me/joinchat/ANdMghuzjWnYWZwK565aEA',
              center=Location(latitude=41.371136, longitude=2.133323)),
    Group(name='Carrer Masnou',
          link='https://t.me/cMasnouSants',
          center=Location(latitude=41.3761, longitude=2.1398)),
    Group(name='Carrer Begur',
          link='https://t.me/CarrerBegur',
          center=Location(latitude=41.3734, longitude=2.1305)),
    Group(name='Sant Andreu',
          link='https://t.me/suportsantandreu',
          center=Location(latitude=41.436372, longitude=2.191330)),
    Group(name='Raval',
          link='https://t.me/RavalSuport',
          center=Location(latitude=41.378782, longitude=2.169290)),
    Group(name='Poblenou',
          link='https://t.me/SuportMutuP9',
          center=Location(latitude=41.403531, longitude=2.203162)),
    Group(name='Vallcarca',
          link='https://t.me/VallcarcaVKK',
          center=Location(latitude=41.412576, longitude=2.143283)),
    Group(name='Gràcia',
          link='https://t.me/suportgracia',
          center=Location(latitude=41.4029, longitude=2.1569)),
    Group(name='Clot - Camp de l\'Arpa',
          link='https://t.me/XarxaSuportCA',
          center=Location(latitude=41.4132, longitude=2.1821)),
    Group(name='Sant Antoni',
          link='https://t.me/santantonicovid19',
          center=Location(latitude=41.3785, longitude=2.1588)),
    Group(name='Mercat de Sants',
          link='https://t.me/joinchat/AS5arRzobwCq3VvUSX8bqQ',
          center=Location(latitude=41.3751, longitude=2.1337)),
    Group(name='Creu Coberta',
          link='https://t.me/creucuesquerra',
          center=Location(latitude=41.3751, longitude=2.1462)),
    Group(name='Olzinelles',
          link='https://t.me/olzinelles',
          center=Location(latitude=41.3733, longitude=2.1366)),
    Group(name='Barceloneta',
          link='https://t.me/joinchat/QjDQuxq-jgGVbNwVOFSGGw',
          center=Location(latitude=41.3825, longitude=2.1859)),
    Group(name='El Carmel',
          link='623144345',
          center=Location(latitude=41.422, longitude=2.1554)),
    Group(name='El Carmel',
          link='https://twitter.com/espailatregua',
          center=Location(latitude=41.4066, longitude=2.1584)),
]


def groups_by_distance(location: Location) -> List[GroupProposal]:
    proposals = map(
        lambda group: GroupProposal(group, group.distance(location)),
        GROUP_LIST
    )
    return sorted(proposals, key=lambda proposal: proposal.distance)
